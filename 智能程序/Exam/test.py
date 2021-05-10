class Matrix:
    def __init__(self, n, m, fill=0, matrix=None, stroke=(0, 0)) -> None:
        self.shape_r = n
        self.shape_c = m
        if matrix:
            self.matrix = matrix
            self.stroke_r = stroke[0]
            self.stroke_c = stroke[1]
        else:
            self.matrix = [fill] * (n * m)
            self.stroke_r = m
            self.stroke_c = 1

    def print(self):
        print('--------')
        print('matrix', self.matrix)
        print('Stroke:', self.stroke_r, self.stroke_c)
        for r in range(self.shape_r):
            for c in range(self.shape_c):
                print(self.matrix[(r) * self.stroke_r +
                              (c) * self.stroke_c], end=' ')
            print('')
        print('--------')

    def set_value(self, pos, value):
        try:
            r, c = pos
            if r > self.shape_r or r < 1 or c > self.shape_c or c < 1:
                raise ValueError('越界')
            self.matrix[(r - 1) * self.stroke_r +
                        (c - 1) * self.stroke_c] = value
        except Exception as e:
            print('设置元素下标越界')

    def get_value(self, pos):
        try:
            r, c = pos
            if r > self.shape_r or r < 1 or c > self.shape_c or c < 1:
                raise ValueError('越界')
            print(self.matrix[(r - 1) * self.stroke_r +
                              (c - 1) * self.stroke_c])
        except Exception as e:
            print('获取元素下标越界')

    def transpose(self):
        return Matrix(self.shape_c, self.shape_r, matrix=self.matrix.copy(), stroke=(self.stroke_c, self.stroke_r))

    def reshape(self, shape):
        r, c = shape
        if self.shape_r * self.shape_c != r * c:
            print('不能将该矩阵转为目标形状')
            return(None)
        if self.stroke_c == 1:
            return Matrix(r, c, matrix=self.matrix.copy(), stroke=(c, 1))
        else:
            m = Matrix(r, c)
            for i in range(self.shape_r):
                for j in range(self.shape_c):
                    m.matrix[i * self.shape_c + j] = self.matrix[i * self.stroke_r + j * self.stroke_c]
            return m


exec(input())