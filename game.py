import time
import sys
import os


def menu():
    choose = ""
    msg = "GOOD-BYE"
    while choose != 'start':
        print ""
        print "Please type the option to start the game"
        print "1. Start"
        print "2. Exit"
        print ""
        choose = raw_input()
        if choose == 'exit':
            for i in range(len(msg)):
                print msg[i],
                time.sleep(.5)
            if raw_input() == "":
                sys.exit()

    return choose

def instructions():
    os.system('cls')
    print "INSTRUCTIONS FOR THE GAME TO PLAY: "
    print """
    1. The game objective is to command the mouse to reach the goal point.
    2. You should not hit the walls which are printed as 1. If hit the game is over.
    3. You should type "up" for moving the mouse upward
    4. "down" for moving downward
    5. "right" for moving towards right
    6. "left" for moving towards left
    """
    print "Press 'Enter' to play the game"
    if raw_input() == "":
        pass

def modifymaze(maze):

    maze[1][1] = 1
    maze[1][2] = 1
    maze[0][1] = 1
    maze[2][1] = 1
    maze[0][1] = 1
    maze[3][3] = 1
    maze[0][2] = 'G'
    return maze
def display(current, new_maze):
    new_maze[current[0]][current[1]] = 'H'
    for row in new_maze:
        print " ".join(map(str,row))
        print ""
    new_maze[current[0]][current[1]] = 0

    print "Choose next move"

def move(prompt, current, maze):
    i = int(current[0])
    j = int(current[1])
    try:
        if prompt == "up":
            i = i - 1
            if i == -1:
                raise Exception("out")
        if prompt == "down":
            i = i + 1
            if i == 4:
                raise Exception("out")
        if prompt == "left":
            j = j - 1
            if j == -1:
                raise Exception("out")
        if prompt == "right":
            j = j + 1
            if j == 4:
                raise Exception("out")
    except Exception, e:
        out = "OUT OF MAZE!"
        for i in range(len(out)):
            print out[i],
            time.sleep(.5)
        print "GAME OVER!!!"
        print "Press Enter"
        if raw_input() == "":
            sys.exit()
    current[0] = i
    current[1] = j
    return current

def ishit(current, maze):
    i = current[0]
    j = current[1]
    wall = "YOU HIT THE WALL!!!"
    won = "YOU REACHED THE GOAL. YOU WIN!!!"
    if maze[i][j] == 1:
        for i in range(len(wall)):
            print wall[i],
            time.sleep(.5)

        print "GAME OVER !!!"
        time.sleep(1)
        if raw_input() == "":
            sys.exit()
    elif maze[i][j] == "G":
        for i in range(len(won)):
            print won[i],
            time.sleep(.5)
        if raw_input() == "":
            sys.exit()

    else:
        return "play"


os.system('cls')
print "Welcome to the Mouse-Maze game"
time.sleep(2)
menu()
instructions()
maze = [[0 for i in range(4)]for i in range(4)]

maze = modifymaze(maze)
prompt = ""
play = ""
current = [0,0]
while prompt != "end" or play != "over":
    os.system('cls')
    display(current, maze)
    print """
    1.Up 2.Down 3.Left 4.Right
    """
    prompt = raw_input()
    if prompt == 'end':
        print "Game Over"
        time.sleep(2)
        break
    current = move(prompt, current, maze)
    play = ishit(current, maze)
