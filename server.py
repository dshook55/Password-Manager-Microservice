import socket
from cryptography.fernet import Fernet
import random

def encrypt_password(password):
    key = Fernet.generate_key()
    cipher = Fernet(key)
    
    encrypted_password = cipher.encrypt(password.encode())
    #print("Encrypted Password:",encrypted_password)
    return key, encrypted_password

def generatePassword(length):
    asciiArray =[]
    for i in range(length):
        random_ascii_value = random.randint(33, 126)
        asciiArray.append(random_ascii_value)
    asciiString = ''.join(chr(value) for value in asciiArray)
    return asciiString

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)

    print("Server listening on port 12345...")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connection from {addr}")

        passwordLength = conn.recv(1024)
        passwordLength = int(passwordLength.decode())
        newPassword = generatePassword(passwordLength)


        key, encrypted_password = encrypt_password(newPassword)
        conn.send(key)
        conn.send(encrypted_password)

        conn.close()

if __name__ == "__main__":
    main()