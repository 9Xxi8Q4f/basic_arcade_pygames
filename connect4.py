import pygame
import numpy as np
import sys
import math

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def win_status(board, piece):
	# Check horizontal locations for win
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT):
			if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
				return True

	# Check vertical locations for win
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT-3):
			if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
				return True

	# Check positively sloped diaganols
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT-3):
			if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
				return True

	# Check negatively sloped diaganols
	for c in range(COLUMN_COUNT-3):
		for r in range(3, ROW_COUNT):
			if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
				return True

def print_board(board):
    print(np.flip(board, 0))

game_over = False
board = create_board()
turn= 0
win_status = False

while not game_over:

    #ask for player 1 input
    if turn == 0:
        selection = input("Player 1 Make your Selection (0-6):")
        selection = int(selection)

        if is_valid_location(board, selection):
            row = get_next_open_row(board, selection)
            drop_piece(board, row, selection, 1)

            if win_status(board, 1):
                print("Player 1 Wins!")
                game_over = True

    #ask for player 2 input
    else:
        selection = input("Player 2 Make your Selection (0-6):")
        selection = int(selection)

        if is_valid_location(board, selection):
            row = get_next_open_row(board, selection)
            drop_piece(board, row, selection, 2)

            if win_status(board, 2):
                print("Player 2 Wins!")
                game_over = True

    turn += 11
    turn %= 2
    print_board(board)