import socket




def server():
    #Создаем историю сообщений
    message_history = []

    #Создаем TCP-сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Привязываем его к адресу и порту
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    #Начинаем слушать входящие подключения(максимум 10 в очереди)
    server_socket.listen(10)
    print("Сервер запущен и ждёт подключений")

    while True:
        # Принимаем соединение от клиента
        client_socket, client_address = server_socket.accept()
        print(f"Пользователь с адресом: {client_address} подключился к серверу")

        # Получаем данные от клиента и сохраняем его в историю
        data = client_socket.recv(1024).decode()
        print(f"Пользователь с адресом: {client_address} отправил сообщение: {data}")
        message_history.append(data)

        # Отправляем клиенту историю сообщений
        client_socket.send('\n'.join(message_history).encode())

        client_socket.close()

if __name__ == "__main__":
    server()