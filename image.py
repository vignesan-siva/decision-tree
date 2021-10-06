import tkinter
from PIL import Image,ImageTk
window=tkinter.Tk()
widget=tkinter
img1=Image.open("D:\\real estate project\\city-hospital-building-flat-style-260nw-237369187.jpg")
img=ImageTk.PhotoImage(img1)



label1=widget.Label()
label1.pack()
label1.place(x=50,y=50)
label1.configure(image=img)
button1=widget.Button()
button1.pack()
button1.configure(text="SELECT",font=("Arial",27,'bold'),fg="white",relief="groove",bd=0,activebackground="white",activeforeground="#008F96",bg="#008F96")
button1.place()
#creating window frame
window.title("SHOP MONITORING")
window.geometry("1200x720+10+10")
window.configure(bg="WHITE")
window.mainloop()

