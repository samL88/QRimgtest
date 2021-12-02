from PIL import Image
import qrcode
import qrcode.image.svg
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import RadialGradiantColorMask
# from qrcode.image.styles.moduledrawers import RoundedModuleDrawer

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
DEEP_RED = (170, 0, 0)
TEAL = (0, 255, 255)
BLUE = (0, 0, 255)
GREY = (80,80,80)
#GREY = (35,35,35)
LTGREY = (150,150,150)
YELLOW = (255, 255, 0)
ORANGE = (255, 125, 0)
L_YELLOW = (195,182,108)
D_YELLOW = (142, 116, 56)

lnurl = "LNURL1DP68GURN8GHJ7MR9VAJKUEPWD3HXY6T5WVHXXMMD9AKXUATJD3CZ7CTSDYHHVVF0D3H82UNV9UUNWVCE4EM6P"

# 30% or greater error conversion
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data(lnurl)

factory = qrcode.image.svg.SvgPathImage
svg_img = qrcode.make(lnurl, image_factory=factory)
# make qr svg red color
svg_img.save('qr.svg')


QRimg = qr.make_image(image_factory=StyledPilImage, 
                     color_mask=RadialGradiantColorMask(back_color=WHITE, 
                     center_color=DEEP_RED, edge_color=DEEP_RED))
QRimg.save('images/lnurl.png')

logo = Image.open('images/grey_logo.png')
basewidth = 100

# adjust image size
wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)

# set size of QR code
pos = ((QRimg.size[0] - logo.size[0]) // 2,
       (QRimg.size[1] - logo.size[1])// 2)

QRimg.paste(logo, pos)
QRimg.save('output.png')
QRimg.show()
