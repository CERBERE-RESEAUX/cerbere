from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


def accepter_connexions_entrantes():
###gestion des clients
    while True:
        client, adresse_client = SERVER.accept()
        print("%s:%s est connecte." % adresse_client)
        client.send(bytes("Entrez votre nom : ", "utf8"))
        addresses[client] = adresse_client
        Thread(target=accueil_client, args=(client,)).start()


def accueil_client(client):  # Prend le socket client comme argument. Gère une seule connexion client.

    nom = client.recv(BUFSIZ).decode("utf8")
    bienvenu = 'Bienvenue %s!' % nom
    client.send(bytes(bienvenu, "utf8"))

    client_en_attente = '.......En attente du client ......'
    client.send(bytes(client_en_attente, "utf8"))

    msg = "%s a rejoint le chat!" % nom
    diffusion(bytes(msg, "utf8"))
    clients[client] = nom

    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            diffusion(msg, nom+": ")
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            diffusion(bytes("%s à quitté la discussion." % nom, "utf8"))
            break


def diffusion(msg, prefix=""):  # Le préfixe sert à l'identification du nom. la foncion "diffusion" diffusez un message à tous les clients.

    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)

        
clients = {}
addresses = {}

HOTE = ''
PORT = 33000
BUFSIZ = 1024
ADDR = (HOTE, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("En attente de connexion...")
    ACCEPT_THREAD = Thread(target=accepter_connexions_entrantes)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
