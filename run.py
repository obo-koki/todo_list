import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import pickle
import datetime

from listbox import ListBox4
from schedule import Schedule
from entry import Entry
from mycalendar import MyCalendar
from memo import Memo

#class ToDo:
    #def __init__(self,ID,thing,date,time,importance,place):
        #self.ID = ID
        #self.thing = thing
        #self.date = date
        #self.time = time
        #self.importance = importance
        #self.place = place

class Main(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.notebook = ttk.Notebook(self)
        self.listbox = ListBox4(self.notebook)
        self.sche = Schedule(self.notebook)

        self.entry = Entry(self,self.listbox, self.sche)
        self.entry.pack(pady=5,padx=5)
        self.calendar = MyCalendar(self.notebook,self.entry.date.txt)
        self.memo = Memo(self)

        self.notebook.add(self.calendar,text="カレンダー",padding=3)
        self.notebook.add(self.listbox,text="リスト表",padding=3)
        self.notebook.add(self.sche,text="今日のスケジュール",padding=3)
        self.notebook.add(self.memo,text="  メモ  ",padding=3)
        self.notebook.pack()
        #self.to_do_list = []

        #treeviewが選択された時の処理
        self.entry.tree.tree.bind("<<TreeviewSelect>>", self.add_entry)

        #ファイルの読み込み
        #try:
        f = open("list.txt","rb")
        to_do_list = pickle.load(f)
        for value in to_do_list:
            #一番上のEntry Boxへの追加
            ind = self.entry.tree.tree.insert("","end",values=value)
            self.entry.tree.index_list.append(ind)

            #List Boxへの追加
            self.listbox.add_list(value[0],value[1],value[2],value[3])

            #Scheduleへの追加
            self.sche.add_list(value[0])

        f.close()
        #except:
            #print ("保存ファイルが存在しません")

    def add_entry(self,event):
        selected = self.entry.tree.tree.selection()[0]
        value = self.entry.tree.tree.item(selected)["values"]
        self.entry.thing.txt.delete(0,tk.END)
        self.entry.thing.txt.insert(tk.END,value[0])
        self.entry.date.txt.delete(0,tk.END)
        self.entry.date.txt.insert(tk.END,value[1])
        #self.entry.time.txt.delete(0,tk.END)
        self.entry.time.combo.set(value[2])
        self.entry.importance.combo.set(value[3])
        self.entry.place.txt.delete(0,tk.END)
        self.entry.place.txt.insert(tk.END,value[4])

if __name__ =="__main__":
    master = tk.Tk()
    master.title("ToDo List")
    main = Main(master)
    main.pack()
    #windowを閉じるときの処理
    def on_closing():
        flag = messagebox.askyesnocancel("閉じる","保存しますか？")
        #保存
        if flag == True:
            f = open("list.txt","wb")
            to_do_list = []
            for index in main.entry.tree.index_list:
                to_do_list.append(main.entry.tree.tree.item(index)["values"])
            pickle.dump(to_do_list,f)
            f.close()
        #保存しない
        elif flag==False:
            if not messagebox.askyesno("閉じる","本当に保存しませんか？"):
                return
        #キャンセル
        elif flag==None:
            return
        master.destroy()

    master.protocol("WM_DELETE_WINDOW",on_closing)
    master.mainloop()