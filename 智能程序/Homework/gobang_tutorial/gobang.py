# coding=utf-8

from typing import List, Tuple


class SuperPiece:
    def is_empty(self) -> bool:
        """
        Determine whether the piece is empty.

        Returns:
            bool: True if the piece is empty
        """
        raise NotImplementedError

    def is_black(self) -> bool:
        """
        Determine whether the piece is black.

        Returns:
            bool: True if the piece is black
        """
        raise NotImplementedError

    def is_white(self) -> bool:
        """
        Determine whether the piece is white.

        Returns:
            bool: True if the piece is white
        """
        raise NotImplementedError


class SuperChessboard:
    def __init__(self, size: int):
        """
        Initialization.

        Args:
            size (int): the length and width of the chessboard
        """
        self.size = size

    def get_board_size(self) -> int:
        """
        Get the chessboard size.

        Returns:
            int: the size of the chessboard
        """
        return self.size

    def set_piece(self, piece: SuperPiece, position: tuple) -> bool:
        """
        Set a given piece in a given position only if the position in the chessboard
        is empty.

        Args:
            piece (SuperPiece): the piece to be set
            position (tuple): the position to set the piece, with the form of (x,y), 
            x is the row index and y is the column index, which should large than 0,
            i.e. x,y is in [1, size]

        Returns:
            bool: True if the piece is set successfully; False is there is not empty
            in the given position.
        """
        raise NotImplementedError

    def set_black_piece(self, position: tuple) -> bool:
        """
        Set a black piece in a given position only if the position in the chessboard
        is empty.

        Args:
            position (tuple): the position to set the piece, with the form of (x,y), 
            x is the row index and y is the column index, which should large than 0,
            i.e. x,y is in [1, size]

        Returns:
            bool: True if the piece is set successfully; False is there is not empty
            in the given position.
        """
        raise NotImplementedError

    def set_white_piece(self, position: tuple) -> bool:
        """
        Set a white piece in a given position only if the position in the chessboard
        is empty.

        Args:
            position (tuple): the position to set the piece, with the form of (x,y), 
            x is the row index and y is the column index, which should large than 0,
            i.e. x,y is in [1, size]

        Returns:
            bool: True if the piece is set successfully; False is there is not empty
            in the given position.
        """
        raise NotImplementedError

    def set_empty_piece(self, position: tuple):
        """
        Set a empty piece in a given position.

        Args:
            position (tuple): the position to set the piece, with the form of (x,y), 
            x is the row index and y is the column index, which should large than 0,
            i.e. x,y is in [1, size]
        """
        raise NotImplementedError

    def get_piece(self, position: tuple) -> SuperPiece:
        """
        Get the piece in the given position.

        Args:
            position (tuple): querying position, with the form of (x,y), 
            x is the row index and y is the column index, which should large than 0,
            i.e. x,y is in [1, size]

        Returns:
            SuperPiece: the piece in the given position
        """
        raise NotImplementedError

    def is_empty(self, position: tuple) -> bool:
        """
        Determine whether the position in the chessboard is empty.

        Args:
            position (tuple): querying position, with the form of (x,y), 
            x is the row index and y is the column index, which should large than 0,
            i.e. x,y is in [1, size]

        Returns:
            bool: True if the piece in the given position is empty
        """
        raise NotImplementedError

    def is_over_boundary(self, position: tuple) -> bool:
        """
        Determine whether the position in the chessboard is over boundary.

        Args:
            position (tuple): querying position, with the form of (x,y), 
            x is the row index and y is the column index, which should large than 0,
            i.e. x,y is in [1, size]

        Returns:
            bool: True if the piece in the given position is over boundary
        """
        raise NotImplementedError


class SuperGame:
    def __init__(self):
        """
        Initialization. We have initialized the `display` and `round_num`, but left the
        `board_size` and `board` uninitialized.
        """
        self.display = Display()
        self.round_num = 1

        # 以下参数需要初始化
        self.board_size = 0
        self.board = None

    def start(self):
        """
        Start the game.
        """
        self.game_loop()

    def show_board(self):
        """
        Show current chessboard to the user.
        """
        self.display.display_board(self.board)

    def game_loop(self):
        """
        Start the game main loop.
        In this function, you should first call the `self.display.display_help_info()`,
        then enter a for/while loop, in which you should do things bellow:
            1. update `self.round_num`.
            2. display current round info by calling `self.display.display_round`.
            3. display chessboard by calling `super().show_board()`.
            4. get position input by calling `self.display.input_position()`.
                4.1. call `self.display.display_position_empty_error()` if there
                is not empty in the position.
                4.2. call `self.display.display_position_boundary_error()` if the
                position exceeds the boundary.
                4.3. call `self.display.display_position_info(position, self.black_turn)` if
                the position is valid.
            5. set a black/white piece in the input position.
            6. break loop if black/white wins the game.
        """
        raise NotImplementedError

    def win_judging(self) -> bool:
        """
        Determine whether black/white wins the game.

        Returns:
            bool: True if black/white wins the game
        """
        raise NotImplementedError


class Display:
    def __init__(self, gbk_console=False, ascii_piece=False):
        """
        Initialization.

        Args:
            gbk_console (bool): use gbk encoding, if your program outputs messy code, you
            can try it.
        """
        import sys
        import io

        sys.stdout = io.TextIOWrapper(
            sys.stdout.buffer, encoding="gbk" if gbk_console else "utf-8"
        )

        self.black_unit = "●" if not ascii_piece else "x"
        self.white_unit = "○" if not ascii_piece else "o"
        self.empty_unit = "+"

    def input_board_size(self) -> int:
        """
        Get chessboard size from user.

        Returns:
            int: the size of the chessboard
        """
        self.info("请输入棋盘大小:")
        size = int(input())
        return size

    def input_position(self) -> tuple:
        """
        Get next position from user to set a piece.

        Returns:
            tuple: the position tuple, with the form of (x,y), x is the row index
            and y is the column index, which should large than 0, i.e. x,y is in [1, size]
        """
        self.info("请输入坐标:")
        position = tuple(map(int, input().split()))
        while True:
            if len(position) == 2:
                break
            self.info("输入坐标格式错误", True)
            self.info("请输入坐标:")
            position = tuple(map(int, input().split()))
        return position

    def info(self, message: str, space_line=False):
        """
        Print a message to user.

        Args:
            message (str): the message string to print
            space_line (bool): whether to print another '\n' after the message
        """
        print(message)
        if space_line:
            print("")

    def display_winner(self, black_win: bool):
        """
        Print game winner info.

        Args:
            black_win (bool): wether the winner is black
        """
        win_message = "{}棋获胜".format("黑" if black_win else "白")
        self.info(win_message, True)

    def display_round(self, round_num, black_turn: bool):
        """
        Print round info.

        Args:
            round_num (int): current round
            black_turn (bool): wether the round is black's round
        """
        self.split_line(20)
        round_message = "回合{} {}棋回合:".format(
            round_num, "黑" if black_turn else "白")
        self.info(round_message, True)

    def display_position_info(self, position: tuple, black_turn: bool):
        """
        Print the input position info of this round.

        Args:
            position (tuple): the input position of this round, with the form of (x,y), 
            x is the row index and y is the column index, which should large than 0,
            i.e. x,y is in [1, size]
            black_turn (bool): wether the round is black's round
        """
        position_info = "{}棋落子位置为 ({} {})".format(
            "黑" if black_turn else "白", position[0], position[1]
        )
        self.info(position_info, True)

    def display_help_info(self):
        """
        Print help message.
        """
        title = "帮助信息:"
        position_info = '坐标的形式如"3 5"，表示第3行第5列。坐标从1开始，最大不超过棋盘大小。'
        self.info(title)
        self.info(position_info, True)

    def display_position_boundary_error(self):
        """
        Print position boundary error message.
        """
        self.info("输入的坐标范围有误", True)

    def display_position_empty_error(self):
        """
        Print position empty error message.
        """
        self.info("该位置已经有棋子了", True)

    def split_line(self, width):
        """
        Print `--` for width times.
        """
        print("--" * width)

    def display_board(self, chessboard: SuperChessboard):
        """
        Display chessboard.

        Args:
            chessboard (SuperChessboard): the chessboard to display
        """
        board_size = chessboard.get_board_size()
        self.split_line(board_size + 1)
        # print coordinate
        row_str = "{:<2}" * board_size
        print("  " + row_str.format(*list(range(1, board_size + 1))))

        for i in range(1, board_size + 1):
            board_row = []
            for j in range(1, board_size + 1):
                piece = chessboard.get_piece((i, j))
                if piece.is_empty():
                    board_row.append(self.empty_unit)
                elif piece.is_white():
                    board_row.append(self.white_unit)
                else:
                    board_row.append(self.black_unit)
            row_str = "{:<2d}".format(i) + " ".join(board_row)
            print(row_str)
        self.split_line(board_size + 1)


# your code here

class Piece(SuperPiece):

    type = 0

    def __init__(self, type: str) -> None:
        """
        Initialization.

        Args:
            type (str): type of the piece. You can use 'empty', 'black' or 'white'.
        """
        if type == 'empty':
            self.type = 0
        elif type == 'black':
            self.type = 1
        elif type == 'white':
            self.type = 2
        else:
            raise ValueError(
                'Type of piece must be "empty", "black" or "white".')

    def is_empty(self) -> bool:
        if self.type == 0:
            return True
        else:
            return False

    def is_black(self) -> bool:
        if self.type == 1:
            return True
        else:
            return False

    def is_white(self) -> bool:
        if self.type == 2:
            return True
        else:
            return False


class Chessboard(SuperChessboard):

    def __init__(self, size: int):
        super().__init__(size)
        self.board: List[List[SuperPiece]] = [[Piece('empty') for j in range(size)] for i in range(size)]

    def set_piece(self, piece: SuperPiece, position: Tuple[int, int]) -> bool:
        if self.is_over_boundary(position) or not self.is_empty(position):
            return False
        else:
            x, y = position
            self.board[x - 1][y - 1] = piece
            return True

    def set_black_piece(self, position: Tuple[int, int]) -> bool:
        piece = Piece('black')
        return self.set_piece(piece, position)

    def set_white_piece(self, position: Tuple[int, int]) -> bool:
        piece = Piece('white')
        return self.set_piece(piece, position)

    def get_piece(self, position: Tuple[int, int]) -> SuperPiece:
        if self.is_over_boundary(position):
            return None
        else:
            x, y = position
            return self.board[x - 1][y - 1]

    def is_empty(self, position: Tuple[int, int]) -> bool:
        x, y = position
        if self.board[x - 1][y - 1] == None or self.board[x - 1][y - 1].is_empty():
            return True
        else:
            return False

    def is_over_boundary(self, position: Tuple[int, int]) -> bool:
        x, y = position
        size = self.get_board_size()
        if x > size or y > size or x < 1 or y < 1:
            return True
        else:
            return False



class Game(SuperGame):

    def __init__(self):
        """
        Initialization.

        Args:
            board_size (str): The size of the board. Usually it is 15.
            board (SuperChessBoard): The board. It can be None.
        """
        super().__init__()
        self.board_size = self.display.input_board_size()
        if self.board_size < 5:
            self.display.info('棋盘大小不能小于 5!')
            exit()
        self.board = Chessboard(self.board_size)

    def game_loop(self):

        self.display.display_help_info()

        while True:
            self.black_turn = self.round_num % 2 == 1
            self.display.display_round(self.round_num, self.black_turn)
            self.show_board()

            while True:
                position = self.display.input_position()
                if self.board.is_over_boundary(position):
                    self.display.display_position_boundary_error()
                elif not self.board.is_empty(position):
                    self.display.display_position_empty_error()
                else:
                    # Valid
                    self.display.display_position_info(position, self.black_turn)
                    break

            if self.black_turn:
                self.board.set_black_piece(position)
            else:
                self.board.set_white_piece(position)
            
            if self.win_judging():
                self.show_board()
                self.display.display_winner(self.black_turn)
                break

            self.round_num += 1

    def win_judging(self) -> bool:
        board = self.board
        is_win = False
        for x in range(1, self.board_size - 4 + 1):
            for y in range(1, self.board_size - 4 + 1):
                if board.get_piece((x, y)).is_empty():
                    continue
                elif board.get_piece((x, y)).is_black():
                    is_end = False
                    for i in range(1, 5):
                        if not board.get_piece((x + i, y)).is_black():
                            is_end = True
                            break
                    if not is_end:
                        is_win = True
                        break

                    is_end = False
                    for i in range(1, 5):
                        if not board.get_piece((x, y + i)).is_black():
                            is_end = True
                            break
                    if not is_end:
                        is_win = True
                        break

                    is_end = False
                    for i in range(1, 5):
                        if not board.get_piece((x + i, y + i)).is_black():
                            is_end = True
                            break
                    if not is_end:
                        is_win = True
                        break
                else:
                    is_end = False
                    for i in range(1, 5):
                        if not board.get_piece((x + i, y)).is_white():
                            is_end = True
                            break
                    if not is_end:
                        is_win = True
                        break

                    is_end = False
                    for i in range(1, 5):
                        if not board.get_piece((x, y + i)).is_white():
                            is_end = True
                            break
                    if not is_end:
                        is_win = True
                        break

                    is_end = False
                    for i in range(1, 5):
                        if not board.get_piece((x + i, y + i)).is_white():
                            is_end = True
                            break
                    if not is_end:
                        is_win = True
                        break
            if is_win:
                break

        return is_win
            


if __name__ == "__main__":
    g = Game()
    g.start()
