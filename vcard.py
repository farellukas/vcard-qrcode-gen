# vCard generator

import vobject # docs found in https://pypi.org/project/vobject/ and vCard 3.0 format in https://www.evenx.com/vcard-3-0-format-specification

# create vCard instance
vcard_obj = vobject.vCard()

# add name (requried)
vcard_obj.add('n')
vcard_obj.n.value = vobject.vcard.Name( family='Doe', given='John' )

# add formatted name (required)
vcard_obj.add('fn')
vcard_obj.fn.value = 'John Doe'

# create vCard string
vcard_str = vcard_obj.serialize()