import numpy as np


def interchange(mat, row1, row2):
    """
        Row switching. A row within the matrix 'mat' will be switched with another row.
        
        Args:
            mat (numpy.matrix): the matrix to apply row switching transformation.
            row1 (int): the row index to be switched. The row index is in [0, mat.shape[0]-1]
            row2 (int): the another row index to be switched. The row index is in [0, mat.shape[0]-1]
    """


def scale(mat, row, scale):
    """
        Row multiplication. Each element in a given row will be multiplied by a non-zero constant. It is also known as scaling a row.

        Args:
            mat (numpy.matrix): the matrix to apply row multiplication transformation.
            row (int): the row index to be multiplied. The row index is in [0, mat.shape[0]-1]
            scale (int or float): the multiplier value.
    """


def add(mat, row1, row2, scale):
    """
        Row addition. A given row will be replaced by the sum of that row and a multiple of another row.
        Which mean (row2 of mat) = (row2 of mat) + scale * (row1 of mat).

        Args:
            mat (numpy.matrix): the matrix to apply row addition transformation.
            row1 (int): the row index1. The row index is in [0, mat.shape[0]-1]
            row2 (int): the row index2. The row index is in [0, mat.shape[0]-1]
            scale (int or float): the multiplier value.
    """



def test1():
    globals_dict = globals()
    assert "interchange" in globals_dict, "function 'interchange' is not defined."
    assert "scale" in globals_dict, "function 'scale' is not defined."
    assert "add" in globals_dict, "function 'add' is not defined."
    import numpy as np

    test_mat = np.array([[1, 2, 3], [4, 5, 6], [0, 8, 9]])
    orig_mat = test_mat.copy()
    dest_mat1 = np.array([[1, 2, 3], [0, 8, 9], [4, 5, 6]])
    dest_mat2 = np.array([[4, 5, 6], [0, 8, 9], [1, 2, 3]])
    interchange(test_mat, 2, 1)
    assert np.all(
        test_mat == dest_mat1
    ), "wrong answer for calling 'interchange(mat, 2, 1)' s.t. mat =\n{}\nexpect:\n{}\nbut got:\n{}".format(
        orig_mat, dest_mat1, test_mat
    )
    orig_mat = test_mat.copy()
    interchange(test_mat, 2, 0)
    assert np.all(
        test_mat == dest_mat2
    ), "wrong answer for calling 'interchange(mat, 2, 0)' s.t. mat =\n{}\nexpect:\n{}\nbut got:\n{}".format(
        orig_mat, dest_mat2, test_mat
    )
    orig_mat = test_mat.copy()
    interchange(test_mat, 2, 2)
    assert np.all(
        test_mat == orig_mat
    ), "wrong answer for calling 'interchange(mat, 2, 2)' s.t. mat =\n{}\nexpect:\n{}\nbut got:\n{}".format(
        orig_mat, orig_mat, test_mat
    )

    print("--------------------------------------\nfunction 'interchange' check passed.")

    test_mat = np.array([[1, 2, 3], [4, 5, 6], [0, 8, 9]], dtype=np.float_)
    orig_mat = test_mat.copy()
    dest_mat1 = np.array([[2, 4, 6], [4, 5, 6], [0, 8, 9]], dtype=np.float_)
    dest_mat2 = np.array([[2, 4, 6], [6.0, 7.5, 9.0], [0, 8, 9]], dtype=np.float_)
    scale(test_mat, 0, 2.0)
    assert np.all(
        test_mat == dest_mat1
    ), "wrong answer for calling 'scale(mat, 0, 2.0)' s.t. mat =\n{}\nexpect:\n{}\nbut got:\n{}".format(
        orig_mat, dest_mat1, test_mat
    )
    orig_mat = test_mat.copy()
    scale(test_mat, 1, 1.5)
    assert np.all(
        test_mat == dest_mat2
    ), "wrong answer for calling 'scale(mat, 1, 1.5)' s.t. mat =\n{}\nexpect:\n{}\nbut got:\n{}".format(
        orig_mat, dest_mat2, test_mat
    )
    print("--------------------------------------\nfunction 'scale' check passed.")

    test_mat = np.array([[1, 2, 3], [4, 5, 6], [0, 8, 9]], dtype=np.float_)
    orig_mat = test_mat.copy()
    dest_mat1 = np.array([[1, 2, 3], [4, 5, 6], [0.5, 9.0, 10.5]], dtype=np.float_)
    add(test_mat, 0, 2, 0.5)
    assert np.all(
        test_mat == dest_mat1
    ), "wrong answer for calling 'add(mat, 0, 2, 0.5)' s.t. mat =\n{}\nexpect:\n{}\nbut got:\n{}".format(
        orig_mat, dest_mat1, test_mat
    )

    orig_mat = test_mat.copy()
    add(test_mat, 0, 2, 0.0)
    assert np.all(
        test_mat == orig_mat
    ), "wrong answer for calling 'add(mat, 0, 2, 0.0)' s.t. mat =\n{}\nexpect:\n{}\nbut got:\n{}".format(
        orig_mat, orig_mat, test_mat
    )
    print("--------------------------------------\nfunction 'add' check passed.")


def test2():
    pass


def test3():
    pass


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        if sys.argv[1] == "test1":
            test1()
        elif sys.argv[1] == "test2":
            test2()
        elif sys.argv[1] == "test3":
            test3()
