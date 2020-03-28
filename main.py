# -*- coding: utf-8 -*-
import Tkinter as tk

class App:
    def __init__(self):
        # ウィンドウを初期化
        self.master = tk.Tk()
        self.master.title('TODOアプリ')
        self.master.geometry('400x300')

        #入力エリア作成
        self.input_area = InputArea(self.master)
        self.input_area.pack()

    def mainloop(self):
        # masterに処理を委譲
        self.master.mainloop()

class InputArea(tk.Frame):
    def __init__(self,master):
        super(InputArea, self).__init__(master)

        self.label1 = tk.Label(self, text="TODO")
        self.label.pack(side="left")

        self.entry = tk.Entry(self)
        self.entry.pack(side="left")

        self.add_btn = tk.Button(self, text="追加",command = self._click_add_btn)
        self.add_btn.pack(side="left")
    
    def _click_add_btn(self):
        print("add",self.entry.get())


def main():
    app = App()
    app.mainloop()

if __name__ == '__main__':
    main()