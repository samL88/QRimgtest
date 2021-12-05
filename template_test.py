#!/usr/bin/env python

from jinja2 import Template 
import pyqrcode
import subprocess
import base64

'''
EDIT YOUR TEMPLATE FILE 
to refer to lnurl_file and qr_code, idnumber, expires and sats
with {{ }}

example: {{sats}}

'''

def create_laisee_qrcode(lnurl: str, idnumber: str, expires: str, sats: str, template_file: str):

    try:
        lnurl_file = "images/lnurl_" + idnumber + ".png" # make this id number based to prevent collision
        output_svg = 'output_' + idnumber + '.svg'
        output_png = 'output_' + idnumber + '.png'

        # todo: check if lnurl is valid
        pyqr = pyqrcode.create(lnurl,  error='H')

        # change your QR code foreground and background colors here
        pyqr.png(lnurl_file, scale=3, module_color=[170,0,0,255], background=[255, 255, 255])
    
        with open(lnurl_file, 'rb') as fp:
            data = fp.read()
            base64qr = base64.b64encode(data).decode('utf-8')
            # print(base64qr)
            fp.close()

        qr_code = "\"data:image/png;base64," + base64qr + "\""

        with open(template_file, 'r') as tf:
            templ = tf.read()
            tf.close()

        tm = Template(templ)
        msg = tm.render(qrcode=qr_code, idnumber=idnumber, expires=expires, sats=sats)

        with open(output_svg, 'w') as f:
            f.write(msg)
            f.close()

        subprocess.run(['rsvg-convert', output_svg, '-o', output_png, '-w' , '600'], cwd=".")

        return output_png

    except Exception as e: 
        return str(e)

if __name__ == "__main__":

    template_file = 'templates/inlet_tiger_cut.svg'
    lnurl = "LNURL1DP68GURN8GHJ7MR9VAJKUEPWD3HXY6T5WVHXXMMD9AKXUATJD3CZ7CTSDYHHVVF0D3H82UNV9UUNWVCE4EM6P"
    idnumber = "f7bsdfs"
    expires = "2022-03-15"
    sats = "2500"

    output_png = create_laisee_qrcode(lnurl, idnumber, expires, sats, template_file)
    print(f'Output PNG created: {output_png}')


    # view file created , works on OSX only
    # subprocess.run(['open', output_png])


