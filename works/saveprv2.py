def displayPathtoPrincess(n,grid):
    princess, bot = [], []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'p':
                princess.append(i)
                princess.append(j)

    if bot[0] > princess[0]:
        if bot[1] > princess[1]:
            for arr in range (bot[0]-princess[0]):
                print("UP")
            for b in range (bot[1]-princess[1]):
                print("LEFT")
        else:
            for arr in range (bot[0] - princess[0]):
                print("UP")
            for b in range (princess[1]-bot[1]):
                print("RIGHT")
    else:
        if bot[1] > princess[1]:
            for arr in range (princess[0]-bot[0]):
                print("DOWN")
            for b in range (bot[1]-princess[1]):
                print("LEFT")
        else:
            for arr in range (princess[0]-bot[0]):
                print("DOWN")
            for b in range (princess[1]-bot[1]):
                print('RIGHT')
