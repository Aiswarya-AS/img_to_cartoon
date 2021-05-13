import curses
from random import randint

WINDOW_WIDTH = 60  # number of columns of window box
WINDOW_HEIGHT = 20 # number of rows of window box
#setupwindow
curses.initscr()
win=curses.newwin(WINDOW_HEIGHT,WINDOW_WIDTH,0,0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)


#snake and food
snake=[(4,4),(4,3),(4,2)]
food=(6,6)
win.addch(food[0],food[1],'#')


#game logic
score=0
ESC=27
key=curses.KEY_RIGHT
while key!=ESC:
    win.addch(0,2,'score' +str(score)+' ')
    win.timeout(150-(len(snake))//5 +len(snake)//10 % 120) #increase speed
    prev_key=key
    event=win.getch()
    key=event if event !=-1 else prev_key
    if key not in(curses.KEY_RIGHT,curses.KEY_LEFT,curses.KEY_UP,curses.KEY_DOWN,ESC):
     key=prev_key


    #calculate the next coordination
    y = snake[0][0]
    x = snake[0][1]
    if key == curses.KEY_DOWN:
        y += 1
    if key==curses.KEY_UP:
        y -= 1
    if key==curses.KEY_LEFT:
        x -= 1
    if key == curses.KEY_DOWN:
        x += 1
    snake.insert(0, (y, x))

   #check if we hit the border
    if y == 0:
        break
    if y == WINDOW_HEIGHT-1:
        break
    if x == 0:
        break
    if x == WINDOW_WIDTH:
        break



    #sanke run over itself
    if snake[0] in snake[1:]:break
    if snake[0]==food:
        # eat food
        food=()
        while food == ():
            food=(randint(1,WINDOW_HEIGHT-2),randint(1,WINDOW_WIDTH-2))
            if food in snake:
                food=()
        win.addch(food[0],food[1],'#')
    else:


        #move snake
        last=snake.pop()
        win.addch(last[0],last[1],' ')

    win.addch(snake[0][0],snake[0][1],'*')
curses.endwin()
print(f"final score={score}")


