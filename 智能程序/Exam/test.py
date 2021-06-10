class Block:
    def __init__(self, father_block, value: int):
        self.father_block = father_block
        self.value = value
        self.current_block = self
        if self.father_block:
            self.check_num: int = self.father_block.check_num + self.value
        else:
            self.check_num: int = 0

    def __iter__(self):
        self.current_block = self
        return self

    def __next__(self):
        if self.current_block:
            value = self.current_block.value
            self.current_block = self.current_block.father_block
            return value
        else:
            raise StopIteration()

    def check(self):
        if not self.father_block:
            return True
        if self.father_block.check_num + self.value != self.check_num:
            return False
        return self.father_block.check()
        
# 测试用代码, 请不要改动
while True:
    exec(input())