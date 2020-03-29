# モジュールのインポート
import tkinter as tk
import tkinter.ttk as ttk

class TreeView(tk.Frame):
    def __init__(self,master = None):
        tk.Frame.__init__(self,master)
        # ツリービューの作成
        self.tree = ttk.Treeview(self)
        # 列インデックスの作成
        self.tree["columns"] = (1,2,3,4,5)
        # 表スタイルの設定(headingsはツリー形式ではない、通常の表形式)
        self.tree["show"] = "headings"
        # 各列の設定(インデックス,オプション(今回は幅を指定))
        self.tree.column(1,width=187)
        self.tree.column(2,width=70)
        self.tree.column(3,width=50)
        self.tree.column(4,width=50)
        self.tree.column(5,width=187)
        # 各列のヘッダー設定(インデックス,テキスト)
        self.tree.heading(1,text="やること")
        self.tree.heading(2,text="日付")
        self.tree.heading(3,text="時間")
        self.tree.heading(4,text="重要度")
        self.tree.heading(5,text="場所")

        # レコードの作成
        # 1番目の引数-配置場所（ツリー形式にしない表設定ではブランクとする）
        # 2番目の引数-end:表の配置順序を最下部に配置
        #             (行インデックス番号を指定することもできる)
        # 3番目の引数-values:レコードの値をタプルで指定する
        self.tree.insert("","end",values=("解析","2017/05/10","9:00","高","職場"))
        self.tree.pack(side="left")

if __name__=="__main__":
    master = tk.Tk()
    master.title("treeview")
    t = TreeView(master)
    t.pack()
    master.mainloop()