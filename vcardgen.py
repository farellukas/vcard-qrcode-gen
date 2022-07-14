# vCard generator

import vobject # docs found in https://pypi.org/project/vobject/ and vCard 3.0 format in https://www.evenx.com/vcard-3-0-format-specification

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
    vcard.n.value = vobject.vcard.Name( family=last, given=given_names )

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
    vcard.org.type_param = ''

# add address
def add_vcard_address(vcard, street, locality, region, postal_code):
    vcard.add('adr')
    address = f'{street};{locality};{region};{postal_code}'
    vcard.adr.value = address
    vcard.adr.type_param = 'dom,work'

# add phone
def add_vcard_phone(vcard, phone):
    vcard.add('tel')
    vcard.tel.value = phone
    vcard.tel.type_param = 'WORK'

# create vCard string
def output_vcard(vcard):
    return vcard.serialize()