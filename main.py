import numpy as np

'''------------------------------------常數設定-----------------------------------'''
LAYER = 3
'''------------------------------------定義函式-----------------------------------'''


# 建立layer^2個空白string  - clear
def clear_table():
    new_table = np.full(LAYER ** 2, " ")
    return new_table


# 設定分格線的函數
def print_dash(n):
    dash = ""
    # range 裡面設的公式是用來讓分隔線呈現好看一點。
    for i in range(n*4-2):
        dash += "-"
    return dash


# 顯示表格與當前結果
def show_table(t):
    for n in range(len(t)//LAYER):
        i = n*LAYER
        print(" | ".join(t[i:(i+LAYER)]))
        # 執行到最後一次時，不要加上「---------」
        if n != (len(t)//LAYER - 1):
            print(print_dash(LAYER))


# Greeting and explain how to play this game
def show_rule():
    print(f"How to play this Tic Tac Toe game? \nPlease enter a number that is chosen from 1 to {LAYER ** 2} "
          f"to put your symbol in the place below.\nYou can't put your symbol in the same position "
          f"if that position has been occupied.\n")
    show_table(numbers)
    print("\nPlayer 1: Your symbol is 'O'.\nPlayer 2: Your symbol is 'X'.\n")
    print("Let's get started.")


# 執行詢問要放的位置之函數
def enter(n):
    who = [k for k, v in player.items() if v == n][0]
    return input(f"Now, It's {who}'s turn. Which position do you want to occupy? "
                 f"Please enter the number of the position :\n")


# 玩家執行遊戲，決定要放置的位置，並顯示結果
def your_turn(who):
    try:
        put = int(enter(who))
        if table[put-1] != " ":
            print("This position has been occupied, Please choose another position.")
            your_turn(who)
        else:
            table[put-1] = who
    except ValueError:
        print(f"Sorry, please enter a number that is chosen from 1 to {LAYER ** 2}"
              f" to put your symbol in the place below.")
        your_turn(who)
    # 顯示目前結果
    show_table(table)


def check_win(tables):
    row = tables.reshape(LAYER, LAYER)
    column = row.T
    for n in range(LAYER):
        # 做「橫向」確認加總symbols數，看是否連一直線。透過np.sum的方式，來加總"O/x"數量。
        row_player1 = np.sum(row[n] == player["Player 1"])
        row_player2 = np.sum(row[n] == player["Player 2"])
        # 做「直向」確認加總symbols數，看是否連一直線。
        column_player1 = np.sum(column[n] == player["Player 1"])
        column_player2 = np.sum(column[n] == player["Player 2"])
        if LAYER in [row_player1, column_player1]:
            print("Game over!")
            print("The winner is Player 1.")
            return True
        if LAYER in [row_player2, column_player2]:
            print("Game over!")
            print("The winner is Player 2.")
            return True
    # 處理「斜邊」連線，從左上到右下，間隔LAYER+1會連成一線，；右上到左下，間隔LAYER-1，會連成一線。
    hypotenuse1_player1 = np.sum(tables[::LAYER+1] == player["Player 1"])
    hypotenuse2_player1 = np.sum(tables[LAYER-1::LAYER-1] == player["Player 1"])
    hypotenuse1_player2 = np.sum(tables[0::LAYER+1] == player["Player 2"])
    hypotenuse2_player2 = np.sum(tables[LAYER-1::LAYER-1] == player["Player 2"])
    if LAYER in [hypotenuse1_player1, hypotenuse2_player1]:
        print("Game over!")
        print("The winner is Player 1.")
        return True
    if LAYER in [hypotenuse1_player2, hypotenuse2_player2]:
        print("Game over!")
        print("The winner is Player 2.")
        return True
    # 處理「平手」
    if " " not in table:
        print("Game over!")
        print("It's a draw.")
        return True


'''------------------------------------0. 前置作業-----------------------------------'''
player = {"Player 1": "O", "Player 2": "X"}
numbers = [str(n) for n in range(1, LAYER ** 2+1)]


'''------------------------------------1. 開始遊戲-----------------------------------'''
is_play = True
while is_play:
    show_rule()
    # 建立一個空白表格list來放本次遊戲。
    table = clear_table()
    show_table(table)

    is_end = False
    # take turn，餘數偶數時player 1，單數則換player 2放。
    n = 2
    while not is_end:
        if n % 2 == 0:
            your_turn(player["Player 1"])
        else:
            your_turn(player["Player 2"])
        n += 1
        is_end = check_win(table)

    # 當遊戲結束時，詢問是否繼續玩，若輸入「y」，則繼續玩，否則則退出遊戲。
    if is_end:
        is_continue = input("If you want to play it again, please enter 'y'. ").lower()
        if is_continue != "y":
            is_play = False
