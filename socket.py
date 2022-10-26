import os
import socket
import time

PORT = 4011
menu = ("For Host press -h-\nFor Client press -c-\nExit press -x-\nYour chice is:")
choice = input(menu)
while True:

  def sock():
      if choice == "c":
          host = input("Enter Host Name: ")
          sock_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      
          # Trying to connect to socket.
          try:
              sock_client.connect((host, PORT))
              print("Connected Successfully")
          except:
              print("Unable to connect")
              exit(0)
      
          # Send file.
          file_name = sock_client.recv(100).decode()
          file_size = sock_client.recv(100).decode()
      
          # Opening and reading file.
          with open("C:/Users/itayh/PycharmProjects/python/SOCKET_TFTP/file/" + file_name, "wb") as file:
              c = 0
              # Starting the time capture.
              start_time = time.time()
      
              # Running the loop while file is recieved.
              while c <= int(file_size):
                  data = sock_client.recv(1024)
                  if not (data):
                      break
                  file.write(data)
                  c += len(data)
      
              # Ending the time capture.
              end_time = time.time()
      
          print("File transfer Complete.Total time: ", end_time - start_time)
      
          # Closing the socket.
          sock_client.close()
          return
      elif choice == "h":
          sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          sock_server.bind((socket.gethostname(), PORT))
          sock_server.listen(5)
          print("Host Name: ", sock_server.getsockname())
      
          # Accepting the connection.
          try:
              client, addr = sock_server.accept()
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
          sock_server.close()
          return
      else:
          print("Please enter a vaild input!!!!")
  if choice == "x":
    print("Bye Bye Thank You :)")
    break
  sock()