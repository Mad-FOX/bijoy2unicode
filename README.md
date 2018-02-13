
# bijoy2unicode

## Purpose
Python 3 package for converting Bijoy &lt;=> Unicode (UTF-8) for Bengali/Bangla.

The package is also available via pip.

## Version

>  0.1.1

## License
MIT

## Installation

    pip install bijoy2unicode

## Example

    test = converter.Unicode()
    bijoy_text = 'Dfq cv‡k av‡bi kx‡l †ewóZ cvwb‡Z fvmgvb RvZxq dzj kvcjv| Zvi gv_vq cvUMv‡Qi ci¯úi mshy³ wZbwU cvZv Ges Dfh cv‡k `ywU K‡i ZviKv|'
    
    print(bijoy_text)
    
    toPrint=test.convertBijoyToUnicode(bijoy_text)
    print(toPrint)
    # উভয় পাশে ধানের শীষে বেষ্টিত পানিতে ভাসমান জাতীয় ফুল শাপলা। তার মাথায় পাটগাছের পরস্পর সংযুক্ত তিনটি পাতা এবং উভয পাশে দুটি করে তারকা।

    toPrint=test.convertUnicodeToBijoy(toPrint)
    print(toPrint)


## References:

https://github.com/bahar/BijoyToUnicode

https://github.com/sh-sabbir/UnicodeToBijoy

https://blog.jetbrains.com/pycharm/2017/05/how-to-publish-your-package-on-pypi/