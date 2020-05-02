import tkinter as tk
from entrybox import EntryBoxPlace,EntryBoxDate,EntryBoxThing
from pulldown import PulldownTime,PullDownImportance
from treeview import TreeView

class Entry(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.tree = TreeView(self)
        self.tree.pack()
        self.thing = EntryBoxThing(self)
        self.thing.pack(side="left")
        self.date = EntryBoxDate(self)
        self.date.pack(side="left")
        self.time = PulldownTime(self)
        self.time.pack(side="left")
        self.importance = PullDownImportance(self)
        self.importance.pack(side="left")
        self.place = EntryBoxPlace(self)
        self.place.pack(side="left")
        self.add_btn = tk.Button(self,text="追加",command = self._add_treeview)
        self.add_btn.pack()
        self.del_btn = tk.Button(self,text="削除",command=self._del_treeview)
        self.del_btn.pack()
    
    def _add_treeview(self):
        thing = self.thing.txt.get()
        self.thing.txt.delete(0, tk.END)
        date = self.date.txt.get()
        self.date.txt.delete(0, tk.END)
        time = self.time.combo.get()
        self.time.combo.delete(0,tk.END)
        importance = self.importance.combo.get()
        self.importance.combo.delete(0,tk.END)
        place = self.place.txt.get()
        self.place.txt.delete(0,tk.END)
        ind = self.tree.tree.insert("","end",
                    values=(thing,
                            date,
                            time,
                            importance,
                            place)
                    )
        self.tree.index_list.append(ind)

    def _del_treeview(self):
        try:
            selected = self.tree.tree.selection()[0]
            self.tree.tree.delete(selected)
            self.tree.index_list.remove(selected)
        except:
            pass
    
if __name__ =="__main__":
    master = tk.Tk()
    master.title("Entry")
    e = Entry(master)
    e.pack()
    master.mainloop()