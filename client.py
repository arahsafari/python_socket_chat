# Import library socket
import socket               
 
# bikin objek socket dari librarynya
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# definisi ipserver dan port server
ipserver = '192.168.1.11'
port = 48666               
 
# konek ke server dengan ip dan portnya
s.connect((ipserver, port))

input_string = raw_input("string yang mau dikirim : ")
s.sendall(input_string)
# ambil data string dari server
print s.recv(6000)
# tutup koneksi socket
s.close()