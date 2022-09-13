from django.shortcuts import render
from django.http import HttpResponse
from qr_generator.modules import qrcodegen, vcardgen

# Create your views here.
def index(request):
  return render(request, 'index.html')

def qr(request):
  # gather POST data
  first_name = request.POST['first_name']
  middle_name = request.POST['middle_name']
  last_name = request.POST['last_name']

  email = request.POST['email']
  phone = request.POST['phone']

  company = request.POST['company']
  position = request.POST['position']

  street = request.POST['street']
  city = request.POST['city']
  region = request.POST['region']
  postal_code = request.POST['postal_code']
  country = request.POST['country']

  website = request.POST['website']

  # create vCard
  vcard = vcardgen.create_vcard()

  vcardgen.add_vcard_name(vcard, first_name, middle_name, last_name)
  vcardgen.add_vcard_email(vcard, email)
  vcardgen.add_vcard_phone(vcard, phone)
  vcardgen.add_vcard_company(vcard, company, position)
  vcardgen.add_vcard_address(vcard, street, city, region, postal_code, country)
  vcardgen.add_vcard_website(vcard, website)

  vcard_output = vcardgen.output_vcard(vcard)

  # create QR code
  qr = qrcodegen.create_qr(1, 10, 5)
  qrcodegen.add_qr_content(qr, vcard_output)
  qrcodegen.compile_qr(qr)
  qr_img = qrcodegen.generate_qr(qr, 'black', 'white')

  response = HttpResponse(content_type='image/jpg')
  qr_img.save(response, 'JPEG')

  return response