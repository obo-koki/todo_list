import tkinter as tk
from mycalendar import MyCalendar
from treeview import TreeView
from entry import Entry
class Tab1(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.entry = Entry(self)
        self.entry.pack()
        self.calendar = MyCalendar(self)
        self.calendar.pack()
    
if __name__ =="__main__":
    master = tk.Tk()
    master.title("tab1")
    tab1 = Tab1(master)
    tab1.pack()
    master.mainloop()