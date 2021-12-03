#from PIL import Image
import qrcode
import qrcode.image.svg
#from qrcode.image.styledpil import StyledPilImage
#from qrcode.image.styles.colormasks import RadialGradiantColorMask

RED = (255, 0, 0)
DEEP_RED = (170, 0, 0)
WHITE = (255, 255, 255)

lnurl = "LNURL1DP68GURN8GHJ7MR9VAJKUEPWD3HXY6T5WVHXXMMD9AKXUATJD3CZ7CTSDYHHVVF0D3H82UNV9UUNWVCE4EM6P"

# 30% or greater error conversion
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data(lnurl)

factory = qrcode.image.svg.SvgPathImage
svg_img = qrcode.make(lnurl, image_factory=factory)
svg_img.save('qrred.svg')


#QRimg = qr.make_image(image_factory=StyledPilImage, 
#                     color_mask=RadialGradiantColorMask(back_color=WHITE, 
#                     center_color=DEEP_RED, edge_color=DEEP_RED))
#QRimg.save('images/red_lnurl.png')
#QRimg.show()
