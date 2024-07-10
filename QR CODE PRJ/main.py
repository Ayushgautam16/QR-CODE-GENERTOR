import qrcode as qr
img= qr.make("https://www.linkedin.com/in/ayush-gautam-9baa14248?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3B4c5TkR0kTD%2BC0ij4DYeDXw%3D%3D")

img.save("Ayush Gautam linkedin profile.png")

print("QR code image saved successfully.")