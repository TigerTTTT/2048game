from bll import GameController


class GameView:
    """
        2048游戏操作界面
    """
    def __init__(self):
        self.controller = GameController()

    def start_game(self):
        """
            输入WASD进行上左下右移动
        :return:
        """
        print("W:上   A：左   S：下   D：右")
        while True:
            move = input("请输入移动方向:")
            if move == "A":
                self.controller.left_shift()
                self.controller.add_2_to_list_2048()
                self.controller.print_interface_of_game()
            elif move == "D":
                self.controller.right_shift()
                self.controller.add_2_to_list_2048()
                self.controller.print_interface_of_game()
            elif move == "W":
                self.controller.up_shift()
                self.controller.add_2_to_list_2048()
                self.controller.print_interface_of_game()
            elif move == "S":
                self.controller.down_shift()
                self.controller.add_2_to_list_2048()
                self.controller.print_interface_of_game()
            else:
                print("输入有误!重新输入!")
                continue
