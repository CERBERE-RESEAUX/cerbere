from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter

#### ICI C'EST POUR GERER LA PARTIE RECEPTION
def receive():    
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        except OSError:
            break


#### ICI C'EST LA PARTIE POUR GERER L'ENVOI
def send(event=None):    
    msg = my_msg.get()
    my_msg.set("")
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()
        top.quit()

def on_closing(event=None):
    my_msg.set("{quit}")
    send()

top = tkinter.Tk()
top.title("CERBERE CHAT")

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()  
my_msg.set("Votre message.")
scrollbar = tkinter.Scrollbar(messages_frame)  # pour revenir au message passé (scrollbar)

msg_list = tkinter.Listbox(messages_frame, height=20, width=70, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Envoyer", command=send)
send_button.pack()

top.protocol("WM_DELETE_WINDOW", on_closing)


serveur_tchat = "'chat.cerbere-apps.com'"


HOST = input('Adresse serveur \n ' "si aucune adresse =  " + serveur_tchat + " = adresse serveur cerbere utilisée de base")

if not HOST:
	HOST = serveur_tchat
else:
    HOST = int(HOST)
	
PORT = input('Port serveur (base 33000 \n si différend entrez le port) : ')
if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop() 
