import draw

def main():
    prc = 0.6
    sides = 6
    for i in range(1,11):
        n = 100*i
        draw.draw_flake(sides,n,prc)

if __name__ == "__main__":
    main()