# 8**) Шахматный король ходит по горизонтали, вертикали и диагонали,
#
#  но только на 1 клетку. Даны две различные клетки шахматной доски,
#
# определите, может ли король попасть с первой клетки на вторую одним ходом.
#
#
#  Пример
#  Cell 1 coordinates:
#  >>4, 4
#  Cell 2 coordinated:
#  >>5, 5
#  YES
#  Конь
#  Определите, может ли конь попасть с первой клетки на вторую одним ходом.
#  Ладья
#  Определите, может ли ладья попасть с первой клетки на вторую одним ходом.
#  Ферзь
#  Определите, может ли ферзь попасть с первой клетки на вторую одним ходом.
#  Слон
#  определите, может ли слон попасть с первой клетки на вторую одним ходом.

class ChessGame:
    def __init__(self):
        pass

    def is_king_can_move(self, start, end):
        return abs(start[0] - end[0]) <= 1 and abs(start[1] - end[1]) <= 1

    def is_rook_can_move(self, start, end):
        return start[0] == end[0] or start[1] == end[1]

    def is_elephant_can_move(self, start, end):
        return abs(start[0] - end[0]) == abs(start[1] - end[1])

    def is_queen_can_move(self, start, end):
        return self.is_rook_can_move(start, end) or self.is_elephant_can_move(start, end)

    def is_horse_can_move(self, start, end):
        dx = abs(start[0] - end[0])
        dy = abs(start[1] - end[1])
        return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)


def print_move_result(result):
    if result:
        print('YES')
    else:
        print('NO')


game_1 = ChessGame()

print('=======КОРОЛЬ=======')
print_move_result(game_1.is_king_can_move([4, 4], [5, 5]))
print_move_result(game_1.is_king_can_move([2, 2], [2, 3]))
print_move_result(game_1.is_king_can_move([2, 2], [3, 2]))
print_move_result(game_1.is_king_can_move([2, 2], [3, 3]))
print_move_result(game_1.is_king_can_move([2, 2], [1, 1]))
print_move_result(game_1.is_king_can_move([2, 2], [2, 4]))
print_move_result(game_1.is_king_can_move([2, 2], [4, 4]))

print('=======ЛАДЬЯ=======')
print_move_result(game_1.is_rook_can_move([2, 2], [2, 5]))
print_move_result(game_1.is_rook_can_move([2, 2], [4, 2]))
print_move_result(game_1.is_rook_can_move([2, 2], [3, 3]))
print_move_result(game_1.is_rook_can_move([2, 2], [1, 4]))

print('=======СЛОН=======')
print_move_result(game_1.is_elephant_can_move([2, 2], [4, 4]))
print_move_result(game_1.is_elephant_can_move([2, 4], [3, 3]))
print_move_result(game_1.is_elephant_can_move([2, 3], [4, 1]))
print_move_result(game_1.is_elephant_can_move([2, 4], [4, 4]))
print_move_result(game_1.is_elephant_can_move([2, 2], [2, 5]))

print('=======ФЕРЗЬ=======')
print_move_result(game_1.is_queen_can_move([2, 3], [4, 5]))
print_move_result(game_1.is_queen_can_move([1, 3], [1, 1]))
print_move_result(game_1.is_queen_can_move([4, 4], [1, 1]))
print_move_result(game_1.is_queen_can_move([2, 3], [4, 4]))
print_move_result(game_1.is_queen_can_move([2, 2], [4, 5]))

print('=======КОHЬ=======')
print_move_result(game_1.is_horse_can_move([1, 2], [3, 3]))
print_move_result(game_1.is_horse_can_move([4, 4], [2, 3]))
print_move_result(game_1.is_horse_can_move([3, 1], [1, 2]))
print_move_result(game_1.is_horse_can_move([4, 4], [2, 1]))
print_move_result(game_1.is_horse_can_move([3, 1], [1, 5]))
