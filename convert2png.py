import pyvips

image = pyvips.Image.new_from_file("svgs/2022-01_tiger.svg", dpi=300)
image.write_to_file("tiger.png")


image = pyvips.Image.thumbnail("svgs/2022-01_tiger.svg", width=200, height=300)
image.write_to_file("tigerthumb.png")


