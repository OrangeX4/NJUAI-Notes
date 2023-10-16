import stanza
import json
import os
from tqdm import tqdm


def clean_data(document):
    '''
    Clean the document to a single sentence
    '''
    document = document.replace('-LRB-', '(')
    document = document.replace('-RRB-', ')')
    document = document.replace(':', ',')
    document = document[:-1].replace('.', '').replace('!', ',') + document[-1]
    document = document[0] + document[1:].lower()
    document = document.replace('$t$', '$T$')
    return document


def load_data(path):
    data = []
    with open(path, 'r') as f:
        lines = f.readlines()
        for i in range(len(lines) // 3):
            sentence = clean_data(lines[3 * i + 0].strip())
            target = lines[3 * i + 1].strip().lower()
            label = lines[3 * i + 2].strip()
            document = sentence.replace(r'$T$', target)
            data.append({
                'sentence': sentence,
                'target': target,
                'label': label,
                'document': document,
            })
    return data


nlp = stanza.Pipeline(
    lang='en', processors='tokenize,mwt,pos,lemma,depparse')
def depparse(documents):
    '''
    Input: a list of documents, each document is a string
    Output: a list of documents, each document is a stanza Document object
    '''
    in_docs = [stanza.Document([], text=d) for d in documents]
    out_docs = nlp(in_docs)
    return out_docs


def build_graph(words):
    '''
    Input: a stanza Document object with .to_dict()[0] method
    Output: a graph represented by a list of lists
            like [[3], [2], [1, 3], [2], [5], [4]]
    '''
    # build graph
    graph = [[] for _ in range(len(words) + 1)]
    for word in words:
        # ignore word.deprel
        graph[word['id']].append(word['head'])
        graph[word['head']].append(word['id'])
    return graph


def depparse_and_build_graph_with_cache(documents, cache_path=None):
    '''
    Input: a list of documents, each document is a string
    Output: a list of dict with words and graph
    '''
    # load cache
    cache = {}
    if cache_path:
        if not os.path.exists(cache_path):
            with open(cache_path, 'w') as f:
                json.dump({}, f)
        with open(cache_path, 'r') as f:
            cache = json.load(f)
    # depparse and build graph
    no_cache_documents = list(set(documents) - set(cache.keys()))
    if no_cache_documents:
        no_cache_docs = depparse(no_cache_documents)
    else:
        no_cache_docs = []
    no_cache_map = {no_cache_documents[i]: no_cache_docs[i].to_dict() for i in range(len(no_cache_documents))}
    result = {}
    for document in documents:
        if document not in cache:
            assert len(no_cache_map[document]) == 1, document
            cache[document] = {
                'words': no_cache_map[document][0],
                'graph': build_graph(no_cache_map[document][0])
            }
        result[document] = cache[document]
    # save cache
    if cache_path:
        with open(cache_path, 'w') as f:
            json.dump(cache, f, indent=4)
    return result


def bfs(graph, start):
    '''
    Input: a graph represented by a list of lists
    Output: a list of distances from the start node to each node
    '''
    dist = [-1 for _ in range(len(graph))]
    # note that dist[start] = 1 for simplying the calculation of weights
    dist[start] = 1
    stack = [start]
    step = 0
    while stack:
        step_num = len(stack)
        for _ in range(step_num):
            cur = stack.pop(0)
            for next in graph[cur]:
                if dist[next] == -1:
                    dist[next] = step + 1
                    stack.append(next)
        step += 1
    return dist


def dist_to_weights(dist, h=lambda x: 1 / x ** 2):
    '''
    Input: a list of distances from the start node to each node
    Output: a list of weights for each node using the function h
    '''
    weights = [h(x) for x in dist]
    return weights


def dist_from_root(words, start):
    '''
    Find the distance from the start node to the root node
    '''
    words = [None, *words]
    dist = 0
    cur = start
    while cur != 0:
        dist += 1
        cur = words[cur]['head']
    return dist


def get_target_id(sentence, target, words):
    start_char = sentence.find(r'$T$')
    start_id = 0
    for i, word in enumerate(words):
        if word['start_char'] == start_char:
            start_id = i + 1
            break
    assert start_id != 0
    # find the id closest to the root
    min_dist = float('inf')
    min_start_id = start_id
    for i in range(start_id, start_id + len(target.split())):
        dist = dist_from_root(words, i)
        if dist < min_dist:
            min_dist = dist
            min_start_id = i
    return min_start_id


def preprocess(data_path, saved_path, cache_path):
    input_data = load_data(data_path)
    output_data = []
    batch = 128
    for i in tqdm(range(len(input_data) // batch + 1)):
        # 每批次 batch 条
        data_batch = input_data[i * batch: (i + 1) * batch]
        # 取出每条数据的 document
        documents = [d['document'] for d in data_batch]
        # depparse_and_build_graph_with_cache
        result = depparse_and_build_graph_with_cache(documents, cache_path)
        for i in range(batch):
            if i >= len(data_batch):
                break
            item = result[documents[i]]
            tokens = [words['text'] for words in item['words']]
            target_id = get_target_id(data_batch[i]['sentence'], data_batch[i]['target'], item['words'])
            dist = bfs(item['graph'], target_id)
            weights = dist_to_weights(dist)
            output_data.append({
                **data_batch[i],
                'tokens': tokens,
                'dist': dist,
                'weights': weights,
            })
        with open(saved_path, 'w') as f:
            json.dump(output_data, f, indent=4)



if __name__ == '__main__':
    # 用于断点重跑的缓存
    cache_path = 'data/depparse_and_build_graph_cache.json'
    preprocess('data/train.txt', 'data/train_preprocessed.json', cache_path)
    preprocess('data/test.txt', 'data/test_preprocessed.json', cache_path)
    # 读取 train_preprocessed.json 和 test_preprocessed.json 中的 tokens
    with open('data/train_preprocessed.json') as f:
        train_data = json.load(f)
    with open('data/test_preprocessed.json') as f:
        test_data = json.load(f)
    
    # 过滤词表, 生成 word_vectors_filtered.txt, 但是只用于 rnn, 这里就注释掉了
    # tokens = []
    # for item in train_data + test_data:
    #     tokens += item['tokens']
    # tokens = set(tokens)
    # result = ''
    # with open('data/word_vectors.txt', encoding='utf-8') as f:
    #     for line in tqdm(f):
    #         word = line.split()[0]
    #         if word in tokens:
    #             result += line
    # with open('data/word_vectors_filtered.txt', 'w') as f:
    #     f.write(result)