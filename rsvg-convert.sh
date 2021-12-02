#!/bin/sh

# On Mac
# brew install librsvg
# docs: https://www.systutorials.com/docs/linux/man/1-rsvg-convert/

rsvg-convert qr.svg -o qr.png -b white -w 1000 -h 1000