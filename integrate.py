import tkinter as tk
import tkinter.ttk as ttk
from listbox import ListBox4
from schedule import Schedule
from entry import Entry
from mycalendar import MyCalendar

class Main(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.entry = Entry(self)
        self.entry.pack()
        self.notebook = ttk.Notebook(self)
        self.calendar = MyCalendar(self.notebook)
        self.listbox = ListBox4(self.notebook)
        self.listbox.pack()
        self.sche = Schedule(self.notebook)
        self.sche.pack()

        self.notebook.add(self.calendar,text="カレンダー",padding=3)
        self.notebook.add(self.listbox,text="リスト表",padding=3)
        self.notebook.add(self.sche,text="今日のスケジュール",padding=3)
        self.notebook.pack()
        
if __name__ =="__main__":
    master = tk.Tk()
    master.title("ToDo List")
    main = Main(master)
    main.pack()
    main.mainloop()