import tkinter as tk
from tkinter import *
import threading
import socket 
import time
import csv

root = tk.Tk()
#root.attributes('-fullscreen',True)
root.configure(background='black')	

check_livingroom=1
check_bedroom=1
check_bathroom=1
check_kitchen=1


def saveval():

	global bathroomvarr
	global bathroomvarg
	global bathroomvarb
	global bathroomvarw
	global bathroomvary
	global bathroomvarbr

	global kitchenvarr
	global kitchenvarg
	global kitchenvarb
	global kitchenvarw
	global kitchenvary
	global kitchenvarbr

	global livingroomvarr
	global livingroomvarg
	global livingroomvarb
	global livingroomvarw
	global livingroomvary
	global livingroomvarbr

	global bedroomvarr
	global bedroomvarg
	global bedroomvarb
	global bedroomvarw
	global bedroomvary
	global bedroomvarbr

	global check_livingroom
	global check_bedroom
	global check_bathroom
	global check_kitchen

	while True:
		time.sleep(5)
		with open('csvfile.txt', mode='w') as value_csv:
			value_writer = csv.writer(value_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
			value_writer.writerow(['bathroomr','bathroomg','bathroomb','bathroomw','bathroomy','bathroombr','kitchenr','kitcheng','kitchenb','kitchenw','kitcheny','kitchenbr','livingroomr','livingroomg','livingroomb','livingroomw','livingroomy','livingroombr','bedroomr','bedroomg','bedroomb','bedroomw','bedroomy','bedroombr','checklivingroom','checkbedroom','checkbathroom','checkkitchen'])
			value_writer.writerow([bathroomvarr.get(),bathroomvarg.get(),bathroomvarb.get(),bathroomvarw.get(),bathroomvary.get(),bathroomvarbr.get(),kitchenvarr.get(),kitchenvarg.get(),kitchenvarb.get(),kitchenvarw.get(),kitchenvary.get(),kitchenvarbr.get(),livingroomvarr.get(),livingroomvarg.get(),livingroomvarb.get(),livingroomvarw.get(),livingroomvary.get(),livingroomvarbr.get(),bedroomvarr.get(),bedroomvarg.get(),bedroomvarb.get(),bedroomvarw.get(),bedroomvary.get(),bedroomvarbr.get(),check_livingroom,check_bedroom,check_bathroom,check_kitchen])


		


def client():
	global bathroomvarbr
	global bathroomvarr
	global bathroomvarg
	global bathroomvarb
	global bathroomvarw
	global bathroomvary

	global kitchenvarr
	global kitchenvarg
	global kitchenvarb
	global kitchenvarw
	global kitchenvary
	global kitchenvarbr

	global livingroomvarr
	global livingroomvarg
	global livingroomvarb
	global livingroomvarw
	global livingroomvary
	global livingroomvarbr

	global bedroomvarr
	global bedroomvarg
	global bedroomvarb
	global bedroomvarw
	global bedroomvary
	global bedroomvarbr
	
	
#These are all the IP addresses allocated to the Phillip Hue Lightbulbs on the network, note that you NEED a WAN connection for initial DHCP reservation via HUE APP. 
	bath_ip = {'10.0.0.40','10.0.0.41','10.0.0.42','10.0.0.43'}
	kitchen_ip = {'10.0.0.20','10.0.0.21'}
	living_ip = {'10.0.0.10','10.0.0.11'}
	bed_ip = {'10.0.0.30','10.0.0.31'}
	while True:
		global check_bathroom
		if check_bathroom == 1:

			for i in bath_ip:
				try:

					UDP_IP = i
					UDP_PORT = 38899
					MESSAGE = '{{"params":{{"dimming":{},"orig":"ios"}},"id":36,"method":"setPilot"}}'.format(bathroomvarbr.get())
					sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
					sock.sendto(bytes(MESSAGE, "utf-8"), (UDP_IP, UDP_PORT))
					time.sleep(0.1)
					MESSAGES = '{{"method":"setPilot","id":14,"params":{{"r":{},"g":{},"b":{},"c":{},"w":{},"orig":"ios"}}}}'.format(bathroomvarr.get(), bathroomvarg.get(), bathroomvarb.get(), bathroomvarw.get(), bathroomvary.get())
					socks = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
					socks.sendto(bytes(MESSAGES, "utf-8"), (UDP_IP, UDP_PORT))
					#print(MESSAGES)
				except:
					pass

		global check_kitchen
		if check_kitchen == 1:

			for i in kitchen_ip:
				try:

					UDP_IP = i
					UDP_PORT = 38899
					MESSAGE = '{{"params":{{"dimming":{},"orig":"ios"}},"id":36,"method":"setPilot"}}'.format(kitchenvarbr.get())
					sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
					sock.sendto(bytes(MESSAGE, "utf-8"), (UDP_IP, UDP_PORT))
					time.sleep(0.1)
					MESSAGES = '{{"method":"setPilot","id":14,"params":{{"r":{},"g":{},"b":{},"c":{},"w":{},"orig":"ios"}}}}'.format(kitchenvarr.get(), kitchenvarg.get(), kitchenvarb.get(), kitchenvarw.get(), kitchenvary.get())
					socks = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
					socks.sendto(bytes(MESSAGES, "utf-8"), (UDP_IP, UDP_PORT))
					#print(MESSAGES)
				except:
					pass

		global check_livingroom
		if check_livingroom == 1:

			for i in living_ip:
				try:

					UDP_IP = i
					UDP_PORT = 38899
					MESSAGE = '{{"params":{{"dimming":{},"orig":"ios"}},"id":36,"method":"setPilot"}}'.format(livingroomvarbr.get())
					sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
					sock.sendto(bytes(MESSAGE, "utf-8"), (UDP_IP, UDP_PORT))
					time.sleep(0.1)
					MESSAGES = '{{"method":"setPilot","id":14,"params":{{"r":{},"g":{},"b":{},"c":{},"w":{},"orig":"ios"}}}}'.format(livingroomvarr.get(), livingroomvarg.get(), livingroomvarb.get(), livingroomvarw.get(), livingroomvary.get())
					socks = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
					socks.sendto(bytes(MESSAGES, "utf-8"), (UDP_IP, UDP_PORT))
					#print(MESSAGES)
				except:
					pass

		for i in bed_ip:
			global check_bedroom
			if check_bedroom==1:

				try:

					UDP_IP = i
					UDP_PORT = 38899
					MESSAGE = '{{"params":{{"dimming":{},"orig":"ios"}},"id":36,"method":"setPilot"}}'.format(bedroomvarbr.get())
					sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
					sock.sendto(bytes(MESSAGE, "utf-8"), (UDP_IP, UDP_PORT))
					time.sleep(0.1)
					MESSAGES = '{{"method":"setPilot","id":14,"params":{{"r":{},"g":{},"b":{},"c":{},"w":{},"orig":"ios"}}}}'.format(bedroomvarr.get(), bedroomvarg.get(), bedroomvarb.get(), bedroomvarw.get(), bedroomvary.get())
					socks = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
					socks.sendto(bytes(MESSAGES, "utf-8"), (UDP_IP, UDP_PORT))
					#print(MESSAGES)
				except:
					pass
			


# Initialized Variables for the sliders that control bulb Values

livingroomvarr = tk.IntVar(value=20.0)
livingroomvarg = tk.IntVar(value=30.0)
livingroomvarb = tk.IntVar(value=40.0)

livingroomvarw = tk.IntVar(value=50.0)
livingroomvary = tk.IntVar(value=60.0)
livingroomvarbr = tk.IntVar(value=70.0)

bathroomvarr = tk.IntVar(value = 20.0)
bathroomvarg = tk.IntVar(value = 30.0)
bathroomvarb = tk.IntVar(value = 40.0)
bathroomvarw = tk.IntVar(value = 50.0)
bathroomvary = tk.IntVar(value = 60.0)
bathroomvarbr = tk.IntVar(value = 80.0)

kitchenvarr = tk.IntVar(value=20.0)
kitchenvarg = tk.IntVar(value=30.0)
kitchenvarb = tk.IntVar(value=40.0)
kitchenvarw = tk.IntVar(value=50.0)
kitchenvary = tk.IntVar(value=60.0)
kitchenvarbr = tk.IntVar(value=70.0)

bedroomvarr = tk.IntVar(value=20.0)
bedroomvarg = tk.IntVar(value=30.0)
bedroomvarb = tk.IntVar(value=40.0)
bedroomvarw = tk.IntVar(value=50.0)
bedroomvary = tk.IntVar(value=60.0)
bedroomvarbr = tk.IntVar(value=70.0)

#Open the CSV that holds the values of the bulb Variables, This allows persistance over reboots. This also sets the initial values of the bulbs based on the variables in the CSV 

with open('csvfile.txt', mode='r') as csv_file:
	csv_reader= csv.DictReader(csv_file)
	for row in csv_reader:	
		bathroomvarr.set(float(row['bathroomr']))
		bathroomvarg.set(float(row['bathroomg']))
		bathroomvarb.set(float(row['bathroomb']))
		bathroomvarw.set(float(row['bathroomw']))
		bathroomvary.set(float(row['bathroomy']))
		bathroomvarbr.set(float(row['bathroombr']))

		kitchenvarr.set(float(row['kitchenr']))
		kitchenvarg.set(float(row['kitcheng']))
		kitchenvarb.set(float(row['kitchenb']))
		kitchenvarw.set(float(row['kitchenw']))
		kitchenvary.set(float(row['kitcheny']))
		kitchenvarbr.set(float(row['kitchenbr']))

		livingroomvarr.set(float(row['livingroomr']))
		livingroomvarg.set(float(row['livingroomg']))
		livingroomvarb.set(float(row['livingroomb']))
		livingroomvarw.set(float(row['livingroomw']))
		livingroomvary.set(float(row['livingroomy']))
		livingroomvarbr.set(float(row['livingroombr']))

		bedroomvarr.set(float(row['bedroomr']))
		bedroomvarg.set(float(row['bedroomg']))
		bedroomvarb.set(float(row['bedroomb']))
		bedroomvarw.set(float(row['bedroomw']))
		bedroomvary.set(float(row['bedroomy']))
		bedroomvarbr.set(float(row['bedroombr']))

		check_livingroom=row['checklivingroom']
		check_bedroom=row['checkbedroom']
		check_bathroom=row['checkbathroom']
		check_kitchen=row['checkkitchen']






p = threading.Thread(target=client)
p.setDaemon(True)
p.start()

p1 = threading.Thread(target=saveval)
p1.setDaemon(True)
p1.start()

def winroom():

	for x in root.winfo_children():
		x.destroy()

	spacer = Label(root, text='', bg='black')
	spacer.pack()
	spacerr = Label(root, text='', bg='black')
	spacerr.pack()
	spacerrr = Label(root, text='', bg='black')
	spacerrr.pack()

	butkit = Button(root, text='KITCHEN', bg='black', padx=82, pady=35, fg='white', bd=5, command=kitchen)
	butkit.pack()

	butliv = Button(root, text='LIVING ROOM', bg='black', padx=65, pady=35, fg='white', bd=5, command=livingroom)
	butliv.pack()

	butbed = Button(root, text='BEDROOM', bg='black', padx=76, pady=35, fg='white', bd=5, command=bedroom)
	butbed.pack()

	butbat = Button(root, text='BATHROOM', bg='black', padx=72, pady=35, fg='white', bd=5, command=bath)
	butbat.pack()

def bath():

	global bathroomvarr
	global bathroomvarg
	global bathroomvarb
	global bathroomvarw
	global bathroomvary
	global bathroomvarbr
	
	varr = bathroomvarr
	varg = bathroomvarg
	varb = bathroomvarb
	varw = bathroomvarw
	vary = bathroomvary
	varbr = bathroomvarbr


	for x in root.winfo_children():
		x.destroy()

	def setvalr(val):
		global bathroomvarr
		bathroomvarr.value = val

	def setvalg(val):
		global bathroomvarg
		bathroomvarg.value = val

	def setvalb(val):
		global bathroomvarb
		bathroomvarb.value = val

	def setvalw(val):
		global bathroomvarw
		bathroomvarw.value = val

	def setvaly(val):
		global bathroomvary
		bathroomvary.value = val

	def setvalbr(val):
		global bathroomvarbr
		bathroomvarbr.value = val

	def setvaloff():
		global check_bathroom
		check_bathroom = 0
		bath_ip = {'10.0.0.40','10.0.0.41','10.0.0.42','10.0.0.43'}
		time.sleep(0.2)
		for i in bath_ip:
			try:

				UDP_IP = i
				UDP_PORT = 38899
				MESSAGES = '{"Params":{"orig":"ios","state":false},"id":29,"method":"setPilot"}'
				socks = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
				socks.sendto(bytes(MESSAGES, "utf-8"), (UDP_IP, UDP_PORT))
			except:
				pass

	def setvalon():
		global check_bathroom
		check_bathroom = 1
	
	

	#RGB Window
	spacer1 = Label(root, text='', bg='black')
	spacer1.pack()
	 
	slideR = Scale(root, from_=1, to=255, orient=HORIZONTAL, showvalue=0, label="RED", width=35, length=800, sliderlength=300, bg='black', fg='white', variable=varr, command=setvalr)
	#slideR.set(bathroomvarr.get())
	slideR.pack()

	slideg = Scale(root, from_=1, to=255, orient=HORIZONTAL, showvalue=0, label="GREEN", width=35, length=800, sliderlength=300, bg='black', fg='white', variable=varg, command=setvalg)
	slideg.set(bathroomvarg.get())
	slideg.pack()

	slideb = Scale(root, from_=1, to=255, orient=HORIZONTAL, showvalue=0, label="BLUE", width=35, length=800, sliderlength=300, bg='black', fg='white', variable=varb, command=setvalb)
	slideb.set(bathroomvarb.get())
	slideb.pack()

	spacer2 = Label(root, text='', bg='black')
	spacer2.pack()

	slidew = Scale(root, from_=1, to=255, orient=HORIZONTAL, showvalue=0, label="WHITE LIGHT", width=35, length=800, sliderlength=300, bg='black', fg='white', variable=varw, command=setvalw)
	slidew.set(bathroomvarw.get())
	slidew.pack()

	slidey = Scale(root, from_=1, to=255, orient=HORIZONTAL, showvalue=0, label="NATURAL LIGHT", width=35, length=800, sliderlength=300, bg='black', fg='white', variable=vary, command=setvaly)
	slidey.set(bathroomvary.get())
	slidey.pack()

	slidebr = Scale(root, from_=20, to=100, orient=HORIZONTAL, showvalue=0, label="BRIGHTNESS", width=35, length=800, sliderlength=300, bg='black', fg='white', variable=varbr, command=setvalbr)
	slidebr.set(bathroomvarbr.get())
	slidebr.pack()

	spacer3 = Label(root, text='                           ', bg='black')
	spacer3.pack(side=LEFT)


	buton = Button(root, text='ON', bg='black', padx=50, pady=45, fg='white', bd=5, command=setvalon)
	buton.pack(side=LEFT)

	spacer4 = Label(root, text='                          ', bg='black')
	spacer4.pack(side=LEFT)

	butoff = Button(root, text='OFF', bg='black', padx=50, pady=45, fg='white', bd=5, command=setvaloff)
	butoff.pack(side=LEFT)

	spacer4 = Label(root, text='                          ', bg='black')
	spacer4.pack(side=LEFT)

	butroom = Button(root, text='ROOMS', bg='black', padx=50, pady=45, fg='white', bd=5, command=winroom)
	butroom.pack(side=LEFT)

def kitchen():

	global kitchenvarr
	global kitchenvarg
	global kitchenvarb
	global kitchenvarw
	global kitchenvary
	global kitchenvarbr
	
	varr = kitchenvarr
	varg = kitchenvarg
	varb = kitchenvarb
	varw = kitchenvarw
	vary = kitchenvary
	varbr = kitchenvarbr



	def setvalr(val):
		global kitchenvarr
		kitchenvarr.value = val

	def setvalg(val):
		global kitchenvarg
		kitchenvarg.value = val

	def setvalb(val):
		global kitchenvarb
		kitchenvarb.value = val

	def setvalw(val):
		global kitchenvarw
		kitchenvarw.value = val

	def setvaly(val):
		global kitchenvary
		kitchenvary.value = val

	def setvalbr(val):
		global kitchenvarbr
		kitchenvarbr.value = val

	def setvaloff():
		global check_kitchen
		check_kitchen = 0
		kitchen_ip = {'10.0.0.20','10.0.0.21'}
		time.sleep(0.2)
		for i in kitchen_ip:
			try:

				UDP_IP = i
				UDP_PORT = 38899
				MESSAGES = '{"Params":{"orig":"ios","state":false},"id":29,"method":"setPilot"}'
				socks = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
				socks.sendto(bytes(MESSAGES, "utf-8"), (UDP_IP, UDP_PORT))
			except:
				pass

	def setvalon():
		global check_kitchen
		check_kitchen = 1
	


	for x in root.winfo_children():
		x.destroy()

	#RGB Window
	spacer1 = Label(root, text='', bg='black')
	spacer1.pack()
	 
	slideR = Scale(root, from_=1, to=255, orient=HORIZONTAL, showvalue=0, label="RED", width=35, length=800, sliderlength=300, bg='black', fg='white', variable=varr, command=setvalr)
	slideR.set(kitchenvarr.get())
	slideR.pack()

	slideg = Scale(root, from_=1, to=255, orient=HORIZONTAL, showvalue=0, label="GREEN", width=35, length=800, sliderlength=300, bg='black', fg='white', variable=varg, command=setvalg)
	slideg.set(kitchenvarg.get())
	slideg.pack()

	slideb = Scale(root, from_=1, to=255, orient=HORIZONTAL, showvalue=0, label="BLUE", width=35, length=800, sliderlength=300, bg='black', fg='white', variable=varb, command=setvalb)
	slideb.set(kitchenvarb.get())
	slideb.pack()

	spacer2 = Label(root, text='', bg='black')
	spacer2.pack()

	slidew = Scale(root, from_=1, to=255, orient=HORIZONTAL, showvalue=0, label="WHITE LIGHT", width=35, length=800, sliderlength=300, bg='black', fg='white', variable=varw, command=setvalw)
	slidew.set(kitchenvarw.get())
	slidew.pack()

	slidey = Scale(root, from_=1, to=255, orient=HORIZONTAL, showvalue=0, label="NATURAL LIGHT", width=35, length=800, sliderlength=300, bg='black', fg='white', variable=vary, command=setvaly)
	slidey.set(kitchenvary.get())
	slidey.pack()

	slidebr = Scale(root, from_=20, to=100, orient=HORIZONTAL, showvalue=0, label="BRIGHTNESS", width=35, length=800, sliderlength=300, bg='black', fg='white', variable=varbr, command=setvalbr)
	slidebr.set(kitchenvarbr.get())
	slidebr.pack()

	spacer3 = Label(root, text='                           ', bg='black')
	spacer3.pack(side=LEFT)


	buton = Button(root, text='ON', bg='black', padx=50, pady=45, fg='white', bd=5, command=setvalon)
	buton.pack(side=LEFT)

	spacer4 = Label(root, text='                          ', bg='black')
	spacer4.pack(side=LEFT)

	butoff = Button(root, text='OFF', bg='black', padx=50, pady=45, fg='white', bd=5, command=setvaloff)
	butoff.pack(side=LEFT)

	spacer4 = Label(root, text='                          ', bg='black')
	spacer4.pack(side=LEFT)

	butroom = Button(root, text='ROOMS', bg='black', padx=50, pady=45, fg='white', bd=5, command=winroom)
	butroom.pack(side=LEFT)

def bedroom():

	global bedroomvarr
	global bedroomvarg
	global bedroomvarb
	global bedroomvarw
	global bedroomvary
	global bedroomvarbr
	
	varr = bedroomvarr
	varg = bedroomvarg
	varb = bedroomvarb
	varw = bedroomvarw
	vary = bedroomvary
	varbr = bedroomvarbr


	def setvalr(val):
		global bedroomvarr
		bedroomvarr.value = val

	def setvalg(val):
		global bedroomvarg
		bedroomvarg.value = val

	def setvalb(val):
		global bedroomvarb
		bedroomvarb.value = val

	def setvalw(val):
		global bedroomvarw
		bedroomvarw.value = val

	def setvaly(val):
		global bedroomvary
		bedroomvary.value = val

	def setvalbr(val):
		global bedroomvarbr
		bedroomvarbr.value = val

	def setvaloff():
		global check_bedroom
		check_bedroom = 0
		bed_ip = {'10.0.0.30','10.0.0.31'}
		time.sleep(0.2)
		for i in bed_ip:
			try:

				UDP_IP = i
				UDP_PORT = 38899
				MESSAGES = '{"Params":{"orig":"ios","state":false},"id":29,"method":"setPilot"}'
				socks = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
				socks.sendto(bytes(MESSAGES, "utf-8"), (UDP_IP, UDP_PORT))
			except:
				pass

	def setvalon():
		global check_bedroom
		check_bedroom = 1	


	for x in root.winfo_children():
		x.destroy()

	#RGB Window
	spacer1 = Label(root, text='', bg='black')
	spacer1.pack()
	 
	slideR = Scale(root, from_=1, to=255, orient=HORIZONTAL, showvalue=0, label="RED", width=35, length=800, sliderlength=300, bg='black', fg='white', variable=varr, command=setvalr)
	slideR.set(bedroomvarr.get())	
	slideR.pack()

	slideg = Scale(root, from_=1, to=255, orient=HORIZONTAL, showvalue=0, label="GREEN", width=35, length=800, sliderlength=300, bg='black', fg='white', variable=varg, command=setvalg)
	slideg.set(bedroomvarg.get())	
	slideg.pack()

	slideb = Scale(root, from_=1, to=255, orient=HORIZONTAL, showvalue=0, label="BLUE", width=35, length=800, sliderlength=300, bg='black', fg='white', variable=varb, command=setvalb)
	slideb.set(bedroomvarb.get())	
	slideb.pack()

	spacer2 = Label(root, text='', bg='black')
	spacer2.pack()

	slidew = Scale(root, from_=1, to=255, orient=HORIZONTAL, showvalue=0, label="WHITE LIGHT", width=35, length=800, sliderlength=300, bg='black', fg='white', variable=varw, command=setvalw)
	slidew.set(bedroomvarw.get())	
	slidew.pack()

	slidey = Scale(root, from_=1, to=255, orient=HORIZONTAL, showvalue=0, label="NATURAL LIGHT", width=35, length=800, sliderlength=300, bg='black', fg='white', variable=vary, command=setvaly)
	slidey.set(bedroomvary.get())	
	slidey.pack()

	slidebr = Scale(root, from_=20, to=100, orient=HORIZONTAL, showvalue=0, label="BRIGHTNESS", width=35, length=800, sliderlength=300, bg='black', fg='white', variable=varbr, command=setvalbr)
	slidebr.set(bedroomvarbr.get())	
	slidebr.pack()

	spacer3 = Label(root, text='                           ', bg='black')
	spacer3.pack(side=LEFT)


	buton = Button(root, text='ON', bg='black', padx=50, pady=45, fg='white', bd=5, command=setvalon)
	buton.pack(side=LEFT)

	spacer4 = Label(root, text='                          ', bg='black')
	spacer4.pack(side=LEFT)

	butoff = Button(root, text='OFF', bg='black', padx=50, pady=45, fg='white', bd=5, command=setvaloff)
	butoff.pack(side=LEFT)

	spacer4 = Label(root, text='                          ', bg='black')
	spacer4.pack(side=LEFT)

	butroom = Button(root, text='ROOMS', bg='black', padx=50, pady=45, fg='white', bd=5, command=winroom)
	butroom.pack(side=LEFT)

def livingroom():

	global livingroomvarr
	global livingroomvarg
	global livingroomvarb
	global livingroomvarw
	global livingroomvary
	global livingroomvarbr
	
	varr = livingroomvarr
	varg = livingroomvarg
	varb = livingroomvarb
	varw = livingroomvarw
	vary = livingroomvary
	varbr = livingroomvarbr

	def setvalr(val):
		global livingroomvarr
		livingroomvarr.value = val

	def setvalg(val):
		global livingroomvarg
		livingroomvarg.value = val

	def setvalb(val):
		global livingroomvarb
		livingroomvarb.value = val

	def setvalw(val):
		global livingroomvarw
		livingroomvarw.value = val

	def setvaly(val):
		global livingroomvary
		livingroomvary.value = val

	def setvalbr(val):
		global livingroomvarbr
		livingroomvarbr.value = val

	def setvaloff():
		global check_livingroom
		check_livingroom = 0
		living_ip = {'10.0.0.10','10.0.0.11'}
		time.sleep(0.2)
		for i in living_ip:
			try:

				UDP_IP = i
				UDP_PORT = 38899
				MESSAGES = '{"Params":{"orig":"ios","state":false},"id":29,"method":"setPilot"}'
				socks = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
				socks.sendto(bytes(MESSAGES, "utf-8"), (UDP_IP, UDP_PORT))
			except:
				pass

	def setvalon():
		global check_livingroom
		check_livingroom = 1






	

	
	global livingroomvar

	for x in root.winfo_children():
		x.destroy()

	#RGB Window
	spacer1 = Label(root, text='', bg='black')
	spacer1.pack()
	 
	slideR = Scale(root, from_=1, to=255, orient=HORIZONTAL, showvalue=0, label="RED", width=35, length=800, sliderlength=300, bg='black', fg='white', variable=varr, command=setvalr)
	slideR.set(livingroomvarr.get())	
	slideR.pack()

	slideg = Scale(root, from_=1, to=255, orient=HORIZONTAL, showvalue=0, label="GREEN", width=35, length=800, sliderlength=300, bg='black', fg='white', variable=varg, command=setvalg)
	slideg.set(livingroomvarg.get())	
	slideg.pack()

	slideb = Scale(root, from_=1, to=255, orient=HORIZONTAL, showvalue=0, label="BLUE", width=35, length=800, sliderlength=300, bg='black', fg='white', variable=varb, command=setvalb)
	slideb.set(livingroomvarb.get())	
	slideb.pack()

	spacer2 = Label(root, text='', bg='black')	
	spacer2.pack()

	slidew = Scale(root, from_=1, to=255, orient=HORIZONTAL, showvalue=0, label="WHITE LIGHT", width=35, length=800, sliderlength=300, bg='black', fg='white', variable=varw, command=setvalw)
	slidew.set(livingroomvarw.get())	
	slidew.pack()

	slidey = Scale(root, from_=1, to=255, orient=HORIZONTAL, showvalue=0, label="NATURAL LIGHT", width=35, length=800, sliderlength=300, bg='black', fg='white', variable=vary, command=setvaly)
	slidey.set(livingroomvary.get())	
	slidey.pack()

	slidebr = Scale(root, from_=20, to=100, orient=HORIZONTAL, showvalue=0, label="BRIGHTNESS", width=35, length=800, sliderlength=300, bg='black', fg='white', variable=varbr, command=setvalbr)
	slidebr.set(livingroomvarbr.get())	
	slidebr.pack()

	spacer3 = Label(root, text='                           ', bg='black')
	spacer3.pack(side=LEFT)


	buton = Button(root, text='ON', bg='black', padx=50, pady=45, fg='white', bd=5, command=setvalon)
	buton.pack(side=LEFT)

	spacer4 = Label(root, text='                          ', bg='black')
	spacer4.pack(side=LEFT)

	butoff = Button(root, text='OFF', bg='black', padx=50, pady=45, fg='white', bd=5, command=setvaloff)
	butoff.pack(side=LEFT)

	spacer4 = Label(root, text='                          ', bg='black')
	spacer4.pack(side=LEFT)

	butroom = Button(root, text='ROOMS', bg='black', padx=50, pady=45, fg='white', bd=5, command=winroom)
	butroom.pack(side=LEFT)


winroom()




root.mainloop()
