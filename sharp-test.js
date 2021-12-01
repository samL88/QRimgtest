const sharp = require('sharp');


sharp("svgs/2022-01_tiger.svg")
    .resize(3502, 2385)
    .png()
    .toFile("tiger_hc.png")
    .then(function(info) {
        console.log(info)
      })
    .catch(function(err) {
        console.log(err)
    })
  