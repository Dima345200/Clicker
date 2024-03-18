import time
import random
import os
import requests
from tkinter import ttk
import tkinter as tk
from threading import Thread
import sqlite3

sql = sqlite3.connect('savebase')
cur = sql.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS datasave (
money BIGINT,
level BIGINT,
exp BIGINT
)''')

money = 0
root = tk.Tk()
root.geometry('300x300+10+10')
root.title('Clicker')
root.resizable(False, False)
root.config(bg='#949494')

def leave():
    global level
    global money
    global exp
    cur.execute("SELECT money FROM datasave")
    if cur.fetchone() is None:
        cur.execute(f"INSERT INTO datasave VALUES ({money}, {level}, {exp})")
    else:
        cur.execute(f"UPDATE datasave SET money = {money}")
        cur.execute(f"UPDATE datasave SET level = {level}")
        cur.execute(f"UPDATE datasave SET exp = {exp}")
    sql.commit()
    exit()
def deleting():
    cur.execute("DELETE FROM datasave")
    sql.commit()
    exit()
def shop():
    game()
def game():
    global cash
    global work
    global money
    global level
    global expm
    global exp
    global shopb
    global levell
    global cash
    global save_exit
    global deleting_save
    global expl
    cash = ttk.Label(root, text=f'{money} ₽', font=('Arial', '25', 'bold'), background='#949494')
    cash.place(relx=0.25, rely=0.1, anchor=tk.CENTER)
    levell = ttk.Label(root, text=f'Ур. {level}', font=('Arial', '25', 'bold'), background='#949494')
    levell.place(relx=0.75, rely=0.1, anchor=tk.CENTER)
    expl = ttk.Label(root, text=f'{exp}/{expm}', font=('Arial', '10', 'bold'), background='#949494')
    expl.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    def click():
        global work
        global money
        global expm
        global level
        global work
        global shopb
        global levell
        global expl
        global exp
        work.destroy()
        shopb.destroy()
        money += 1
        exp += 1
        if exp == expm:
            level += 1
            exp = 0
        expm = (level + 1) * 5
        cooldown = ttk.Label(root, text='Подождите...', font=('Arial', '17', 'bold'), background='#949494')
        cooldown.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        if level == 0:
            time.sleep(3)
        elif level == 1 and level == 2:
            time.sleep(2.5)
        elif level >= 3 and level < 6:
            time.sleep(2)
        elif level >= 6 and level < 10:
            time.sleep(1.5)
        elif level >= 10 and level < 15:
            time.sleep(1)
        elif level >= 15 and level <= 20:
            time.sleep(0.5)
        else:
            time.sleep(0.25)
        cooldown.destroy()
        shopb = ttk.Button(root, text='Магазин', padding=3, command=shop)
        shopb.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
        work = ttk.Button(root, text='Нажми', padding=3, command=new_thread_click)
        work.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        game()
    def new_thread_click():
        t1 = Thread(target=click)
        t1.start()
    work = ttk.Button(root, text='Нажми', padding=3, command=new_thread_click)
    work.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
def start():
    global work
    global money
    global expm
    global level
    global work
    global shopb
    global save_exit
    global deleting_save
    global exp
    save_exit = ttk.Button(root, text='Сохранить и выйти', padding=2, command=leave)
    save_exit.place(relx=0.75, rely=0.9, anchor=tk.CENTER)
    deleting_save = ttk.Button(root, text='Удалить сохранения', padding=2, command=deleting)
    deleting_save.place(relx=0.25, rely=0.9, anchor=tk.CENTER)
    shopb = ttk.Button(root, text='Магазин', padding=3, command=shop)
    shopb.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
    cur.execute("SELECT money FROM datasave")
    if cur.fetchone() is None:
        money = 0
        level = 0
        exp = 0
        expm = 5
    else:
        cur.execute("SELECT money FROM datasave")
        money = cur.fetchone()[0]
        cur.execute("SELECT level FROM datasave")
        level = cur.fetchone()[0]
        cur.execute("SELECT exp FROM datasave")
        exp = cur.fetchone()[0]
        expm = (level + 1) * 5
    gamel.destroy()
    game()
def about():
    def back_menu():
        global gamel
        global work
        global aboutb
        global back_menub
        global textl
        textl.destroy()
        back_menub.destroy()
        work = ttk.Button(root, text='Старт', padding=3, command=start)
        work.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        aboutb = ttk.Button(root, text='Создатель', padding=3, command=about)
        aboutb.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
    global work
    global aboutb
    global back_menub
    global textl
    work.destroy()
    aboutb.destroy()
    back_menub = ttk.Button(root, text='Назад', padding=3, command=back_menu)
    back_menub.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
    textl = ttk.Label(root, text='Discord - dima3452\n\nGitHub - Dima345200', font=('Arial', '12', 'bold'), background='#949494')
    textl.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
gamel = ttk.Label(root, text='Clicker', font=('Arial', '25', 'bold'), background='#949494')
gamel.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
work = ttk.Button(root, text='Старт', padding=3, command=start)
work.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
aboutb = ttk.Button(root, text='Создатель', padding=3, command=about)
aboutb.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

root.mainloop()