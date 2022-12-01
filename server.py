import pymysql
import socket, pickle
import threading
import json

HEADER_LENGTH = 10

def get_client_data(server):
    header_length = server.recv(HEADER_LENGTH)
    message_length = int(header_length.decode("utf-8").strip())
    data_res = server.recv(message_length)
    data_res = pickle.loads(data_res)
    return data_res

def send_text(sending_socket, text):
    # data = text.encode()
    # sending_socket.send(data)
    sending_socket.sendall(bytes(text,encoding="utf-8"))
    sending_socket.send(text)

HOST = 'localhost'
PORT = 8082
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
print('Start Server...')
connection_socket, addr = server_socket.accept()

message = get_client_data(connection_socket)
message["status"] = 1
print(message)

con = pymysql.connect(
    host="localhost", user="root", password="", database="mmt")
cur = con.cursor()
print(message["method"])

if message["method"] == "login":
    cur.execute("select * from user where username=%s and password = %s and status = 1",
                (message["user_name"], message["password"]))
    row = cur.fetchone()

    if row == None:
        text = "Not"
        connection_socket.send(text.encode())
    else:
        cur.execute("UPDATE user SET IP = %s WHERE username = %s and password = %s", (message["ip"], message["user_name"], message["password"]))
        text = "Ok"
        connection_socket.send(text.encode())
elif message["method"] == "show":
    cur.execute("select id, name, IP, image from user")
    rows = cur.fetchall()
    lists = [list(x) for x in rows]
    jsonStr = json.dumps(lists)

    # data = message.encode()
    # connection_socket.send(data)
    send_text(connection_socket, jsonStr)
else:
    cur.execute("INSERT INTO user (name, username, password, IP, status) values (%s, %s, %s, %s, 1)", (message["name"], message["user_name"], message["password"], message["ip"]))
    con.commit()
    print("Sign up successfully!!")

connection_socket.close()
server_socket.close()
print("End Server...")