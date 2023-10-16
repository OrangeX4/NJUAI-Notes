import os

# 执行命令 ./src/solvers/GMAA ./problems/Dec-Tiger.pgmx -B BnB -G FSPC -Q QPOMDP -h4

config = {
    '-B': ['AM', 'CE', 'MP', 'BnB'],
    '-G': ['MAAstar', 'FSPC', 'kGMAA'],
    '-Q': ['QMDP', 'QMAA', 'QPOMDP'],
}

horizon = '4'

for b in config['-B']:
    for g in config['-G']:
        for q in config['-Q']:
            command = './src/solvers/GMAA ./problems/Dec-Tiger.pgmx -B %s -G %s -Q %s -h %s' % (b, g, q, horizon)
            os.system(command)


# 打开路径 ../.madp/results/GMAA/Dec-Tiger, 搜索所有类似所有文件
# 解析标题如
# GMAA_Dec-Tiger_FSPC_QMDP_h4_restarts1_NoCache_BGIP-AM_AM_restarts10
# GMAA_Dec-Tiger_MAAstar_QMDP_h4_restarts1_NoCache_BGIP-BFS
# GMAA_Dec-Tiger_MAAstar_QMDP_h4_restarts1_NoCache_BGIP-BnB_ka0_JTOIdentityMapping_CCI1
# 读取文件, 解析第三行的 # h 4	 avg GMAA time (s): 57928.330000 avg value: 8.421449
# 并为每一行生成类似 [BFS], [MAAstar], [QMDP], [是], [8.421449], [57928.33 s], 的输出

result = []
for filename in os.listdir('../.madp/results/GMAA/Dec-Tiger'):
    if filename.startswith('GMAA_Dec-Tiger'):
        B = ''
        G = ''
        Q = ''
        for b in config['-B'] + ['BFS']:
            if b in filename:
                B = b
                break
        for g in config['-G']:
            if g in filename:
                G = g
                break
        for q in config['-Q']:
            if q in filename:
                Q = q
                break
        if B == '' or G == '' or Q == '':
            print('Error: %s' % filename)
            assert False
        with open('../.madp/results/GMAA/Dec-Tiger/' + filename, 'r') as f:
            lines = f.readlines()
            if lines[2].startswith('# h ' + horizon):
                line = lines[2].split()
                time = line[7]
                value = line[10]
                optimized = '是' if value == '8.421449' else '否'
                result.append('[%s], [%s], [%s], [%s], [%s], [%s s]' % (B, G, Q, optimized, value, time))

result.sort()
for r in result:
    print(r)