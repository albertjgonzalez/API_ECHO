import tkinter as tk
from tkinter import messagebox
from app.api_checker import check_endpoint as check_endpoint_func


def submit():
    client_url_value = url.get()
    isapi_value = isapi.get()
    client_id_value = clientID.get()

    result = check_endpoint_func(client_url_value)
    isapi_result = check_endpoint_func(isapi_value)

    url_status_label.config(text="URL Status: " + str(result))
    isapi_status_label.config(text="ISAPI Status: " + str(isapi_result))

    print(result)
    print(isapi_result)


root = tk.Tk()
root.geometry("400x400")
root.title("API Checker")

title = tk.Label(root, text="API Checker")
title.pack()

client_label = tk.Label(root, text="CLIENT ID")
client_label.pack()

clientID = tk.Entry(root, width=30)
clientID.pack()

url_label = tk.Label(root, text="URL")
url_label.pack()

url = tk.Entry(root, width=30)
url.pack()

isapi_label = tk.Label(root, text="ISAPI")
isapi_label.pack()

isapi = tk.Entry(root, width=30)
isapi.pack()

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

url_status_label = tk.Label(root, text="URL Status")
url_status_label.pack(pady=5)

isapi_status_label = tk.Label(root, text="ISAPI Status")
isapi_status_label.pack(pady=5)

if __name__ == "__main__":
    root.mainloop()
