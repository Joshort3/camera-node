# import base64, requests, sys

# file = sys.argv[1]
# with open(file, "rb") as image_file:
#     # data = base64.b64encode(image_file.read())
#     data = image_file.read()

# url = "http://localhost:8080/"
# headers = {"Content-type": "image/jpeg", "Accept":"text/plain"}

# response = requests.post(url, data=data, headers=headers)

import socket, sys, os

#TCP_IP = '10.0.1.201'
#TCP_PORT = 7777
#BUFFER_SIZE=1024
def server_connect(image):
    TCP_IP = '127.0.0.1'
    TCP_PORT = 6666
    BUFFER_SIZE= 1024

    file = image
    with open(file, "rb") as image_file:
        MESSAGE = image_file.read()

    mlen = os.path.getsize(file)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    print('image size: ' + str(mlen))
    s.send(str(mlen).encode('ascii'))
    a = s.recv(len('SIZE'))
    print(a)
    s.sendall(MESSAGE)
    data = s.recv(BUFFER_SIZE)
    s.close()
    print("Server Connection Finished!")
    print("received data:", data)

server_connect('image.jpg')
