import tkinter as tk
import requests
import json
import global_settings as gs

def center_window(window):
    window_width = window.winfo_reqwidth()
    window_height = window.winfo_reqheight()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))
    window.geometry(f'+{x}+{y}')

def login():
    username = username_entry.get()
    password = password_entry.get()
    
    payload = {
        'email': username,
        'password': password,
        'device_name': gs.get('device_name'),
    }
    try:
        url_login = gs.get('url_base') + gs.get('url_login')
        response = requests.post(url_login, json=payload, headers={"Accept": "application/json","Content-Type": "application/json"})
        if response.status_code == 200:
            token = response.text
            global_settings = gs.load()
            global_settings['login_token'] = token
            print(global_settings)
            gs.save(global_settings)
            print('Login successful. Token saved.')
            window.destroy()
        else:
            print('Login failed.')
    
    except requests.exceptions.RequestException as e:
        print('An error occurred during the login request:', e)

def main():
    global username_entry
    global password_entry
    global window
    # Create the main window
    window = tk.Tk()
    window.title('Login')
    window.geometry('300x150')
    center_window(window)

    # Create the login label and entry
    username_label = tk.Label(window, text='Username:')
    username_label.pack()
    username_entry = tk.Entry(window)
    username_entry.insert(tk.END, 'api@api.com')
    username_entry.pack()

    # Create the password label and entry
    password_label = tk.Label(window, text='Password:')
    password_label.pack()
    password_entry = tk.Entry(window, show='*')
    password_entry.insert(tk.END, '123')
    password_entry.pack()

    # Create the login button
    login_button = tk.Button(window, text='Login', command=login)
    login_button.pack()

    # Run the application
    window.mainloop()

if __name__ == "__main__":
    main()