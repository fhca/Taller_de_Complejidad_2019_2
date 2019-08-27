import numpy as np
import matplotlib.pyplot as plt


def dimension_fractal(orb):
    """(orb.real, orb.imag)"""
    # pares = orb.view('(2,)float')  # ver complejos como par de reales
    # pares = np.array((orb.real, orb.imag)).T
    # escalas = np.logspace(6, 15, num=16, endpoint=True, base=2)
    escalas = np.logspace(0.01, 10, num=16, endpoint=False, base=2)
    ns = []
    for escala in escalas:
        h, _, _ = np.histogram2d(orb.real, orb.imag, bins=(escala, escala))
        n = np.sum(h > 0)
        ns.append(n)
        if n >= orb.shape[0]:
            # if TRACE: print("biip!")
            break
    coeffs = np.polyfit(np.log2(escalas[:len(ns)]), np.log2(ns), 1)
    return coeffs[0]
