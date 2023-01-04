#import the necessary libraries
import tkinter
from tkinter import*
from textblob import TextBlob
# create the main window 
root=Tk()
#set the title of the window
root.title("Spelling Corrector")
#set the size of the window
root.geometry("700x400")
#set the background color of the window
root.config(background="#dae6f6")
#define the function to correct the spelling of the input word
def check_spelling():
#get the input word
    word=enter_text.get()
#create a Textblob object with the input word
    a=TextBlob(word)
#correct the spelling of the input word using the correct method of the Textblob object
    right=str(a.correct())
#create a label to display the corrected text
    cs=Label(root,text="corrected text is:",font=("poppins",20),bg="#dae6f6",fg="#364971")
#place the label at a specific position in the window
    cs.place(x=100,y=250)
#set the text of the label widget to the corrected word
    spell.config(text=right)
#create the haeding label
heading=Label(root,text="SPELLING CHECKER",font=("trebuchet ms",30,"bold"),bg="#dae6f6",fg="#364971")
#place the heading label in the window using the pack() method
heading.pack(pady=(50,0))
#create an entry field to take the input
enter_text=Entry(root,justify="center",width=30,font=("poppins",25),bg="white",border=2)
#place the entry field in the window using pack() method
enter_text.pack(pady=10)
#set the focus on the entry field
enter_text.focus()
#create a button to perform the spelling correction
button=Button(root,text="check",font=("arial",20,"bold"),fg="white",bg="red",command=check_spelling)
#place the button in the window using pack() method
button.pack()
#create a label widget to display the corrected word
spell=Label(root,font=("poppins",20),bg="#dae6f6",fg="#364971")
#place the label widget at a specific position in the window
spell.place(x=350,y=250)
#start the event loop of the GUI appliaction
root.mainloop()
