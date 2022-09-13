# vCard generator

import vobject # docs found in https://pypi.org/project/vobject/ and vCard 3.0 format in https://www.evenx.com/vcard-3-0-format-specification or https://datatracker.ietf.org/doc/html/rfc6350

# create vCard instance
def create_vcard():
    return vobject.vCard()

# add name (requried) and formatted name (required)
def add_vcard_name(vcard, first, middle, last):
    vcard.add('n')
    if middle == "":
        given_names = first
    else:
        given_names = first + " " + middle
    vcard.n.value = vobject.vcard.Name( family=last, given=first, additional=middle )

    vcard.add('fn')
    vcard.fn.value = f"{given_names} {last}"

# add email
def add_vcard_email(vcard, email):
    vcard.add('email')
    vcard.email.value = email
    vcard.email.type_param = 'INTERNET'  # parameter types for vCard

# add company
def add_vcard_company(vcard, company, position):
    vcard.add('org')
    temp = []
    temp.append(company)
    temp.append(position)
    vcard.org.value = temp

# add address
def add_vcard_address(vcard, street, city, region, postal_code, country):
    vcard.add('adr')
    vcard.adr.value = vobject.vcard.Address(street, city, region, postal_code, country)

# add phone
def add_vcard_phone(vcard, phone):
    vcard.add('tel')
    vcard.tel.value = phone
    vcard.tel.type_param = 'WORK'

# add website
def add_vcard_website(vcard, website):
    vcard.add('url')
    vcard.url.value = website

# create vCard string
def output_vcard(vcard):
    return vcard.serialize()