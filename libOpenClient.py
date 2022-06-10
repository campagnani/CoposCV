import socket

class cordCart:
	x=0.0
	y=0.0
	z=0.0
	a=0.0
	e=0.0
	r=0.0

class cordJunta:
	j1=0.0
	j2=0.0
	j3=0.0
	j4=0.0
	j5=0.0
	j6=0.0


class libOpenClient:
	socketClient = 0
	
	def __init__(self, ipServidor='localhost', porta=54000):
		# Criando um socket TCP/IP
		global socketClient
		socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#, socket.SOCK_NONBLOCK)
		# Conectando ao servidor
		print('Tentando conectar a ' + ipServidor + ' através da porta ' + str(porta))
		socketClient.connect((ipServidor,porta))
		#socketClient.setblocking(0)
	
	def __del__(self):
		global socketClient
		print('Fechando socket')
		socketClient.close()
	
	def envia_msg(self, msg):
		global socketClient
		socketClient.sendall(str.encode(msg))
	
	def recebe_msg(self):
		global socketClient
		mensagemCompleta = b''
		while True:
			msg_byte = socketClient.recv(1)
			if (msg_byte==b'\x00'):
				return mensagemCompleta.decode('UTF-8')
			else:
				mensagemCompleta += msg_byte
			
	def listen_cart(self):
		self.envia_msg('lc')
		msg = self.recebe_msg()
		msg = msg.split(" ")
		saida = cordCart()
		saida.x = float(int(msg[0]))/1000
		saida.y = float(int(msg[1]))/1000
		saida.z = float(int(msg[2]))/1000
		saida.a = float(int(msg[3]))/1000
		saida.e = float(int(msg[4]))/1000
		saida.r = float(int(msg[5]))/1000
		return saida
	
	def listen_junta(self):
		self.envia_msg('lj')
		msg = self.recebe_msg()
		msg = msg.split(" ")
		saida = cordJunta()
		saida.j1 = float(int(msg[0]))/1000000
		saida.j2 = float(int(msg[1]))/1000000
		saida.j3 = float(int(msg[2]))/1000000
		saida.j4 = float(int(msg[3]))/1000000
		saida.j5 = float(int(msg[4]))/1000000
		saida.j6 = float(int(msg[5]))/1000000
		return saida

##### EXEMPLO 1: Apenas fazer o listen em coordenadas cartezianas salvando em uma variável
#oc = libOpenClient()
#coordenadas_Cartesianas = oc.listen_cart()
#print("X: " + str(coordenadas_Cartesianas.x) + "\tY: " +  str(coordenadas_Cartesianas.y) )


##### EXEMPLO 2: Escrevendo um valor qualquer nas juntas antes de fazer o listen
#oc = libOpenClient('localhost')
#oc.envia_msg('j 1000000 100000 10000 1000 100 10')
#oc.recebe_msg() #Ler para esvaziar a pilha
#coordenadas_Juntas = oc.listen_junta()
#print("J1: " + str(coordenadas_Juntas.j1) + "\tJ2: " +  str(coordenadas_Juntas.j2) )

