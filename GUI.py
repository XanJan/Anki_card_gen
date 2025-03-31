import customtkinter as ctk

root = ctk.CTk()

def initMainWindow(root, width, height):
    root.geometry(str(width) + 'x' + str(height))
    root.mainloop()

initMainWindow(root, 600, 600)
