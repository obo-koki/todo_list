# -*- coding:utf-8 -*-
import tkinter as tk
import copy
import datetime

# カレンダーを作成するフレームクラス
class MyCalendar(tk.Frame):
    def __init__(self,master=None,entrybox=None):
        tk.Frame.__init__(self,master)
        # 現在の日付を取得
        now = datetime.datetime.now()
        # 現在の年と月を属性に追加
        self.year = now.year
        self.month = now.month

        #ボタンが押されたときに埋めるエントリーボックスの指示
        self.entry_box = entrybox
        # frame_top部分の作成
        frame_top = tk.Frame(self)
        frame_top.pack(pady=5)
        self.previous_month = tk.Label(frame_top, text = "<", font = ("",14))
        self.previous_month.bind("<1>",self.change_month)
        self.previous_month.pack(side = "left", padx = 10)
        self.current_year = tk.Label(frame_top, text = self.year, font = ("",18))
        self.current_year.pack(side = "left")
        self.current_month = tk.Label(frame_top, text = self.month, font = ("",18))
        self.current_month.pack(side = "left")
        self.next_month = tk.Label(frame_top, text = ">", font = ("",14))
        self.next_month.bind("<1>",self.change_month)
        self.next_month.pack(side = "left", padx = 10)

        # frame_week部分の作成
        frame_week = tk.Frame(self)
        frame_week.pack()
        button_mon = d_button(frame_week, text = "Mon")
        button_mon.grid(column=0,row=0)
        button_tue = d_button(frame_week, text = "Tue")
        button_tue.grid(column=1,row=0)
        button_wed = d_button(frame_week, text = "Wed")
        button_wed.grid(column=2,row=0)
        button_thu = d_button(frame_week, text = "Thu")
        button_thu.grid(column=3,row=0)
        button_fri = d_button(frame_week, text = "Fri")
        button_fri.grid(column=4,row=0)
        button_sta = d_button(frame_week, text = "Sat", fg = "blue")
        button_sta.grid(column=5,row=0)
        button_san = d_button(frame_week, text = "San", fg = "red")
        button_san.grid(column=6,row=0)

        # frame_calendar部分の作成
        self.frame_calendar = tk.Frame(self)
        self.frame_calendar.pack()

        # 日付部分を作成するメソッドの呼び出し
        self.create_calendar(self.year,self.month)
    
    def enter_box(self,date):
        def enter():
            self.entry_box.delete(0,tk.END)
            month_str = str(self.month)
            date_str = str(date)
            if self.month < 10:
                month_str = "0"+ month_str
            if date < 10:
                date_str = "0"+date_str
            enter_text = str(self.year) + "/"+ month_str + "/" + date_str
            self.entry_box.insert(tk.END,enter_text)
        return enter

    def create_calendar(self,year,month):
        # ボタンがある場合には削除
        try:
            for key,item in self.day.items():
                item.destroy()
        except:
            pass
            
        # calendarモジュールのインスタンスを作成
        import calendar
        cal = calendar.Calendar()
        # 指定した年月のカレンダーをリストで返す
        days = cal.monthdayscalendar(year,month)

        # 日付ボタンを格納する変数をdict型で作成
        self.day = {}
        # for文を用いて、日付ボタンを生成
        now = datetime.datetime.now()
        for i in range(0,42):
            c = i - (7 * int(i/7))
            r = int(i/7)
            try:
            # 日付が0でなかったら、ボタン作成
                if days[r][c] != 0:
                    date = days[r][c]
                    if year == now.year and month == now.month and now.day == date:
                        self.day[i] = tk.Button(self.frame_calendar,text = date,background="SkyBlue1",
                            font=("",14),height=2, width=4, relief="flat",command=self.enter_box(date))
                        self.day[i].grid(column=c,row=r)
                    else:
                        self.day[i] = tk.Button(self.frame_calendar,text = date,
                            font=("",14),height=2, width=4, relief="flat",command=self.enter_box(date))
                        self.day[i].grid(column=c,row=r)
            except:
                """
                月によっては、i=41まで日付がないため、日付がないiのエラー回避が必要
                """
                break

    def change_month(self,event):
        # 押されたラベルを判定し、月の計算
        if event.widget["text"] == "<":
            self.month -= 1
        else:
            self.month += 1
        # 月が0、13になったときの処理
        if self.month == 0:
            self.year -= 1
            self.month = 12
        elif self.month == 13:
            self.year +=1
            self.month =1
        # frame_topにある年と月のラベルを変更する
        self.current_year["text"] = self.year
        self.current_month["text"] = self.month
        # 日付部分を作成するメソッドの呼び出し
        self.create_calendar(self.year,self.month)

class d_button(tk.Button):
    def __init__(self,master=None,cnf={},**kw):
        tk.Button.__init__(self,master,cnf,**kw)
        self.configure(font=("",14),height=2, width=4, relief="flat")
            
if __name__ =="__main__":
    master = tk.Tk()
    master.title("Calendar App")
    a = ""
    m_c = MyCalendar(master,a)
    m_c.pack()
    master.mainloop()