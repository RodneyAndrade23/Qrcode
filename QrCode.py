import qrcode

qr = qrcode.QRCode(None,
                   qrcode.ERROR_CORRECT_H)
qr.add_data('https://static.vasco.com.br/wp-content/uploads/2021/08/detalhes-site06-1024x576.png')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save('qrcode-site.png')

