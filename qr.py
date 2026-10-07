import qrcode
text = input("Text or URL: ")
img = qrcode.make(text)
img.save("qr_code.png")
print("Saved as qr_code.png")
