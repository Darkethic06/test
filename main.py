from socket import AF_INET, SOCK_STREAM, gethostbyname
import socket
import time 


startTime = time.time()




if __name__ == '__main__':
    target = input("Enter the Ip : ")
    t_Ip = gethostbyname(target)
    print("Statrted Scanning on host : " ,t_Ip)
    for i  in range(0,65536):
        s = socket.socket(AF_INET, SOCK_STREAM)  
        con = s.connect_ex((t_Ip,i))
        if(con == 0):
            print("Port,",i ," is open")
        s.close()


print("Time taken : " , time.time() - startTime)