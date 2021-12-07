from tkinter import *
import tkinter as tk
from tkinter import messagebox

def preventClose():
    pass

Window = tk.Tk()
Window.title("Комплектующие офисов")
Window.geometry('610x300')
Window.resizable(width=False, height=False)
Window.withdraw()
Window.protocol("WM_DELETE_WINDOW", preventClose)
Window["bg"] = '#FFFFFF'

Window_1 = tk.Tk()
Window_1.title("Добавить")
Window_1.geometry('580x80')
Window_1.protocol("WM_DELETE_WINDOW", preventClose)
Window_1.withdraw()
Window_1.resizable(width=False, height=False)
#Window_1.deiconify()

Window_2 = Tk()
Window_2.title("Вход в БД")
Window_2.geometry('260x100')
Window_2.protocol("WM_DELETE_WINDOW", preventClose)
Window_2.resizable(width=False, height=False)

f_1 = open("Dann_1", 'r+')
f_2 = open("Dann_2", 'r+')
f_3 = open("Dann_3", 'r+')
f_4 = open("Dann_4", 'r+')

Mass_1 = []
Mass_2 = []
Mass_3 = []
Mass_4 = []

j = 0
while j < 30:
    Mass_1.append(f_1.readline())
    j += 1
j = 0
while j < 30:
    Mass_2.append(f_2.readline())
    j += 1
j = 0
while j < 30:
    Mass_3.append(f_3.readline())
    j += 1
j = 0
while j < 30:
    Mass_4.append(f_4.readline())
    j += 1
i = 0

def Naz():
    Window_1.withdraw()

def Vhod():
    f_5 = open("Log", 'r+')
    f_6 = open("Par", 'r+')
    Mass_5 = []
    Mass_6 = []
    j = 0
    while j < 30:
        Mass_5.append(f_5.readline())
        j += 1
    j = 0
    while j < 30:
        Mass_6.append(f_6.readline())
        j += 1
    if len(Text_13.get()) != 1:
        Iskom_1 = Text_13.get()
        Iskom_1 = Iskom_1 + "\n"
        Iskom_2 = Text_14.get()
        Iskom_2 = Iskom_2 + "\n"
        Text_13.delete(0, END)
        Text_14.delete(0, END)
        j = 0
        i = 0
        k = 2
        l = 2
        ExitFlag=False
        for i_1 in Mass_5:
            if i_1 == Iskom_1:
                index_1 = Mass_5.index(i_1, j, k)
                for i_2 in Mass_6:
                    if i_2 == Iskom_2:
                        index_2 = Mass_6.index(i_2, i, l)
                        if index_1 == index_2:
                            Window_2.withdraw()
                            Window.deiconify()
                            ExitFlag = True
                            break
                    l += 1
                    i += 1
                l = 2
                i = 0
            if (ExitFlag):
                break
            k += 1
            j += 1

def Uv():
    if Text_14["show"] == "*":
        Text_14["show"] = ""
    else:
        Text_14["show"] = "*"

def Poisk():
    But_9.place_forget()
    Text_12.place_forget()

    f_1 = open("Dann_1", 'r+')
    f_2 = open("Dann_2", 'r+')
    f_3 = open("Dann_3", 'r+')
    f_4 = open("Dann_4", 'r+')

    Mass_1 = []
    Mass_2 = []
    Mass_3 = []
    Mass_4 = []

    j = 0
    while j < 30:
        Mass_1.append(f_1.readline())
        j += 1
    j = 0
    while j < 30:
        Mass_2.append(f_2.readline())
        j += 1
    j = 0
    while j < 30:
        Mass_3.append(f_3.readline())
        j += 1
    j = 0
    while j < 30:
        Mass_4.append(f_4.readline())
        j += 1

    i = 0
    Text_2.configure(state=tk.NORMAL)
    Text_3.configure(state=tk.NORMAL)
    Text_4.configure(state=tk.NORMAL)
    Text_10.configure(state=tk.NORMAL)
    Text_2.delete("1.0", "end")
    Text_3.delete("1.0", "end")
    Text_4.delete("1.0", "end")
    Text_10.delete("1.0", "end")
    if len(Text_1.get()) == 0:
        Mass_1.append("@")
        while True:
            if Mass_1[i] == "@":
                Mass_1.pop(-1)
                i = 0
                break
            Text_2.insert(INSERT, Mass_1[i])
            i += 1

        Mass_2.append("@")
        while True:
            if Mass_2[i] == "@":
                Mass_2.pop(-1)
                i = 0
                break
            Text_3.insert(INSERT, Mass_2[i])
            i += 1

        Mass_3.append("@")
        while True:
            if Mass_3[i] == "@":
                Mass_3.pop(-1)
                i = 0
                break
            Text_4.insert(INSERT, Mass_3[i])
            i += 1

        Mass_4.append("@")
        while True:
            if Mass_4[i] == "@":
                Mass_4.pop(-1)
                i = 0
                break
            Text_10.insert(INSERT, Mass_4[i])
            i += 1
    if len(Text_1.get()) != 0:
        Iskom_1 = Text_1.get() + "\n"
        Text_2.delete("1.0", "end")
        Text_3.delete("1.0", "end")
        Text_4.delete("1.0", "end")
        Text_10.delete("1.0", "end")
        j = 0
        for i_1 in Mass_1:
            if i_1 == Iskom_1:
                index = Mass_1.index(i_1, j, -1)
                Text_2.insert(INSERT, i_1)
                Text_3.insert(INSERT, Mass_2[index])
                Text_4.insert(INSERT, Mass_3[index])
                Text_10.insert(INSERT, Mass_4[index])
            j += 1
    if len(Text_5.get()) != 0:
        Iskom_2 = Text_5.get() + "\n"
        Text_2.delete("1.0", "end")
        Text_3.delete("1.0", "end")
        Text_4.delete("1.0", "end")
        Text_10.delete("1.0", "end")
        j = 0
        for i_2 in Mass_2:
            if i_2 == Iskom_2:
                index = Mass_2.index(i_2, j, -1)
                Text_3.insert(INSERT, i_2)
                Text_2.insert(INSERT, Mass_1[index])
                Text_4.insert(INSERT, Mass_3[index])
                Text_10.insert(INSERT, Mass_4[index])
            j += 1
    if len(Text_6.get()) != 0:
        Iskom_3 = Text_6.get() + "\n"
        Text_2.delete("1.0", "end")
        Text_3.delete("1.0", "end")
        Text_4.delete("1.0", "end")
        Text_10.delete("1.0", "end")
        j = 0
        for i_3 in Mass_3:
            if i_3 == Iskom_3:
                index = Mass_3.index(i_3, j, -1)
                Text_4.insert(INSERT, i_3)
                Text_2.insert(INSERT, Mass_1[index])
                Text_3.insert(INSERT, Mass_2[index])
                Text_10.insert(INSERT, Mass_4[index])
            j += 1

    if len(Text_1.get()) != 0 and len(Text_5.get()) != 0:
        Text_2.delete("1.0", "end")
        Text_3.delete("1.0", "end")
        Text_4.delete("1.0", "end")
        Text_10.delete("1.0", "end")
        Iskom_1 = Text_1.get() + "\n"
        Iskom_2 = Text_5.get() + "\n"
        k = 0
        l = 0
        q = 2
        w = 2
        for i_4 in Mass_1:
            if i_4 == Iskom_1:
                index_1 = Mass_1.index(i_4, k, q)
                Per_1 = i_4
                Per_2 = Mass_2[index_1]
                for i_5 in Mass_2:
                    if i_5 == Iskom_2:
                        index_2 = Mass_2.index(i_5, l, w)
                        Per_4 = i_5
                        Per_5 = Mass_1[index_2]
                        if Per_1 == Per_5 and Per_2 == Per_4:
                            Text_2.insert(INSERT, i_4)
                            Text_3.insert(INSERT, Mass_2[index_1])
                            Text_4.insert(INSERT, Mass_3[index_1])
                            Text_10.insert(INSERT, Mass_4[index_1])
                            break
                    w += 1
                    l += 1
                w = 2
                l = 0
            q += 1
            k += 1
        q = 2
        k = 0
    if len(Text_1.get()) != 0 and len(Text_6.get()) != 0:
        Text_2.delete("1.0", "end")
        Text_3.delete("1.0", "end")
        Text_4.delete("1.0", "end")
        Text_10.delete("1.0", "end")
        Iskom_1 = Text_1.get() + "\n"
        Iskom_2 = Text_6.get() + "\n"
        k = 0
        l = 0
        q = 2
        w = 2
        for i_4 in Mass_1:
            if i_4 == Iskom_1:
                index_1 = Mass_1.index(i_4, k, q)
                Per_1 = i_4
                Per_2 = Mass_3[index_1]
                for i_5 in Mass_3:
                    if i_5 == Iskom_2:
                        index_2 = Mass_3.index(i_5, l, w)
                        Per_4 = i_5
                        Per_5 = Mass_1[index_2]
                        if Per_1 == Per_5 and Per_2 == Per_4:
                            Text_2.insert(INSERT, i_4)
                            Text_3.insert(INSERT, Mass_2[index_1])
                            Text_4.insert(INSERT, Mass_3[index_1])
                            Text_10.insert(INSERT, Mass_4[index_1])
                            break
                    w += 1
                    l += 1
                w = 2
                l = 0
            q += 1
            k += 1
        q = 2
        k = 0
    if len(Text_5.get()) != 0 and len(Text_6.get()) != 0:
        Text_2.delete("1.0", "end")
        Text_3.delete("1.0", "end")
        Text_4.delete("1.0", "end")
        Text_10.delete("1.0", "end")
        Iskom_1 = Text_5.get() + "\n"
        Iskom_2 = Text_6.get() + "\n"
        k = 0
        l = 0
        q = 2
        w = 2
        for i_4 in Mass_2:
            if i_4 == Iskom_1:
                index_1 = Mass_2.index(i_4, k, q)
                Per_1 = i_4
                Per_2 = Mass_3[index_1]
                for i_5 in Mass_3:
                    if i_5 == Iskom_2:
                        index_2 = Mass_3.index(i_5, l, w)
                        Per_4 = i_5
                        Per_5 = Mass_2[index_2]
                        if Per_1 == Per_5 and Per_2 == Per_4:
                            Text_3.insert(INSERT, i_4)
                            Text_2.insert(INSERT, Mass_1[index_1])
                            Text_4.insert(INSERT, Mass_3[index_1])
                            Text_10.insert(INSERT, Mass_4[index_1])
                            break
                    w += 1
                    l += 1
                w = 2
                l = 0
            q += 1
            k += 1
        q = 2
        k = 0
    But_6.place_forget()
    Text_2.configure(state=tk.DISABLED)
    Text_3.configure(state=tk.DISABLED)
    Text_4.configure(state=tk.DISABLED)
    Text_10.configure(state=tk.DISABLED)

def Dobav_1():
    Window_1.deiconify()
    But_6.place_forget()
    But_9.place_forget()
    Text_12.place_forget()
    Text_7.focus()

def Dobav_2():
    Text_2.configure(state=tk.NORMAL)
    Text_3.configure(state=tk.NORMAL)
    Text_4.configure(state=tk.NORMAL)
    Text_2.delete("1.0", "end")
    Text_3.delete("1.0", "end")
    Text_4.delete("1.0", "end")
    if len(Text_7.get()) == 0 or len(Text_8.get()) == 0 or len(Text_9.get()) == 0:
        messagebox.showinfo("Оповещение", "Введите данные ПОЛНОСТЬЮ")
    else:
        f_1 = open("Dann_1", 'a')
        f_2 = open("Dann_2", 'a')
        f_3 = open("Dann_3", 'a')
        f_4 = open("Dann_4", 'a')
        Per_1 = Text_7.get()
        Per_2 = Text_8.get()
        Per_3 = Text_9.get()
        f_1.write(Per_1)
        f_1.write("\n")
        f_2.write(Per_2)
        f_2.write("\n")
        f_3.write(Per_3)
        f_3.write("\n")
        with open('Dann_4') as f:
            Kol_Str = sum(1 for _ in f)
        Kol_Str = Kol_Str+1
        f_4.write(str(Kol_Str) + "\n")

        f_1 = open("Dann_1", 'r+')
        f_2 = open("Dann_2", 'r+')
        f_3 = open("Dann_3", 'r+')
        f_4 = open("Dann_4", 'r+')

        Mass_1 = []
        Mass_2 = []
        Mass_3 = []
        Mass_4 = []

        j = 0
        while j < 30:
            Mass_1.append(f_1.readline())
            j += 1
        j = 0
        while j < 30:
            Mass_2.append(f_2.readline())
            j += 1
        j = 0
        while j < 30:
            Mass_3.append(f_3.readline())
            j += 1
        j = 0
        while j < 30:
            Mass_4.append(f_4.readline())
            j += 1

        i = 0
        Text_2.configure(state=tk.NORMAL)
        Text_3.configure(state=tk.NORMAL)
        Text_4.configure(state=tk.NORMAL)
        Text_10.configure(state=tk.NORMAL)
        Text_2.delete("1.0", "end")
        Text_3.delete("1.0", "end")
        Text_4.delete("1.0", "end")
        Text_10.delete("1.0", "end")
        if len(Text_10.get("1.0", END)) == 1:
            Mass_1.append("@")
            while True:
                if Mass_1[i] == "@":
                    Mass_1.pop(-1)
                    i = 0
                    break
                Text_2.insert(INSERT, Mass_1[i])
                i += 1

            Mass_2.append("@")
            while True:
                if Mass_2[i] == "@":
                    Mass_2.pop(-1)
                    i = 0
                    break
                Text_3.insert(INSERT, Mass_2[i])
                i += 1

            Mass_3.append("@")
            while True:
                if Mass_3[i] == "@":
                    Mass_3.pop(-1)
                    i = 0
                    break
                Text_4.insert(INSERT, Mass_3[i])
                i += 1

            Mass_4.append("@")
            while True:
                if Mass_4[i] == "@":
                    Mass_4.pop(-1)
                    i = 0
                    break
                Text_10.insert(INSERT, Mass_4[i])
                i += 1
        messagebox.showinfo("Оповищение", "Данные были успешно добавлены")
    Text_2.configure(state=tk.DISABLED)
    Text_3.configure(state=tk.DISABLED)
    Text_4.configure(state=tk.DISABLED)
    Text_10.configure(state=tk.DISABLED)
    Text_7.delete(0, END)
    Text_8.delete(0, END)
    Text_9.delete(0, END)

def Izm():
    But_9.place_forget()
    Text_12.place_forget()
    if len(Text_1.get()) != 0 or len(Text_5.get()) != 0 or len(Text_6.get()) != 0:
        Poisk()
        Text_2.configure(state=tk.NORMAL)
        Text_3.configure(state=tk.NORMAL)
        Text_4.configure(state=tk.NORMAL)
    else:
        f_1 = open("Dann_1", 'r+')
        f_2 = open("Dann_2", 'r+')
        f_3 = open("Dann_3", 'r+')

        Mass_1 = []
        Mass_2 = []
        Mass_3 = []

        j = 0
        while j < 30:
            Mass_1.append(f_1.readline())
            j += 1
        j = 0
        while j < 30:
            Mass_2.append(f_2.readline())
            j += 1
        j = 0
        while j < 30:
            Mass_3.append(f_3.readline())
            j += 1
        i = 0
        Text_2.configure(state=tk.NORMAL)
        Text_3.configure(state=tk.NORMAL)
        Text_4.configure(state=tk.NORMAL)
        Text_2.delete("1.0", "end")
        Text_3.delete("1.0", "end")
        Text_4.delete("1.0", "end")
        Poisk()
        Text_2.configure(state=tk.NORMAL)
        Text_3.configure(state=tk.NORMAL)
        Text_4.configure(state=tk.NORMAL)

    But_6.place(x=475, y=155)

def Sohr():
    if len(Text_2.get("1.0", END)) == 1 and len(Text_3.get("1.0", END)) == 1 and len(Text_4.get("1.0", END)) == 1:
        But_6.place_forget()
    if len(Text_1.get()) != 0 or len(Text_5.get()) != 0 or len(Text_6.get()) != 0:
        f_1 = open("Dann_1", 'r+')
        f_2 = open("Dann_2", 'r+')
        f_3 = open("Dann_3", 'r+')
        f_4 = open("Dann_4", 'r+')

        Mass_1 = []
        Mass_2 = []
        Mass_3 = []
        Mass_4 = []

        j = 0
        while j < 30:
            Mass_1.append(f_1.readline())
            j += 1
        j = 0
        while j < 30:
            Mass_2.append(f_2.readline())
            j += 1
        j = 0
        while j < 30:
            Mass_3.append(f_3.readline())
            j += 1
        j = 0
        while j < 30:
            Mass_4.append(f_4.readline())
            j += 1
        Iskom_4 = Text_10.get("1.0", END)
        Men_4 = Text_2.get("1.0", END)
        Men_5 = Text_3.get("1.0", END)
        Men_6 = Text_4.get("1.0", END)
        iskom_4 = Iskom_4.split("\n")
        men_4 = Men_4.split("\n")
        men_5 = Men_5.split("\n")
        men_6 = Men_6.split("\n")
        l = 0
        iskom_4.append("@")
        for i_1 in iskom_4:
            if iskom_4[l] == "@":
                break
            else:
                iskom_4[l] = (str(i_1) + "\n")
                l += 1
        l = 0
        men_4.append("@")
        for i_2 in men_4:
            if men_4[l] == "@":
                break
            else:
                men_4[l] = (str(i_2) + "\n")
                l += 1
        l = 0
        men_5.append("@")
        for i_3 in men_5:
            if men_5[l] == "@":
                break
            else:
                men_5[l] = (str(i_3) + "\n")
                l += 1
        l = 0
        men_6.append("@")
        for i_4 in men_6:
            if men_6[l] == "@":
                break
            else:
                men_6[l] = (str(i_4) + "\n")
                l += 1
        i = 0
        while True:
            Iskom_4 = iskom_4[i]
            Men_4 = men_4[i]
            Men_5 = men_5[i]
            Men_6 = men_6[i]
            for i_4 in Mass_4:
                if i_4 == Iskom_4:
                    index = Mass_4.index(i_4, 0, -1)
                    Mass_1[index] = Men_4
                    Mass_2[index] = Men_5
                    Mass_3[index] = Men_6
                    break
            if iskom_4[i] == "@":
                del iskom_4[i]
                i = 0
                break
            if men_4[i] == "@":
                del men_4[i]
                i = 0
                break
            if men_5[i] == "@":
                del men_5[i]
                i = 0
                break
            if men_6[i] == "@":
                del men_6[i]
                i = 0
                break
            else:
                i += 1
        Per_1 = ''.join(Mass_1)
        Per_2 = ''.join(Mass_2)
        Per_3 = ''.join(Mass_3)
        f_1 = open("Dann_1", 'r+')
        f_2 = open("Dann_2", 'r+')
        f_3 = open("Dann_3", 'r+')
        f_1.seek(0)
        f_1.truncate()
        f_2.seek(0)
        f_2.truncate()
        f_3.seek(0)
        f_3.truncate()
        Per_1 = Per_1
        Per_1 = Per_1[:-1]
        Per_2 = Per_2
        Per_2 = Per_2[:-1]
        Per_3 = Per_3
        Per_3 = Per_3[:-1]
        f_1.write(Per_1)
        f_2.write(Per_2)
        f_3.write(Per_3)
        f_1.write("\n")
        f_2.write("\n")
        f_3.write("\n")

        But_6.place_forget()
        Text_2.configure(state=tk.DISABLED)
        Text_3.configure(state=tk.DISABLED)
        Text_4.configure(state=tk.DISABLED)
        messagebox.showinfo("Оповещение", "Данные были успешно сохранены")
    if (len(Text_1.get()) == 0 and len(Text_5.get()) == 0 and len(Text_6.get()) == 0) and (len(Text_2.get("1.0", END)) != 1 and len(Text_3.get("1.0", END)) != 1 and len(Text_4.get("1.0", END)) != 1):
        f_1 = open("Dann_1", 'r+')
        f_2 = open("Dann_2", 'r+')
        f_3 = open("Dann_3", 'r+')
        f_4 = open("Dann_4", 'r+')

        RMass_1 = []
        RMass_2 = []
        RMass_3 = []
        RMass_4 = []

        j = 0
        while j < 30:
            RMass_1.append(f_1.readline())
            j += 1
        j = 0
        while j < 30:
            RMass_2.append(f_2.readline())
            j += 1
        j = 0
        while j < 30:
            RMass_3.append(f_3.readline())
            j += 1
        j = 0
        while j < 30:
            RMass_4.append(f_4.readline())
            j += 1

        f_1.seek(0)
        f_1.truncate()
        f_2.seek(0)
        f_2.truncate()
        f_3.seek(0)
        f_3.truncate()
        Per_1 = Text_2.get("1.0", END)
        Per_1 = Per_1[:-1]
        Per_1 = Per_1[:-1]
        Per_2 = Text_3.get("1.0", END)
        Per_2 = Per_2[:-1]
        Per_2 = Per_2[:-1]
        Per_3 = Text_4.get("1.0", END)
        Per_3 = Per_3[:-1]
        Per_3 = Per_3[:-1]
        f_1.write(Per_1)
        f_2.write(Per_2)
        f_3.write(Per_3)
        f_1.write("\n")
        f_2.write("\n")
        f_3.write("\n")
        with open('Dann_1') as f_1:
            Kol_Str_1 = sum(1 for _ in f_1)
        with open('Dann_2') as f_2:
            Kol_Str_2 = sum(1 for _ in f_2)
        with open('Dann_3') as f_3:
            Kol_Str_3 = sum(1 for _ in f_3)
        with open('Dann_4') as f_4:
            Kol_Str_4 = sum(1 for _ in f_4)
            Kol_Str_4 = Kol_Str_4 + 1
        if Kol_Str_1 == Kol_Str_2 == Kol_Str_3 == Kol_Str_4:
            Poisk()
            messagebox.showinfo("Оповещение", "Данные были успешно сохранены")
        else:
            f_1 = open("Dann_1", 'r+')
            f_2 = open("Dann_2", 'r+')
            f_3 = open("Dann_3", 'r+')
            f_4 = open("Dann_4", 'r+')

            f_1.seek(0)
            f_1.truncate()
            f_2.seek(0)
            f_2.truncate()
            f_3.seek(0)
            f_3.truncate()
            f_4.seek(0)
            f_4.truncate()
            i = 0
            while i < 30:
                f_1.write(RMass_1[i])
                i += 1
            i = 0
            while i < 30:
                f_2.write(RMass_2[i])
                i += 1
            i = 0
            while i < 30:
                f_3.write(RMass_3[i])
                i += 1
            i = 0
            while i < 30:
                f_4.write(RMass_4[i])
                i += 1
            Poisk()
            messagebox.showinfo("Оповещение", "При изменении колличества строк требуется пользоваться кнопками <Добавить> и <Удалить>")
        Poisk()
        But_6.place_forget()

def Exit():
    Window.destroy()
    Window_1.destroy()
    Window_2.destroy()

def Nas():
    Window.withdraw()
    Window_1.withdraw()
    Window_2.deiconify()
    Text_13.focus()

def Pod():
    f_1 = open("Dann_1", 'r+')
    f_2 = open("Dann_2", 'r+')
    f_3 = open("Dann_3", 'r+')
    f_4 = open("Dann_4", 'r+')

    Mass_1 = []
    Mass_2 = []
    Mass_3 = []
    Mass_4 = []

    j = 0
    while j < 30:
        Mass_1.append(f_1.readline())
        j += 1
    j = 0
    while j < 30:
        Mass_2.append(f_2.readline())
        j += 1
    j = 0
    while j < 30:
        Mass_3.append(f_3.readline())
        j += 1
    j = 0
    while j < 30:
        Mass_4.append(f_4.readline())
        j += 1
    for i_1 in Mass_4:
        if i_1 == (Text_12.get("1.0", END)):
            index = Mass_4.index(i_1)
            Mass_1.pop(index)
            Mass_2.pop(index)
            Mass_3.pop(index)
    with open('Dann_1') as f_1:
        Kol_Str_1 = sum(1 for _ in f_1)
    Kol_Str = Kol_Str_1 - 1
    Mass_5 = []
    j = 0
    i = 1
    while j < 30:
        if j == Kol_Str:
            break
        Mass_5.append(str(i) + "\n")
        i += 1
        j += 1

    Kol_Str_2 = Kol_Str_1 + 1

    f_1 = open("Dann_1", 'r+')
    f_2 = open("Dann_2", 'r+')
    f_3 = open("Dann_3", 'r+')
    f_4 = open("Dann_4", 'r+')

    f_1.seek(0)
    f_1.truncate()
    f_2.seek(0)
    f_2.truncate()
    f_3.seek(0)
    f_3.truncate()
    f_4.seek(0)
    f_4.truncate()

    i = 0
    while i < Kol_Str_2:
        f_1.write(Mass_1[i])
        i += 1
    i = 0
    while i < Kol_Str_2:
        f_2.write(Mass_2[i])
        i += 1
    i = 0
    while i < Kol_Str_2:
        f_3.write(Mass_3[i])
        i += 1
    i = 0
    while i < Kol_Str:
        f_4.write(Mass_5[i])
        i += 1
    f_1 = open("Dann_1", 'r+')
    f_2 = open("Dann_2", 'r+')
    f_3 = open("Dann_3", 'r+')
    f_4 = open("Dann_4", 'r+')

    Mass_1 = []
    Mass_2 = []
    Mass_3 = []
    Mass_4 = []

    j = 0
    while j < 30:
        Mass_1.append(f_1.readline())
        j += 1
    j = 0
    while j < 30:
        Mass_2.append(f_2.readline())
        j += 1
    j = 0
    while j < 30:
        Mass_3.append(f_3.readline())
        j += 1
    j = 0
    while j < 30:
        Mass_4.append(f_4.readline())
        j += 1

    i = 0
    Text_2.configure(state=tk.NORMAL)
    Text_3.configure(state=tk.NORMAL)
    Text_4.configure(state=tk.NORMAL)
    Text_10.configure(state=tk.NORMAL)
    Text_2.delete("1.0", "end")
    Text_3.delete("1.0", "end")
    Text_4.delete("1.0", "end")
    Text_10.delete("1.0", "end")
    if len(Text_10.get("1.0", END)) == 1:
        Mass_1.append("@")
        while True:
            if Mass_1[i] == "@":
                Mass_1.pop(-1)
                i = 0
                break
            Text_2.insert(INSERT, Mass_1[i])
            i += 1

        Mass_2.append("@")
        while True:
            if Mass_2[i] == "@":
                Mass_2.pop(-1)
                i = 0
                break
            Text_3.insert(INSERT, Mass_2[i])
            i += 1

        Mass_3.append("@")
        while True:
            if Mass_3[i] == "@":
                Mass_3.pop(-1)
                i = 0
                break
            Text_4.insert(INSERT, Mass_3[i])
            i += 1

        Mass_4.append("@")
        while True:
            if Mass_4[i] == "@":
                Mass_4.pop(-1)
                i = 0
                break
            Text_10.insert(INSERT, Mass_4[i])
            i += 1
    Text_2.configure(state=tk.DISABLED)
    Text_3.configure(state=tk.DISABLED)
    Text_4.configure(state=tk.DISABLED)
    Text_10.configure(state=tk.DISABLED)
    But_9.place_forget()
    Text_12.place_forget()
    Lab_8.place_forget()
    messagebox.showinfo("Оповещение", "Данные были удалены")

def Del():
    But_6.place_forget()
    Poisk()
    But_9.place(x=475, y=185)
    Lab_8.place(x=505, y=160)
    Text_12.place(x=525, y=160)

def multyple_yview(*args):
    Text_10.yview(*args)
    Text_2.yview(*args)
    Text_3.yview(*args)
    Text_4.yview(*args)

def on_mouse_wheel(event):
    if event.widget.master is Fr:
        Fr.yview_scroll(-event.delta//30, 'units')

def Tab_1(event):
    Text_14.focus()

def Tab_2(event):
    Vhod()
    Text_1.focus()

def Tab_3(self):
    Text_5.focus()

def Tab_4(self):
    Text_6.focus()

def Tab_5(self):
    Poisk()
    Text_1.focus()

def Tab_6(self):
    Text_8.focus()

def Tab_7(self):
    Text_9.focus()

def Tab_8(self):
    Dobav_2()
    Text_7.focus()

def Esc(self):
    if Lab_11["fg"] == '#FFFFFF':
        Lab_11["fg"] = '#000000'
    else:
        Lab_11["fg"] = '#FFFFFF'

Window.bind("<Escape>", Esc)

But_1 = Button(Window, text="Поиск", command=Poisk, width=16)
But_1.place(x=475, y=35)
But_2 = Button(Window, text="Добавить", command=Dobav_1, width=16)
But_2.place(x=475, y=65)
But_3 = Button(Window_1, text="Добавить", command=Dobav_2, width=16)
But_3.place(x=449, y=15)
But_4 = Button(Window_1, text="Назад", command=Naz, width=16)
But_4.place(x=449, y=45)
But_5 = Button(Window, text="Изменить", command=Izm, width=16)
But_5.place(x=475, y=125)
But_6 = Button(Window, text="Сохранить", command=Sohr, width=16)
But_6.place()
But_7 = Button(Window, text="Назад", command=Nas, width=16)
But_7.place(x=475, y=255)
But_8 = Button(Window, text="Удалить", command=Del, width=16)
But_8.place(x=475, y=95)
But_9 = Button(Window, text="Подтвердить", command=Pod, width=16)
But_9.place()
But_10 = Button(Window_2, text="Выйти", command=Exit, width=16)
But_10.place(x=130, y=65)
But_11 = Button(Window_2, text="Войти", command=Vhod, width=16)
But_11.place(x=10, y=65)
But_12 = Button(Window_2, text="<0>", command=Uv, font=("", "7", ""))
But_12.place(x=200, y=40)

Lab_1 = Label(Window, text="Наименование")
Lab_1.place(x=51, y=18)
Lab_2 = Label(Window, text="Идентификационный номер")
Lab_2.place(x=215, y=18)
Lab_3 = Label(Window, text="Кабинет")
Lab_3.place(x=379, y=18)
Lab_4 = Label(Window_1, text="Наименование")
Lab_4.place(x=15, y=18)
Lab_5 = Label(Window_1, text="Идентификационный номер")
Lab_5.place(x=179, y=18)
Lab_6 = Label(Window_1, text="Кабинет")
Lab_6.place(x=343, y=18)
Lab_7 = Label(Window, text="ID")
Lab_7.place(x=15, y=18)
Lab_8 = Label(Window, text="ID")
Lab_8.place()
Lab_9 = Label(Window_2, text="Логин: ")
Lab_9.place(x=30, y=10)
Lab_10 = Label(Window_2, text="Пароль: ")
Lab_10.place(x=30, y=40)
Lab_11 = Label(Window, text="Автор: Разварин Матвей Сергеевич (PANIKAN)", fg='#FFFFFF')
Lab_11.place(x=10, y=0)

Fr = Frame(Window)
Fr.place(x=15, y=70)

Fr.bind('<MouseWheel>', on_mouse_wheel)

text_scroll = Scrollbar(Fr)
text_scroll.pack(side=RIGHT, fill=Y)

Text_1 = Entry(Window, width=27)
Text_1.place(x=51, y=38)
Text_1.bind("<Return>", Tab_3)
Text_10 = Text(Fr, width=4, height=13, yscrollcommand=text_scroll.set, wrap="none")
Text_10.pack(side=LEFT, fill=Y)
Text_10.configure(state=tk.DISABLED)
Text_2 = Text(Fr, width=20, height=13, yscrollcommand=text_scroll.set, wrap="none")
Text_2.pack(side=LEFT, fill=Y)
Text_2.configure(state=tk.DISABLED)
Text_3 = Text(Fr, width=20, height=13, yscrollcommand=text_scroll.set, wrap="none")
Text_3.pack(side=LEFT, fill=Y)
Text_3.configure(state=tk.DISABLED)
Text_4 = Text(Fr, width=8, height=13, yscrollcommand=text_scroll.set, wrap="none")
Text_4.pack(side=LEFT, fill=Y)
Text_4.configure(state=tk.DISABLED)
Text_5 = Entry(Window, width=27)
Text_5.place(x=215, y=38)
Text_5.bind("<Return>", Tab_4)
Text_6 = Entry(Window, width=11)
Text_6.place(x=379, y=38)
Text_6.bind("<Return>", Tab_5)
Text_7 = Entry(Window_1, width=27)
Text_7.place(x=15, y=38)
Text_7.bind("<Return>", Tab_6)
Text_8 = Entry(Window_1, width=27)
Text_8.place(x=179, y=38)
Text_8.bind("<Return>", Tab_7)
Text_9 = Entry(Window_1, width=11)
Text_9.place(x=343, y=38)
Text_9.bind("<Return>", Tab_8)
Text_11 = Text(Window, width=4, height=1)
Text_11.place(x=15, y=38)
Text_11.configure(state=tk.DISABLED)
Text_12 = Text(Window, width=4, height=1)
Text_12.place()
Text_13 = Entry(Window_2, width=18)
Text_13.place(x=80, y=10)
Text_13.focus()
Text_13.bind("<Return>", Tab_1)
Text_14 = Entry(Window_2, show="*", width=18)
Text_14.place(x=80, y=40)
Text_14.bind("<Return>", Tab_2)

text_scroll.config(command=multyple_yview)

Window.mainloop()