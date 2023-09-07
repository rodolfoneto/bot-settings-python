
import bot_data as BotData
import account as Account
import random
import detail_account
import global_settings as gs

import tkinter as tk
from tkinter import ttk

my_array = BotData.get_accounts_directory()

accounts = []
for item in my_array:
    random_number = random.randint(gs.get('min_time_to_request'), gs.get('max_time_to_request'))
    acc = Account.Account(item, random_number)
    accounts.append(acc)

def refresh_window():
    for item in accounts:
        item.execute_request()
    window.after(1000, refresh_window)

window = tk.Tk()
window.title("Hero Bot")
window.geometry("800x600")

def double_click(event):
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