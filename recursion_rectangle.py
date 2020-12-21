'''Drawing of nested squares with recursion

'''

import time
import graphics as gr

def fractal_rectangle(vert_a, vert_b, vert_c, vert_d, deep = 8):
    '''Drawing rectangle by it's vertexes positions

    Keyword arguments:
    vert_a, vert_b, vert_c, vert_d -- corteges of two int coordinates
                                      х and y ((0.0, 0.0))
    deep -- deep of recursion drawing

    '''
    if deep < 1:
        return
    for vert_m, vert_n in ((vert_a, vert_b), (vert_b, vert_c),
        (vert_c, vert_d), (vert_d, vert_a)):
        gr.Line(gr.Point(*vert_m), gr.Point(*vert_n)).draw(win)
    vert_a1 = (vert_a[0] * (1 - SHIFT_K) + vert_b[0] * SHIFT_K,
        vert_a[1] * (1 - SHIFT_K) + vert_b[1] * SHIFT_K)
    vert_b1 = (vert_b[0] * (1 - SHIFT_K) + vert_c[0] * SHIFT_K,
        vert_b[1] * (1 - SHIFT_K) + vert_c[1] * SHIFT_K)
    vert_c1 = (vert_c[0] * (1 - SHIFT_K) + vert_d[0] * SHIFT_K,
        vert_c[1] * (1 - SHIFT_K) + vert_d[1] * SHIFT_K)
    vert_d1 = (vert_d[0] * (1 - SHIFT_K) + vert_a[0] * SHIFT_K,
        vert_d[1] * (1 - SHIFT_K) + vert_a[1] * SHIFT_K)
    fractal_rectangle(vert_a1, vert_b1, vert_c1, vert_d1, deep - 1)

win = gr.GraphWin("Russian game", 300, 300)

SHIFT_K = 0.1
fractal_rectangle((2, 2), (202, 2), (202, 202), (2, 202), 100)
time.sleep(10)
