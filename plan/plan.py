# coding=utf-8
import tkinter as tk


class Plan:
    add = False

    def __init__(self):
        self.wd = tk.Tk()
        self.var = tk.StringVar(value="init")

    def hit_add(self):
        if not self.add:
            self.add = True
            self.var.set("123")
        else:
            self.add = False
            self.var.set("345")

    def txtEntry(self,s):
        t = tk.Entry(self.wd,show=s)
        t.insert('insert',"qweqw")
        t.pack()
        return t

    def window(self):
        wd = self.wd
        wd.title('plan')
        wd.geometry('700x500')
        var = tk.StringVar(value="123")

        def aa():
            var.set("asd")
        # self.var = tk.StringVar()
        l = tk.Label(wd, textvariable=self.var,  # 标签的文字
                     bg='green',  # 背景颜色
                     font=('Arial', 12),  # 字体和字体大小
                     width=15, height=2  # 标签长宽
                     )
        l.pack(expand=tk.YES)

        b = tk.Button(wd,
                      text='hit me',  # 显示在按钮上的文字
                      width=15, height=2,
                      command=self.hit_add)  # 点击按钮式执行的命令
        b.bind("<asda>",None)
        b.pack(fill=tk.NONE,side=tk.BOTTOM,expand=tk.YES)  # 按钮位置
        self.txtEntry("")
        return wd


if __name__ == '__main__':
    p = Plan()
    w = p.window()
    w.mainloop()
