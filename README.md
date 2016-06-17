# UPNA | Sistemas Inteligentes | Othello

**Autor:** Álvaro Orduna León

**Descripción:** Proyecto número 2 de la asignatura Sistemas Inteligentes, impartida en el grado de Ingeniería Informatica por la Universidad Pública de Navarra

**Objetivo:** Implementar diferentes algoritmos de juego, para posteriormente compararlos. Los primeros algoritmos son triviales (primer movimiento posible, aleatorio, etc). El resto, conllevan algo de inteligencia, ya que estudian los movimientos posteriores mediante el método *minimax* estudiado en clase. La diferencia entre estos últimos es la forma de valorar la idoneidad de los movimientos, es decir, la *heurística*.

## Uso

La ejecución del programa es la que sigue:

    python python_gui.py [-p1] [-d1] [-p2] [-d2] [-h] [-v]

donde:

    -p1    Nombre del algoritmo del jugador 1
    -d1    Profundidad utilizada por el algoritmo del jugador 1 (por defecto: 3)
    -p2    Nombre del algoritmo del jugador 2
    -d2    Profundidad utilizada por el algoritmo del jugador 2 (por defecto: 3)
    -h,    Muestra la ayuda (en inglés)
    -v     Muestra estados parciales del juego en la consola

Los nombres de los algoritmos disponibles son:

    first, random, guzzler, minimax, alphabeta, best

## Resultados

* Las tablas representan al ganador de diferentes enfrentamientos realizados entre el algoritmo del jugador 1 y el del jugador 2.
* El algoritmo del jugador 1 viene dado por la fila, es decir, si cogemos la segunda fila, el jugador 1 opera con el algoritmo `GUZZLER`.
* El algoritmo del jugador 2 viene dado por la columna, es decir, si cogemos la última columna, el jugador 2 opera con el algoritmo `BEST`.
* El número de cada casilla indica el número del jugador que gana.

Así, en la tabla *__resultados ideales__* tenemos que en el vencendor de enfrentar el algoritmo `GUZZLER` (jugador 1) contra el algoritmo `FIRST` (jugador 2) es el jugador 1, es decir, el algoritmo `GUZZLER`.

**NOTA:** Los *__resultados ideales__* mostrados al final del documento se dan bajo la premisa:

`FIRST < GUZZLER < MINIMAX < ALPHABETA < BEST`

donde `A < B` significa que `A` es peor algoritmo de juego que `B`.

### Resultados reales

| Algoritmos | FIRST | GUZZLER | MINIMAX | ALPHABETA | BEST |
|------------|:-----:|:-------:|:-------:|:---------:|:----:|
| FIRST      | 2 | 1 | 2 | 1 | 1 |
| GUZZLER    | 1 | 2 | 2 | 2 | 2 |
| MINIMAX    | 1 | 2 | 2 | 2 | 2 |
| ALPHABETA  | 1 | 2 | 2 | 2 | 2 |
| BEST       | 1 | 2 | 2 | 2 | 2 |

### Resultados ideales

| Algoritmos | FIRST | GUZZLER | MINIMAX | ALPHABETA | BEST |
|------------|:-----:|:-------:|:-------:|:---------:|:----:|
| FIRST      | * | 2 | 2 | 2 | 2 |
| GUZZLER    | 1 | * | 2 | 2 | 2 |
| MINIMAX    | 1 | 1 | 2 | 2 | 2 |
| ALPHABETA  | 1 | 1 | 1 | 2 | 2 |
| BEST       | 1 | 1 | 1 | 1 | 2 |
