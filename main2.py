
import bot_data as BotData
import requests_bot as RequestBot
import account as Account
import time
import random
import detail_account

import tkinter as tk
from tkinter import ttk


my_array = BotData.get_accounts_directory()
# print(my_array)
# step_size = 10
accounts = []
for item in my_array:
    random_number = random.randint(10, 60)
    acc = Account.Account(item, random_number)
    accounts.append(acc)

def refresh_window():
    for item in accounts:
        item.execute_request()
    window.after(1000, refresh_window)
    # flag = True
    # count = 0
    # while flag:
    #     accounts[count].execute_request()
    #     count = count + 1

    #     if count >= len(accounts):
    #         count = 0
    #         time.sleep(1)

window = tk.Tk()
window.title("Hero Bot")
window.geometry("800x600")

def double_click(event):
    # selected_item = listbox.get(listbox.curselection())
    account = accounts[listbox.curselection()[0]]
    da = detail_account.DetailAccount(window, account)
    da.open_window()

label = tk.Label(window, text="Contas")
label.pack()

listbox = tk.Listbox(window)
listbox.pack(fill=tk.BOTH, expand=True)
listbox.bind("<Double-Button-1>", double_click)

scrollbar = ttk.Scrollbar(listbox, orient=tk.VERTICAL, command=listbox.yview)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

for index, account in enumerate(accounts):
    listbox.insert(tk.END, account.account_id)
    account.listbox_index = index
    account.listbox = listbox

window.after(1000, refresh_window)

window.mainloop()