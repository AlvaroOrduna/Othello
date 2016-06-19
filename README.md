# UPNA | Intelligent Systems
## Project #2: Othello

__Author:__ [Álvaro Orduna León](https://github.com/AlvaroOrduna)

__Description:__ second project for the subject Intelligent Systems imparted in the Degree of Computer Science from the Public University of Navarra (UPNA)


### Goal

Implement different game algorithms, to later compare them. The first algorithms are trivial (first possible move, random ...). The rest involve some intelligence, because they study subsequent moves by the _minimax method_. The difference between them is how to assess the suitability of movements, ie _heuristics_.

### Usage

    python python_gui.py [-p1] [-d1] [-p2] [-d2] [-h] [-v]

        -p1    Player 1 algorithm
        -d1    Depth for player 1 (default: 3)
        -p2    Player 2 algorithm
        -d2    Depth for player 2 (default: 3)
        -h,    Show this help
        -v     Shows partial state gaming console

The names of the available algorithms are:

    first, random, guzzler, minimax, alphabeta, best

### License (MIT)

    Copyright (c) 2016 Álvaro Orduna León

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
