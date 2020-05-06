import tkinter as tk
from entrybox import EntryBoxPlace,EntryBoxDate,EntryBoxThing
from pulldown import PulldownTime,PullDownImportance
from treeview import TreeView
import datetime

class Entry(tk.Frame):
    def __init__(self,master, listbox, schedule):
        tk.Frame.__init__(self,master)
        self.tree = TreeView(self)
        self.tree.grid(row =0, column = 0, columnspan=7, sticky=tk.W+tk.E)

        self.thing = EntryBoxThing(self)
        #self.thing.pack(side="left")
        self.thing.grid(row = 1, column = 0, columnspan=1, sticky=tk.W+tk.E)

        self.date = EntryBoxDate(self)
        #self.date.pack(side="left")
        self.date.grid(row = 1, column = 1, columnspan=1, sticky=tk.W+tk.E)

        self.time = PulldownTime(self)
        #self.time.pack(side="left")
        self.time.grid(row = 1, column = 2, columnspan=1, sticky=tk.W+tk.E)

        self.importance = PullDownImportance(self)
        #self.importance.pack(side="left")
        self.importance.grid(row = 1, column = 3, columnspan=1, sticky=tk.W+tk.E)

        self.place = EntryBoxPlace(self)
        #self.place.pack(side="left")
        self.place.grid(row = 1, column = 4, columnspan=3, sticky=tk.W+tk.E)

        self.add_btn = tk.Button(self,text="追加",command = self._add_treeview)
        #self.add_btn.pack()
        self.add_btn.grid(row = 2, column = 4, columnspan=1, sticky=tk.W+tk.E)

        self.del_btn = tk.Button(self,text="削除",command=self._del_treeview)
        #self.del_btn.pack()
        self.del_btn.grid(row = 2, column = 5, columnspan=1, sticky=tk.W+tk.E)

        self.edit_btn = tk.Button(self,text="編集",command=self._edit_treeview)
        #self.del_btn.pack()
        self.edit_btn.grid(row = 2, column = 6, columnspan=1, sticky = tk.W+tk.E)

        self.listbox = listbox
        self.schedule = schedule
    
    def _add_treeview(self):
        #ツリービューへの追加
        thing = self.thing.txt.get()
        date = self.date.txt.get()
        time = self.time.combo.get()
        importance = self.importance.combo.get()
        place = self.place.txt.get()
        if thing =="" or date =="" or time =="" or importance =="" or \
            self._is_invalid(date,time):
            tk.messagebox.showwarning("warning","入力に誤りがあります")
            return
        self.importance.combo.delete(0,tk.END)
        self.time.combo.delete(0,tk.END)
        self.date.txt.delete(0, tk.END)
        self.thing.txt.delete(0, tk.END)
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
    
    def _edit_treeview(self):
        #try:
            selected = self.tree.tree.selection()[0]
            value = self.tree.tree.item(selected)["values"]

            #Scheduleの削除
            self.schedule.delete_list(value[0])
            #ListBoxの削除
            self.listbox.delete(value)

            thing = self.thing.txt.get()
            date = self.date.txt.get()
            time = self.time.combo.get()
            importance = self.importance.combo.get()
            place = self.place.txt.get()

            if thing =="" or date =="" or time =="" or importance =="" or \
                self._is_invalid(date,time) :
                tk.messagebox.showwarning("warning","入力に誤りがあります")
                return

            self.importance.combo.delete(0,tk.END)
            self.time.combo.delete(0,tk.END)
            self.date.txt.delete(0, tk.END)
            self.thing.txt.delete(0, tk.END)
            self.thing.txt.delete(0, tk.END)
            self.place.txt.delete(0,tk.END)

            new_values = [thing,date,time,importance,place]

            #ツリービューの変更
            self.tree.tree.item(selected,values = new_values)

            #Scheduleの追加
            self.schedule.add_list(thing)

            #ListBoxの追加
            self.listbox.add_list(thing,date,time,importance)
            
        #except:
            #pass

    def _is_invalid(self,date,time):
        try:
            year_month_date = date.split("/")
            hour_minute = time.split(":")
            year_month_date = [int(n) for n in year_month_date]
            hour_minute = [int(n) for n in hour_minute]
            deadline = datetime.datetime(year_month_date[0],year_month_date[1],year_month_date[2],
                hour_minute[0],hour_minute[1])
            return False
        except:
            return True
        
    
if __name__ =="__main__":
    master = tk.Tk()
    master.title("Entry")
    e = Entry(master)
    e.pack()
    master.mainloop()