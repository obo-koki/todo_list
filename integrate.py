import tkinter as tk
import tkinter.ttk as ttk
from tab1 import Tab1
from tab2 import Tab2
from tab3 import Tab3

class Main(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        notebook = ttk.Notebook(self)
        tab1 = Tab1(notebook)
        tab1.pack()
        tab2 = Tab2(notebook)
        tab2.pack()
        tab3 = Tab3(notebook)
        tab3.pack()

        notebook.add(tab1,text="カレンダー",padding=3)
        notebook.add(tab2,text="リスト表",padding=3)
        notebook.add(tab3,text="今日のスケジュール",padding=3)
        notebook.pack()
        
if __name__ =="__main__":
    master = tk.Tk()
    master.title("ToDo List")
    main = Main(master)
    main.pack()
    main.mainloop()