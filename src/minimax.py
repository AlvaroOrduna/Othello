# -*- coding: utf-8 -*-
# minimax:

import sys

ALGORITHM_FIRST = 0
ALGORITHM_RANDOM = 1
ALGORITHM_GUZZLER = 2
ALGORITHM_MINIMAX_DEEP = 3
ALGORITHM_MINIMAX_DEEP_ALPHA_BETA = 4
ALGORITHM_BEST = 5

algorithmP1 = ALGORITHM_BEST
algorithmP2 = ALGORITHM_RANDOM

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
        return minimaxDeepAlphaBeta(game, 3, 3, -INFINITE, INFINITE, not False)
    elif algorithm == ALGORITHM_BEST:
        return best(game, 3, 3, -INFINITE, INFINITE, not False)
    else:
        if game.player == -1:
            sys.exit("ERROR: Unknown algorithm for player 1")
        elif game.player == 1:
            sys.exit("ERROR: Unknown algorithm for player 2")
        else:
            sys.exit("ERROR: Unknown algorithm for unknown player")


###############################################################################
# OBJETIVO 0: Devolver el primer movimiento posible                           #
###############################################################################
def first(game):
    """ Returns the first of the valid movements """
    moves = game.generate_moves()
    return (1, moves[0])


###############################################################################
# OBJETIVO 1: Devolver un movimiento al azar                                  #
###############################################################################
def random(game):
    """ Returns one of the valid random movements """
    import random

    moves = game.generate_moves()
    return (1, random.choice(moves))


###############################################################################
# OBJETIVO 2: Devolver el siguiente movimiento que más piezas coma            #
###############################################################################
def guzzler(game):
    """ Returns the movement which eat more pieces """
    moves = game.generate_moves()
    bestScore = -100

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
        if bestScore <= newScore:
            nextMove = move

    return (1, nextMove)


###############################################################################
# OBJETIVO 3: Implementar el algoritmo minimax y devolver la jugada que nos   #
#             haga tener más piezas a una profundidad dada (2, 4, 6...)       #
###############################################################################
def minimaxDeep(game, deep, maxDeep, maxPlayer):
    """ Implements minimax algorithm and returns the movement
        which give us more pieces in a given depth """

    if game.terminal_test() or deep == 0:
        # Si el juego ha terminado o si la profundidad
        # es la máxima posible, devolvemos la puntuación
        # del tablero como heurística.
        return game.score()

    if maxPlayer:
        # Si estamos jugando con MAX (máquina), entonces
        # devolver el mejor movimiento posible, es decir,
        # el que más fichas coma.
        bestScore = -INFINITE
        moves = game.generate_moves()

        for move in moves:
            tempGame = game.copy()
            tempGame.play_move(move)
            newScore = -minimaxDeep(tempGame, deep - 1, maxDeep, not maxPlayer)
            if bestScore <= newScore:
                bestScore = newScore
                nextMove = move

    else:
        # Si estamos jugando con MIN (humano), entonces
        # devolver el peor movimiento posible, es decir,
        # el que menos fichas coma.
        bestScore = INFINITE
        moves = game.generate_moves()

        for move in moves:
            tempGame = game.copy()
            tempGame.play_move(move)
            newScore = -minimaxDeep(tempGame, deep - 1, maxDeep, not maxPlayer)
            if bestScore >= newScore:
                bestScore = newScore
                nextMove = move

    if deep == maxDeep:
        # Si deep es igual a maxDeep es que hemos
        # vuelto a la raíz del árbol y por lo tanto
        # tenemos que devolver el siguiente movimiento.
        return (1, nextMove)
    else:
        # Si no, debemos devolver el resultado de aplicar
        # este movimiento.
        return bestScore


###############################################################################
# OBJETIVO 4: Mejorar el algoritmo minimaxDeep con la poda alfa – beta        #
###############################################################################
def minimaxDeepAlphaBeta(game, deep, maxDeep, alpha, beta, maxPlayer):
    """ Implements minimax algorithm with alpha-beta pruning
        and returns the movement which give us more pieces in
        a given depth """

    last_alpha = -INFINITE

    moves = game.generate_moves()

    # Como estamos en MAX (es el primer movimiento)
    # hacemos la poda de beta.
    for move in moves:
        # Para cada movimiento posible,
        # calculamos alpha expandiendo sus
        # hijos.
        tempGame = game.copy()
        tempGame.play_move(move)
        alpha = max(alpha, alphaBeta(tempGame, deep - 1,
                                     maxDeep, alpha, beta, not maxPlayer, 'simple'))

        # Realizamos la poda beta
        # nextMove será el mejor de los
        # movimientos posibles, es decir,
        # el que mayor alpha tenga.
        if last_alpha <= alpha:
            nextMove = move

    return (1, nextMove)


###############################################################################
# OBJETIVO 5: Mejorar el algoritmo minimaxDeepAlphaBeta con la creación de    #
#             una heurística que contemple la relevancia de las posiciones    #
###############################################################################
def best(game, deep, maxDeep, alpha, beta, maxPlayer):
    """ Implements minimax algorithm with alpha-beta pruning
        and returns the movement which give us more pieces in
        a given depth. The difference with this is that it
        implements a more complex heuristic. """

    last_alpha = -INFINITE

    moves = game.generate_moves()

    # Como estamos en MAX (es el primer movimiento)
    # hacemos la poda de beta.
    for move in moves:
        # Para cada movimiento posible,
        # calculamos alpha expandiendo sus
        # hijos.
        tempGame = game.copy()
        tempGame.play_move(move)
        alpha = max(alpha, alphaBeta(tempGame, deep - 1,
                                     maxDeep, alpha, beta, not maxPlayer, 'weighted'))

        # Realizamos la poda beta
        # nextMove será el mejor de los
        # movimientos posibles, es decir,
        # el que mayor alpha tenga.
        if last_alpha <= alpha:
            nextMove = move

    return (1, nextMove)


###############################################################################
# OBJETIVOS 4 y 5: Fucnión alphaBeta encargada de expandir y podar            #
###############################################################################
def alphaBeta(game, deep, maxDeep, alpha, beta, maxPlayer, heuristic):
    """ Expand the child nodes in search of the best.
        The heuristic used is given by the last argument.
        It can be:
            * simple:       it is the game score.
            * weighted:     it is a weighted sum of the score,
                            which takes into account the best and
                            worst positions. """

    if game.terminal_test() or deep == 0:
        # Si el juego ha terminado o si la profundidad
        # es la máxima posible, devolvemos la puntuación
        # del tablero como heurística.
        if heuristic == 'simple':
            return game.score()
        elif heuristic == 'weighted':
            return bestHeuristic(game)

    moves = game.generate_moves()

    if maxPlayer:
        for move in moves:
            # Para cada movimiento posible,
            # calculamos alpha expandiendo sus
            # hijos.
            tempGame = game.copy()
            tempGame.play_move(move)
            alpha = max(alpha, alphaBeta(tempGame, deep - 1,
                                         maxDeep, alpha, beta, False, heuristic))

            # Realizamos la poda beta
            if beta <= alpha:
                break
        return alpha

    else:
        for move in moves:
            # Para cada movimiento posible,
            # calculamos beta expandiendo sus
            # hijos.
            tempGame = game.copy()
            tempGame.play_move(move)
            beta = min(beta, alphaBeta(tempGame, deep - 1,
                                       maxDeep, alpha, beta, not False, heuristic))

            # Realizamos la poda alpha
            if beta <= alpha:
                break
        return beta


###############################################################################
# OTROS: Funciones necesarias para el correcto funcionamiento del resto de    #
#        objetivos                                                            #
###############################################################################
def bestHeuristic(game):
    """ Calculates a score considering that:
        * "corner":        the corners are the best positions
        * "edge":          the edges are also good positions
        * "nearby edge":   the positions next to the edges are bad
        * "nearby corner": among the bad positions, the worst are the four corners """

    # Establecer los pesos de cada tipo de casilla
    cornerWeight = 200
    edgeWeight = 100
    cornerNearbyWeight = -200
    edgeNearbyWeight = -100
    restWeight = 1

    score = 0

    for i in range(8):
        for j in range(8):
            if isCorner(8, i, j):
                score += cornerWeight * game.board[i][j]
            elif isEdge(8, i, j):
                score += edgeWeight * game.board[i][j]
            elif isNearbyCorner(8, i, j):
                score += cornerNearbyWeight * game.board[i][j]
            elif isNearbyEdge(8, i, j):
                score += edgeNearbyWeight * game.board[i][j]
            else:
                score += restWeight * game.board[i][j]

    return score * game.player


def isCorner(size, i, j):
    """ Returns true if the given position is an corner """
    return (i == 0 and i == 0) or (i == 0 and j == size) or (i == size and j == 0) or (i == size and j == size)


def isEdge(size, i, j):
    """ Returns true if the given position is an edge """
    return (i == 0) or (j == 0) or (i == size) or (j == size)


def isNearbyCorner(size, i, j):
    """ Returns true if the given position is an nearby corner """
    return (i == 1 and i == 1) or (i == 1 and j == size - 1) or (i == size - 1 and j == 1) or (i == size - 1 and j == size - 1)


def isNearbyEdge(size, i, j):
    """ Returns true if the given position is an nearby edge """
    return (i == 1) or (j == 1) or (i == size - 1) or (j == size - 1)
