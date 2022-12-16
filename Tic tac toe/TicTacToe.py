
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

root=Tk()
root.title('Tic Tac Toe')
root.resizable(False,False)
root.geometry('+%d+%d'%(500,100))
root.geometry('600x600')


#Window-1
canvas1=Canvas(width=600,height=600,bg='white')
canvas1.grid(columnspan=3,rowspan=5)

wd1=Image.open('Window 1.png')
wd1=ImageTk.PhotoImage(image=wd1)


canvas1.create_image(0,0,image=wd1,anchor='nw')




#Window-2

def next_window():
    canvas1.destroy()
    play1.destroy()
    
    canvas2=Canvas(width=600,height=600,bg='white')
    canvas2.grid(columnspan=3,rowspan=5)
    
    sw=Image.open('bottom-left.png')
    sw=ImageTk.PhotoImage(image=sw)

    w=Image.open('w.png')
    w=ImageTk.PhotoImage(image=w)

    e=Image.open('e.png')
    e=ImageTk.PhotoImage(image=e)

    se=Image.open('se.png')
    se=ImageTk.PhotoImage(image=se)

    ne=Image.open('top right.png')
    ne=ImageTk.PhotoImage(image=ne)

    nw=Image.open('nw.png')
    nw=ImageTk.PhotoImage(image=nw)

    l1=Label(image=sw,borderwidth=0)
    l1.image=sw
    l1.grid(row=4,column=0,sticky='sw')

    l2=Label(image=w,borderwidth=0)
    l2.image=w
    l2.grid(row=2,column=0,sticky='w')

    l3=Label(image=e,borderwidth=0)
    l3.image=e
    l3.grid(row=2,column=2,sticky='e')

    l4=Label(image=ne,borderwidth=0)
    l4.image=ne
    l4.grid(row=0,column=2,sticky='ne')

    l5=Label(image=se,borderwidth=0)
    l5.image=se
    l5.grid(row=4,column=2,sticky='se')

    l6=Label(image=nw,borderwidth=0)
    l6.image=nw
    l6.grid(row=0,column=0,sticky='nw')


    e1=Entry(root,width=40,borderwidth=5)
    e1.grid(row=1,column=1)

    e2=Entry(root,width=40,borderwidth=5)
    e2.grid(row=2,column=1)

    name1=Label(root,text='Player 1:',bg='white',fg='#20bebe')
    name1.grid(row=1,column=0,sticky='e')

    name2=Label(root,text='Player 2:',bg='white',fg='#20bebe')
    name2.grid(row=2,column=0,sticky='e')

    play=Image.open('play.png')
    play=ImageTk.PhotoImage(image=play)

    





        

#Window-3
    def plays():

        n1=e1.get()
        n2=e2.get()

        canvas2.destroy()

        canvas=Canvas(root,height=600,width=600,bg='white')
        canvas.grid(columnspan=3,rowspan=3)

        name1.destroy()
        name2.destroy()
        e1.destroy()
        e2.destroy()
        l1.destroy()
        l2.destroy()
        l3.destroy()
        l4.destroy()
        l5.destroy()
        l6.destroy()
        play2.destroy()

        root.geometry('636x674')

                     
        #Buttons
        global win
        win=False

        global n
        n=0

        global k
        k=9

        global l
        l=[[' ', ' ',' '],[' ',' ',' '],[' ',' ',' ']]


        global s
        s=' '


        def click(r,c):
            
            global win
            global s
            
            
            global k
            if k>0:
                global n
                n=n+1
                if n%2==0:
                    s='O'
                else:
                    s='X'
                l[r][c]=s
                
                
                
                b=Button(root,text=s,font=('Helvetica',61),padx=40,pady=35,bg='white',fg='#20bebe')
                b.grid(row=r,column=c)
                
                k=k-1

                if (l[0][0]==l[0][1] and l[0][1]==l[0][2] and l[0][0]!=' '):
                    
                    win=True

                elif (l[1][0]==l[1][1] and l[1][1]==l[1][2] and l[1][0]!=' '):
                    #global win
                    win=True

                elif (l[2][0]==l[2][1] and l[2][1]==l[2][2] and l[2][0]!=' '):
                    #global win
                    win=True

                elif (l[0][0]==l[1][0] and l[1][0]==l[2][0] and l[0][0]!=' '):
                    
                    win=True

                elif (l[0][1]==l[1][1] and l[1][1]==l[2][1] and l[0][1]!=' '):
                    
                    win=True

                elif (l[0][2]==l[1][2] and l[1][2]==l[2][2] and l[0][2]!=' ' ):
                    
                    win=True

                elif (l[0][0]==l[1][1] and l[1][1]==l[2][2] and l[0][0]!=' '):
                    
                    win=True

                elif (l[0][2]==l[1][1] and l[1][1]==l[2][0] and l[0][2]!=' '):
                    
                    win=True

                if win==True:
                    k=0
                    

                print(win)

                if win==True:
                    if s=='X':
                        messagebox.showinfo('Game ended',n1+' WON!')

                    else:
                        messagebox.showinfo('Game ended',n2+' WON!')
                        

                elif win==False  and k==0:
                    messagebox.showinfo('Game ended','Draw match!')





          
        #text='X',font=('Helvetica',61),padx=42,pady=35

        b1=Button(root,text=' ',bg='white',padx=100,pady=100,command=lambda:click(0,0))
        b2=Button(root,text=' ',bg='white',padx=100,pady=100,command=lambda:click(0,1))
        b3=Button(root,text=' ',bg='white',padx=100,pady=100,command=lambda:click(0,2))
        b4=Button(root,text=' ',bg='white',padx=100,pady=100,command=lambda:click(1,0))
        b5=Button(root,text=' ',bg='white',padx=100,pady=100,command=lambda:click(1,1))
        b6=Button(root,text=' ',bg='white',padx=100,pady=100,command=lambda:click(1,2))
        b7=Button(root,text=' ',bg='white',padx=100,pady=100,command=lambda:click(2,0))
        b8=Button(root,text=' ',bg='white',padx=100,pady=100,command=lambda:click(2,1))
        b9=Button(root,text=' ',bg='white',padx=100,pady=100,command=lambda:click(2,2))



        b1.grid(row=0,column=0)
        b2.grid(row=0,column=1)
        b3.grid(row=0,column=2)
        b4.grid(row=1,column=0)
        b5.grid(row=1,column=1)
        b6.grid(row=1,column=2)
        b7.grid(row=2,column=0)
        b8.grid(row=2,column=1)
        b9.grid(row=2,column=2)
        

    play2=Button(root,image=play,borderwidth=0,command=plays)
    play2.image=play
    play2.grid(column=1,row=4)




play=Image.open('play.png')
play=ImageTk.PhotoImage(image=play)
    

play1=Button(root,image=play,borderwidth=0,command=next_window)
play1.grid(column=1,row=4)




root.mainloop()
