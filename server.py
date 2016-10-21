import socket
from socketinteract import base





s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('localhost', 10000))
s.listen(1)

while True:
    print('waiting for connection')
    connection, client_address = s.accept()


    try:
        print('connection from', client_address)

        toReturn = ''
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print('received ' + str(data))

            if data:
                toReturn += data.decode('ascii')
                connection.sendall(1)
                pass
            else:
                print('no more data from', client_address)
                print(toReturn)
                connection.sendall(str.encode('Response'))
                break

    finally:
        # Clean up the connection
        connection.close()