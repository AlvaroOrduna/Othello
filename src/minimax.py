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
algorithmP2 = ALGORITHM_MINIMAX_DEEP_ALPHA_BETA

INFINITE = float('Inf')


def minimax(game, maxply, algorithm):
    if algorithm == ALGORITHM_FIRST:
        return first(game)
    elif algorithm == ALGORITHM_RANDOM:
        return random(game)
    elif algorithm == ALGORITHM_GUZZLER:
        return guzzler(game)
    elif algorithm == ALGORITHM_MINIMAX_DEEP:
        return minimaxDeep(game, 3, 3, not False)
    elif algorithm == ALGORITHM_MINIMAX_DEEP_ALPHA_BETA:
        return minimaxDeepAlphaBeta(game, 3, 3, INFINITE, -INFINITE, not False)
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


def minimaxDeep(game, deep, maxDeep, maxPlayer):
    """ Implements minimax algorithm and returns the movement
        which give us more pieces in a given depth """

    if game.terminal_test() or deep == 0:
        # Si el juego a terminado o si la profundidad
        # es la máxima posible, devolvemos la puntuación
        # del tablero como heurística.
        return game.score()

    if maxPlayer:
        # Si estamos jugando con MAX (máquina), entonces
        # devolver el mejor movimiento posible, es decir,
        # el que más fichas coma.
        currentScore = -INFINITE
        moves = game.generate_moves()

        for move in moves:
            tempGame = game.copy()
            tempGame.play_move(move)
            newScore = -minimaxDeep(tempGame, deep - 1, maxDeep, not maxPlayer)
            if currentScore <= newScore:
                nextMove = move

    else:
        # Si estamos jugando con MIN (humano), entonces
        # devolver el peor movimiento posible, es decir,
        # el que menos fichas coma.
        currentScore = INFINITE
        moves = game.generate_moves()

        for move in moves:
            tempGame = game.copy()
            tempGame.play_move(move)
            newScore = -minimaxDeep(tempGame, deep - 1, maxDeep, not maxPlayer)
            if currentScore >= newScore:
                nextMove = move

    if deep == maxDeep:
        # Si deep es igual a maxDeep es que hemos
        # vuelto a la raíz del árbol y por lo tanto
        # tenemos que devolver el siguiente movimiento.
        return (1, nextMove)
    else:
        # Si no, debemos devolver el resultado de aplicar
        # este movimiento.
        tempGame = game.copy()
        tempGame.play_move(nextMove)
        return tempGame.score()


def minimaxDeepAlphaBeta(game, deep, maxDeep, alpha, beta, maxPlayer):
    """ Implements minimax algorithm with alpha-beta pruning
        and returns the movement which give us more pieces in
        a given depth """

    if game.terminal_test() or deep == 0:
        # Si el juego a terminado o si la profundidad
        # es la máxima posible, devolvemos la puntuación
        # del tablero como heurística.
        return game.score()

    if maxPlayer:
        moves = game.generate_moves()

        for move in moves:
            # Para cada movimiento posible,
            # calculamos alpha expandiendo sus
            # hijos.
            tempGame = game.copy()
            tempGame.play_move(move)
            alpha = max(alpha, minimaxDeepAlphaBeta(tempGame, deep - 1,
                                                    maxDeep, alpha, beta, False))

            # Condición de salida. Hace que se mantenga
            # el valor válido de alpha y asigna el nuevo
            # valor del siguiente movimiento.
            if beta <= alpha:
                nextMove = move
                break

    else:
        moves = game.generate_moves()

        for move in moves:
            # Para cada movimiento posible,
            # calculamos beta expandiendo sus
            # hijos.
            tempGame = game.copy()
            tempGame.play_move(move)
            beta = min(beta, minimaxDeepAlphaBeta(tempGame, deep - 1,
                                                  maxDeep, alpha, beta, not False))

            # Condición de salida. Hace que se mantenga
            # el valor válido de beta y asigna el nuevo
            # valor del siguiente movimiento.
            if beta <= alpha:
                nextMove = move
                break

    if deep == maxDeep:
        # Si deep es igual a maxDeep es que hemos
        # vuelto a la raíz del árbol y por lo tanto
        # tenemos que devolver el siguiente movimiento.
        return (1, nextMove)
    elif maxPlayer:
        # Si estamos jugando con MAX debemos devolver
        # el valor de alpha
        return alpha
    else:
        # Si estamos jugando con MIN debemos devolver
        # el valor de beta
        return beta
