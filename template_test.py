#!/usr/bin/env python

from jinja2 import Template 

with open('templates/inlet_tiger_cut.svg', 'r') as f:
    templ = f.read()

qrcode = "\"images/red_lnurl.png\""

qrcode = "\"" + "qrred.svg" + "\""
idnumber = "f7dfwer7a8cd43aabsdfs"
expires = "2022-03-15"
sats = "2000"

tm = Template(templ)
msg = tm.render(qrcode=qrcode, idnumber=idnumber, expires=expires, sats=sats)

with open('output.svg', 'w') as f:
    res = f.write(msg)
    f.close()