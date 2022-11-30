import pymysql
import socket
import pickle 
import json

HEADER_LENGTH = 10

def get_client_data(server):
    header_length = server.recv(HEADER_LENGTH)
    message_length = int(header_length.decode("utf-8").strip())
    data_res = server.recv(message_length)
    data_res = pickle.loads(data_res)
    return data_res

# def send_text(sending_socket, text):
#     data = text.encode()
#     sending_socket.send(data)
def send_text(sending_socket, text):
    # Connect to server and send data
    sending_socket.sendall(bytes(text,encoding="utf-8"))
    sending_socket.send(text)


HOST = 'localhost'
PORT = 8082
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
connection_socket, addr = server_socket.accept()
print('Start Server...')

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
# elif message["method"] == "show_friend":
#     cur.execute("select * from user")
#     row = cur.fetchall()
#     # print(row)
#     # print(type(row))
    
#     message2 = {}
#     message2["list"] = row

#     msg = pickle.dumps(message)
#     msg = bytes(f"{len(msg):<{11}}", "utf-8") + msg

#     connection_socket.send(msg)

    
elif message["method"] == "signup":
    cur.execute("INSERT INTO user (name, username, password, IP, status, image) values (%s, %s, %s, %s, 1, 'https://genk.mediacdn.vn/k:thumb_w/640/2016/photo-1-1473821552147/top6suthatcucsocvepikachu.jpg')", (message["name"], message["user_name"], message["password"], message["ip"]))
    con.commit()
    print("Sign up successfully!!")
elif message["method"] == "show":
    message = [[0, 'Bubuchacha', '192.168.1.6', 'https://e1.pngegg.com/pngimages/401/429/png-clipart-sharingan-all-files-mangekyo-sharingan.png'], [1, 'Chachabubu', '192.168.1.4', 
    'https://www.stockvault.net//data/2018/08/28/254043/thumb16.jpg'], [2, 'Chacha', '192.168.1.11', 'https://e1.pngegg.com/pngimages/401/429/png-clipart-sharingan-all-files-mangekyo-sharingan.png'], [3, 'Bubu', '192.168.1.12', 'https://i.pinimg.com/550x/09/b5/9a/09b59abebfda060a3725143e7955a0f9.jpg'], [4, 'Chacha', '192.168.1.15', 'https://e1.pngegg.com/pngimages/401/429/png-clipart-sharingan-all-files-mangekyo-sharingan.png'], [5, 'Bubu', '192.168.1.16', 'https://www.stockvault.net//data/2018/08/28/254043/thumb16.jpg'], [6, 'bubu', '192.168.1.15', 'https://e1.pngegg.com/pngimages/401/429/png-clipart-sharingan-all-files-mangekyo-sharingan.png'], [7, 'chacha', '192.168.1.16', 'https://www.stockvault.net//data/2018/08/28/254043/thumb16.jpg']]
    jsonStr = json.dumps(message)



    # data = message.encode()
    # connection_socket.send(data)
    send_text(connection_socket, jsonStr)




connection_socket.close()
server_socket.close()
print("End Server...")
