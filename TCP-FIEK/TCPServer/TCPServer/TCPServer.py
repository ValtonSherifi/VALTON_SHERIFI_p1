import socket
from threading import Thread
from builtins import reversed
import datetime
import threading
import sys
from _thread import *
import random
import binascii

def fib(n): 
    if (n <= 1): 
        return n; 
    return fib(n-1) + fib(n-2); 


def metodat(inputklienti,clientSocket,clientAddress):
    connection=clientSocket
    address=clientAddress
    if(inputklienti[0]=='IPAdresa'):
        connection.send(str.encode("IP Adresa e juaj eshte: "+address[0]))


    elif(inputklienti[0]=='nrPortit'):
       connection.send(str.encode("Ju jeni duke perdorur portin: "+str(address[1])))

    elif(inputklienti[0]=='Printimi'):
        s=' '.join(inputklienti[1:])
        if not s:
            connection.send(str.encode("Pas 'PRINTIMI' shtypeni tekstin!"))
        else:
            connection.send(str.encode(s))
        
            
    elif(inputklienti[0]=='EmriIKompjuterit'):
        try:
            hostname=socket.gethostname()
            connection.send( str.encode("Emri i kompjuterit tuaj eshte: "+hostname))
        except Exception:
            connection.send(str.encode("Emri i kompjuterit tuaj nuk dihet."))

    elif(inputklienti[0]=='Koha'):
        result=str(datetime.datetime.now())
        connection.send(str.encode(result))

    elif(inputklienti[0]=='Loja'):
        data = str(random.sample(range(1, 49), 7))
        connection.send(str.encode(data))

    elif(inputklienti[0]=='Bashketingelloret'):
        try:
            fjala=''.join(inputklienti[1:])
            bashketingelloret=("bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ ")
            nr=0
            for x in fjala:
                if x in bashketingelloret:
                    nr += 1 
            connection.send(str.encode("Teksti qe ju shtypet ka "+ str(nr) +" bashketingellore."))
        except Exeption:
                connection.send(str.encode("Pas 'BASHKETINGELLORE' shtypeni tekstin!"))

    elif(inputklienti[0]=='Mbledhja'):
        try: 
          first_number =(int(inputklienti[1]))
          second_number = (int(inputklienti[2]))
          sum = first_number + second_number
          connection.send(str.encode(str(sum)))
        except Exception:
            connection.send(str.encode("Pas 'MBLEDHJA' shtypeni dy numra!"))

    elif(inputklienti[0]=='HiqNumrat'):
        try:
            stringu =''.join(str(inputklienti[1:]))
            rezultati = ''.join(i for i in stringu if not i.isdigit()) 
            connection.send(str.encode(rezultati))
        except Exception:
            connectio.send(str.encode("Ju Lutem Shtypeni mire!"))

    elif(inputklienti[0]=='Fibonacci'):
        try:
            n=fib(int(inputklienti[1]))
            connection.send(str.encode(str(n)))
        except Exception:
            connection.send(str.encode("Pas 'fibbonacci' shtypeni numrin!"))


          
       
       

    elif(inputklienti[0]=='Konvertimi'):
        konvertimet="Mundesit e konverimev:\nKilowattToHorsePower  \nHorsepowerToKilowatt  \nDegreesToRadians \nRadiansToDegrees \nGallonsToLiters \nLitersToGallons"
        try:
            b=inputklienti[1];
            a=float(inputklienti[2])
            c=''
            if(b=="KilowattToHorsepower"):
                c=(a*1.341)
                connection.send(str.encode(str(c)))
            elif(b=="HorsepowerToKilowatt"):
                c=(a/1.341)
                connection.send(str.encode(str(c)))
            elif(b=="DegreesToRadians"):
                c=a*(3.14/180)
                connection.send(str.encode(str(c)))
            elif(b=="RadiansToDegrees"):
                c=a*(180/3.14)
                connection.send(str.encode(str(c)))
            elif(b=="GallonsToLiters"):
                c=(a*3.785)
                connection.send(str.encode(str(c)))
            elif(b=="LitersToGallons"):
                c=(a/3.785)
                connection.send(str.encode(str(c)))

        except Exception:
            connection.send(str.encode("Pas 'KONVERTIMI' shkruani 'LlojiIKonvertimit' pastaj shifren!\n"+konvertimet))

   
           


class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        self.caddress=clientAddress
        print ("U shtua nje lidhje me adresen: ", clientAddress)
    def run(self):
        msg = ''
        while True:
            data = self.csocket.recv(1024)
            msg = data.decode()
            inputklienti = msg.split()
            try:
                metodat(inputklienti,self.csocket,self.caddress)
            except Exception:
                self.csocket.send(str.encode("Nuk e keni shenuar keresen mire!"))
           
        
            
   



LOCALHOST = ''
PORT = 12000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
try:
    server.bind((LOCALHOST, PORT))
except socket.error as e:
    print(str(e))

print('Serveri u startua ne localhost, porti:'+str(PORT))

print('Serveri tani mund te pranoj kerkesa')

while True:
    server.listen(5)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()



  

