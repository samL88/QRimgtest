#!/bin/sh

# On Mac
# brew install librsvg
# docs: https://www.systutorials.com/docs/linux/man/1-rsvg-convert/

rsvg-convert output.svg > output.png

#-b white -w 1000 -h 1000