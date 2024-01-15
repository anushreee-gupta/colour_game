import customtkinter
from PIL import Image
import random
from time import sleep
import numpy as np
import matplotlib.pyplot as plt

colours = ['Grey','Red','Blue','Green','Pink','Black','Yellow','Orange','White','Purple','Brown']
score = 0
timeleft = 32
toggle_mode = True

def timer():
    global timeleft
    if timeleft > 0:
        timeleft -=1
        timeL.configure(text = "Time left:" + str(timeleft))
        timeL.after(1000,timer)
    if timeleft == 0:
        end()
        

def nextcolour():
    global score
    global timeleft
    if timeleft > 0:
        user.focus_set()
        if user.get().lower() == colours[1].lower():
            score +=1
        user.delete(0, customtkinter.END)
        random.shuffle(colours)
        user.configure(text_color = colours[0])
        mainlabel.configure(text_color = str(colours[1]), text = str(colours[0]))
        scoreL.configure(text = "Score: " + str(score))
def start(event):
    if timeleft == 32:
        timer()
        nextcolour()
    elif timeleft==0:
        end()
    elif user.get().lower() == colours[1].lower():
        nextcolour()
def btnfn(event):
    welcome1.place_forget()
    instructions1.place_forget()
    btn.place_forget()
    modebtn.place_forget()
    welcome2.configure(font=('Perpetua', 20))
    mainlabel.place(relx=0.5, rely=0.3, anchor='center')
    scoreL.place(relx=0.5, rely=0.4, anchor='center')
    timeL.place(relx=0.5, rely=0.45, anchor='center')
    user.place(relx=0.5, rely=0.6, anchor='center')
    user.focus_set()
    start(sleep(0.2))

def end():
    global arry
    arry = np.append(arry,int(score))
    np.savetxt(f,np.array([score]), delimiter=',', fmt="%d")
    f.close()
    user.configure(state='disabled')
    user.destroy()
    mainlabel.destroy()
    welcome2.destroy()
    scoreL.configure(text="Your score is "+str(score),font=("Perpetua",20))
    timeL.destroy()
    endL.place(relx=0.5, rely=0.5, anchor='center')
    statsbtn.place(relx=0.5, rely=0.6, anchor='center')

def toggle_btn(event):
    global toggle_mode
    if toggle_mode:
        modebtn.configure(image= off, fg_color = '#252524')
        customtkinter.set_appearance_mode("dark")
        toggle_mode = False
    else:
        customtkinter.set_appearance_mode("light")
        modebtn.configure(image= on, fg_color = '#ebebeb')
        toggle_mode = True

def statsview(event):
    global arry
    plt.plot(arry, marker='o', markerfacecolor = 'b', color='k')
    plt.ylim(-1,30)
    plt.ylabel('Score')
    plt.xlabel('Device')
    plt.show()

# Window
root = customtkinter.CTk()
root.title("Color confusion")
root.geometry("640x360") # ,1880x720

on = customtkinter.CTkImage(Image.open("light.png"), size = (100,50))
off = customtkinter.CTkImage(Image.open("dark.png"),size = (100,50))




customtkinter.set_appearance_mode("light")
#Instructions and information
welcome1 = customtkinter.CTkLabel(root, text = "Welcome to Colour Confusion!", font=("Lucida Handwriting",24))
welcome1.place(relx = 0.5, rely = 0.1, anchor = 'center')
welcome2 = customtkinter.CTkLabel(root, text = "Guess the colour of word displaying a colour name.", font=("Perpetua",18))
welcome2.place(relx = 0.5, rely = 0.2, anchor = 'center')
instructions1 = customtkinter.CTkLabel(root, text="You have 30 seconds!\n Are you ready?", font=("Perpetua",18))

#colour name to be updated
mainlabel = customtkinter.CTkLabel(root, text='      ',font=("Baskerville Old Face",35), fg_color = 'lightgrey')

scoreL = customtkinter.CTkLabel(root, text="Score:"+str(score), font=("Perpetua",18))
timeL = customtkinter.CTkLabel(root, text = "Time left:" + str(timeleft), font=("Perpetua",18))

#input box
user = customtkinter.CTkEntry(root, corner_radius=32, font=("Perpetua",18), fg_color='lightgrey')
user.bind('<Return>',start)

#end
endL = customtkinter.CTkLabel(root,text="Game Over! Thank you for playing", font=("Perpetua",24))

modebtn = customtkinter.CTkButton(root, text='', image=on, border_width=None, fg_color='#ebebeb')
modebtn.bind('<Button-1>', toggle_btn)
modebtn.place(relx=0.01, rely = 0.85)

btn = customtkinter.CTkButton(root, text="Start", corner_radius=32, text_color='black',fg_color='#84cccb', hover_color='#c28d9c',font=("Perpetua",18))
instructions1.place(relx = 0.5, rely = 0.3, anchor = 'center')
btn.bind('<Button-1>', btnfn)
btn.place(relx = 0.5, rely = 0.4, anchor = 'center')

f = open('scores.csv','a')
arry = np.loadtxt('scores.csv', delimiter=',', dtype=int)
statsbtn = customtkinter.CTkButton(root, text='Stats',  corner_radius=32, text_color='black',fg_color='#84cccb', hover_color='#c28d9c',font=("Perpetua",18))
statsbtn.bind('<Button-1>', statsview)

root.mainloop()