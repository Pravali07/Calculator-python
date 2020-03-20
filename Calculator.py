#import everything from tkinter
from tkinter import *
#import font module
import tkinter.font as font


#declaring global variables
expression=""
flag = 0
wrong = 0

def press(num):
    #pointing out global variables
    global expression
    global flag, wrong

    #concatenating expression variable
    expression=expression+str(num)

    #updating the expression by using set
    equation.set(expression)

    #checking whether more than one operator is given consecutively like '8++'
    if str(num).isdigit():
        flag = 0
    else:
        flag += 1
    if flag == 2:
        wrong = 1

#function for clear button
def clear():
    #pointing out global variables
    global expression
    expression=""

    #clearing the contents in entry field
    equation.set(" ")

    
#function for displaying output when pressed "="
def equal():
    #pointing out the global variables
    global flag, wrong
    global expression

    #displaying error when more than one operator is given consecutively like '8++'
    if wrong == 1:
            equation.set("ERROR")
            expression=""
    else:

    #here we use try and except so that it helps in handling the error like 'division by zero' etc
        try:
            #eval function is used to evaluate the given expression
            total=str(eval(expression))
            equation.set(total)

            #initializing the expression variable by empty string
            expression=""

        #if any error occurs, it will be handled by except block
        except:
            equation.set("ERROR")
            expression=""
    flag = 0

if __name__=="__main__":

    #creating the root window
    master=Tk()

    #set the title for the window
    master.title('Calculator')

    #set the configuration for the window
    master.geometry('650x480')

    #set the background for the window
    master.configure(background='black')

    #set the required fonts
    myFont = font.Font(size=12)
    fnt=font.Font(size=18)

    #StringVar() is a variable class, which initializes equation variable to a empty string 
    equation=StringVar()

    #create the entry field for showing the expression
    val=Entry(master,textvariable=equation,bg='grey',fg='white',font=fnt,justify="right")
    val.place(x=10,y=10,width=630,height=100)

    #create the buttons in the main window at required positions
    btn1=Button(master,text='1',width=15,height=3,bg='black',fg='white',font=myFont,command=lambda:press(1)).place(x=10,y=140)
    btn2=Button(master,text='2',width=15,height=3,bg='black',fg='white',font=myFont,command=lambda:press(2)).place(x=170,y=140)
    btn3=Button(master,text='3',width=15,height=3,bg='black',fg='white',font=myFont,command=lambda:press(3)).place(x=330,y=140)
    btn4=Button(master,text='+',width=15,height=3,bg='black',fg='white',font=myFont,command=lambda:press("+")).place(x=490,y=140)
    btn5=Button(master,text='4',width=15,height=3,bg='black',fg='white',font=myFont,command=lambda:press(4)).place(x=10,y=220)
    btn6=Button(master,text='5',width=15,height=3,bg='black',fg='white',font=myFont,command=lambda:press(5)).place(x=170,y=220)
    btn7=Button(master,text='6',width=15,height=3,bg='black',fg='white',font=myFont,command=lambda:press(6)).place(x=330,y=220)
    btn8=Button(master,text='-',width=15,height=3,bg='black',fg='white',font=myFont,command=lambda:press("-")).place(x=490,y=220)
    btn9=Button(master,text='7',width=15,height=3,bg='black',fg='white',font=myFont,command=lambda:press(7)).place(x=10,y=300)
    btn10=Button(master,text='8',width=15,height=3,bg='black',fg='white',font=myFont,command=lambda:press(8)).place(x=170,y=300)
    btn11=Button(master,text='9',width=15,height=3,bg='black',fg='white',font=myFont,command=lambda:press(9)).place(x=330,y=300)
    btn12=Button(master,text='*',width=15,height=3,bg='black',fg='white',font=myFont,command=lambda:press("*")).place(x=490,y=300)
    btn13=Button(master,text='0',width=15,height=3,bg='black',fg='white',font=myFont,command=lambda:press(0)).place(x=10,y=380)
    btn14=Button(master,text='CLEAR',width=15,height=3,bg='black',fg='white',font=myFont,command=lambda:clear()).place(x=170,y=380)
    btn15=Button(master,text='=',width=15,height=3,bg='black',fg='white',font=myFont,command=equal).place(x=330,y=380)
    btn16=Button(master,text='/',width=15,height=3,bg='black',fg='white',font=myFont,command=lambda:press("/")).place(x=490,y=380)

    #run the gui
    master.mainloop()
