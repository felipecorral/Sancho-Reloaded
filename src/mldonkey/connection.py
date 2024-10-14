import socket

class MLDonkeyConnection:
    def __init__(self, ip, port, username=None, password=None):
        self.ip = ip
        self.port = int(port)
        self.username = username
        self.password = password

    def authenticate(self, s):
            if self.username and self.password:
                auth_command = f"auth {self.username} {self.password}\n"
                s.sendall(auth_command.encode('utf-8'))
                response = s.recv(4096).decode('utf-8')

                if "Authentication successful" in response:
                    print("Authentication successful.")
                    return True
                else:
                    print("Authentication Error.")
                    return False
            return True  # continue if not user and password

    def send_command(self, command):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.ip, self.port))
                print(f"Connected to server {self.ip}:{self.port}")

                # Auth if necesary
                if not self.authenticate(s):
                    return "Error: Authentication unsuccessful."

                # Send command
                s.sendall((command + '\n').encode('utf-8'))

                # Read response
                response = ""
                while True:
                    part = s.recv(4096).decode('utf-8')
                    if not part:
                        break
                    response += part

                return response
        except Exception as e:
            return f"Error: {str(e)}"
