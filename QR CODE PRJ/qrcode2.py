import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data('https://www.linkedin.com/in/ayush-gautam-9baa14248?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3B4c5TkR0kTD%2BC0ij4DYeDXw%3D%3D')
qr.make(fit=True)

img = qr.make_image(fill_color='blue', back_color='white')

img.save('linkedin_qr.png')
