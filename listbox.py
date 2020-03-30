import tkinter as tk
import tkinter.ttk as ttk

class ListBox(tk.Frame):
    def __init__(self,master=None,color="white"):
        tk.Frame.__init__(self,master)
        self.listarray = []
        self.txt = tk.StringVar(value=self.listarray)
        self.listbox = tk.Listbox(self, listvariable= self.txt,
                width=48,height=13,background=color)
        self.listbox.pack()

class ListBox4(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.lb_up_left = ListBox(self,"misty rose")
        self.lb_up_left.grid(row=0,column=0)
        self.lb_up_right = ListBox(self,"wheat1")
        self.lb_up_right.grid(row=0,column=1)
        self.lb_down_left = ListBox(self,"lemon chiffon")
        self.lb_down_left.grid(row=1,column=0)
        self.lb_down_right = ListBox(self,"DarkSlateGray1")
        self.lb_down_right.grid(row=1,column=1)
        
if __name__ =="__main__":
    master = tk.Tk()
    master.title("list box")
    listbox = ListBox4(master)
    listbox.pack()
    listbox.mainloop()