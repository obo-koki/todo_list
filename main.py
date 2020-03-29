# -*- coding: utf-8 -*-
import tkinter as tk

class App:
    def __init__(self):
        # ウィンドウを初期化
        self.master = tk.Tk()
        self.master.title('TODOアプリ')
        self.master.geometry('400x300')

        #入力エリア作成
        self.input_area = InputArea(self.master)
        self.input_area.pack()
        self.input_area.click_add_btn = self.click_add_btn

        self.list_area = ListArea(self.master)
        self.list_area.pack()

    def mainloop(self):
        # masterに処理を委譲
        self.master.mainloop()

    def click_add_btn(self):
        todo = self.input_area.entry.get()
        self.input_area.entry.delete(0,"end")
        self.list_area.listbox.insert("end", todo)

class InputArea(tk.Frame):
    def __init__(self,master):
        super().__init__(master)

        self.click_add_btn = None

        self.label1 = tk.Label(self, text="TODO")
        self.label1.pack(side="left")

        self.entry = tk.Entry(self)
        self.entry.pack(side="left")

        self.add_btn = tk.Button(self, text="追加",command = self._click_add_btn)
        self.add_btn.pack(side="left")
    
    def _click_add_btn(self):
        if self.click_add_btn:
            self.click_add_btn()

class ListArea(tk.Frame):
    def __init__(self,master):
        super(ListArea, self).__init__(master)

        self.listbox = tk.Listbox(self,height=5)
        self.listbox.pack()

        self.del_btn = tk.Button(self,text="削除",command=self._click_del_btn)
        self.del_btn.pack()

    def _click_del_btn(self):
        print("delete selections")
        sel = self.listbox.curselection()
        for i in sel[::-1]:
            self.listbox.delete(i)
        
class Thing:
    def __init__(self,name,date,importance,place, send):
        self.name = name
        self.date = date
        self.importance = importance
        self.place = place
        self.send = send

def main():
    app = App()
    app.mainloop()

if __name__ == '__main__':
    main()