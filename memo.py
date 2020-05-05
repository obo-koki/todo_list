import tkinter as tk
import tkinter.font as font

class Memo(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self,master)

        #フォント指定
        my_font = font.Font(self,size=12,family = "MS Gothic")

        #エディタの作成
        text_widget = tk.Text(self, wrap = tk.WORD, font = my_font, width=60,height=26)
        text_widget.pack()
        #text_widget.grid(column=0, row=0, sticky = (tk.N, tk.S, tk.E, tk.W))

if __name__=="__main__":
    master = tk.Tk()
    master.title("memo")
    t = Memo(master)
    t.pack()
    master.mainloop()