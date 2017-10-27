# Imports everything from tkinter
from tkinter import *

# Creating our class, Window, and inheriting from the Frame class. Frame is a class from the tkinter module.

class Window(Frame):
    # Define settings upon initialization. Here you can specify...
    def __init__(self, master=None):
        # ...parameters that you want to send through the Frame class.
        Frame.__init__(self, master)
        # Reference to the master widget, which is the wk window.
        self.master = master
        # This runs init_window, a method below.
        self.init_window()

    # Creation of init_window
    def init_window(self):

        # Changing the title of the our master widget
        self.master.title("GUI")

        # Allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # Creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # Create the file object
        file = Menu(menu)

        # Adds a command to the menu option, calling it exit, and the command it runs on the even is client_exit
        file.add_command(label="Exit", command=self.client_exit)

        # Adds file to the menu
        menu.add_cascade(label="File", menu=file)

        # Create the file object
        edit = Menu(menu)

        edit.add_command(label="Undo")

        # Add "file" to the menu
        menu.add_cascade(label="Edit", menu=edit)

        # # Creating a button instance
        # quit_button = Button(self, text="QUIT", command=self.client_exit)

        # Place the button on my window
        # quit_button.place (x=0, y=0)

    def client_exit(self):
        exit()

# Root window created. Here, that would be the only window, but you can have windows within windows.
root = Tk()

# Size of the window
root.geometry("400x300")

# Creation of an instance
app = Window(root)
# mainloop
root.mainloop()