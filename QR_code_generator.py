from tkinter import *
import qrcode
from PIL import Image, ImageTk
import os

root = Tk()
root.title("QR generator")
root.geometry("1000x550")
root.config(bg="#AE2321")
root.resizable(False, False)

# icon image
image_icon = PhotoImage(file="icon.png")
root.iconphoto(False, image_icon)

def generate():
    name = title.get()
    text = entry.get()
    qr = qrcode.make(text)
    qr.save("Qrcode/" + str(name) + ".png")

    # Check if the logo file exists
    logo_path = "pb.png"
    if not os.path.exists(logo_path):
        print(f"Error: File not found - {logo_path}")
        return

    # Create QR code without logo
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Add logo to QR code
    logo = Image.open(logo_path)
    img.paste(logo, (int((img.size[0] - logo.size[0]) / 2), int((img.size[1] - logo.size[1]) / 2)))

    img.save("Qrcode/" + str(name) + ".png")

    # Display the QR code with logo
    global QRImage
    QRImage = ImageTk.PhotoImage(file="Qrcode/" + str(name) + ".png")
    Image_view.config(image=QRImage)


Image_view = Label(root, bg="#AE2321")
Image_view.pack(padx=50, pady=10, side=RIGHT)

Label(root, text="Title", fg="white", bg="#AE2321", font=15).place(x=50, y=170)

title = Entry(root, width=13, font="arial 15")
title.place(x=50, y=200)

entry = Entry(root, width=28, font="arial 15")
entry.place(x=50, y=250)

Button(root, text="GENERATE", width=20, height=2, bg="black", fg="white", command=generate).place(x=50, y=300)

root.mainloop()
