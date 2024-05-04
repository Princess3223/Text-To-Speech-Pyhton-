#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import libraries

from tkinter import *
from gtts import gTTS
from playsound import playsound

#window

root = Tk()
root.geometry('350x300')
root.resizable(0,0)
root.config(bg = 'ghost white')
root.title('Pyhton Mini-Project Text-To-Speech')


#heading
Label(root, text = 'TEXT_TO_SPEECH' , font='arial 20 bold' , bg ='white smoke').pack()
Label(root, text ='Princess Kachhadiya' , font ='arial 15 bold', bg = 'white smoke').pack(side = BOTTOM)




#label
Label(root, text ='Enter Text', font ='arial 15 bold', bg ='white smoke').place(x=20,y=60)


##text variable
Msg = StringVar()


#Entry
entry_field = Entry(root,textvariable =Msg, width ='50')
entry_field.place(x=20 , y=100)


#defining function

def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('Voice.mp3')
    playsound('Voice.mp3')
    

def Exit():
    root.destroy()

def Reset():
    Msg.set("")

#Button
Button(root, text = "PLAY" , font = 'arial 15 bold', command = Text_to_speech,bg = 'Blue', width =4).place(x=35, y=140)
Button(root,text = 'CANCEL',font = 'arial 15 bold' , command = Exit, bg = 'Red').place(x=100,y=140)
Button(root, text = 'RESET', font='arial 15 bold', command = Reset, bg = 'green').place(x=205 , y =140)


#infinite loop to run program
root.mainloop()


# In[ ]:





# In[ ]:




