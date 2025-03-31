import tkinter as tk
import customtkinter as ctk

root = ctk.CTk()
width = 600
height = 600

root.geometry(str(width) + 'x' + str(height))
lable = ctk.CTkLabel(root, text="Anki card generator",            
                     width=120, 
                height=50, 
                font=('Roboto', 12))
#print(ctk._fonts)

lable.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

def button_callback():
    print("button clicked")

button = ctk.CTkButton(root, text="my button", command=button_callback)
button.pack(padx=20, pady=70)

root.mainloop()