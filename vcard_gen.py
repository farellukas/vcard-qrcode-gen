# vCard generator

import vobject # docs found in https://pypi.org/project/vobject/ and vCard 3.0 format in https://www.evenx.com/vcard-3-0-format-specification

# create vCard instance
def create_vcard():
    return vobject.vCard()

# add name (requried) and formatted name (required)
def add_vcard_name(vcard, first, middle, last):
    vcard.add('n')
    given_names = first + " " + middle
    vcard.n.value = vobject.vcard.Name( family=last, given=given_names )

    vcard.add('fn')
    vcard.fn.value = f"{first} {middle} {last}"

# create vCard string
def output_vcard(vcard):
    return vcard.serialize()