#from PIL import Image
import qrcode
import qrcode.image.svg
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import RadialGradiantColorMask

RED = (255, 0, 0)
DEEP_RED = (170, 0, 0)
WHITE = (255, 255, 255)

lnurl = "LNURL1DP68GURN8GHJ7MR9VAJKUEPWD3HXY6T5WVHXXMMD9AKXUATJD3CZ7CTSDYHHVVF0D3H82UNV9UUNWVCE4EM6P"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# 30% or greater error conversion
#qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data(lnurl)
qr.make(fit=True)

factory = qrcode.image.svg.SvgPathImage

# QR_PATH_STYLE = {'fill': '#000000', 'fill-opacity': '1',
#                     'fill-rule': 'nonzero', 'stroke': 'none'}

# update fill color to red, # gold yellow #C3B66C

red = '#ae0909'
yellow = '#C3B66C'
black = '#000000'

factory.QR_PATH_STYLE['fill'] = black
print(factory.QR_PATH_STYLE['fill'])

svg_img = qrcode.make(lnurl, image_factory=factory)
svg_img.save('qrred.svg')

#QRimg = qr.make_image(image_factory=StyledPilImage, 
#                     color_mask=RadialGradiantColorMask(back_color=WHITE, 
#                     center_color=DEEP_RED, edge_color=DEEP_RED))
#QRimg.save('images/red_lnurl.png')
#QRimg.show()
