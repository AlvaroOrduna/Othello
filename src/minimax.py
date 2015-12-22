# -*- coding: utf-8 -*-
# minimax:

import sys

ALGORITHM_FIRST = 0
ALGORITHM_RANDOM = 1
ALGORITHM_GUZZLER = 2
ALGORITHM_MINIMAX_DEEP = 3
ALGORITHM_MINIMAX_DEEP_ALPHA_BETA = 4
ALGORITHM_BEST = 5


algorithmP1 = ALGORITHM_RANDOM
algorithmP2 = ALGORITHM_GUZZLER


def minimax(game, maxply, algorithm):
    if algorithm == ALGORITHM_FIRST:
        return first(game)
    elif algorithm == ALGORITHM_RANDOM:
        return random(game)
    elif algorithm == ALGORITHM_GUZZLER:
        return guzzler(game)
    elif algorithm == ALGORITHM_MINIMAX_DEEP:
        return minimaxDeep(game, deep)
    elif algorithm == ALGORITHM_MINIMAX_DEEP_ALPHA_BETA:
        return minimaxDeepAlphaBeta(game, deep)
    elif algorithm == ALGORITHM_BEST:
        return best(game)
    else:
        if game.player == -1:
            sys.exit("ERROR: Unknown algorithm for player 1")
        elif game.player == 1:
            sys.exit("ERROR: Unknown algorithm for player 2")
        else:
            sys.exit("ERROR: Unknown algorithm for unknown player")


def first(game):
    """ Returns the first of the valid movements """
    moves = game.generate_moves()
    return (1, moves[0])


def random(game):
    """ Returns one of the valid random movements """
    import random

    moves = game.generate_moves()
    return (1, random.choice(moves))


def guzzler(game):
    """ Returns the movement which eat more pieces """
    moves = game.generate_moves()
    currentScore = -100

    for move in moves:
        # Copiamos el tablero para volver
        # al estado inicial de la función
        tempGame = game.copy()

        # Ejecutamos el siguiente movimiento
        tempGame.play_move(move)

        # Obtenemos la puntuación obtenida
        # al ejecutar el nuevo movimiento
        newScore = -1 * tempGame.score()

        # Si la nueva puntuación es mayor que
        # la mejor hasta
        if currentScore <= newScore:
            nextMove = move

    return (1, nextMove)
