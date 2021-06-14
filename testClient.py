import socket

# python C:\Users\yyyma\PycharmProjects\testMultipleClientsServerWithValidation\testClient.py
MAX_MSG_LENGTH = 1024
SERVER_PORT = 5556
SERVER_IP = "192.168.1.12"


def main():
    for i in range(100):
        # Connection part
        client_test_1 = socket.socket()
        client_test_1.connect((SERVER_IP, SERVER_PORT))
        # Send massage part
        client_test_1.send("  FIND 214181919".encode())
        # Receive data part and display
        data = client_test_1.recv(MAX_MSG_LENGTH).decode()
        print(data)
        # Close connection with the server
        client_test_1.close()



if __name__ == '__main__':
    main()
