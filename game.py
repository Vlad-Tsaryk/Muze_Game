import sys

class Game:
    def __init__(self):
        self.wals = []
        self.muze = []
        self.start = []
        self.finish = []

    def set_start(self, start_y, start_x):
        self.start = [start_y, start_x]
        self.muze[start_y][start_x] = '●ᴥ●'

    def set_finish(self, finish_y, finish_x):
        self.finish = [finish_y, finish_x]
        self.muze[finish_y][finish_x] = '🦴'

    def find_wall(self, y, x):
        try:
            self.wals.index([y, x])
        except ValueError:
            return False
        print("Шарик заблудился")
        sys.exit()

    def creat_muze(self):
        self.muze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                     [1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1],
                     [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                     [1, 0, 0, 1, 1, 1, 1, 1, 2, 2, 1, 2, 2, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                     [1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1],
                     [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                     [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                     [1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                     [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 2, 2, 1, 1, 1, 0, 0, 0, 0, 0, 1],
                     [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                     [1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1],
                     [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                     [1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
                     [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
                     [1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1],
                     [1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 1, 0, 0, 1],
                     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
                     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    def print_muze(self, muze):
        for i in range(len(muze)):
            for j in range(len(muze[i])):
                if muze[i][j] == 0:
                    muze[i][j] = '   '
                elif muze[i][j] == 1:
                    muze[i][j] = '***'
                elif muze[i][j] == 2:
                    muze[i][j] = '   '
                    self.wals.append([i, j])

            print(''.join(map(str, muze[i])))

    def save(self):
        pass
    def load_save(self):
        pass


class Ball():
    def __init__(self, y, x):
        self.__x = x
        self.__y = y
        self.__g = 1

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if 0 < x < 25:
            self.__x = x
        else:
            print('Value out of range')

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if 0 < y < 22:
            self.__y = y
        else:
            print('Value out of range')

    def move_x(self, x,muze):
        if muze[self.__y][x] !='***':
            # if muze[self.__y][self.__x] == muze[self.__y][x]:
            #     print('Шарик струсил и убежал')
            #     sys.exit()

            muze[self.__y][self.__x] = '   '
            self.__x = x
        else:
            print('Шарик ударился о стену')
            sys.exit()


    def move_y(self, y,muze):
        if muze[y][self.__x] !='***':
            # if muze[self.__y][self.__x] == muze[y][self.__x]:
            #     print('Шарик струсил и убежал')
            #     sys.exit()
            muze[self.__y][self.__x] = '   '
            self.__y = y
        else:
            print('Шарик ударился о стену')
            sys.exit()



player = Ball(1, 0)
game = Game()
game.creat_muze()
game.set_start(player.y, player.x)
game.set_finish(20, 24)
game.print_muze(game.muze)

while True:
    side = input()
    if side == 'w' and not game.find_wall(player.y - 1, player.x):
        player.move_y(player.y - 1,game.muze)
    elif side == 's' and not game.find_wall(player.y + 1, player.x):
        player.move_y(player.y + 1,game.muze)
    elif side == 'd' and  not game.find_wall(player.y, player.x + 1):
        player.move_x(player.x + 1,game.muze)
    elif side == 'a' and  not game.find_wall(player.y, player.x - 1):
        player.move_x(player.x - 1,game.muze)
    game.muze[player.y][player.x] = '●ᴥ●'
    for i in range(len(game.muze)): print(''.join(map(str, game.muze[i])))
    print('Шарик нашел правильный путь')

# wals = []
# muze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#         [1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
#         [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
#         [1, 0, 0, 1, 1, 1, 1, 1, 2, 2, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
#         [1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1],
#         [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#         [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#         [1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#         [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
#         [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
#         [1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1],
#         [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
#         [1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
#         [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
#         [1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1],
#         [1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
#         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
#         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, '🦴'],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
#
# player = Ball(1, 0)
#
# muze[player.y][player.x] = '●ᴥ●'
# for i in range(len(muze)):
#     for j in range(len(muze[i])):
#         if muze[i][j] == 0:
#             muze[i][j] = '   '
#         elif muze[i][j] == 1:
#             muze[i][j] = '***'
#         elif muze[i][j] == 2:
#             muze[i][j] = '   '
#             wals.append([i,j])
#
#     print(''.join(map(str, muze[i])))
#
# def find_wall(y,x):
#     try:
#         wals.index([y,x])
#     except ValueError:
#         return False
#     print("Шарик заблудился")
#     sys.exit()
#
# print(wals)
# while game:
#     side = input()
#     if side == 'w' and muze[player.y - 1][player.x] != '***' and  not find_wall(player.y - 1,player.x):
#         player.move_y(player.y - 1)
#     elif side == 's' and muze[player.y + 1][player.x] != '***'and  not find_wall(player.y + 1,player.x):
#         player.move_y(player.y + 1)
#     elif side == 'd' and muze[player.y][player.x + 1] != '***' and  not find_wall(player.y,player.x + 1):
#         player.move_x(player.x + 1)
#     elif side == 'a' and muze[player.y][player.x - 1] != '***' and  not find_wall(player.y,player.x - 1):
#         player.move_x(player.x - 1)
#     # if side == 'w' and muze[player.x][player.y-1] != '##':
#     #     player.move_y(player.y - 1)
#     # elif side == 's' and muze[player.x][player.y+1] != '##':
#     #     player.move_y(player.y + 1)
#     # elif side == 'd' and muze[player.x+1][player.y] != '##':
#     #     player.move_x(player.x + 1)
#     # elif side == 'a' and muze[player.x-1][player.y] != '##':
#     #     player.move_x(player.x - 1)
#     else:
#         print("Шарик ударился о стену")
#         break
#     # print(player.old_y,player.old_x)
#     print('Шарик нашел правильный путь')
#     muze[player.y][player.x]= '●ᴥ●'
#     print(player.y,player.x)
#     for i in range(len(muze)): print(''.join(map(str, muze[i])))
