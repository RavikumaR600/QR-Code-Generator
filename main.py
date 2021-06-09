import qrcode
qr=qrcode.QRCode(
    version= 1,
    box_size=50,
    border=5
)
data = "hello this is qr code"
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black",back_color="white")
img.save("1.png")