
# bijoy2unicode

# Why I forked this
I found the unicode to bijoy functionality in original repo as not working properly or partially functioning. Note this repo only provides unicode to bijoy functionality, not the reverse functionality.

## Main Purpose
I was creating an app using [Kivy](https://github.com/kivy/kivy). Unfortunately, Bangla Unicode text can't be implemented in Kivy. After a little searching, I found [this repo](https://github.com/Mad-FOX/bijoy2unicode) which was not functioning properly converting Unicode Bangla text to ANCI Bangla text. After a little tweaking, I somehow managed to get this work, Alhamdulillah.
### Warning
Code I've added in the repo is not optimized correctly (as I'm a noob). But it does it's job correctly (as far as I've tested). Feel free to submit issues and suggestions.



## Installation
    
    Just copy the unicode2bijoy folder to project folder.

## Example
    from unicode2bijoy import converter
    
    test = converter.Unicode()
    
    uni_text = 'উভয় পাশে ধানের শীষে বেষ্টিত পানিতে ভাসমান জাতীয় ফুল শাপলা। তার মাথায় পাটগাছের পরস্পর সংযুক্ত তিনটি পাতা এবং উভয পাশে দুটি করে তারকা।'
    #print(bijoy_text)
 
    

    toPrint=test.convertUnicodeToBijoy(uni_text)
    print(toPrint)
Output:
    ```Dfq cv‡k av‡bi kx‡l ‡ewóZ cvwb‡Z fvmgvb RvZxq dyj kvcjv| Zvi gv_vq cvUMv‡Qi ci¯úi mshy³ wZbwU cvZv Ges Dfh cv‡k `ywU K‡i ZviKv|```


## References:
https://github.com/Mad-FOX/bijoy2unicode

https://github.com/bahar/BijoyToUnicode

https://github.com/sh-sabbir/UnicodeToBijoy

https://blog.jetbrains.com/pycharm/2017/05/how-to-publish-your-package-on-pypi/
