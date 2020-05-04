import tkinter as tk
import tkinter.ttk as ttk
import datetime

class ListBox(tk.Frame):
    def __init__(self,master=None,color="white"):
        tk.Frame.__init__(self,master)
        self.listarray = []
        self.txt = tk.StringVar(value=self.listarray)
        self.listbox = tk.Listbox(self, listvariable= self.txt,
                width=40,height=13,background=color)
        self.listbox.pack()

class ListBox4(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.up_left = ListBox(self,"misty rose")
        self.up_left.grid(row=0,column=0)
        self.up_right = ListBox(self,"wheat1")
        self.up_right.grid(row=0,column=1)
        self.down_left = ListBox(self,"lemon chiffon")
        self.down_left.grid(row=1,column=0)
        self.down_right = ListBox(self,"DarkSlateGray1")
        self.down_right.grid(row=1,column=1)

        self.date_th = 7
    
    def add_list(self,thing,date,time,importance):
        now = datetime.datetime.now()
        ref  = now + datetime.timedelta(days=self.date_th)
        year_month_date = date.split("/")
        hour_minute = time.split(":")
        year_month_date = [int(n) for n in year_month_date]
        hour_minute = [int(n) for n in hour_minute]
        deadline = datetime.datetime(year_month_date[0],year_month_date[1],year_month_date[2],
            hour_minute[0],hour_minute[1])
        content = "●"+" "+thing+" "+date
        if importance =="高" and deadline <=ref:
            self.up_left.listbox.insert(tk.END, content) 
        elif importance =="高" and deadline >ref:
            self.up_right.listbox.insert(tk.END, content)
        elif importance =="低" and deadline <=ref:
            self.down_left.listbox.insert(tk.END, content)
        else:
            self.down_right.listbox.insert(tk.END, content)

    def delete(self,value):
        del_content = "●"+" "+value[0]+" "+value[1]
        self.delete_content(self.up_left, del_content)
        self.delete_content(self.up_right, del_content)
        self.delete_content(self.down_left, del_content)
        self.delete_content(self.down_right, del_content)
    
    def delete_content(self,listbox,del_content):
        content_list = listbox.listbox.get(0,999)
        for i in range(len(content_list)):
            if del_content == content_list[i]:
                listbox.listbox.delete(i)
        
if __name__ =="__main__":
    master = tk.Tk()
    master.title("list box")
    listbox = ListBox4(master)
    listbox.pack()
    listbox.mainloop()