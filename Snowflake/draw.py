from point import Point
import matplotlib.pyplot as plt
from math import cos,sin,pi
from random import randint
from time import time

def starting_points(n):
    # n is the amount of points we want at the beginning
    points = []
    if n<4:
        print("There should be at least 4 points")
        return

    angle = 2/n*pi

    for i in range(n):
        points.append(Point(cos(angle*(i+1)),sin(angle*(i+1))))
        
    return points

def draw_flake(sides,n,prc):
    
    t = time()
    _, ax = plt.subplots()
    
    points = starting_points(sides)
    for point in points:
        ax.scatter(point.x,point.y,s=5,c="k")

    inx_lim = sides-1
    n_prc = 1-prc

    rand1 = randint(0,inx_lim)
    rand2 = randint(0,inx_lim)
    curr = points[rand1].mid_point(points[rand2],prc,n_prc)

    for _ in range(n):
        ax.scatter(curr.x, curr.y, s=3, c="b")
        rand = randint(0,inx_lim)
        curr = curr.mid_point(points[rand],prc,n_prc)

    ax.set_title(f"Snowflake\nn = {n}, prc = {prc}")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_xlabel(f"Elapsed time: {round(time()-t,2)} seconds")

    plt.savefig(f"n{n}prc{int(prc*100)}.png")
