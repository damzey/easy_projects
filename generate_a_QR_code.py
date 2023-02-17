import qrcode
import time
import os

def delay():
    time.sleep(2)

def create_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

cwd = os.getcwd()

print()
print('Welcome to this Python program, where you will be creating your own QR code.',end =' ')
print('The first example is auto-generated')
time.sleep(1)

website_link = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
qr.add_data(website_link)
qr.make()
img = qr.make_image(fill_color = 'black', back_color = 'white')
create_folder(cwd+"\\qrcodes")
img.save('qrcodes\\youtube_qr.png')

print('The auto-generated code is now created and has been stored in the "qrcodes" folder')
delay()
print()
print('Time to create your own QR code..')
delay()

website_link = input('Please type the link you want to make a QR code for: ')
version = int(input('Please input the size of the QR code. Values range from 1-40: '))
box_size = int(input('Please enter how many pixels you want each "box" in the QR code to have: '))
border = int(input('Please enter how thick (in terms of boxes) do you want the border to be: '))
fill_color = input('Please enter what color you want the line color to be: ')
back_color = input('Please enter what color you want to set the background to: ')

delay()

requested_qr = qrcode.QRCode(version = version, box_size = box_size, border = border)
requested_qr.add_data(website_link)
requested_qr.make(fit=True)
new_img = qr.make_image(fill_color = fill_color, back_color = back_color)
create_folder(cwd+"\\qrcodes")
new_img.save('qrcodes\\requested_qrcode.png')
