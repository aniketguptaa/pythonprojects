import qrcode
image = qrcode.make("https://www.droplets.ml")
image.save("qrcode.png", "PNG")