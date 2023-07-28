import tkinter as tk
from tkinter import ttk
import urllib.request


def check_endpoint(url):
    try:
        response = urllib.request.urlopen(url, timeout=5)
        return True
    except:
        return False


def on_client_id_selected(selected_client_id, selected_environment, clients, url_entry, isapi_entry, b2b_entry,
                          b2c_entry, muramasa_entry, url_status, isapi_status, b2b_status, b2c_status, muramasa_status):
    # After selecting a client, set the environment to 'dev' if not already selected
    if not selected_environment.get():
        selected_environment.set('dev')

    # Populate the input fields, but don't set the status yet.
    selected_id = selected_client_id.get()
    selected_client = next(client for client in clients if client.id == selected_id)
    env_data = selected_client.__dict__[selected_environment.get()]

    url_entry.delete(0, tk.END)
    isapi_entry.delete(0, tk.END)
    b2b_entry.delete(0, tk.END)
    b2c_entry.delete(0, tk.END)
    muramasa_entry.delete(0, tk.END)

    url_entry.insert(0, env_data.get("b2b_url", ""))
    isapi_entry.insert(0, env_data.get("b2b_isapi", ""))
    b2b_entry.insert(0, env_data.get("b2b_url", ""))
    b2c_entry.insert(0, env_data.get("b2c_url", ""))
    muramasa_entry.insert(0, env_data.get("muramasa", ""))


def submit(url_entry, isapi_entry, b2b_entry, b2c_entry, muramasa_entry, url_status, isapi_status, b2b_status,
           b2c_status, muramasa_status):
    url = url_entry.get()
    isapi = isapi_entry.get()
    b2b = b2b_entry.get()
    b2c = b2c_entry.get()
    muramasa = muramasa_entry.get()

    # Set status to "Loading..." while checking endpoints
    url_status.config(text="Loading...")
    isapi_status.config(text="Loading...")
    b2b_status.config(text="Loading...")
    b2c_status.config(text="Loading...")
    muramasa_status.config(text="Loading...")

    # Use after method to delay the submit function call and simulate loading
    url_entry.after(100, lambda: check_and_update_endpoint(url, url_status))
    isapi_entry.after(100, lambda: check_and_update_endpoint(isapi, isapi_status))
    b2b_entry.after(100, lambda: check_and_update_endpoint(b2b, b2b_status))
    b2c_entry.after(100, lambda: check_and_update_endpoint(b2c, b2c_status))
    muramasa_entry.after(100, lambda: check_and_update_endpoint(muramasa, muramasa_status))


def check_and_update_endpoint(url, status_label):
    status_label.config(text="Online" if check_endpoint(url) else "Offline")
