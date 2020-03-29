import tkinter as tk
from mycalendar import MyCalendar
from treeview import TreeView
from entry import Entry

class Tab2(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.entry = Entry(self)
        self.entry.pack()
    
if __name__ =="__main__":
    master = tk.Tk()
    master.title("tab2")
    tab2 = Tab2(master)
    tab2.pack()
    master.mainloop()