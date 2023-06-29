import os
import paramiko
import socket
import sys
import threading

CWD = os.path.dirname(os.path.realpath(__file__))
HOSTKEY = paramiko.RSAKey(filename=os.path.join(CWD, 'id_rsa'))

#clase servidor con funciones de checkear el canal y el usuario y contraseña
class Server(paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()

    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_auth_password(self, username, password):
        if (username == 'user') and (password == 'pass'):
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED

if __name__ == '__main__':

    #ip y puerto donde se va a ejecutar el servidor
    server = '127.0.0.1'
    ssh_port = 22222
    try:
        #creamos socket tcp
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((server, ssh_port))
        sock.listen(100)
        print('[+] Listening for connection...')
        client, addr = sock.accept()
    except Exception as e:
        print('[-] Listen failed' + str(e))
        sys.exit(1)

    else:
        print(f'[+] Got a connection from ', addr)

    bhSession = paramiko.Transport(client)
    bhSession.add_server_key(HOSTKEY)
    server = Server()
    bhSession.start_server(server=server)

    #Espera a que el cliente abra un canal ssh
    chan = bhSession.accept(20)

    if chan is None:
        print('*** No Channel.')
        sys.exit(1)

    print('[+] Authenticated!')
    print(chan.recv(1024).decode())

    print('============================================')

    try:
        while True:
            print('Waiting for msg from Client ...')
            msg_from_client = chan.recv(1024).decode()
            print('Mensaje recibido:', msg_from_client, '\n')
            if msg_from_client != '':
                msg_send = '[FROM SERVER]: ' + msg_from_client
                msg_send = msg_send.encode()
                chan.send(msg_send)
            else:
                print('Cerrando el servidor')
                bhSession.close()
                break

            
    except KeyboardInterrupt:
        bhSession.close()
