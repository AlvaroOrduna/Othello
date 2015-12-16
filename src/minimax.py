# minimax:


def minimax(game, maxply, algorithm):
    if algorithm == 0:
        return first(game)
    elif algorithm == 1:
        return random(game)
    elif algorithm == 2:
        return guzzler(game)
    elif algorithm == 3:
        return minmaxDeep(game, deep)
    elif algorithm == 4:
        return minmaxDeepAlphaBeta(game, deep)
    else:
        return best(game)
