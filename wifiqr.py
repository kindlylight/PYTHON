import qrcode
img = qrcode.make('p
rakash pariyar')

###WIFI LINK
wifi_type = 'WPA'
wifi_ssid = "DIFICOM"
wifi_password = 'P@55w0rd!'
wifi= f"WIFI:T: {wifi_type};S:{wifi_ssid};P:{wifi_password};;"
img= qrcode.make(wifi)
type(img)  # qrcode.image.pil.PilImage
img.save("Prakashimg.png")