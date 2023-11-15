import socket
from tkinter import *

def forward():
    
    msg_encoded=e1.get().encode("UTF-8")
    s.send(msg_encoded)
    
    
def receive():
    
    
    
    data=s.recv(1024)
    l3=Label(window,text="{}".format(data.decode('UTF-8')),bg="light grey")
    l3.place(x=100,y=180)
    
    

def connect():
    global s
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ip=socket.gethostbyname(socket.gethostname())
    s.connect((ip,2000))
    
     
def close():
    s.close()

window = Tk()


window.geometry("300x250+150+200")
window.title("Client")
window.resizable(width=False,height=False)
window.configure(background="light grey")
b1=Button(window,text='Send',fg='white',bg='grey',command=forward)
b2=Button(window,text='Receive',fg='white',bg='grey',command=receive)
b3=Button(window,text='Connect',fg='white',bg='grey',command=connect)
b4=Button(window,text='Close',fg='white',bg='grey',command=close)
l1=Label(window,text="Forward Msg",bg="light grey")
l2=Label(window,text="Received Msg",bg="light grey")
e1=Entry(window)
e1.place(x=100,y=60)
l1.place(x=20,y=60)
l2.place(x=20,y=180)
b1.place(x=70,y=120)
b2.place(x=120,y=120)
b3.place(x=180,y=120)
b4.place(x=125,y=160)
window.mainloop()























