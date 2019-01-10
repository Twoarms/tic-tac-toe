# Tic-Tac-Toe

import random

def drawBoard(board):
    #Cette fonction affiche le tableau entré

    #"board' est une list de 10 strings representant board, ignore index 0
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def inputPlayerLetter():
    #Choix du joueur pour X ou O, retourne liste avec lettre du joueur comme premier element et celle ordi deuxieme
    letter = ''
    while not (letter == 'X' or letter == 'O':
        print('Voulez-vous être X ou O ?')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else :
        return ['O', 'X']

def whoGoesFirst():
        #Choisis premier joueur au hasard
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    #Donné un tableau et la lettre du joeur, retourne True si joueur a gagné
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or #hhaut
            (bo[4] == le and bo[5] == le and bo[6] == le) or #hmilieu
            (bo[1] == le and bo[2] == le and bo[3] == le) or #hbas
            (bo[7] == le and bo[4] == le and bo[1] == le) or #vgauche
            (bo[8] == le and bo[5] == le and bo[2] == le) or #vmilieu
            (bo[9] == le and bo[6] == le and bo[3] == le) or #vdroite
            (bo[7] == le and bo[5] == le and bo[3] == le) or
            (bo[9] == le and bo[5] == le and bo[1] == le))
