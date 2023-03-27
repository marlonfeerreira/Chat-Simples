import socket
import threading

HOST = 'localhost'
PORT = 5000

def handle_client(conn, addr):
    print(f'Novo cliente conectado: {addr}')

    while True:
        data = conn.recv(1024)
        if not data:
            break
        message = data.decode()
        print(f'Mensagem recebida de {addr}: {message}')
        if message == 'bye':
            break
        conn.sendall(data)

    print(f'Cliente desconectado: {addr}')
    conn.close()

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()

        print(f'Servidor iniciado em {HOST}:{PORT}')

        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()

start_server()