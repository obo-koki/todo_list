import tkinter as tk
import tkinter.ttk as ttk
from listbox import ListBox4
from schedule import Schedule
from entry import Entry
from mycalendar import MyCalendar
from tkinter import messagebox
import pickle

class Main(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.entry = Entry(self)
        self.entry.pack()
        self.notebook = ttk.Notebook(self)
        self.calendar = MyCalendar(self.notebook,self.entry.date.txt)
        self.listbox = ListBox4(self.notebook)
        self.listbox.pack()
        self.sche = Schedule(self.notebook)
        self.sche.pack()

        self.notebook.add(self.calendar,text="カレンダー",padding=3)
        self.notebook.add(self.listbox,text="リスト表",padding=3)
        self.notebook.add(self.sche,text="今日のスケジュール",padding=3)
        self.notebook.pack()

        #ファイルの読み込み
        try:
            f = open("list.txt","rb")
            to_do_list = pickle.load(f)
            for value in to_do_list:
                ind = self.entry.tree.tree.insert("","end",values=value)
                self.entry.tree.index_list.append(ind)
            f.close()
        except:
            print ("保存ファイルが存在しません")

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
            print ("保存しました")
        #保存しない
        elif flag==False:
            if messagebox.askyesno("閉じる","本当に保存しませんか？"):
                print ("保存しません")
            else:
                return
        #キャンセル
        elif flag==None:
            return
        master.destroy()

    master.protocol("WM_DELETE_WINDOW",on_closing)
    master.mainloop()