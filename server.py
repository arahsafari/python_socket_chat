# Import library socket
import socket

# bikin objek socket dari librarynya
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# definisi ipserver dan port server
ipserver = ''
port = 48666

s.bind((ipserver, port))
print "socket di bind ke %s port %d" % (ipserver,port)

# ini buat listener socketnya
s.listen(5)

# forever loop
while True:

    # dapetin koneksi dari client ke server
    c, addr = s.accept()
    print 'Koneksi dari', addr

    # dapetin data dari client
    data = c.recv(6000)
    print "Pesan dari ", addr , " : " , data

    if not data:
        break

    # kirim data balik ke client
    data = "ini message dari server : "+data + "SERVER"
    c.sendall(data)
    c.close()