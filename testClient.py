import socket

# python C:\Users\yyyma\PycharmProjects\testMultipleClientsServerWithValidation\testClient.py
MAX_MSG_LENGTH = 1024
SERVER_PORT = 5556
SERVER_IP = "192.168.1.12"

imgcounter = 1
basename = "image%s.png"
end_while = False


def main():
    for i in range(1):
        # Connection part
        client_test_1 = socket.socket()
        client_test_1.connect((SERVER_IP, SERVER_PORT))

        client_test_1.send("  PICTURE j".encode("utf-8"))
        print("massage sent: " + "PICTURE j")
        while True:
            answer1 = client_test_1.recv(4096).decode()
            txt1 = str(answer1)
            print("answer1: " + txt1)

            if txt1.startswith('SIZE'):
                tmp = txt1.split()
                size = int(tmp[1])
                client_test_1.send("GOT SIZE".encode("utf-8"))
                print("massage sent: " + "GOT SIZE")
            elif txt1.startswith('BYE'):
                client_test_1.shutdown()
                print("client_test_1.shutdown()")
                break
            elif answer1:
                myfile = open(basename % imgcounter, 'wb')
                data = client_test_1.recv(40960000).decode()
                print("answer1: " + str(data))
                if not data:
                    myfile.close()
                    break
                myfile.write(data)
                myfile.close()
                client_test_1.send("GOT IMAGE".encode("utf-8"))
                print("massage sent: " + "GOT IMAGE")
                client_test_1.shutdown()
        client_test_1.close()


if __name__ == '__main__':
    main()
