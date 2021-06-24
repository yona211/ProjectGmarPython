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
        # סתם לבדוק 100 התחברויות שונות במקביל ועם
        # בקשות שונות, ולראות איך השרת מגיב והאם הוא קורס.
        if (i % 2) == 0:
            client_test_1.send("  WINNERS jh".encode("utf-8"))
        else:
            client_test_1.send("  PHONE 214181919".encode("utf-8"))
        client_test_1.close()


if __name__ == '__main__':
    main()
