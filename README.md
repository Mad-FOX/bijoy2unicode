
# bijoy2unicode

## Purpose
Python 3 package for converting Bijoy &lt;=> Unicode (UTF-8) for Bengali/Bangla.

The package is also available via pip.

## Version

>  0.1.0

## Installation

    pip install bijoy2unicode

## Example

    test = converter.Unicode()
    bijoy_text = 'Dfq cv‡k av‡bi kx‡l †ewóZ cvwb‡Z fvmgvb RvZxq dzj kvcjv| Zvi gv_vq cvUMv‡Qi ci¯úi mshy³ wZbwU cvZv Ges Dfh cv‡k `ywU K‡i ZviKv|'
    
    print(bijoy_text)
    toPrint=test.convertBijoyToUnicode(bijoy_text)
    print(toPrint)
    toPrint=test.convertUnicodeToBijoy(bijoy_text)
    print(toPrint)


## References:

https://github.com/bahar/BijoyToUnicode

https://github.com/sh-sabbir/UnicodeToBijoy
