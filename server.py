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

HOST = ''
PORT = 8082
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
print('Start Server...')

def server_login(message):
    cur.execute("select * from user where username=%s and password = %s and status = 1",
                (message["user_name"], message["password"]))
    row = cur.fetchone()

    if row == None:
        text = "Not"
        connection_socket.send(text.encode())
    else:
        cur.execute("UPDATE user SET IP = %s WHERE username = %s and password = %s", (message["ip"], message["user_name"], message["password"]))
        con.commit()
        cur.execute("SELECT * FROM user WHERE username = %s and password = %s", (message["user_name"], message["password"]))
        row = cur.fetchone()
        print(row[0])
        text = str(row[0])
        connection_socket.send(text.encode())

def server_show(message):
    # cur.execute("select id, name, IP, image from user")
    cur.execute("select id, name, IP, image from user where id in (select friend_user_id from friend where user_id = %s) and IP != '0.0.0.0'", (message["id"]))
    rows = cur.fetchall()
    lists = [list(x) for x in rows]
    jsonStr = json.dumps(lists)

    # data = message.encode()
    # connection_socket.send(data)
    send_text(connection_socket, jsonStr)

def server_signup(message):
    cur.execute("select * from user where username = %s", (message["user_name"]))
    row = cur.fetchone()
    if row == None:
        cur.execute("INSERT INTO user (name, username, password, IP, status, image) values (%s, %s, %s, %s, 1, 'https://genk.mediacdn.vn/k:thumb_w/640/2016/photo-1-1473821552147/top6suthatcucsocvepikachu.jpg')", (message["name"], message["user_name"], message["password"], message["ip"]))
        con.commit()
        text = "Ok"
        print("Sign up successfully!!")
        connection_socket.send(text.encode())
    else:
        text = "Not"
        connection_socket.send(text.encode())


def server_logout(mess):

    # print("UPDATE user SET IP = %s WHERE id = %i", ("0.0.0.0", int(mess["id"])))
    cur.execute("UPDATE user SET IP = %s WHERE id = %s", ("0.0.0.0", int(mess["id"])))
    con.commit()

def server_showall(mess):
    cur.execute("select id, name, IP, image from user where id != %s AND id not in (select friend_user_id from friend where user_id=%s)", (mess["id"],mess["id"]))
    rows = cur.fetchall()
    lists = [list(x) for x in rows]
    jsonStr = json.dumps(lists)

    # data = message.encode()
    # connection_socket.send(data)
    send_text(connection_socket, jsonStr)


def server_addfriend(message, connect_socket2):
    print(message)
    cur.execute("select * from user where name = %s", (message["friend_name"]))
    row = cur.fetchone()
    print(row)
    print(row[0])
    cur.execute("insert into friend (user_id, friend_user_id) values (%s, %s)", (message["id"], row[0]))
    con.commit()
    cur.execute("insert into friend (user_id, friend_user_id) values (%s, %s)", (row[0], message["id"]))
    con.commit()
    print("Add successfully!!")
    connect_socket2.send("hello".encode())


while 1:
    connection_socket, addr = server_socket.accept()

    message = get_client_data(connection_socket)
    message["status"] = 1
    print(message)

    con = pymysql.connect(
        host="localhost", user="root", password="", database="mmt")
    cur = con.cursor()
    print(message["method"])

    if message["method"] == "login":
        loginThread=threading.Thread(target=server_login, args=(message,))
        loginThread.start()
    elif message["method"] == "show":
        print(message)
        showThread=threading.Thread(target=server_show, args=(message,))
        showThread.start()
    elif message["method"] == "signup":
        signupThread=threading.Thread(target=server_signup, args=(message,))
        signupThread.start()
    elif message["method"] == "logout":
        logoutThread=threading.Thread(target=server_logout, args=(message,))
        logoutThread.start()
    elif message["method"]=="showall":
        showAllThread=threading.Thread(target=server_showall,args=(message,))
        showAllThread.start()
    elif message["method"]=="addfriend":
        addFriendThread=threading.Thread(target=server_addfriend,args=(message,connection_socket,))
        addFriendThread.start()

connection_socket.close()
server_socket.close()
print("End Server...")