import socket , time

HOST = "127.0.0.1"
PORT = 63000

with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s :
    s.bind((HOST,PORT))
    s.listen()
    conn , addr = s.accept()
    print("Client connected!!")
    print(type(conn) , type(addr))
    with conn:
        print("Connected by" , addr)
        while True :
            data = conn.recv(1024)
            print("data:"+str(data))
            if not data : 
                break
            conn.sendall(data)