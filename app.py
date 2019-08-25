from tkinter import *

frame_width = 800
frame_height = 450


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)               
        self.master = master
        self.init_window()
        
    def init_window(self):
        
        #Change the title of window      
        self.master.title("My Python GUI")

        #Fill the window
        self.pack(fill=BOTH, expand=1)

        #Create a button
        action_button = Button(self, text="Print")        
        action_button.place(x=20, y=20)
        action_button.config(height=9, width=16)

        
        
#Initialize Tkinter
root = Tk()

#size of the window
root_geometry = "{}x{}".format(frame_width, frame_height)
root.geometry(root_geometry)

#Get the window class, pass the root variable
app = Window(root)

#The program constantly checks for updates
root.mainloop()