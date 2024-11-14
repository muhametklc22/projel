from queue import Queue
import socket
import threading
from IPy import IP

hedef = input("Hedef IP adresini girin:")
proxy_ip = input("Proxy IP adresi girin:")  # Örnek: '94.245.56.147'

print("""
  _____           _          _____                 
 |  __ \         | |        / ____|                
 | |__) |__  _ __| |_ _____| (___   ___ __ _ _ __  
 |  ___/ _ \| '__| __|______\___ \ / __/ _` | '_ \ 
 | |  | (_) | |  | |_       ____) | (_| (_| | | | |
 |_|   \___/|_|   \__|     |_____/ \___\__,_|_| |_|

""")

kuyruk = Queue()
acik_portlar = []

def banner_al(s):
    s.recv(1024)

def ip_kontrol(ip):
    try:
        IP(ip)
        hedef_ip = ip
        return hedef_ip
    except ValueError:
        hedef_ip = socket.gethostbyname(ip)
        return hedef_ip

def port_tara(port):
    try:
        soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soket.connect((ip_kontrol(hedef), port))
        soket.sendto(("GET /" + hedef + " HTTP/1.1\r\n").encode('ascii'), (hedef, port))
        soket.sendto(("Host: " + proxy_ip + "\r\n\r\n").encode('ascii'), (hedef, port))
        return soket
    except:
        return False

def portlari_al(mod):
    if mod == 1:
        for port in range(1, 1025):
            kuyruk.put(port)
    elif mod == 2:
        for port in range(1, 48129):
            kuyruk.put(port)
    elif mod == 3:
        portlar = [20, 21, 22, 23, 25, 53, 80, 110, 443]
        for port in portlar:
            kuyruk.put(port)
    elif mod == 4:
        baslangic = int(input("Başlangıç portunu girin:"))
        bitis = int(input("Bitiş portunu girin:"))
        for port in range(baslangic, bitis):
            kuyruk.put(port)
    elif mod == 5:
        portlar = input("Portları girin (boşlukla ayırın):")
        portlar = portlar.split()
        portlar = list(map(int, portlar))
        for port in portlar:
            kuyruk.put(port)

def isci():
    while not kuyruk.empty():
        port = kuyruk.get()
        config = port_tara(port)
        if config:
            try:
                banner = banner_al(config)
                print("Port {} açık!".format(port) + ' : ' + str(banner.decode().strip('\n')))
            except:
                print("Port {} açık!".format(port))
            acik_portlar.append(port)
        else:
            print("Port {} kapalı!".format(port))

def tarayici_calistir(thread_sayisi, mod):
    portlari_al(mod)

    thread_listesi = []

    for t in range(thread_sayisi):
        thread = threading.Thread(target=isci)
        thread_listesi.append(thread)

    for thread in thread_listesi:
        thread.start()

    for thread in thread_listesi:
        thread.join()

    print("Açık portlar:", acik_portlar)

mod = int(input("Modu seçin [1:1-1024, 2:1-48128, 3:Belirli Portlar, 4:Özel(Aralık), 5:Özel(Specifik)]:"))
thread_sayisi = int(input("İş parçacığı (thread) sayısını girin:"))
tarayici_calistir(thread_sayisi, mod)
