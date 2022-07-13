# vCard QR Code Generator

import qrcodegen, vcardgen

def main():
    first_name = input("Enter contact's first name: ")
    middle_name = input("Enter contact's middle names (if any): ")
    last_name = input("Enter contact's last name: ")

    if middle_name == "":
        full_name = f"{first_name} {last_name}"
    else:
        full_name = f"{first_name} {middle_name} {last_name}"

    vcard = vcardgen.create_vcard()

    vcardgen.add_vcard_name(vcard, first_name, middle_name, last_name)
    vcard_output = vcardgen.output_vcard(vcard)

    qr = qrcodegen.create_qr(1, 10, 5)
    qrcodegen.add_qr_content(qr, vcard_output)
    qrcodegen.compile_qr(qr)
    qr_img = qrcodegen.generate_qr(qr, 'black', 'white')
    qrcodegen.save_qr_img(qr_img, full_name, "output")


main()