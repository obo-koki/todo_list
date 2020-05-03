import tkinter as tk
import tkinter.ttk as ttk
import datetime

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
        self.up_left = ListBox(self,"misty rose")
        self.up_left.grid(row=0,column=0)
        self.up_right = ListBox(self,"wheat1")
        self.up_right.grid(row=0,column=1)
        self.down_left = ListBox(self,"lemon chiffon")
        self.down_left.grid(row=1,column=0)
        self.down_right = ListBox(self,"DarkSlateGray1")
        self.down_right.grid(row=1,column=1)

        self.date_th = 7
    
    def add_list(self,thing,deadline,importance):
        now = datetime.datetime.now()
        ref  = now + datetime.timedelta(days=self.date_th)
        if importance =="高" and deadline <=ref:
            self.up_left.listbox.insert(tk.END, thing)
        elif importance =="高" and deadline >ref:
            self.up_right.listbox.insert(tk.END, thing)
        elif importance =="低" and deadline <=ref:
            self.down_left.listbox.insert(tk.END, thing) 
        else:
            self.down_right.listbox.insert(tk.END, thing)

    #def delete(self,)
        
if __name__ =="__main__":
    master = tk.Tk()
    master.title("list box")
    listbox = ListBox4(master)
    listbox.pack()
    listbox.mainloop()