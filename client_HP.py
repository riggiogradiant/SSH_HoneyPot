# import os

# def run_ssh_command():
#     # Solicitar al usuario el nombre de usuario
#     username = input("Enter username: ")

#     # Construir el comando SSH
#     command = f"ssh -p 2222 {username}@localhost"

#     # Ejecutar el comando SSH
#     os.system(command)

# # Main
# if __name__ == "__main__":
#     run_ssh_command()

#=============================================================================================================================
# import paramiko

# def ssh_connect(ip, port, user, passwd):
#     client = paramiko.SSHClient()
#     client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     client.connect(ip, port=port, username=user, password=passwd)
#     print('Connected to the SSH server.')

#     # Abrir un canal SSH
#     channel = client.get_transport().open_session()

#     # Solicitar un shell interactivo
#     channel.get_pty()
#     channel.invoke_shell()

#     # Interactuar directamente con el shell del servidor
#     # channel.send('\n')
#     # channel.send('\n')
#     output = channel.recv(1024).decode()
#     print('--- Output ---')
#     print(output)

#     while True:
#         # Leer la entrada del usuario
#         command = input('Enter command or <CR> to exit: ')

#         if command == '':
#             break

#         # Enviar el comando al canal SSH
#         channel.send(command + '\n')

#         # Recibir la salida del comando
#         output = channel.recv(1024).decode()
#         print('--- Output ---')
#         print(output)

#     # Cerrar el canal y la conexión
#     channel.close()
#     client.close()

# # main
# if __name__ == '__main__':
#     import getpass
#     user = input('Username: ')

#     # getpass: para no ver la contraseña cuando se escribe
#     password = getpass.getpass()

#     # Puerto e IP en el que está configurado el server.py de Cowrie
#     ip = 'localhost'
#     port = 2222
#     ssh_connect(ip, port, user, password)
import paramiko
import time

def ssh_connect(ip, port, user, passwd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=user, password=passwd)
    print('Connected to the SSH server.')

    # Abrir un canal SSH interactivo
    channel = client.invoke_shell()
    output = channel.recv(1024).decode()
    print(output)


    while True:
        # Leer la entrada del usuario
        command = input('Enter command or <CR> to exit: ')

        if command == '':
            break

        # Enviar el comando al canal SSH
        channel.send(command + '\n')

        time.sleep(0.2)

        # Recibir la salida del comando
        output = channel.recv(1024).decode()
        print('--- Output ---')
        print(output)

    # Cerrar el canal y la conexión
    channel.close()
    client.close()

# main
if __name__ == '__main__':
    import getpass
    user = input('Username: ')

    # getpass: para no ver la contraseña cuando se escribe
    password = getpass.getpass()

    # Puerto e IP en el que está configurado el server.py de Cowrie
    ip = 'localhost'
    port = 2222
    ssh_connect(ip, port, user, password)
