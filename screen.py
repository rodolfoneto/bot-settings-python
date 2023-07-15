import tkinter as tk
from pathlib import Path
import json
import requests

def open_file():
    account = "1625103499"
    file_path = load_global_settings_json()['bot_path'] + "/config__/"+account+"/settings.json"
    if Path(file_path).exists() == False or Path(file_path).is_file() == False:
        raise Exception("Arquivo da conta "+account+" nao encontrado")
    with open(file_path, 'r') as file:
        setting_obj = json.load(file)
    return setting_obj


def main():
    global text
    window = tk.Tk()
    window.title("Teste Tela")
    window.geometry("800x600")

    button = tk.Button(window, text="Btn 01")
    button.pack()

    text = tk.Text(window)
    text.pack()

    window.mainloop()




if __name__ == "__main__":
    main()