import tkinter as tk
# import bot_data
import login
import requests_bot
import files_bot
import datetime
import global_settings as gs

def load_accounts_name():
    items = files_bot.get_accounts_directory()
    listbox.delete(0,tk.END)
    for item in items:
        try:
            response = requests_bot.make_request(item)
            if response.status_code == 200:
                json_data = response.json()
                files_bot.save_web_settings(item, json_data[item])
            elif response.status_code == 401:
                login.main()
            else:
                listbox.insert(tk.END, item + ' - ' + response.status_code + ' - '+ now.strftime("%Y-%m-%d %H:%M:%S"))
            now = datetime.datetime.now()
            listbox.insert(tk.END, item + ' - Updated ' + now.strftime("%Y-%m-%d %H:%M:%S"))
        except Exception:
            listbox.insert(tk.END, "OFF LINE -" + item)

def center_window(window):
    window_width = window.winfo_reqwidth()
    window_height = window.winfo_reqheight()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width / 2) - (window_width / 2) - 300)
    y = int((screen_height / 2) - (window_height / 2) - 300)
    window.geometry(f'+{x}+{y}')

def create_window():
    global listbox
    global countdown

    window = tk.Tk()
    window.title("Lords Mobile Bot")
    window.geometry("800x600")
    center_window(window)

    label = tk.Label(window, text="Contas")
    label.pack()

    listbox = tk.Listbox(window)
    listbox.pack(fill=tk.BOTH, expand=True)

    button = tk.Button(window, text="Start Process", command=load_accounts_name)
    button.pack()

    countdown_label = tk.Label(window, text="Countdown: --")
    countdown_label.pack(side=tk.BOTTOM)

    def update_countdown():
        global countdown
        countdown -= 1
        countdown_label.config(text="Refresh: " + str(countdown))
        window.after(1000, update_countdown)
        if countdown == 0:
            countdown = gs.get('time_to_request')
            load_accounts_name()

    countdown = gs.get('time_to_request')
    window.after(1000, update_countdown)

    window.mainloop()

if __name__ == "__main__":
    create_window()