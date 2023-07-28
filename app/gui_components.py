import tkinter as tk
import urllib.request


def check_endpoint(url):
    try:
        response = urllib.request.urlopen(url, timeout=5)
        return True
    except:
        return False


def get_status_label_text(is_online):
    return "Online" if is_online else "Offline"


def on_client_id_selected(selected_client_id, selected_environment, clients, url_entry, isapi_entry, b2b_entry,
                          b2c_entry, muramasa_entry, url_status, isapi_status, b2b_status, b2c_status, muramasa_status):
    # Clear the status labels
    url_status.config(text="")
    isapi_status.config(text="")
    b2b_status.config(text="")
    b2c_status.config(text="")
    muramasa_status.config(text="")

    if not selected_environment.get():
        selected_environment.set('dev')

    # Rest of the function remains unchanged
    selected_id = selected_client_id.get()
    selected_client = next(client for client in clients if client.id == selected_id)
    env_data = selected_client.__dict__[selected_environment.get()]

    url_entry.delete(0, tk.END)
    isapi_entry.delete(0, tk.END)
    b2b_entry.delete(0, tk.END)
    b2c_entry.delete(0, tk.END)
    muramasa_entry.delete(0, tk.END)

    url_entry.insert(0, env_data.get("b2c_url", ""))
    isapi_entry.insert(0, env_data.get("b2c_isapi", ""))
    b2b_entry.insert(0, env_data.get("b2b_url", ""))
    b2c_entry.insert(0, env_data.get("b2b_isapi", ""))
    muramasa_entry.insert(0, env_data.get("muramasa", ""))


def submit(url_entry, isapi_entry, b2b_entry, b2c_entry, muramasa_entry, url_status, isapi_status, b2b_status, b2c_status, muramasa_status):
    url = url_entry.get()
    isapi = isapi_entry.get()
    b2b = b2b_entry.get()
    b2c = b2c_entry.get()
    muramasa = muramasa_entry.get()
    url_status.config(text=get_status_label_text(check_endpoint(url)))
    isapi_status.config(text=get_status_label_text(check_endpoint(isapi)))
    b2b_status.config(text=get_status_label_text(check_endpoint(b2b)))
    b2c_status.config(text=get_status_label_text(check_endpoint(b2c)))
    muramasa_status.config(text=get_status_label_text(check_endpoint(muramasa)))


def on_environment_selected(selected_client_id, selected_environment, clients, url_entry, isapi_entry, b2b_entry,
                            b2c_entry, muramasa_entry, url_status, isapi_status, b2b_status, b2c_status, muramasa_status):
    # Clear the status labels
    url_status.config(text="")
    isapi_status.config(text="")
    b2b_status.config(text="")
    b2c_status.config(text="")
    muramasa_status.config(text="")

    if not selected_environment.get():
        selected_environment.set('dev')

    # Rest of the function remains unchanged
    selected_id = selected_client_id.get()
    selected_client = next(client for client in clients if client.id == selected_id)
    env_data = selected_client.__dict__[selected_environment.get()]

    url_entry.delete(0, tk.END)
    isapi_entry.delete(0, tk.END)
    b2b_entry.delete(0, tk.END)
    b2c_entry.delete(0, tk.END)
    muramasa_entry.delete(0, tk.END)

    url_entry.insert(0, env_data.get("b2c_url", ""))
    isapi_entry.insert(0, env_data.get("b2c_isapi", ""))
    b2b_entry.insert(0, env_data.get("b2b_url", ""))
    b2c_entry.insert(0, env_data.get("b2b_isapi", ""))
    muramasa_entry.insert(0, env_data.get("muramasa", ""))
