import tkinter as tk
import tkinter.ttk as ttk
from listbox import ListBox4
from schedule import Schedule
from entry import Entry
from mycalendar import MyCalendar
from tkinter import messagebox
import pickle
import datetime

class Main(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.notebook = ttk.Notebook(self)
        self.listbox = ListBox4(self.notebook)
        self.sche = Schedule(self.notebook)

        self.entry = Entry(self,self.listbox, self.sche)
        self.entry.pack()
        self.calendar = MyCalendar(self.notebook,self.entry.date.txt)

        self.notebook.add(self.calendar,text="カレンダー",padding=3)
        self.notebook.add(self.listbox,text="リスト表",padding=3)
        self.notebook.add(self.sche,text="今日のスケジュール",padding=3)
        self.notebook.pack()

        #ファイルの読み込み
        #try:
        f = open("list.txt","rb")
        to_do_list = pickle.load(f)
        print (to_do_list)
        for value in to_do_list:
            #一番上のEntry Boxへの追加
            ind = self.entry.tree.tree.insert("","end",values=value)
            self.entry.tree.index_list.append(ind)

            #List Boxへの追加->日付と重要度による場合分け
            #時間の抽出
            year = int(value[1][0:4])
            month = int(value[1][5:7])
            date = int(value[1][8:10])
            hour = int(value[2][0:2])
            minute = int(value[2][3:5])
            deadline = datetime.datetime(year,month,date,hour,minute)
            #重要度の抽出
            importance = value[3]
            self.listbox.add_list(value[0],deadline,importance)

            #Scheduleへの追加
            self.sche.add_list(value[0])

        f.close()
        #except:
            #print ("保存ファイルが存在しません")

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