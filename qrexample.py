import pyqrcode
from PIL import Image

# lnurl = "LNURL1DP68GURN8GHJ7MR9VAJKUEPWD3HXY6T5WVHXXMMD9AKXUATJD3CZ7CTSDYHHVVF0D3H82UNV9UUNGDC6YFG49"
lnurl ="LNURL1DP68GURN8GHJ7MR9VAJKUEPWD3HXY6T5WVHXXMMD9AKXUATJD3CZ7CTSDYHHVVF0D3H82UNV9UUNWVCE4EM6P"

lnurl = "LNURL1DP68GUP69UHKCMMRV9KXSMMNWSAR2VPSXQHKCMN4WFK8QTMPWP5J7A339AKXUATJDSHNZY2859U"

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data(lnurl)

img_1 = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
img_2 = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask())
img_2.save('lnurl.png')

#url = pyqrcode.QRCode(lnurl,error = 'H')
#url.png('lnurl.png',scale=10)

im = Image.open('lnurl.png')
im = im.convert("RGBA")
logo = Image.open('logo.png')
box = (220,220,320,320)
im.crop(box)
region = logo
region = region.resize((box[2] - box[0], box[3] - box[1]))
im.paste(region,box)
im.show()
