import os
import tkinter as tk
import nmap
import json


def show_entry_fields():
    print("=================================================================================")
    json_res = nmScan.scan(e1.get(), e2.get()) 
    print(json.dumps((json_res), indent=4))
    
def show_all_ports():
    print("=================================================================================")
    json_res = nmScan.scan(e1.get(), '20-30')
    print(json.dumps((json_res), indent=4))

nmScan = nmap.PortScanner()

master = tk.Tk()
master.geometry('300x150')

tk.Label(master, text="host: ").grid(row=0)
tk.Label(master, text="ports interval: ").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

tk.Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=tk.W, pady=4)
tk.Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=tk.W, pady=4)
tk.Button(master, text='auto', command=show_all_ports).grid(row=3, column=2, sticky=tk.W, pady=4)

tk.mainloop()