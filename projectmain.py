from tkinter import *
from tkinter import messagebox

#To keep the track of the player playing
click=True
#To keep the track on number of boxes selected
count=0

Font_style= ("Comic Sans MS", 13, "bold")

#Checking winner based on conditions
def checkwinner():
    if(b1["text"]==b2["text"]==b3["text"]=="X" or b4["text"]==b5["text"]==b6["text"]=="X"
       or b7["text"]==b8["text"]==b9["text"]=="X" or b1["text"]==b5["text"]==b9["text"]=="X"
       or b3["text"]==b5["text"]==b7["text"]=="X" or b1["text"]==b4["text"]==b7["text"]=="X"
       or b2["text"]==b5["text"]==b8["text"]=="X" or b3["text"]==b6["text"]==b9["text"]=="X"):
        messagebox.showinfo("Tic Tac Toe", "Winner is player 1")
        root.destroy()
        master.destroy()
    elif(b1["text"]==b2["text"]==b3["text"]=="O" or b4["text"]==b5["text"]==b6["text"]=="O"
       or b7["text"]==b8["text"]==b9["text"]=="O" or b1["text"]==b5["text"]==b9["text"]=="O"
       or b3["text"]==b5["text"]==b7["text"]=="O" or b1["text"]==b4["text"]==b7["text"]=="O"
       or b2["text"]==b5["text"]==b8["text"]=="O" or b3["text"]==b6["text"]==b9["text"]=="O"):
        messagebox.showinfo("Tic Tac Toe","Winner is player 2")
        root.destroy()
        master.destroy()
    elif(count==9):
        messagebox.showinfo("Tic Tac Toe","It's a tie")
        root.destroy()
        master.destroy()

#task to be performed when the button is clicked        
def onclick(b):
    global click,count
    #player 1 turn
    if b["text"]=="" and click==True:
        b["text"]="X"
        click=False
        count+=1
        checkwinner()
    #player 2 turn
    elif b["text"]=="" and click==False:
        b["text"]="O"
        click=True
        count+=1
        checkwinner()
    #tie condition
    else:
        messagebox.showerror("Tic Tac Toe","The box is already selected")
    
#directs to the game window
def open_window():
    global root
    # try and except is used so that the game window is created only once onclicking
    try:
        if root.state=="normal":
            root.focus()
    except:
        #creating the game window
        root=Toplevel(master)
        root.title("Tic Tac Toe")
        root.geometry("260x340")
        root.config(bg="#240046")
        root.iconphoto(FALSE,icon)

        l1=Label(root,text="Player1=X\n\nPlayer2=O",bg="#240046",font=Font_style,foreground="white").grid(row=0,columnspan=3)

        #creating buttons
        global b1,b2,b3,b4,b5,b6,b7,b8,b9
        b1= Button(root,text="",width=11,height=5,bg="#fef9ff",activebackground="#f7f7ff",command=lambda:onclick(b1))
        b2= Button(root,text="",width=11,height=5,bg="#fef9ff",activebackground="#f7f7ff",command=lambda:onclick(b2))
        b3= Button(root,text="",width=11,height=5,bg="#fef9ff",activebackground="#f7f7ff",command=lambda:onclick(b3))

        b4= Button(root,text="",width=11,height=5,bg="#fef9ff",activebackground="#f7f7ff",command=lambda:onclick(b4))
        b5= Button(root,text="",width=11,height=5,bg="#fef9ff",activebackground="#f7f7ff",command=lambda:onclick(b5))
        b6= Button(root,text="",width=11,height=5,bg="#fef9ff",activebackground="#f7f7ff",command=lambda:onclick(b6))

        b7= Button(root,text="",width=11,height=5,bg="#fef9ff",activebackground="#f7f7ff",command=lambda:onclick(b7))
        b8= Button(root,text="",width=11,height=5,bg="#fef9ff",activebackground="#f7f7ff",command=lambda:onclick(b8))
        b9= Button(root,text="",width=11,height=5,bg="#fef9ff",activebackground="#f7f7ff",command=lambda:onclick(b9))
        
        #placing buttons in proper locations
        b1.grid(row=1,column=0)
        b2.grid(row=1,column=1)
        b3.grid(row=1,column=2)

        b4.grid(row=2,column=0)
        b5.grid(row=2,column=1)
        b6.grid(row=2,column=2)

        b7.grid(row=3,column=0)
        b8.grid(row=3,column=1)
        b9.grid(row=3,column=2)

#creating the main tkinter window
master=Tk()
master.geometry("250x305")
master.title("Tic Tac Toe")

#changing the icon of the window
icon = PhotoImage(file = r"tictactoe_icons.png")
master.iconphoto(False, icon)

master.config(bg="#001233")
img=PhotoImage(file=r"tictactoe_image.png")
img1=img.subsample(3,3)
l1=Label(master,image=img1).place(x=28,y=20,height=150,width=190)
photoimage=PhotoImage(file=r"button_play.png")

#Play button to start the game
b=Button(master,bg="#5e60ce",image=photoimage,activebackground="#5e60ce",command=open_window).place(x=65,y=210,height=40,width=120)

mainloop()
