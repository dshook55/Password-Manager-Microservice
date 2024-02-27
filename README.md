# Password-Manager-Microservice
Client sends an integer(n), generates a password of length n, and then encrypts it.

Communication Contract:

A) Requesting Services From the Server:

In order to request data from the server, the client will have to develop a secure connection. In the current example, I am using sockets. The server is listening on port 12345. When the server is running, all you would have to do is run the client side program and the connection should be made. Once the socket connection is made, the server will be listening for an integer from the client. This integer tells the server that it must generate and send a password of that length. Once it generates the password, it encrypts it, and it will send it(and the decryption key) to the client.


B) Receiving Services As a Client:

To connect to the server as a client, you have to connect to socket 12345. Once you send an integer to the server, it responds first with the encryption key and then the encrypted password. As a client, you will have to assign the variables in that order because that is how they will be sent. Once the client receives the key and encrypted password, they can decide if they want to decrypt it or keep it encrypted and store the key/password seperately. In its current configuration, it decrypts it automatically.

C) UML Diagram:


![Screenshot 2024-02-26 170140](https://github.com/dshook55/Password-Manager-Microservice/assets/133323327/83ed8458-d56c-4645-8578-ed61196e68f8)





