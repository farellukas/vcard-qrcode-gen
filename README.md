# vcard-qrcode-gen
A python-based vCard QR code generator with web interface support

## Setup
1. Install the python 3.9 from https://www.python.org/ 
2. Clone this repository and using the terminal, `cd` to the directory
3. Run `pip install -r requirements.txt` to install the required dependencies

## Usage
### CLI
1. Make a new directory called "output" (this is where all the QR codes will be generated)
2. Run `python main.py` to start the program
3. Fill in the desired fields (any required fields are labelled with (required))
4. Once finished, the QR code will be generated in the "output" folder

### Web UI
1. `cd` to the directory `VCardMaker`
2. Run `python manage.py runserver` to start the web application
3. Open the web application in the browser at http://localhost:8000
4. Fill in the desired fields (any required fields are labelled with *)
5. Once finished, the QR code will be generated in next webpage (right click > save image, to save the image in your local computer)