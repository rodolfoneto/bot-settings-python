import time
import requests_bot as RequestBot
import files_bot as FileBot
import ValidationParams as Validation
from datetime import datetime
import login

class Account:
    def __init__(self, account_id, time_to_next_request = 600, listbox_index = 0, listbox = None):
        self.account_id = account_id
        if account_id == '1625103499' :
             self.last_request_time = 0
        else:
            self.last_request_time = time.time()
        self.time_to_next_request = time_to_next_request
        self.last_status_code = 0
        self.last_update = None
        self.exist_in_herobot = False
        self.listbox_index = listbox_index
        self.listbox = listbox
        self.seconds_to_next_request = time_to_next_request

    def execute_request(self):
        current_time = time.time()
        self.seconds_to_next_request = int(self.time_to_next_request - (current_time - self.last_request_time))
        
        # conf = self.listbox.itemcget(self.listbox_index, "bg")
        # self.listbox.delete(self.listbox_index)
        # self.listbox.insert(self.listbox_index, f"{self.account_id} | {self.seconds_to_next_request}")
        # self.listbox.itemconfig(self.listbox_index, conf)

        if self.last_request_time == 0 or current_time - self.last_request_time >= self.time_to_next_request:
            self.time_to_next_request = 30
            response = RequestBot.make_request_to_get_by_id(self.account_id)
            if response.status_code == 200 :
                # print(f"Req: {self.account_id} | 200")
                json_data = response.json()
                Validation.validation(json_data)
                FileBot.save_web_settings(self.account_id, json_data)
                
                # self.listbox.tag_add("green_bg", self.listbox_index)
                self.listbox.itemconfig(self.listbox_index, {'bg': 'green'})

                self.last_update = datetime.now()
                self.exist_in_herobot = True
            elif response.status_code == 404 :
                # print(f"Req: {self.account_id} | 404")
                self.exist_in_herobot = False
                self.listbox.itemconfig(self.listbox_index, {'bg': 'red'})
            elif response.status_code == 429 :
                print('O sistema fez muito request de uma unica vez, fecha esse programa e espera 1 munito ou fala com Rodolfo')
                self.listbox.itemconfig(self.listbox_index, {'bg': 'red'})
            elif response.status_code == 401 :
                print('Erro critico eh necessario logar')
            self.last_status_code = response.status_code
            self.last_request_time = current_time
            print(self.account_id,self.last_status_code,self.exist_in_herobot,self.last_update)
            return True
        else:
            return False
