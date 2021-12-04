# QRimgtest

test repo for embedding logo into QR image and color, format customization

## how to run

You must have rsvg-convert installed 

```sudo apt-get rsvg-convert```

Requires at least python3.8

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 qrexample-working.py 
```

change colors in test_template.py

Also see : https://pypi.org/project/qrcode/
