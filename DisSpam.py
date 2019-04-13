from tkinter import *
import pyautogui
import time
import threading
from PIL import ImageTk, Image
class Window(Frame):                   
	def __init__(self, master = None):
		Frame.__init__(self, master)
		self.master = master
		
		self.init_window()
		#fm = Frame(master, width=400, height=296, bg="#2C2F33")
		#fm.pack(side=TOP, expand=NO, fill=NONE)
		
		
	def init_window(self):
		self.master.title("DisSpam")
		self.pack(fill=BOTH, expand=1)
		
		runButton = Button(self, text="Spam!", command=self.spam, fg='#99AAB5', bg='#23272A')
		runButton.place(x=155, y=210)
		runButton2 = Button(self, text="Stop", command=self.stap, fg='#23272A', bg='red')
		runButton2.place(x=335, y=225)
	def stap(self):
		global stp
		stp = 1
		stp += 1
	def spam(self):
		global stp
		global i
		stp = 1
		if box.get() == 1 and at.get() == 1 and infinite.get() == 0:
			l = i.get()
			g = 1
			time.sleep(5)
			while g <= l:
				root.update()
				if stp != 1:
					break
					stp = 1
				root.update()
				time.sleep(0.9)
				root.update()
				pyautogui.typewrite("@" + (tag.get()), interval=0)
				pyautogui.typewrite(['enter'])
				pyautogui.typewrite(['enter'])
				root.update()
				g += (1)
		elif box.get() == 0 and at.get() == 0 and infinite.get() == 0:
			l = i.get()
			g = 1
			time.sleep(5)
			while g <= l:
				root.update()
				if stp != 1:
					break
					stp = 1
				root.update()
				pyautogui.typewrite((tag.get()), interval=0)
				pyautogui.typewrite(['enter'])
				pyautogui.typewrite(['enter'])
				root.update()
				g += (1)
		elif box.get() == 1 and at.get() == 0 and infinite.get() == 0:
			l = i.get()
			g = 1
			time.sleep(5)
			while g <= l:
				root.update()
				if stp != 1:
					break
					stp = 1
				root.update()
				time.sleep(0.9)
				root.update()
				pyautogui.typewrite((tag.get()), interval=0)
				pyautogui.typewrite(['enter'])
				pyautogui.typewrite(['enter'])
				root.update()
				g += (1)
		elif box.get() == 0 and at.get() == 1 and infinite.get() == 0:
			while g <= l:
				root.update()
				if stp != 1:
					break
					stp = 1
				root.update()
				pyautogui.typewrite("@" + (tag.get()), interval=0)
				pyautogui.typewrite(['enter'])
				pyautogui.typewrite(['enter'])
				root.update()
				g += (1)
		elif box.get() == 1 and at.get() == 1 and infinite.get() == 1:
			time.sleep(5)#2C2F33
			while(True):
				root.update()
				if stp != 1:
					break
					stp = 1
				root.update()
				time.sleep(0.9)
				root.update()
				pyautogui.typewrite("@" + (tag.get()), interval=0)
				pyautogui.typewrite(['enter'])
				pyautogui.typewrite(['enter'])
				root.update()
				
		elif box.get() == 0 and at.get() == 0 and infinite.get() == 1:
			time.sleep(5)
			while(True):
				root.update()
				if stp != 1:
					break
					stp = 1
				root.update()
				pyautogui.typewrite((tag.get()), interval=0)
				pyautogui.typewrite(['enter'])
				pyautogui.typewrite(['enter'])
				root.update()
		elif box.get() == 1 and at.get() == 0 and infinite.get() == 1:
			time.sleep(5)
			while(True):
				root.update()
				if stp != 1:
					break
					stp = 1
				root.update()
				time.sleep(0.9)
				root.update()
				pyautogui.typewrite((tag.get()), interval=0)
				pyautogui.typewrite(['enter'])
				pyautogui.typewrite(['enter'])
				root.update()
		elif box.get() == 0 and at.get() == 1 and infinite.get() == 1:
			time.sleep(5)
			while(True):
				root.update()
				if stp != 1:
					break
					stp = 1
				root.update()
				pyautogui.typewrite("@" + (tag.get()), interval=0)
				pyautogui.typewrite(['enter'])
				pyautogui.typewrite(['enter'])
				root.update()
root = Tk()


tag = StringVar()

box = IntVar()

at = IntVar()

i = IntVar()

infinite = IntVar()

root.geometry("400x295")
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='myicon.gif'))

app = Window(root)

label = Label(root, text = "DisSpam by TechGuyTechTips", font=("bold", 10),fg="darkred").pack()

label1 = Label(root, text="Enter Discord Tag:", font=("arial",12, "bold"), fg="black").place(x=17, y=27)

label2 = Label(root, text="Enter Number of Pings: ", font=("arial",12, "bold"), fg="black").place(x=17, y=60)

label3 = Label(root, text="You Dont have too use full username.", font=("arial",10, "bold"), fg="red").place(x=17, y=150)

label4 = Label(root, text="You have 5 seconds to get back into discord before it starts pinging.", font=("arial",8, "bold"), fg="red").place(x=17, y=170)

entry_box = Entry(root, textvariable=(tag), width=25, bg="#7289DA").place(x=180, y=25)

entry_box = Entry(root, textvariable=i, width=3, bg="#7289DA").place(x=207, y=60)

Checkbutton(root, text="Bypass Anti-spam", variable=box).place(x=200, y=90)

Checkbutton(root, text="Include @ sign", variable=at).place(x=50, y=90)

Checkbutton(root, text="Infinite pings", variable=infinite).place(x=125, y=126)

root.mainloop()
