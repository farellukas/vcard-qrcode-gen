# QR code generator

import qrcode  # docs found in https://pypi.org/project/qrcode/

# Initialize QRCOde class
def create_qr(qr_size, box_size, border_size):
    return qrcode.QRCode(
        version=qr_size,  # size of qr code
        box_size=box_size,  # change size of each box in the qr code (in px)
        border=border_size  # change the border size (in boxes)
    )

# Add the data that the QR code will hold
def add_qr_content(qr, qr_content):
    qr.add_data(qr_content)

# Compile the QR code data
def compile_qr(qr):
    qr.make(fit=True)  # fit argument is to avoid data overflow (keep at True)

# Make QR code image
def generate_qr(qr, fore_color, back_color):
    return qr.make_image(fill_color=fore_color, back_color=back_color)  # fill_color: color of the boxes, back_color: background color

# Save QR code image in the output folder
def save_qr_img(qr_img, file_name, folder=""):
    if folder == "":
        path = file_name
    else:
        path = folder + "/" + file_name

    qr_img.save(path + ".png")