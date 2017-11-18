import tkinter as tk

'''
top=tk.Tk()

A1=tk.Button(top, text='A1')
A2=tk.Button(top, text='A2')
B1=tk.Button(top, text='B1')
B2=tk.Button(top, text='B2')

A1.grid(row=0,column=0)
A2.grid(row=0,column=1)
B1.grid(row=1,column=0)
B2.grid(row=1,column=1)

top.mainloop()



'''

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.pack()
		self.create_widgets()

	def create_widgets(self):

		self.quit = tk.Button(self, text="QUIT", fg="red",
				      command=root.destroy)

		A1=tk.Button(self, text='A1')
		A2=tk.Button(self, text='A2')
		B1=tk.Button(self, text='B1')
		B2=tk.Button(self, text='B2')

		A1.grid(row=0,column=0)
		A2.grid(row=0,column=1)
		B1.grid(row=1,column=0)
		B2.grid(row=1,column=1)



	def say_hi(self):
		print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()





