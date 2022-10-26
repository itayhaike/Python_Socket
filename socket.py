import os
import socket
import time

PORT = 4011
socket_master = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def client():
    if choice == "c":
        host = input("Enter Host Name: ")
        # Trying to connect to socket.
        try:
            socket_master.connect((host, PORT))
            print("Connected Successfully")
        except:
            print("Unable to connect")
            exit(0)

        # Send file.
        file_name = socket_master.recv(100).decode()
        file_size = socket_master.recv(100).decode()

        # Opening and reading file.
        with open("C:/Users/itayh/PycharmProjects/pythonProject1/PRO@/file/" + file_name, "wb") as file:
            c = 0
            # Starting the time capture.
            start_time = time.time()

            # Running the loop while file is received. Transfer data by packets
            while c <= int(file_size):
                data = socket_master.recv(1024)
                if not (data):
                    break
                file.write(data)
                c += len(data)

            # Ending the time capture.
            end_time = time.time()

        print("File transfer Complete.Total time: ", end_time - start_time)

        # Closing the socket.
        socket_master.close()
        

def server():
    socket_master.bind((socket.gethostname(), PORT))
    socket_master.listen(5)
    print("Host Name: ", socket_master.getsockname())

    # Accepting the connection.
    try:
        client, addr = socket_master.accept()
        print("Connected Successfully")
    except:
        print("Unable to connect")

    # Getting file details.
    file_name = input("File Name:")
    file_size = os.path.getsize(file_name)

    # Sending file_name and detail.
    client.send(file_name.encode())
    client.send(str(file_size).encode())

    # Opening file and sending data.
    with open(file_name, "rb") as file:
        c = 0
        # Starting the time capture.
        start_time = time.time()

        # Running loop while c != file_size.
        while c <= file_size:
            data = file.read(1024)
            if not (data):
                break
            client.sendall(data)
            c += len(data)

        # Ending the time capture.
        end_time = time.time()

    print("File Transfer Complete.Total time: ", end_time - start_time)
    # Cloasing the socket.
    socket_master.close()


while True:

    menu = ("For Server press -s-\nFor Client press -c-\nExit press -x-\nYour chice is:")
    choice = input(menu)

    if choice == "c":
        client()
    elif choice == "s":
        server()
    elif choice == "x":
        print("Bye Bye Thank You :)")
        break
    else:
        print("Please enter a vaild input!!!!")
