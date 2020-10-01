# Image Copy Deleter
# 18.09.2020  03:56
# @fkvd

import os
from tkinter import *
from tkinter import filedialog, ttk, messagebox
from PIL import Image

##### Functions ######
def CID(folder):
	imageAndSize = []
	liste = []

	# Get filename and size
	for file in os.listdir(folder):
		if file.endswith('.'+extension.get()):
			path = os.path.join(folder, file)
			size = os.path.getsize(path)
			liste = [path,size]
			imageAndSize.append(liste)

	# Sort images by their size		
	imageAndSize.sort( key=lambda x: x[1])			

	# Get filename of files that has same size
	# and same pixel value for arbitrary position
	sameSize=[]

	for i in range(len(imageAndSize)-1):
		if(imageAndSize[i][1] == imageAndSize[i+1][1]):		# Check file size
			im1 = Image.open(imageAndSize[i][0])
			im2 = Image.open(imageAndSize[i+1][0])
			if(im1.size==im2.size):							# Check pixel size
				X,Y = im1.size
				pix1 = im1.load()
				pix2 = im2.load()
				if(pix1[0,0]==pix2[0,0] and pix1[X/8,Y/8]==pix2[X/8,Y/8] and \
				   pix1[X/4,Y/4]==pix2[X/4,Y/4] and pix1[X/2,Y/2]==pix2[X/2,Y/2]):
					sameSize.append(imageAndSize[i])

			
	sameSizeLength = str(len(sameSize))

	# Delete copy images
	for i in range(int(sameSizeLength)):
		os.remove(sameSize[i][0])
	
	return sameSizeLength


def clicked():
	window.withdraw()
	try:
		folder_selected = filedialog.askdirectory()
		numberOfCopy = CID(folder_selected)
		messagebox.showinfo('Copy Image Deleter', str(numberOfCopy)+' copy images are deleted.')
	except:
		pass
	window.deiconify()


##### Graphical User Interface #####

window = Tk()
try:								#In case of missing icon file
	window.iconbitmap('icon.ico')
except:
	pass
window.title("Copy Image Deleter")
window.geometry('350x150')
window.resizable(False, False)

n = StringVar() 
extension = ttk.Combobox(window, state="readonly", width = 5, textvariable = n) 
extension['values'] = ('png', 'jpg', 'jpeg') 
extension.grid(column = 0, row = 0, padx=(70,10) , pady=50) 
extension.current(1) 

btn = Button(window, text="Select Folder", command=clicked)
btn.grid(column=1, row=0, padx=0, pady = 0)

window.mainloop()