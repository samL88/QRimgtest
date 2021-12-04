#!/usr/bin/env python

from jinja2 import Template 
from PIL import Image
import qrcode
import qrcode.image.svg
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import RadialGradiantColorMask

import pyqrcode
import subprocess

# QR_PATH_STYLE = {'fill': '#000000', 'fill-opacity': '1',
#                     'fill-rule': 'nonzero', 'stroke': 'none'}
# update fill color to red, # gold yellow #C3B66C

RED = (255, 0, 0)
DEEP_RED = (170, 0, 0)  # '#ae0909'
WHITE = (255, 255, 255)

lnurl = "LNURL1DP68GURN8GHJ7MR9VAJKUEPWD3HXY6T5WVHXXMMD9AKXUATJD3CZ7CTSDYHHVVF0D3H82UNV9UUNWVCE4EM6P"

# this works
lnurl_file = "images/lnurl.png"
pyqr = pyqrcode.create(lnurl)
pyqr.png(lnurl_file, scale=3, module_color=[255,255,255,255], background=[170, 0, 0])

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=0.5,
)

with open('templates/inlet_tiger_cut.svg', 'r') as f:
    templ = f.read()

#qr_code = "\"" + "qrcolor.svg" + "\""
qr_code = "\"" + "images/lnurl.png" + "\""
idnumber = "f7dfwer7a8cd43aabsdfs"
expires = "2022-03-15"
sats = "2500"

tm = Template(templ)
msg = tm.render(qrcode=qr_code, idnumber=idnumber, expires=expires, sats=sats)

output_svg = 'output.svg'
with open(output_svg, 'w') as f:
    res = f.write(msg)
    f.close()

output_png = 'output.png'
subprocess.run(['rsvg-convert', output_svg, '-o', output_png, '-w' , '600'], cwd=".")

# rsvg-convert output.svg -o output.png -w 600
subprocess.run(['open', output_png])