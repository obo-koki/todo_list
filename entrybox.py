import tkinter as tk

class EntryBoxThing(tk.Frame):
    def __init__(self,master = None):
        tk.Frame.__init__(self,master)
        label = tk.Label(self,
                        text="やること")
        label.grid(column=0,row=0)
        self.txt = tk.Entry(self,width=30)
        self.txt.grid(column=0,row=1)

class EntryBoxPlace(tk.Frame):
    def __init__(self,master = None):
        tk.Frame.__init__(self,master)
        label = tk.Label(self,
                        text="場所")
        label.grid(column=0,row=0)
        self.txt = tk.Entry(self,width=30)
        self.txt.grid(column=0,row=1)

class EntryBoxDate(tk.Frame):
    def __init__(self,master = None):
        tk.Frame.__init__(self,master)
        label = tk.Label(self,
                        text="日付")
        label.grid(column=0,row=0)
        self.txt = tk.Entry(self,width=10)
        self.txt.grid(column=0,row=1)

if __name__=="__main__":
    master = tk.Tk()
    master.title("entrybox")
    e_t = EntryBoxThing(master)
    e_t.pack()
    e_p = EntryBoxPlace(master)
    e_p.pack()
    master.mainloop()