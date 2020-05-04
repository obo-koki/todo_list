import tkinter as tk
from entrybox import EntryBoxPlace,EntryBoxDate,EntryBoxThing
from pulldown import PulldownTime,PullDownImportance
from treeview import TreeView
import datetime

class Entry(tk.Frame):
    def __init__(self,master, listbox, schedule):
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
        self.listbox = listbox
        self.schedule = schedule
    
    def _add_treeview(self):
        #ツリービューへの追加
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
        self.tree.index_list.append(ind)#ツリービュー上の識別子の保存
        #List Boxへの追加
        self.listbox.add_list(thing,date,time,importance)

        #Scheduleへの追加
        self.schedule.add_list(thing)

    def _del_treeview(self):
        try:
            #ツリービューの削除
            selected = self.tree.tree.selection()[0]
            value = self.tree.tree.item(selected)["values"]
            thing = value[0]
            self.tree.tree.delete(selected)
            self.tree.index_list.remove(selected)
            #Scheduleの削除
            self.schedule.delete_list(thing)
            #ListBoxの削除 TODO
            self.listbox.delete(value)

        except:
            pass
    
if __name__ =="__main__":
    master = tk.Tk()
    master.title("Entry")
    e = Entry(master)
    e.pack()
    master.mainloop()