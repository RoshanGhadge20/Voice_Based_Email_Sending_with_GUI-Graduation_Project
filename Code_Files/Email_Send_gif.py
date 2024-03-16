
import tkinter as tk
import PIL
from PIL import ImageTk
from PIL import Image


def Mail_send_gif():
    look=tk.Tk()
    look.geometry("500x500")
    look.title("EMAIL_SEND_SUCCESSFULLY")
    img_file="email1.gif"
    info=PIL.Image.open(img_file)
    frames=info.n_frames  # to calculate the total number os frames into the images their are total 115 frames in gif image
    #print(frames)  #to show the frames
    im=[tk.PhotoImage(file=img_file,format=f"gif -index {i}") for i in range(frames)]
    #print("hello  hi")
    anim=None
    count=0
    def animation(count):
        global anim
        im2=im[count]
        gif_label.configure(image=im2)
        count+=1
        if count==frames:
            count=0
            #animation(count)
        anim=look.after(50,lambda :animation(count))

    gif_label=tk.Label(look,image="")
    gif_label.pack()

    animation(count)


    look.mainloop()

