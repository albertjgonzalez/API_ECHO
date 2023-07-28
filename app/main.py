import tkinter as tk
from tkinter import ttk
from data_handler import Client, load_clients
from gui_components import check_endpoint, on_client_id_selected, submit


def fetch_status(url_entry, isapi_entry, b2b_entry, b2c_entry, muramasa_entry, url_status, isapi_status, b2b_status, b2c_status, muramasa_status):
    url = url_entry.get()
    isapi = isapi_entry.get()
    b2b = b2b_entry.get()
    b2c = b2c_entry.get()
    muramasa = muramasa_entry.get()
    url_status.config(text=str(check_endpoint(url)))
    isapi_status.config(text=str(check_endpoint(isapi)))
    b2b_status.config(text=str(check_endpoint(b2b)))
    b2c_status.config(text=str(check_endpoint(b2c)))
    muramasa_status.config(text=str(check_endpoint(muramasa)))


def save_last_selected_client(client_id):
    with open("last_selected.txt", "w") as file:
        file.write(client_id)


def get_last_selected_client():
    try:
        with open("last_selected.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return None



clients = load_clients()
clients_ids = [client.id for client in clients]

app = tk.Tk()
app.title("API Echo")

frame = ttk.Frame(app, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

client_id_label = ttk.Label(frame, text="Client ID:")
client_id_label.grid(column=0, row=0, sticky=tk.W, pady=5)
client_id = tk.StringVar()
client_id.set(get_last_selected_client() or "SKC")
client_id_dropdown = ttk.Combobox(frame, textvariable=client_id, values=clients_ids)
client_id_dropdown.bind("<<ComboboxSelected>>", lambda event: save_last_selected_client(client_id.get()))
client_id_dropdown.grid(column=1, row=0, pady=5, sticky=tk.W)

environment_label = ttk.Label(frame, text="Environment:")
environment_label.grid(column=0, row=1, sticky=tk.W, pady=5)
environment = tk.StringVar()
environment_dropdown = ttk.Combobox(frame, textvariable=environment, values=["dev", "preprod", "prod"])
environment_dropdown.grid(column=1, row=1, pady=5, sticky=tk.W)

url_label = ttk.Label(frame, text="B2B URL:")
url_label.grid(column=0, row=2, sticky=tk.W, pady=5)
url_entry = ttk.Entry(frame, width=50)
url_entry.grid(column=1, row=2, pady=5, sticky=tk.W)

isapi_label = ttk.Label(frame, text="B2B ISAPI:")
isapi_label.grid(column=0, row=3, sticky=tk.W, pady=5)
isapi_entry = ttk.Entry(frame, width=50)
isapi_entry.grid(column=1, row=3, pady=5, sticky=tk.W)

b2b_label = ttk.Label(frame, text="B2B Status:")
b2b_label.grid(column=0, row=4, sticky=tk.W, pady=5)
b2b_entry = ttk.Entry(frame, width=50)
b2b_entry.grid(column=1, row=4, pady=5, sticky=tk.W)

b2c_label = ttk.Label(frame, text="B2C URL:")
b2c_label.grid(column=0, row=5, sticky=tk.W, pady=5)
b2c_entry = ttk.Entry(frame, width=50)
b2c_entry.grid(column=1, row=5, pady=5, sticky=tk.W)

muramasa_label = ttk.Label(frame, text="Muramasa:")
muramasa_label.grid(column=0, row=6, sticky=tk.W, pady=5)
muramasa_entry = ttk.Entry(frame, width=50)
muramasa_entry.grid(column=1, row=6, pady=5, sticky=tk.W)

submit_button = ttk.Button(frame, text="Check Status", command=lambda: app.after(100, submit, url_entry, isapi_entry, b2b_entry, b2c_entry, muramasa_entry, url_status, isapi_status, b2b_status, b2c_status, muramasa_status))
submit_button.grid(column=1, row=7, pady=10, sticky=tk.W)

url_status = ttk.Label(frame, text="")
url_status.grid(column=2, row=2, sticky=tk.W, pady=5)
isapi_status = ttk.Label(frame, text="")
isapi_status.grid(column=2, row=3, sticky=tk.W, pady=5)
b2b_status = ttk.Label(frame, text="")
b2b_status.grid(column=2, row=4, sticky=tk.W, pady=5)
b2c_status = ttk.Label(frame, text="")
b2c_status.grid(column=2, row=5, sticky=tk.W, pady=5)
muramasa_status = ttk.Label(frame, text="")
muramasa_status.grid(column=2, row=6, sticky=tk.W, pady=5)

client_id_dropdown.bind("<<ComboboxSelected>>", lambda event: on_client_id_selected(client_id, environment, clients, url_entry, isapi_entry, b2b_entry, b2c_entry, muramasa_entry, url_status, isapi_status, b2b_status, b2c_status, muramasa_status))
environment_dropdown.bind("<<ComboboxSelected>>", lambda event: on_client_id_selected(client_id, environment, clients, url_entry, isapi_entry, b2b_entry, b2c_entry, muramasa_entry, url_status, isapi_status, b2b_status, b2c_status, muramasa_status))

app.mainloop()