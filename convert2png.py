# -*- coding: utf-8 -*-
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

# doesn't work too well with QR codes
drawing = svg2rlg('qr.svg')
renderPM.drawToFile(drawing, 'outqr.png', fmt='PNG')