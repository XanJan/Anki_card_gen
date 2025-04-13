import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk
import anki_gen

root = ctk.CTk()
width = 600
height = 600
filename = ""

root.geometry(str(width) + 'x' + str(height))
lable = ctk.CTkLabel(root, text="Anki Deck generator",            
                     width=200, 
                height=750, 
                font=('Roboto', 20))
#print(ctk._fonts)

lable.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

textbox = ctk.CTkTextbox(root, width=300, height=25, corner_radius=5)
textbox.insert("0.0", "Path to pdf")  # insert at line 0 character 0
textbox.configure(state="normal") 
textbox.place(relx=0.4, rely=0.4, anchor=tk.CENTER)

infoBox = ctk.CTkTextbox(root, width=550, height=100, corner_radius=5)
infoBox.insert("0.0", "Welcome to the Anki Deck Generator, an app that can take a pdf file with questions and answers and make them into an anki deck.")  # insert at line 0 character 0
infoBox.configure(state="disabled")  # configure textbox to be read-only
infoBox.place(relx=0.5, rely=0.2, anchor=tk.CENTER)


#__________________________________________BUTTON  FUNCTIONS______________________________________________________
def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    textbox.delete("0.0", "end")
    textbox.insert("0.0", filename)
    print("Selected: ", filename)
    
def GenerateAction(event=None):
    anki_gen.GenerateCards(filename, "TestDeckFromGUI")
    print("Generating: ", filename)

#_________________________________________________________________________________________________________________

button1 = ctk.CTkButton(root, text="Upload file", command=UploadAction)
#button.pack(padx=20, pady=70)
button1.place(relx=0.8, rely=0.4, anchor=tk.CENTER)

button2 = ctk.CTkButton(root, text="Generate .apkg file", command=GenerateAction)
#button.pack(padx=20, pady=90)
button2.place(relx = 0.5, rely = 0.6, anchor=tk.CENTER)


root.mainloop()