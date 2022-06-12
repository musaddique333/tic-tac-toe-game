import os


def screen_clear():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


def player1(p1):
    print(f"\n\t{p1} 's turn")
    t = input()
    return int(t)


def player2(p2):
    print(f"\n\t{p2} 's turn")
    t = input()
    return int(t)


def game(*g):
    screen_clear()
    print("\n\n")
    print("\t\t\t   TIC TAC TOE\n\n")
    print(f"\t\t\t  {g[0]}  |  {g[1]}  |  {g[2]} ")
    print("\t\t\t-----|-----|-----")
    print(f"\t\t\t  {g[3]}  |  {g[4]}  |  {g[5]} ")
    print("\t\t\t-----|-----|-----")
    print(f"\t\t\t  {g[6]}  |  {g[7]}  |  {g[8]} ")


def condition(p1, p2, *g):
    f = 0
    if 'X' == g[0] and "X" == g[1] and "X" == g[2]:
        print(f'{p1} is winner')
        f = 1
    elif 'X' == g[3] and "X" == g[4] and "X" == g[5]:
        print(f'{p1} is winner')
        f = 1
    elif 'X' == g[6] and "X" == g[7] and "X" == g[8]:
        print(f'{p1} is winner')
        f = 1
    elif 'X' == g[0] and "X" == g[3] and "X" == g[6]:
        print(f'{p1} is winner')
        f = 1
    elif 'X' == g[1] and "X" == g[4] and "X" == g[7]:
        print(f'{p1} is winner')
        f = 1
    elif 'X' == g[2] and "X" == g[5] and "X" == g[8]:
        print(f'{p1} is winner')
        f = 1
    elif 'X' == g[0] and "X" == g[4] and "X" == g[8]:
        print(f'{p1} is winner')
        f = 1
    elif 'X' == g[2] and "X" == g[4] and "X" == g[6]:
        print(f'{p1} is winner')
        f = 1
    elif 'O' == g[0] and "O" == g[1] and "O" == g[2]:
        print(f'{p2} is winner')
        f = 1
    elif 'O' == g[3] and "O" == g[4] and "O" == g[5]:
        print(f'{p2} is winner')
        f = 1
    elif 'O' == g[6] and "O" == g[7] and "O" == g[8]:
        print(f'{p2} is winner')
        f = 1
    elif 'O' == g[0] and "O" == g[3] and "O" == g[6]:
        print(f'{p2} is winner')
        f = 1
    elif 'O' == g[1] and "O" == g[4] and "O" == g[7]:
        print(f'{p2} is winner')
        f = 1
    elif 'O' == g[2] and "O" == g[5] and "O" == g[8]:
        print(f'{p2} is winner')
        f = 1
    elif 'O' == g[0] and "O" == g[4] and "O" == g[8]:
        print(f'{p2} is winner')
        f = 1
    elif 'O' == g[2] and "O" == g[4] and "O" == g[6]:
        print(f'{p2} is winner')
        f = 1
    return f


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
game(*a)
print("\nEnter name of player 1")
player1name = input()
print("\nEnter name of player 2")
player2name = input()
game(*a)
try:
    i = 0
    while True:
        r = condition(player1name, player2name, *a)
        num = 0
        for j in range(9):
            if a[j] == "X" or a[j] == "O":
                num += 1
        if num == 9:
            game(*a)
            print("\n\tMatch draw!!!!")
            exit()
        else:
            num = 0
        if r == 1:
            exit()
        if i % 2 == 0:
            p11 = player1(player1name)
            while p11 > 9:
                game(*a)
                print("\nplease enter a number between 1 to 9")
                p11 = player1(player1name)
            while p11 < 1:
                game(*a)
                print("\nplease enter a number between 1 to 9")
                p11 = player1(player1name)
            while p11 > 9:
                game(*a)
                print("\nplease enter a number between 1 to 9")
                p11 = player1(player1name)
            if a[p11 - 1] != "X" and a[p11 - 1] != "O":
                a[p11 - 1] = 'X'
                game(*a)
            else:
                print("\nAlready occupied")
                i += 1
        else:
            p22 = player2(player2name)
            while p22 > 9:
                game(*a)
                print("\nplease enter a number between 1 to 9")
                p22 = player2(player2name)
            while p22 < 1:
                game(*a)
                print("\nplease enter a number between 1 to 9")
                p22 = player2(player2name)
            while p22 > 9:
                game(*a)
                print("\nplease enter a number between 1 to 9")
                p22 = player2(player2name)
            if a[p22 - 1] != "X" and a[p22 - 1] != "O":
                a[p22 - 1] = 'O'
                game(*a)
            else:
                game(*a)
                print("\nAlready occupied")
                i += 1
        i += 1
except Exception as e:
    print(e)
print("\n\twrong input")
