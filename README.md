# QRimgtest

test repo for embedding logo into QR image and color, format customization

## how to run

You must have rsvg-convert installed 

```
sudo apt install librsvg2-bin
sudo apt-get update
```

Requires at least python3.8

```
sudo apt install python3.10-venv
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 test_template.py   (may need to downgrade markupsafe to 2.0.1, pip install markupsafe==2.0.1 to fix cannot import name 'soft_unicode' from 'markupsafe')
```

- change colors in test_template.py

- EDIT YOUR SVG TEMPLATE FILE to refer to qr_code, idnumber, expires and sats
with {{ }}, For example: 

```<image
         width="166.29921"
         height="166.51379"
         preserveAspectRatio="none"
         href={{qrcode}}
         id="image4277"
         x="811.72894"
         y="208.38103" />
