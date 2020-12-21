import random


class GameController:
    """
        2048游戏算法代码
    """
    __list_2048 = [[0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0]]

    def move_zero(self):
        """
            将一行列表的零元素移动到末尾
        :return:
        """
        for i in range(len(list_row) - 1, -1, -1):
            if list_row[i] == 0:
                del list_row[i]
                list_row.append(0)

    def add_adjoin(self):
        """
            每行相邻相同数字相加
        :return:
        """
        self.move_zero()
        for i in range(len(self.__list_2048) - 1):
            if list_row[i] == list_row[i + 1]:
                list_row[i] *= 2
                del list_row[i + 1]
                list_row.append(0)

    def left_shift(self):
        """
            左移指令算法
        :return:
        """
        global list_row
        for line in self.__list_2048:
            list_row = line
            self.add_adjoin()

    def right_shift(self):
        """
            右移指令算法
        :return:
        """
        global list_row
        for item in self.__list_2048:
            list_row = item[::-1]
            self.add_adjoin()
            item[::] = list_row[::-1]

    def matrix_transpose(self):
        """
            矩阵转置函数
        :return:
        """
        for r in range(len(self.__list_2048) - 1):
            for c in range(r + 1, len(self.__list_2048)):
                self.__list_2048[c][r], self.__list_2048[r][c] = self.__list_2048[r][c], self.__list_2048[c][r]

    def up_shift(self):
        """
            上移指令算法
        :return:
        """
        self.matrix_transpose()
        self.left_shift()
        self.matrix_transpose()

    def down_shift(self):
        """
            下移指令算法
        :return:
        """
        self.matrix_transpose()
        self.right_shift()
        self.matrix_transpose()

    def print_interface_of_game(self):
        """
            打印界面函数
        :return:
        """
        for item in self.__list_2048:
            print(item[0], item[1], item[2], item[3], sep='\t', end='\n')

    def add_2_to_list_2048(self):
        """
            每次移动都在0的位置添加一个新的2元素
        :return:
        """
        list_index_of_0 = []
        for r in range(len(self.__list_2048)):
            for c in range(len(self.__list_2048)):
                if self.__list_2048[r][c] == 0:  # 0元素的坐标(r,c)
                    list_index_of_0.append((r, c))
        index_of_0 = random.choice(list_index_of_0)  # 随机找到列表中的一个元素
        self.__list_2048[index_of_0[0]][index_of_0[1]] = 2  # 添加新的2元素
