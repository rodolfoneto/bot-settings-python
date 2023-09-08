import tkinter as tk
from tkinter import ttk
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

        # Label para quanto tempo para o proximo request
        self.seconds_next_request = tk.Label(self.detail_window)
        self.seconds_next_request.pack()

        # Crie um Label para o Status do ultimo Request
        self.status_last_request = tk.Label(self.detail_window, text=f"Status Ultimo Request: NULL")
        self.status_last_request.pack()

        # Crie um botao para fazer um Request avulso
        self.request_button = tk.Button(self.detail_window, text="Fazer Request", command=self.make_request)
        self.request_button.pack()

        # Crie um widget Text
        self.last_request = tk.Text(self.detail_window, wrap=tk.WORD) 
        self.last_request.pack(fill=tk.BOTH, expand=True)
        scrollbar = ttk.Scrollbar(self.last_request, orient=tk.VERTICAL, command=self.last_request.yview)
        self.last_request.config(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.draw_window()
        self.set_infos()
        
        self.detail_window.after(1000, self.draw_window)
    
    def make_request(self):
        self.account.make_request()

    def draw_window(self):
        self.seconds_next_request.config(text=f"Prox Request: {self.account.seconds_to_next_request}s")
        if self.account.changed :
            if self.account.last_response_response != None:
                self.set_infos()
            self.account.changed = False
        self.detail_window.after(1000, self.draw_window)
    
    def set_infos(self):
        self.status_last_request.config(text=f"Status Ultimo Request: {self.account.last_response_response.status_code}")
        self.last_request.delete("1.0", tk.END)
        if self.account.last_response_response != None:
            try:
                response_json = simplejson.loads(self.account.last_response_response.text)
                self.last_request.insert(tk.END, simplejson.dumps(response_json, sort_keys=True, indent=4 * ' '))
            except Exception:
                self.last_request.insert(tk.END, 'ENTRAR EM CONTATO COM O DESENVOLVEDOR')
