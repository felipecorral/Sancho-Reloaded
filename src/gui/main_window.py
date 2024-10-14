import tkinter as tk
from mldonkey.connection import MLDonkeyConnection

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sancho Reloaded - Client")
        self.create_widgets()
    
    def create_widgets(self):

        tk.Label(self.root, text="Server IP:").grid(row=0, column=0, padx=10, pady=5)
        self.ip_entry = tk.Entry(self.root)
        self.ip_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Port:").grid(row=1, column=0, padx=10, pady=5)
        self.port_entry = tk.Entry(self.root)
        self.port_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="User:").grid(row=2, column=0, padx=10, pady=5)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Password:").grid(row=3, column=0, padx=10, pady=5)
        self.password_entry = tk.Entry(self.root, show='*')
        self.password_entry.grid(row=3, column=1, padx=10, pady=5)

        # Command
        tk.Label(self.root, text="Command:").grid(row=4, column=0, padx=10, pady=5)
        self.command_entry = tk.Entry(self.root, width=50)
        self.command_entry.grid(row=4, column=1, padx=10, pady=5)

        #Connect button
        connect_button = tk.Button(self.root, text="Connect", command=self.on_connect)
        connect_button.grid(row=5, column=0, columnspan=2, pady=10)

        #Results textBox
        self.result_text = tk.Text(self.root, height=15, width=50)
        self.result_text.grid(row=6, column=0, columnspan=2, padx=10, pady=10)



    def on_connect(self):
        ip = self.ip_entry.get()
        port = self.port_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        command = self.command_entry.get()

        if not ip or not port:
            tk.messagebox.showerror("Error", "You should give a valid server IP and port")
            return

        connection = MLDonkeyConnection(ip, port, username, password)
        response = connection.send_command(command)

        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, response)

    def run(self):
        self.root.mainloop()
