import socket
from cryptography.fernet import Fernet

def decrypt_password(key, encrypted_password):
    cipher = Fernet(key)
    decrypted_password = cipher.decrypt(encrypted_password).decode()
    return decrypted_password

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    size = input("Enter Password Size: ")
    client_socket.send(size.encode())

    key = client_socket.recv(1024)
    encrypted_password = client_socket.recv(1024)

    print(f"It's working")  

    decrypted_password = decrypt_password(key, encrypted_password)
    print(f"Decrypted Password: {decrypted_password}")

    client_socket.close()

if __name__ == "__main__":
    main()