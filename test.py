print(sum(map(lambda g:
    sum(sum(map(i.__ge__, g)) * (i in g or 1000000) * 
        sum(map(i.__lt__, g)) for i in range(max(g))),
    zip(*[(x,y) for y,r in enumerate(open('day11/day11_input.txt'))
                for x,c in enumerate(r) if c=='#']))))