""" Курсовой проект на Python 3.x.
    ЭБбз-18-1 А.С Пархоменко, 2019-2020
    e-mail: T12492247@yandex.ru
    web: https://github.com/Aleksey-Parkhomenko/
    Версия 0.0.1
"""
from tkinter import *
import tkinter.ttk 
from tkinter import messagebox
from tkinter import ttk
import time
from tabulate import tabulate

window = Tk()
window.resizable(height = False, width = False)
window.title('Курсовой проект')
window.geometry("670x420")
nb = tkinter.ttk.Notebook(window)
nb.pack(fill='both', expand='yes')
page1 = tkinter.ttk.Frame(nb)
page2 = tkinter.ttk.Frame(nb)
page3 = tkinter.ttk.Frame(nb)
nb.add(page1, text='Титульный лист')
nb.add(page2, text='Аптека')
nb.add(page3, text='Таблица')

# Функции
def close_window():
    """ Логическая функция, закрытия окна """
    answer = messagebox.askyesno(title="Выход", message="Выйти из программы?")
    if answer == True:
        window.destroy() 
    else:
        return
    
def about():
    win = Toplevel(window)
    lab = Label(win,text=" Курсовой проект является бесплатной программой с открытым исходным кодом,\n\
                созданной в рамка поствленной задачи.\n Лицензия этого продукта были предоставлена\n вам в рамках (MPL).")
    lab.pack()

def show_message():
    messagebox.showinfo("GUI Python", message.get())
 
def read_data():
    global dat,num_dat,tab
    if num_dat > 0:
        messagebox.showinfo("Сообщение",'Данные уже считаны')
        return
    try:
        f = open("data.txt")
        dat = [line.strip() for line in f]
        f.close()
    except:
        print('Фаил data.txt - не найден!')
        raise SystemExit
    view1.configure(text="Загрузка началась")
    time.sleep(1)
    num_dat = len(dat)
    messagebox.showinfo("Сообщение","Загрузка завершена успешно")
    view1.configure(text="Считано строк с данными :")
    view1_1.configure(text=num_dat)
    return

def browse_data():
    global dat,num_dat,tab
    if num_dat == 0:
        view1.configure(text="Данные не считаны")
        return
    if len(tab) == 0:
        tab = [[ " " for i in range(7)] for j in range(num_dat)]
        lin = []
        for i in range(num_dat):
            lin = dat[i].split(' ')
            tab[i] = lin
    for i in range(num_dat):
        columns = ['№', 'Наименвание', 'Фирма', 'Назначение', 'Цена','Группа', 'Производитель']
        view2.configure(text=(tabulate(tab, headers=columns, tablefmt='pipe',stralign='right',colalign="right")))
        messagebox.showinfo("Сообщение","Просмотреть данные можно на вкладке Таблица")
        return

def search_drug():
    global dat,num_dat,tab,message,enter, tx
    if len(tab) == 0:
        view1.configure(text='Таблица не заполнена !')
        return
    fname = (enter.get())
    res = True 
    for i in range(num_dat):
        lowt = tab[i][1].lower() 
        if lowt.count(fname.lower())>0:
            lbl = tab[i]
            view2.configure(text=lbl)
            messagebox.showinfo("Сообщение","Просмотреть данные можно на вкладке Таблица")
            res = False
    if res:
        view1_1.place_forget()
        view1.configure(text='Препарат {0} не обнажен '.format(fname))
        return

def сhange_price():
    global dat,num_dat,tab
    if len(tab) == 0:
        view1.configure(text='Таблица не заполнена !')
        return
    ns = (enter.get())
    price = (enter2.get())
    try:
        num_sot = int(ns)
    except:
        view1.configure(text='Недопустимый номер превората !')
        return
    if num_sot<1 or num_sot>num_dat:
        view1.configure(text='Недопустимый номер превората !')
        return
    tab[num_sot-1][4] = price
    messagebox.showinfo("Сообщение","Изменение цены прошло успешно")
    browse_data()
    return

def save():
    global dat,num_dat,tab
    if len(tab) == 0:
        view1.configure(text='Данные в таблице отсутствуют.')
        return
    try:
        g = open("data.txt","wt")
    except:
        view1.configure(text='Ошибка записи в файл')
        raise SystemExit
    for i in range(num_dat):
        lin = ' '.join(tab[i])+'\n'
        g.write(lin)
    view1.configure(text='Данные в файл сохранены')
    g.close()
    return

# Переменные в программе
dat = [] # Список строк файла
num_dat = 0 # Число строк с данными файла
tab = [] # Таблица данных

# Вкладка №1
lbl=Label(page1,text=" МИНИСТЕРСТВО НАУКИ И ВЫСШЕГО ОБРАЗОВАНИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ\n Тюменский индустриальный университет\n Институт сервиса и отраслевого управления\n Кафедра бизнес-информатики и математики\n \n   Курсовой проект\n по дисциплине: Программирование\n Обработка данных медицинского учреждения ",font=("Ubuntu",12),justify=CENTER)
lbl.grid(column=1,row=0)
lbl0=Label(page1,text=" Выполнил: Пархоменко А.С. \n студент группы ЭБбз-18-1\n Проверил: К.т.н. доцент Сергеев В.В.", justify=LEFT )
lbl0.place( x=430, y=180)
lbl0.config(width=30, height=9)
lbl01=Label(page1,text=" Тюмень\n ТИУ \n 2020", font=("Ubuntu",10),justify=CENTER )
lbl01.place( x=280, y=270)
lbl01.config(width=15, height=10)

# Вкладка №2 кнопки управления
load = Button(page2,text="Считываем файл с данными ...",font=("Ubuntu",10),command=read_data)
load.place( x=450, y=10)
load.config(width=25, height=1)
data = Button(page2,text="Просматриваем данные ... ",font=("Ubuntu",10),justify=LEFT,command=browse_data)
data.place( x=450, y=50)
data.config(width=25, height=1)
search_drug = Button(page2,text="Поиск препарата",font=("Ubuntu",10),justify=LEFT,command=search_drug)
search_drug.place( x=450, y=90)
search_drug.config(width=25, height=1)
сhange_price = Button(page2,text="Изменить цену",font=("Ubuntu",10),justify=LEFT,command=сhange_price)
сhange_price.place( x=450, y=130)
сhange_price.config(width=25, height=1)
save = Button(page2,text="Сохраняем данные в файл...",font=("Ubuntu",10),justify=LEFT,command=save)
save.place( x=450, y=170)
save.config(width=25, height=1)
close_window = Button(page2,text="Выход из программы",font=("Ubuntu",10),justify=LEFT,command=close_window)
close_window.place( x=450, y=210)
close_window.config(width=25, height=1)
about = Button(page2,text="О программе",font=("Ubuntu",10),justify=LEFT,command=about)
about.place( x=450, y=250)
about.config(width=25, height=1)

# Вкладка №2,3 Окно вывода
view1=Label(page2,text="",font=("Ubuntu",10))
view1.place( x=150, y=10)
view1.config(width=0, height=1)
view1_1=Label(page2,text="",font=("Ubuntu",10))
view1_1.place( x=315, y=10)
view1_1.config(width=0, height=1)
view2 = Label(page3,text="Вывод таблицы",font=("Ubuntu",10), justify=LEFT)
view2.grid(column=0,row=0)
view3=Label(page2,text="Поиск:",font=("Ubuntu",10))
view3.place( x=100, y=50)
view3.config(width=0, height=1)
view3=Label(page2,text="Замена:",font=("Ubuntu",10))
view3.place( x=90, y=90)
view3.config(width=0, height=1)

# Вкладка №2 Окно ввода
enter = Entry(page2,width=30,font=("Ubuntu",10))
enter.place( x=150, y=50)
enter2 = Entry(page2,width=30,font=("Ubuntu",10))
enter2.place( x=150, y=90)

window.mainloop()
