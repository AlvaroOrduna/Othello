# Proyecto 2 - Othello

**Autor:** Álvaro Orduna León

**Descripción:** Proyecto número 2 de la asignatura Sistemas Inteligentes, impartida en el grado de Ingeniería Informatica por la Universidad Pbulica de Navarra

**Objetivo:** Implementar diferentes algoritmos de juego, para posteriormente compararlos. Los primeros algoritmos son triviales (primer movimiento posible, aleatorio, etc). El resto, conllevan algo de inteligencia, ya que estudian los movimientos posteriores mediante el método *minimax* estudiado en clase. La diferencia entre estos últimos es la forma de valorar la idoneidad de los movimientos, es decir, la *heurística*.

**Resultados:** La fila representa al algoritmo 1 y la columna al algoritmo 2. El primer valor de cada casilla indica el número del algoritmo ganador y el segundo la puntuación final del ganador.

| Algoritmos | FIRST | GUZZLER | MINIMAX_1 | MINIMAX_2 |
|------------|:-----:|:-------:|:---------:|:---------:|
| GUZZLER    | 1, 34 |         |           |           |
| MINIMAX_1  | 1, 34 | 2, 26   |           |           |
| MINIMAX_2  | 1, 34 | 2, 26   | 2, 26     |           |
| BEST       | 1, 34 | 2, 26   | 2, 26     | 2, 26     |
