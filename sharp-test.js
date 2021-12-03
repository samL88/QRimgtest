const sharp = require('sharp');

async function convert(input, output) {
  sharp(input)
      .resize(3502, 2385)
      .png()
      .toFile(output)
      .then(function(info) {
          console.log(info)
        })
      .catch(function(err) {
          console.log(err)
      })  
}

infile = "svgs/tiger_raw.svg"
outfile = "images/tiger_raw.png"
convert(infile, outfile)
