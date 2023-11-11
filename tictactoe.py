from tkinter import *
import tkinter.font as font

root=Tk()
root.config(bg='darkorchid4')
root.title("Salim's TicTacToe")
box_font=font.Font(family="Bebas Neue",size=15,weight='bold')
label_font=font.Font(family="Bebas Neue",size=20,weight='bold')
exit_font=font.Font(family="Bebas Neue",size=15,weight='bold')
restart_font=font.Font(family="Bebas Neue",size=18,weight='bold')
box1=Button(root,font=box_font,height=7,width=13,bg="magenta4",fg='maroon2',activebackground='magenta4',command=lambda: click1())
box1.grid(row=0,column=0)
box2=Button(root,text="  ",font=box_font,height=7,width=13,bg="magenta4",fg="maroon2",activebackground='magenta4',command=lambda: click2())
box2.grid(row=0,column=1)
box3=Button(root,text="  ",font=box_font,height=7,width=13,bg="magenta4",fg="maroon2",activebackground='magenta4',command=lambda: click3())
box3.grid(row=0,column=2)
box4=Button(root,text="  ",font=box_font,height=7,width=13,bg="magenta4",fg="maroon2",activebackground='magenta4',command=lambda: click4())
box4.grid(row=1,column=0)
box5=Button(root,text="  ",font=box_font,height=7,width=13,bg="magenta4",fg="maroon2",activebackground='magenta4',command=lambda: click5())
box5.grid(row=1,column=1)
box6=Button(root,text="  ",font=box_font,height=7,width=13,bg="magenta4",fg="maroon2",activebackground='magenta4',command=lambda: click6())
box6.grid(row=1,column=2)
box7=Button(root,text="  ",font=box_font,height=7,width=13,bg="magenta4",fg="maroon2",activebackground='magenta4',command=lambda: click7())
box7.grid(row=2,column=0)
box8=Button(root,text="  ",font=box_font,height=7,width=13,bg="magenta4",fg="maroon2",activebackground='magenta4',command=lambda: click8())
box8.grid(row=2,column=1)
box9=Button(root,text="  ",font=box_font,height=7,width=13,bg="magenta4",fg="maroon2",activebackground='magenta4',command=lambda: click9())
box9.grid(row=2,column=2)
label1=Label(root,text="Player1 is playing",font=label_font,bg="darkorchid4",fg="maroon2")
label1.grid(row=3,column=0,columnspan=3)
exit_button=Button(root,text="Exit",font=exit_font,bg="magenta4",fg='maroon2',width=7,height=1,activebackground='magenta4',command=root.quit)
exit_button.grid(row=4,column=2)

restart_button=Button(root,text="↻",font=restart_font,bg="magenta4",fg='maroon2',width=5,height=1,activebackground='magenta4',command=lambda: restart())
restart_button.grid(row=4,column=1)

class Tictactoe:
    def __init__(self):
        self.board=[[0,0,0],[0,0,0],[0,0,0]]
        self.player1=True
        self.player2=False  

board=Tictactoe()
turns=0


def click1():
    global turns
    global box_font
    if board.player1==True:
        box1.config(text="X",state=DISABLED,disabledforeground='maroon2')
        board.board[0][0]="X"
        result=check('X',board.board)
        if result==True:
            label1.config(text="Player1 Won")
            terminate()
        elif result==False and turns==8:
            label1.config(text="Draw") 
        else:
            board.player1=False
            label1.config(text="Player2 is playing")
    else:
        box1.config(text="O",state=DISABLED,disabledforeground='maroon2')
        board.board[0][0]="O"
        result=check('O',board.board)
        if result==True:
            label1.config(text="Player2 Won")
            terminate()
        elif result==False and turns==8:
            label1.config(text="Draw")
        else:
            board.player1=True  
            label1.config(text="Player1 is playing")  
    turns+=1
def click2():
    global turns
    if board.player1==True:
        box2.config(text="X",state=DISABLED,disabledforeground='maroon2')
        board.board[0][1]="X"
        result=check('X',board.board)
        if result==True:
            label1.config(text="Player1 Won")
            terminate()
        elif result==False and turns==8:
            label1.config(text="Draw") 
        else:
            board.player1=False
            label1.config(text="Player2 is playing")
    else:
        box2.config(text="O",state=DISABLED,disabledforeground='maroon2')
        board.board[0][1]="O"
        result=check('O',board.board)
        if result==True:
            label1.config(text="Player2 Won")
            terminate()
        elif result==False and turns==8:
            label1.config(text="Draw")
        else:
            board.player1=True  
            label1.config(text="Player1 is playing")
    turns+=1
def click3():
    global turns
    if board.player1==True:
        box3.config(text="X",state=DISABLED,disabledforeground='maroon2')
        board.board[0][2]="X"
        result=check('X',board.board)
        if result==True:
            label1.config(text="Player1 Won")
            terminate()
        elif result==False and turns==8:
            label1.config(text="Draw") 
        else:
            board.player1=False
            label1.config(text="Player2 is playing")
    else:
        box3.config(text="O",state=DISABLED,disabledforeground='maroon2')
        board.board[0][2]="O"
        result=check('O',board.board)
        if result==True:
            label1.config(text="Player2 Won")
            terminate()
        elif result==False and turns==8:
            label1.config(text="Draw")
        else:
            board.player1=True  
            label1.config(text="Player1 is playing")
    turns+=1
def click4():
    global turns
    if board.player1==True:
        box4.config(text="X",state=DISABLED,disabledforeground='maroon2')
        board.board[1][0]="X"
        result=check('X',board.board)
        if result==True:
            label1.config(text="Player1 Won")
            terminate()
        elif result==False and turns==8:
            label1.config(text="Draw") 
        else:
            board.player1=False
            label1.config(text="Player2 is playing")
    else:
        box4.config(text="O",state=DISABLED,disabledforeground='maroon2')
        board.board[1][0]="O"
        result=check('O',board.board)
        if result==True:
            label1.config(text="Player2 Won")
            terminate()
        elif result==False and turns==8:
            label1.config(text="Draw")
        else:
            board.player1=True  
            label1.config(text="Player1 is playing")
    turns+=1
def click5():
    global turns
    if board.player1==True:
        box5.config(text="X",state=DISABLED,disabledforeground='maroon2')
        board.board[1][1]="X"
        result=check('X',board.board)
        if result==True:
            label1.config(text="Player1 Won")
            terminate()
        elif result==False and turns==8:
            label1.config(text="Draw") 
        else:
            board.player1=False
            label1.config(text="Player2 is playing")
    else:
        box5.config(text="O",state=DISABLED,disabledforeground='maroon2')
        board.board[1][1]="O"
        result=check('O',board.board)
        if result==True:
            label1.config(text="Player2 Won")
            terminate()
        elif result==False and turns==8:
            label1.config(text="Draw")
        else:
            board.player1=True  
            label1.config(text="Player1 is playing")
    turns+=1
def click6():
    global turns
    if board.player1==True:
        box6.config(text="X",state=DISABLED,disabledforeground='maroon2')
        board.board[1][2]="X"
        result=check('X',board.board)
        if result==True:
            label1.config(text="Player1 Won")
            terminate()
        elif result==False and turns==8:
            label1.config(text="Draw") 
        else:
            board.player1=False
            label1.config(text="Player2 is playing")
    else:
        box6.config(text="O",state=DISABLED,disabledforeground='maroon2')
        board.board[1][2]="O"
        result=check('O',board.board)
        if result==True:
            label1.config(text="Player2 Won")
            terminate()
        elif result==False and turns==8:
            label1.config(text="Draw")
        else:
            board.player1=True  
            label1.config(text="Player1 is playing")
    turns+=1
def click7():
    global turns
    if board.player1==True:
        box7.config(text="X",state=DISABLED,disabledforeground='maroon2')
        board.board[2][0]="X"
        result=check('X',board.board)
        if result==True:
            label1.config(text="Player1 Won")
            terminate()
        elif result==False and turns==8:
            label1.config(text="Draw") 
        else:
            board.player1=False
            label1.config(text="Player2 is playing")
    else:
        box7.config(text="O",state=DISABLED,disabledforeground='maroon2')
        board.board[2][0]="O"
        result=check('O',board.board)
        if result==True:
            label1.config(text="Player2 Won")
            terminate()
        elif result==False and turns==8:
            label1.config(text="Draw")
        else:
            board.player1=True  
            label1.config(text="Player1 is playing")
    turns+=1
def click8():
    global turns
    if board.player1==True:
        box8.config(text="X",state=DISABLED,disabledforeground='maroon2')
        board.board[2][1]="X"
        result=check('X',board.board)
        if result==True:
            label1.config(text="Player1 Won")
            terminate()
        elif result==False and turns==8:
            label1.config(text="Draw") 
        else:
            board.player1=False
            label1.config(text="Player2 is playing")
    else:
        box8.config(text="O",state=DISABLED,disabledforeground='maroon2')
        board.board[2][1]="O"
        result=check('O',board.board)
        if result==True:
            label1.config(text="Player2 Won")
            terminate()
        elif result==False and turns==8:
            label1.config(text="Draw")
        else:
            board.player1=True  
            label1.config(text="Player1 is playing")
    turns+=1
def click9():
    global turns
    if board.player1==True:
        box9.config(text="X",state=DISABLED,disabledforeground='maroon2')
        board.board[2][2]="X"
        result=check('X',board.board)
        if result==True:
            label1.config(text="Player1 Won")
            terminate()
        elif result==False and turns==8:
            label1.config(text="Draw") 
        else:
            board.player1=False
            label1.config(text="Player2 is playing")
    else:
        box9.config(text="O",state=DISABLED,disabledforeground='maroon2')
        board.board[2][2]="O"
        result=check('O',board.board)
        if result==True:
            label1.config(text="Player2 Won")
            terminate()
        elif result==False and turns==8:
            label1.config(text="Draw")
        else:
            board.player1=True  
            label1.config(text="Player1 is playing")
    turns+=1
       

def check(char,arr):
    global turns
    flag=False 
    if turns>=4:
        if (arr[0][0]==char and arr[1][1]==char and arr[2][2]==char) or (arr[0][2]==char and arr[1][1]==char and arr[2][0]==char):
            flag=True
        else:
            for i in range(3):
                if (arr[0][i]==char and arr[1][i]==char and arr[2][i]==char) or (arr[i][0]==char and arr[i][1]==char and arr[i][2]==char):
                    flag=True
                    break
    return flag


def restart():
    global turns
    box1.config(text="",state=NORMAL)
    box2.config(text="",state=NORMAL)
    box3.config(text="",state=NORMAL)
    box4.config(text="",state=NORMAL)
    box5.config(text="",state=NORMAL)
    box6.config(text="",state=NORMAL)
    box7.config(text="",state=NORMAL)
    box8.config(text="",state=NORMAL)
    box9.config(text="",state=NORMAL)
    label1.config(text="Player1 is playing")
    turns=0
    board.player1=True
    for row in range(len(board.board)):
        for col in range(len(board.board[row])):
            board.board[row][col]=0


def terminate():
    box1.config(state=DISABLED)
    box2.config(state=DISABLED)
    box3.config(state=DISABLED)
    box4.config(state=DISABLED)
    box5.config(state=DISABLED)
    box6.config(state=DISABLED)
    box7.config(state=DISABLED)
    box8.config(state=DISABLED)
    box9.config(state=DISABLED)

root.mainloop()

