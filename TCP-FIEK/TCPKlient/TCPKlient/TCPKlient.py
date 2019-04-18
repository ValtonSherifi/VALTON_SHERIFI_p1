import socket
import sys 
import select


SERVER= input("Emri i serverit:")
Port= input("Porti:")
PORT = int(Port)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER,PORT))

while True:
    print("\n________________________________________________________________________________________________________________\n\n")
    kerkesa=input("Opcionet:\n -IPAdresa        \n -nrPortit    \n -Bashketingelloret \n -Printimi   "
              +"     \n -EmriIKompjuterit\n -Koha            \n -Loja           \n -Fibonacci     \n -Mbledhja    \n -HiqNumrat      \n"+
              " -Konvertimi    \n\n");
    print("________________________________________________________________________________________________________________\n\n")
    kerkesa=kerkesa.strip()
    if len(kerkesa) > 129:
        print("\n\nKerkesa juaj ka me shum se 128 karaktere!")
        continue
    if not kerkesa:
        print("\n\nZgjedh keresen, per ta mbyllur shtypni 'x'")
        continue
    if kerkesa == "x":
        client.close()
        break
    client.sendall(bytes(kerkesa,'UTF-8'))
    data = client.recv(1024)
    data = data.decode('utf-8')
    print(data)
    print("\n\nShtyp x per ta mbyllur programin")



