import tkinter as tk

class interface:
	def __init__(self):
		
		self.backgroundcolor='white'
		
		####Window
		self.window=tk.Tk()
		self.window.title('Le joli bout de bois')
		self.window.geometry('750x750')

		####mainframe
		self.mainFrame=tk.Frame(self.window,bg='green')
		self.mainFrame.pack(fill="both",expand=True)
		
		self.mainFrame.grid_columnconfigure(0,weight=1,uniform="group1")
		self.mainFrame.grid_columnconfigure(1,weight=1,uniform="group1")
		self.mainFrame.grid_rowconfigure(0,weight=1,uniform="group2")

		
		####frame de gauche
		self.leftFrame=tk.Frame(self.mainFrame,bg='pink')
		self.leftFrame.grid(row=0,column=0,sticky='nsew')

		self.leftFrame.grid_columnconfigure(0,weight=1,uniform="group1")
		self.leftFrame.grid_columnconfigure(1,weight=4,uniform="group1")
		self.leftFrame.grid_columnconfigure(2,weight=1,uniform="group1")
		self.leftFrame.grid_columnconfigure(3,weight=1,uniform="group1")
		#self.leftFrame.grid_columnconfigure(4,weight=1,uniform="group1")
		#self.leftFrame.grid_columnconfigure(5,weight=4,uniform="group1")
		#self.leftFrame.grid_columnconfigure(6,weight=1,uniform="group1")
		#self.leftFrame.grid_columnconfigure(7,weight=1,uniform="group1")
		#self.leftFrame.grid_columnconfigure(8,weight=1,uniform="group1")
		#self.leftFrame.grid_columnconfigure(9,weight=1,uniform="group1")
		#self.leftFrame.grid_columnconfigure(10,weight=1,uniform="group1")
		#self.leftFrame.grid_columnconfigure(11,weight=1,uniform="group1")
		#self.leftFrame.grid_columnconfigure(12,weight=1,uniform="group1")
		#self.leftFrame.grid_columnconfigure(13,weight=1,uniform="group1")
		#self.leftFrame.grid_columnconfigure(14,weight=1,uniform="group1")

		self.leftFrame.grid_rowconfigure(0,weight=1,uniform="group2")
		self.leftFrame.grid_rowconfigure(1,weight=1,uniform="group2")
		self.leftFrame.grid_rowconfigure(2,weight=1,uniform="group2")
		self.leftFrame.grid_rowconfigure(3,weight=1,uniform="group2")
		self.leftFrame.grid_rowconfigure(4,weight=1,uniform="group2")
		self.leftFrame.grid_rowconfigure(5,weight=1,uniform="group2")
		self.leftFrame.grid_rowconfigure(6,weight=1,uniform="group2")
		self.leftFrame.grid_rowconfigure(7,weight=1,uniform="group2")
		self.leftFrame.grid_rowconfigure(8,weight=1,uniform="group2")
		self.leftFrame.grid_rowconfigure(9,weight=1,uniform="group2")
		self.leftFrame.grid_rowconfigure(10,weight=1,uniform="group2")
		self.leftFrame.grid_rowconfigure(11,weight=1,uniform="group2")
		self.leftFrame.grid_rowconfigure(12,weight=1,uniform="group2")
		self.leftFrame.grid_rowconfigure(13,weight=1,uniform="group2")
		self.leftFrame.grid_rowconfigure(14,weight=1,uniform="group2")


		
		###Les labels et entrys
		##enemies mineurs
		#label gauche
		self.labelEmineur=tk.Label(self.leftFrame,text="Enemies mineurs",font=('Helvetica', 15),bg=self.backgroundcolor)
		self.labelEmineur.grid(row=0,column=1,sticky='nsew')
		#entry
		self.entryEmineur=tk.Entry(self.leftFrame,bg=self.backgroundcolor)
		self.entryEmineur.grid(row=0,column=2,sticky='nsew')
		

		##enemies normaux
		#label gauche
		self.labelEnormal=tk.Label(self.leftFrame,text="Enemies normaux",font=('Helvetica', 15),bg=self.backgroundcolor)
		self.labelEnormal.grid(row=2,column=1,sticky='nsew')
		#entry
		self.entryEnormal=tk.Entry(self.leftFrame,bg=self.backgroundcolor)
		self.entryEnormal.grid(row=2,column=2,sticky='nsew')

		##enemies majeurs
		#label gauche
		self.labelEmajeur=tk.Label(self.leftFrame,text="Enemies majeurs",font=('Helvetica', 15),bg=self.backgroundcolor)
		self.labelEmajeur.grid(row=4,column=1,sticky='nsew')
		#entry
		self.entryEmajeur=tk.Entry(self.leftFrame,bg=self.backgroundcolor)
		self.entryEmajeur.grid(row=4,column=2,sticky='nsew')

		##Petit Cache
		#label gauche
		self.labelPetitCache=tk.Label(self.leftFrame,text="Petit cache",font=('Helvetica', 15),bg=self.backgroundcolor)
		self.labelPetitCache.grid(row=6,column=1,sticky='nsew')
		#entry
		self.entryPetitCache=tk.Entry(self.leftFrame,bg=self.backgroundcolor)
		self.entryPetitCache.grid(row=6,column=2,sticky='nsew')

		##Petit tresor
		#label gauche
		self.labelTpetit=tk.Label(self.leftFrame,text="Petit trésors",font=('Helvetica', 15),bg=self.backgroundcolor)
		self.labelTpetit.grid(row=8,column=1,sticky='nsew')
		#entry
		self.entryTpetit=tk.Entry(self.leftFrame,bg=self.backgroundcolor)
		self.entryTpetit.grid(row=8,column=2,sticky='nsew')

		##trésors
		#label gauche
		self.labelT=tk.Label(self.leftFrame,text="Trésors",font=('Helvetica', 15),bg=self.backgroundcolor)
		self.labelT.grid(row=10,column=1,sticky='nsew')
		#entry
		self.entryT=tk.Entry(self.leftFrame,bg=self.backgroundcolor)
		self.entryT.grid(row=10,column=2,sticky='nsew')

		##grand trésors
		#label gauche
		self.labelTgrand=tk.Label(self.leftFrame,text="Enemies normaux",font=('Helvetica', 15),bg=self.backgroundcolor)
		self.labelTgrand.grid(row=12,column=1,sticky='nsew')
		#entry
		self.entryTgrand=tk.Entry(self.leftFrame,bg=self.backgroundcolor)
		self.entryTgrand.grid(row=12,column=2,sticky='nsew')

		##Bouton Loot

		photo = tk.PhotoImage(file='imageCoffre.gif')
		self.boutonLoot=tk.Button(self.leftFrame,image=photo,highlightbackground=self.backgroundcolor)
		self.boutonLoot.grid(row=13,rowspan=2,column=1,columnspan=2,sticky='nsew')


		####frame de Droite
		self.rightFrame=tk.Frame(self.mainFrame,bg='blue')
		self.rightFrame.grid(row=0,column=1,sticky='nsew')
		
		self.labelrightFrameloot=tk.Label(self.rightFrame,text="Loot obtenus",font=('Helvetica', 45),bg=self.backgroundcolor)
		self.labelrightFrameloot.pack(side='top')

		######TEST########
		self.labelrightFrameloot1=tk.Label(self.rightFrame,text="Loot obtenus",font=('Helvetica', 15),bg=self.backgroundcolor)
		self.labelrightFrameloot1.pack()
		self.labelrightFrameloot2=tk.Label(self.rightFrame,text="Loot obtenus",font=('Helvetica', 15),bg=self.backgroundcolor)
		self.labelrightFrameloot2.pack()
		self.labelrightFrameloot3=tk.Label(self.rightFrame,text="Loot obtenus",font=('Helvetica', 15),bg=self.backgroundcolor)
		self.labelrightFrameloot3.pack()

				


		self.window.mainloop()
		

a=interface()
