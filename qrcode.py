###QR Code Generator

import qrcode
img = qrcode.make('PRAKASH PARIYAR')
type(img)  # qrcode.image.pil.PilImage
img.save("Prakashimg.png")