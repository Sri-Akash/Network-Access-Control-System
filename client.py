import tkinter as tk
from tkinter import messagebox
import requests
import time
import ctypes

SERVER_URL = 'http://localhost:5000'

def get_screen_resolution():
    user32 = ctypes.windll.user32
    return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

def check_access():
    client_ip = '192.168.1.35' 
    response = requests.get(f'{SERVER_URL}/get_client_state?client_ip={client_ip}')
    return response.json()['enabled']

def show_popup(message):
    root = tk.Tk()
    root.withdraw()

    screen_width, screen_height = get_screen_resolution()

    popup = tk.Toplevel(root)
    popup.title("Access Denied")
    popup.geometry(f"{screen_width}x{screen_height}+0+0")

    font_style = ("Arial", 30, "bold")
    label = tk.Label(popup, text=message, font=font_style, padx=10, pady=10, fg="red")
    label.pack()

    popup.overrideredirect(1)
    popup.attributes('-topmost', 1)

    root.mainloop()

def main():
    while True:
        access_enabled = check_access()
        if not access_enabled:
            show_popup('You have been no longer allowed to use this system')
            break
        time.sleep(5)  

if __name__ == '__main__':
    main()
