import tkinter as tk
from mycalendar import MyCalendar
from treeview import TreeView
from entry import Entry

class Tab3(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.entry = Entry(self)
        self.entry.pack()
    
if __name__ =="__main__":
    master = tk.Tk()
    master.title("tab3")
    tab3 = Tab3(master)
    tab3.pack()
    master.mainloop()