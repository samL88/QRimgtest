import os
import subprocess

filepath = 'svgs/inlet_tiger_cut.svg'
outfile = 'qr_svg.png'
path = "./"

# brew install librsvg
# docs: https://www.systutorials.com/docs/linux/man/1-rsvg-convert/

if os.path.isfile(filepath):
    # 600 width
    subprocess.run(['rsvg-convert', filepath, '-o', outfile, "-w", '800' ], cwd=path)
    print('convert svg to png file')



'''
Options

-d --dpi-x number
    Set the X resolution of the image in pixels per inch. RSVG's current default is 90dpi 
-p --dpi-y number
    Set the Y resolution of the image in pixels per inch. RSVG's current default is 90dpi 
-x --x-zoom number
    X Zoom factor, as a percentage. If unspecified, 1.0 is used as the default. 
-y --y-zoom number
    Y Zoom factor, as a percentage. If unspecified, 1.0 is used as the default. 
-z ---zoom number
    Zoom factor, as a percentage. If unspecified, 1.0 is used as the default. 
-w --width integer
    Specify how wide you wish the image to be. If unspecified, the natural width of the image is used as the default. 
-h --height integer
    Specify how tall you wish the image to be. If unspecified, the natural height of the image is used as the default. 
-f --format [png, pdf, ps, svg, xml, recording]
    Specify the output format you wish the image to be saved in. If unspecified, PNG is used as the default. 
-o --output filename
    Specify the output filename. If unspecified, outputs to stdout. 
'''
