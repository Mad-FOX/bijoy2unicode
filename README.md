# Why I forked this
I found the unicode to bijoy functionality in original repo as not working properly or partially functioning. Note this repo only provides unicode to bijoy functionality, not the reverse functionality.

## Main Purpose
I was creating an app using [Kivy](https://github.com/kivy/kivy). Unfortunately, Bangla Unicode text can't be implemented in Kivy. After a little searching, I found [this repo](https://github.com/Mad-FOX/bijoy2unicode) which was not functioning properly converting Unicode Bangla text to ANCI Bangla text. After a little tweaking, I somehow managed to get this work, Alhamdulillah.
### Warning
The code I've added in this repo is not optimized correctly (as I'm a noob). But it does it's job correctly (as far as I've tested). Feel free to submit issues and suggestions.



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


## Usage for Kivy
We can use ```[font][/font]``` tag to use Bangla ANSI text with English text in same Label widget. Like this (in kv language):
``` Label:
        text = "[font=font/SutonnyMJ]Avwg evsjvq K_v ewj[/font] means I speak Bangla"
```

But how to generate (English and Bangla mixed) text with tag?

```

    def toBijoy(str):
        def isEnglish(s):
            return s.isascii()
        
        import converter
        test = converter.Unicode()
        b_flag = 0
        ftext = ""
        temp = ''
        for char in str:
            if char == ' ' and b_flag == 0:
                ftext += char
            elif char == ' ' and b_flag == 1:
                temp += char
            elif isEnglish(char) is False:
                if b_flag == 0:
                    temp += "[font=font/SutonnyMJ]" + char
                    b_flag = 1
                else:
                    temp += char
            else:
                if b_flag == 1:
                    temp = test.convertUnicodeToBijoy(temp)
                    
                    if temp[-1:] == '©':
                        temp = temp[:-1]
                    
                    temp = "[/font]" + char
                    ftext += temp
                    b_flag = 0
                    temp = ''
                else:
                    ftext += char
 

        ftext = "".join(ftext)
        return ftext

```


Now we can convert the text (with font tags), call an widget using id, and then assign formatted text.

```
    self.ids.bangla_mixed_text.markup = True
    self.ids.bangla_mixed_text.text = toBijoy(sub_text_g)
```

In kv language we need to do something like this:
```
    Label:
        id: bangla_mixed_text
        text: ''
```


## References:
https://github.com/Mad-FOX/bijoy2unicode

https://github.com/bahar/BijoyToUnicode

https://github.com/sh-sabbir/UnicodeToBijoy

https://blog.jetbrains.com/pycharm/2017/05/how-to-publish-your-package-on-pypi/
