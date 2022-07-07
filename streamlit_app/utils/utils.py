import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import os

def image_path(file):
    return os.path.relpath(os.path.join(os.path.abspath(".."),"images", file))

def v_spacer(height, sb=False) -> None:
    for _ in range(height):
        if sb:
            st.sidebar.write('\n')
        else:
            st.write('\n')

def color_func(val):
    return (1-val, val, 0) #RGB values

def percent_bar(vals):
    fig = plt.figure(figsize=(10,0.5))
    ax = [None]*len(vals)
    for i in range(len(vals)):
        val = vals[i]
        ax[i] = fig.add_subplot(1,len(vals),i+1)
        ax[i].barh([0.5], [val], height=1, color=color_func(val))
        ax[i].axis('off')
        ax[i].set_xlim(0,1)
        ax[i].set_ylim(0,1)
        ax[i].add_patch(Rectangle((0, 0),
                        1, 1,
                        fc ='none', 
                        ec ='k',
                        lw = 4) )
        ax[i].text(0.5,0.5,"{0:.0%}".format(val), ha="center", va="center")
    return fig

def pie_score(x):
    fig = plt.figure(figsize=(5,1))
    ax = fig.add_subplot(111)
    ax.pie([x, 1-x],
                labels=["lettres économisé", "Lettres non-économisé"], 
                explode=[0,0.2],
                autopct='%1.0f%%',
                pctdistance=0.5,
                labeldistance=None,
                shadow=True,
                colors=["g","r"]
            )
    ax.legend(loc=0,
            labels=["lettres économisées", "Lettres non-économisées"],
            prop={'size': 6})
    ax.axis('equal')
    return fig