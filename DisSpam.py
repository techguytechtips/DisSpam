from tkinter import *
import pyautogui
import time
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
		
		runButton = Button(self, text="Spam!", command=self.spam, fg='blue', bg='green')
		runButton.place(x=155, y=210)
	def spam(self):
		global i
		if box.get() == 1:
			l = i.get()
			g = 1
			time.sleep(5)
			while g <= l:
				time.sleep(0.9)
				pyautogui.typewrite("@" + (tag.get()), interval=0)
				pyautogui.typewrite(['enter'])
				pyautogui.typewrite(['enter'])
				g += (1)
		elif box.get() == 0:
			l = i.get()
			g = 1
			time.sleep(5)
			while g <= l:
				pyautogui.typewrite("@" + (tag.get()), interval=0)
				pyautogui.typewrite(['enter'])
				pyautogui.typewrite(['enter'])
				g += (1)
root = Tk()

tag = StringVar()

box = IntVar()

i = IntVar()

root.geometry("400x295")

root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='myicon.gif'))

app = Window(root)

label = Label(root, text = "DisSpam by TechGuyTechTips", font=("bold", 10),fg="darkred").pack()

label1 = Label(root, text="Enter Discord Tag: @", font=("arial",12, "bold"), fg="black").place(x=15, y=25)

label2 = Label(root, text="Enter Number of Pings: ", font=("arial",12, "bold"), fg="black").place(x=17, y=60)

label3 = Label(root, text="You Dont have too use full username.", font=("arial",10, "bold"), fg="red").place(x=17, y=150)

label4 = Label(root, text="You have 5 seconds to get back into discord before it starts pinging.", font=("arial",8, "bold"), fg="red").place(x=17, y=170)

entry_box = Entry(root, textvariable=(tag), width=25, bg="red").place(x=180, y=25)

entry_box = Entry(root, textvariable=i, width=3, bg="red").place(x=207, y=60)

Checkbutton(root, text="Bypass Anti-spam", variable=box).place(x=200, y=100)

root.mainloop()
