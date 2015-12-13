# -*- coding: utf-8 -*-
"""
Description: Code for plotting GMMs
"""

from plot_normal import draw2dnormal

def draw2dgmm(gmm, show = False, axes = None):
    
    for comp in gmm.comps:
        draw2dnormal(comp)
