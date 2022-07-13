# vCard QR code generator

import qrcode  # docs found in https://pypi.org/project/qrcode/

# Initialize QRCOde class
qr = qrcode.QRCode(
    version=1,  # size of qr code
    box_size=10,  # change size of each box in the qr code (in px)
    border=5  # change the border size (in boxes)
)

# Add the data that the QR code will hold
qr.add_data('Some text')

# Compile the QR code data
qr.make(fit=True)  # fit argument is to avoid data overflow (keep at True)

# Make QR code image
img = qr.make_image(fill_color="black", back_color="white")  # fill_color: color of the boxes, back_color: background color

# Save QR code image in the output folder
img.save("output/some_file.png")