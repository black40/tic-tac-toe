#!/usr/env/bin python
import os
import copy
from random import choice


board = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}


def show_board(b):
    os.system('clear')
    for k, v in b.items():
        print(v, end=' ')
        if not k % 3:
            print()
    print('-' * 23)


win_lines = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
             [1, 4, 7], [2, 5, 8], [3, 6, 9],
             [1, 5, 9], [3, 5, 7]]
user_win_lines = copy.deepcopy(win_lines)
comp_win_lines = copy.deepcopy(win_lines)
checklist = [i for i in range(1, 10)]


def find_win_line(line):
    if all(line):
        return False
    return True


def user_move():
    if checklist:
        try:
            num = int(input('Enter number [1 - 9]: '))
            checklist.remove(num)
            board[num] = 'X'
            for line in user_win_lines:
                if num in line:
                    line.remove(num)
        except ValueError:
            print('Enter number [1 - 9]')
            user_move()


def comp_move():
    if checklist:
        num = choice(checklist)
        checklist.remove(num)
        board[num] = 'O'
        for line in comp_win_lines:
            if num in line:
                line.remove(num)


def main():
    show_board(board)
    user_move()
    comp_move()


def determine_winner():
    if find_win_line(user_win_lines):
        return 'User is Winner'
    if find_win_line(comp_win_lines):
        return 'Comp is Winner'
    return 'Draw in Game'


if __name__ == '__main__':
    while not find_win_line(user_win_lines + comp_win_lines) and checklist:
        main()
    show_board(board)
    if determine_winner:
        print(determine_winner())
    print()
