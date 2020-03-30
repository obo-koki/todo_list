# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk

class PullDown(tk.Frame):
    def __init__(self,master = None, time=""):
        tk.Frame.__init__(self,master)
        label = tk.Label(self, text = time)
        label.grid(row=0,column=0)
        self.combo = ttk.Combobox(self,
                        values=[""],
                        width=30)
        self.combo.grid(row=1,column=1)

class Schedule(tk.Frame):
    def __init__(self,master = None):
        tk.Frame.__init__(self,master)
        self.time_list=[]
        for i in range(7,16):
            time_left = PullDown(self, str(i)+":00") 
            time_left.grid(row=i,column=0)
            self.time_list.append(time_left)
            time_right = PullDown(self,str(i+9)+":00")
            time_right.grid(row=i,column=1)
            self.time_list.append(time_right)
        label16 = tk.Label(self, text = "16:00")
        label16.grid(row=16,column=0,sticky=tk.W)
        label24 = tk.Label(self, text = "25:00")
        label24.grid(row=16,column=1,sticky=tk.W)

    def add_list(self,item_str):
        for time in self.time_list:
            time.combo["values"] += (item_str,)

    def delete_list(self,item_str):
        for time in self.time_list:
            li = list(time.combo["values"])
            if item_str in li:
                li.remove(item_str)
            time.combo["values"] = tuple(li)

if __name__ =="__main__":
    master = tk.Tk()
    master.title("schedule")
    sche = Schedule(master)
    sche.pack()
    master.mainloop()