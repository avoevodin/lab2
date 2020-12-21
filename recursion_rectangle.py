# Drawing of nested squares with recursion 

import graphics as gr
import time

def fractal_rectangle(a, b, c, d, deep = 8):
    if deep < 1:
        return
    for m, n in (a, b), (b, c), (c, d), (d, a):
        gr.Line(gr.Point(*m), gr.Point(*n)).draw(win)
    a1 = (a[0] * (1 - SHIFT_K) + b[0] * SHIFT_K, 
        a[1] * (1 - SHIFT_K) + b[1] * SHIFT_K)
    b1 = (b[0] * (1 - SHIFT_K) + c[0] * SHIFT_K, 
        b[1] * (1 - SHIFT_K) + c[1] * SHIFT_K)
    c1 = (c[0] * (1 - SHIFT_K) + d[0] * SHIFT_K, 
        c[1] * (1 - SHIFT_K) + d[1] * SHIFT_K)
    d1 = (d[0] * (1 - SHIFT_K) + a[0] * SHIFT_K, 
        d[1] * (1 - SHIFT_K) + a[1] * SHIFT_K)
    fractal_rectangle(a1, b1, c1, d1, deep - 1)
    
win = gr.GraphWin("Russian game", 300, 300)
    
SHIFT_K = 0.1    
fractal_rectangle((2, 2), (202, 2), (202, 202), (2, 202), 100)
time.sleep(10)