# Requirements
* Python 3
* [Crunch](https://github.com/chrissimpkins/Crunch/blob/master/docs/EXECUTABLE.md)
* Pngcrunch
* Gifsicle (might also need giflossy)
* Jpegtran (libjpeg-progs)
* Jpegoptim 

### Running it on LAMBDA would require all the requriements to be setup in a docker container

# Running
```
lossy("input/png.png","output/lossypng.png")
lossless("input/png.png","output/losslesspng.png")
```

# Compression Rates

Lossless: No change in image quality(Gets rid of metadata and other data from file. <b>Caution: Could get rid of copyright metadata</b>)
<br/>Lossy: Reduces image quality. (The size could be reduced even further by reducing the quality further. <b>Caution: Running it more than once can cause very heavy loss of quality on an image</b>)
<br/><b>Caution: Some compressions can be taxing on the cpu and may consume time</b>

* gif: 
    * gif40.gif
        * Original: 40 kB
        * Compressed lossless: Currently no change. Not working? Need to check
        * Compressed lossy: 25.03 kB
    * gif140.gif
        * Original: 138 kB
        * Compressed lossless: Currently no change. Not working? Need to check
        * Compressed lossy: 125.16 kB
    * gif350.gif
        * Original: 355 kB
        * Compressed lossless: Currently no change. Not working? Need to check
        * Compressed lossy: 276.82 kB
    * gif500.gif
        * Original: 510 kB
        * Compressed lossless: Currently no change. Not working? Need to check
        * Compressed lossy:
    * gif1000.gif
        * Original: 1.03 MB
        * Compressed lossless: Currently no change. Not working? Need to check
        * Compressed lossy: 441 kB
    * gif3500.gif
        * Original: 3.65 MB
        * Compressed lossless: Currently no change. Not working? Need to check
        * Compressed lossy: 1.84 MB
* jpeg:
    * jpeg100.jpeg
        * Original: 102 kB
        * Compressed lossless: 99 kB
        * Compressed lossy: 44 kB
    * jpeg500.jpeg
        * Original: 555 kB
        * Compressed lossless: 552 kB
        * Compressed lossy: 184 kB
    * jpeg1000.jpeg
        * Original: 1 MB
        * Compressed lossless: 1 MB
        * Compressed lossy: 321 kB
    * jpeg2500.jpeg
        * Original: 2.5 MB
        * Compressed lossless: 2.5 MB
        * Compressed lossy: 901 kB
* png:
    * png500.png
        * Original: 513 kB
        * Compressed lossless: 493 kB
        * Compressed lossy: 137
    * png1000.png
        * Original: 1 MB
        * Compressed lossless: 970 kB
        * Compressed lossy: 284
    * png2000.png
        * Original: 2.1 MB
        * Compressed lossless: 2.1 MB
        * Compressed lossy: 565
    * png3000.png
        * Original: 3 MB
        * Compressed lossless: 2.9 MB
        * Compressed lossy: 850 kB    
***

