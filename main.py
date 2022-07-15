# vCard QR Code Generator

from modules import qrcodegen, vcardgen

def main():
    first_name = input("Enter contact's first name: ")
    middle_name = input("Enter contact's middle names (if any): ")
    last_name = input("Enter contact's last name: ")

    email = input("Enter contact's email: ")

    phone = input("Enter contact's phone number: ")

    company = input("Enter contact's company: ")
    position = input("Enter contact's position: ")

    street = input("Enter contact's street: ")
    city = input("Enter contact's city: ")
    region = input("Enter contact's region: ")
    postal_code = input("Enter contact's postal code: ")
    country = input("Enter contact's country: ")

    website = input("Enter contact's website: ")

    if middle_name == "":
        full_name = f"{first_name} {last_name}"
    else:
        full_name = f"{first_name} {middle_name} {last_name}"

    vcard = vcardgen.create_vcard()

    vcardgen.add_vcard_name(vcard, first_name, middle_name, last_name)
    vcardgen.add_vcard_email(vcard, email)
    vcardgen.add_vcard_phone(vcard, phone)
    vcardgen.add_vcard_company(vcard, company, position)
    vcardgen.add_vcard_address(vcard, street, city, region, postal_code, country)
    vcardgen.add_vcard_website(vcard, website)

    vcard_output = vcardgen.output_vcard(vcard)

    qr = qrcodegen.create_qr(1, 10, 5)
    qrcodegen.add_qr_content(qr, vcard_output)
    qrcodegen.compile_qr(qr)
    qr_img = qrcodegen.generate_qr(qr, 'black', 'white')
    qrcodegen.save_qr_img(qr_img, full_name, "output")


main()