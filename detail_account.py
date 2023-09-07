import tkinter as tk
import simplejson

class DetailAccount:

    def __init__(self, window, account):
        self.account = account
        self.window = window

    def open_window(self):
        # Crie uma nova janela para exibir os detalhes do item
        self.detail_window = tk.Toplevel(self.window)
        self.detail_window.geometry("800x600")
        self.detail_window.title("Detalhes do Item")
        
        # Exiba os detalhes do item na nova janela
        self.igg_account = tk.Label(self.detail_window, text=f"Detalhes do Item: {self.account.account_id}")
        self.igg_account.pack()

        self.seconds_next_request = tk.Label(self.detail_window)
        self.seconds_next_request.pack()

        self.status_last_request = tk.Label(self.detail_window, text=f"Status Ultimo Request: NULL")
        self.status_last_request.pack()

        # Crie um widget Text
        self.last_request = tk.Text(self.detail_window, wrap=tk.WORD) 
        self.last_request.pack(fill=tk.BOTH, expand=True)

        self.draw_window()

        self.detail_window.after(1000, self.draw_window)

    def draw_window(self):
        self.seconds_next_request.config(text=f"Prox Request: {self.account.seconds_to_next_request}s")
        if self.account.changed :
            if(self.account.last_response_response != None):
                self.status_last_request.config(text=f"Status Ultimo Request: {self.account.last_response_response.status_code}")
                asd = simplejson.loads(self.account.last_response_response.text)
                # print(asd)
                self.last_request.delete("1.0", tk.END)
                self.last_request.insert(tk.END, simplejson.dumps(asd, sort_keys=True, indent=4 * ' '))
            self.account.changed = False
        self.detail_window.after(1000, self.draw_window)
        
