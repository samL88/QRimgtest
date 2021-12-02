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

infile = "svgs/2022-01_tiger.svg"
outfile = "images/2022tiger.png"
convert(infile, outfile)
