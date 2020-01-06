from . import util

preConversionMap = {
        ' +':' ',
        'yy':'y', # Double Hrosh-u-Kar
        'vv':'v', # Double Aa-Kar
        '­­':'­', # Double Jukto-L - L+Double-L = Triple L
        'y&':'y', # Hoshonto+Hrosh-u
        '„&':'„', # Hoshonto+Ri-Kar
        '‡u':'u‡', # ChondroBindu Error /Typing Mistake
        'wu':'uw', # ChondroBindu Error /Typing Mistake
        ' ,':',',
        ' \\|':'\\|',
        '\\\\ ':'',
        ' \\\\':'',
        '\\\\':'',
        '\n +':'\n',
        ' +\n':'\n',
        '\n\n\n\n\n':'\n\n',
        '\n\n\n\n':'\n\n',
        '\n\n\n':'\n\n'
}

conversionMap = {
    #  Vowels Start
    'Av': 'আ',
    'A': 'অ',
    'B': 'ই',
    'C': 'ঈ',
    'D': 'উ',
    'E': 'ঊ',
    'F': 'ঋ',
    'G': 'এ',
    'H': 'ঐ',
    'I': 'ও',
    'J': 'ঔ',
    #  Constants
    'K': 'ক',
    'L': 'খ',
    'M': 'গ',
    'N': 'ঘ',
    'O': 'ঙ',
    'P': 'চ',
    'Q': 'ছ',
    'R': 'জ',
    'S': 'ঝ',
    'T': 'ঞ',
    'U': 'ট',
    'V': 'ঠ',
    'W': 'ড',
    'X': 'ঢ',
    'Y': 'ণ',
    'Z': 'ত',
    '_': 'থ',
    '`': 'দ',
    'a': 'ধ',
    'b': 'ন',
    'c': 'প',
    'd': 'ফ',
    'e': 'ব',
    'f': 'ভ',
    'g': 'ম',
    'h': 'য',
    'i': 'র',
    'j': 'ল',
    'k': 'শ',
    'l': 'ষ',
    'm': 'স',
    'n': 'হ',
    'o': 'ড়',
    'p': 'ঢ়',
    'q': 'য়',
    'r': 'ৎ',
    's': 'ং',
    't': 'ঃ',
    'u': 'ঁ',
    #  Numbers
    '0': '০',
    '1': '১',
    '2': '২',
    '3': '৩',
    '4': '৪',
    '5': '৫',
    '6': '৬',
    '7': '৭',
    '8': '৮',
    '9': '৯',
    #  Kars
    '•': 'ঙ্',
    'v': 'া', #  Aa-Kar
    'w': 'ি', #  i-Kar
    'x': 'ী', #  I-Kar
    'y': 'ু', #  u-Kar
    'z': 'ু', #  u-Kar
    '“': 'ু', #  u-kar
    '–': 'ু', #  u-kar
    '~': 'ূ', #  U-kar
    'ƒ': 'ূ', #  U-kaar
    '‚': 'ূ', #  U-kaar
    '„„': 'ৃ', # Double Rri-kar Bug
    '„': 'ৃ', #  Ri-Kar
    '…': 'ৃ', #  Ri-Kar
    '†': 'ে', #  E-Kar
    '‡': 'ে', #  E-Kar
    'ˆ': 'ৈ', #  Oi-Kar
    '‰': 'ৈ', #  Oi-Kar
    'Š': 'ৗ', #  Ou-Kar
    '\\|': '।', #  Full-Stop
    '\\&': '্‌', #  Ho-shonto
    # 	Jukto Okkhor
    '\\^': '্ব',
    '‘': '্তু',
    '’': '্থ',
    '‹': '্ক',
    'Œ': '্ক্র',
    '”': 'চ্',
    '—': '্ত',
    '˜': 'দ্',
    '™': 'দ্',
    'š': 'ন্',
    '›': 'ন্',
    'œ': '্ন',
    'Ÿ': '্ব',
    '¡': '্ব',
    '¢': '্ভ',
    '£': '্ভ্র',
    '¤': 'ম্',
    '¥': '্ম',
    '¦': '্ব',
    '§': '্ম',
    '¨': '্য',
    '©': 'র্',
    'ª': '্র',
    '«': '্র',
    '¬': '্ল',
    '­': '্ল',
    '®': 'ষ্',
    '¯': 'স্',
    '°': 'ক্ক',
    '±': 'ক্ট',
    '²': 'ক্ষ্ণ', # shu(kkhno)
    '³': 'ক্ত',
    '´': 'ক্ম',
    'µ': 'ক্র',
    '¶': 'ক্ষ',
    '·': 'ক্স',
    '¸': 'গু',
    '¹': 'জ্ঞ',
    'º': 'গ্দ',
    '»': 'গ্ধ',
    '¼': 'ঙ্ক',
    '½': 'ঙ্গ',
    '¾': 'জ্জ',
    '¿': '্ত্র',
    'À': 'জ্ঝ',
    'Á': 'জ্ঞ',
    'Â': 'ঞ্চ',
    'Ã': 'ঞ্ছ',
    'Ä': 'ঞ্জ',
    'Å': 'ঞ্ঝ',
    'Æ': 'ট্ট',
    'Ç': 'ড্ড',
    'È': 'ণ্ট',
    'É': 'ণ্ঠ',
    'Ê': 'ণ্ড',
    'Ë': 'ত্ত',
    'Ì': 'ত্থ',
    'Í': 'ত্ম',
    'Î': 'ত্র',
    'Ï': 'দ্দ',
    'Ð': '-',
    'Ñ': '-',
    'Ò': '"',
    'Ó': '"',
    'Ô': "'",
    'Õ': "'",
    'Ö': '্র',
    '×': 'দ্ধ',
    'Ø': 'দ্ব',
    'Ù': 'দ্ম',
    'Ú': 'ন্ঠ',
    'Û': 'ন্ড',
    'Ü': 'ন্ধ',
    'Ý': 'ন্স',
    'Þ': 'প্ট',
    'ß': 'প্ত',
    'à': 'প্প',
    'á': 'প্স',
    'â': 'ব্জ',
    'ã': 'ব্দ',
    'ä': 'ব্ধ',
    'å': 'ভ্র',
    'æ': 'ম্ন',
    'ç': 'ম্ফ',
    'è': '্ন',
    'é': 'ল্ক',
    'ê': 'ল্গ',
    'ë': 'ল্ট',
    'ì': 'ল্ড',
    'í': 'ল্প',
    'î': 'ল্ফ',
    'ï': 'শু',
    'ð': 'শ্চ',
    'ñ': 'শ্ছ',
    'ò': 'ষ্ণ',
    'ó': 'ষ্ট',
    'ô': 'ষ্ঠ',
    'õ': 'ষ্ফ',
    'ö': 'স্খ',
    '÷': 'স্ট',
    'ø': 'স্ন', # (sn)eho # †ønØ
    'ù': 'স্ফ',
    'ú': '্প',
    'û': 'হু',
    'ü': 'হৃ',
    'ý': 'হ্ন',
    'þ': 'হ্ম'
}

proConversionMap = {'্্': '্'}

postConversionMap = {
    # Colon with Number/Space
    '০ঃ': '০:',
    '১ঃ': '১:',
    '২ঃ': '২:',
    '৩ঃ': '৩:',
    '৪ঃ': '৪:',
    '৫ঃ': '৫:',
    '৬ঃ': '৬:',
    '৭ঃ': '৭:',
    '৮ঃ': '৮:',
    '৯ঃ': '৯:',
    ' ঃ': ':',
    '\nঃ': '\n:',
    ']ঃ': ']:',
    '\\[ঃ': '\\[:',
    '  ': ' ',
    'অা': 'আ',
    '্‌্‌': '্‌'
}


class Unicode:

    def IsBanglaDigit(self, c):
        if (c >= '০' and c <= '৯'):
            return True
        return False

    def IsBanglaPreKar(self, c):
        if (c == 'ি' or c == 'ৈ' or c == 'ে'):
            return True
        return False

    def IsBanglaPostKar(self, c):
        if (c == 'া' or c == 'ো' or c == 'ৌ' or c == 'ৗ' or c == 'ু' or c == 'ূ' or c == 'ী' or c == 'ৃ'):
            return True
        return False

    def IsBanglaKar(self, c):
        if (self.IsBanglaPreKar(c) or self.IsBanglaPostKar(c)):
            return True
        return False

    def IsBanglaBanjonborno(self, c):
        if (c == 'ক' or c == 'খ' or c == 'গ' or c == 'ঘ' or c == 'ঙ' or c == 'চ' or c == 'ছ' or c == 'জ' or c == 'ঝ' or c == 'ঞ' or c == 'ট' or c == 'ঠ' or c == 'ড' or c == 'ঢ' or c == 'ণ' or c == 'ত' or c == 'থ' or c == 'দ' or c == 'ধ' or c == 'ন' or c == 'প' or c == 'ফ' or c == 'ব' or c == 'ভ' or c == 'ম' or c == 'য' or c == 'র' or c == 'ল' or c == 'শ' or c == 'ষ' or c == 'স' or c == 'হ' or c == 'ড়' or c == 'ঢ়' or c == 'য়' or c == 'ৎ' or c == 'ং' or c == 'ঃ' or c == 'ঁ'):
            return True
        return False

    def IsBanglaSoroborno(self, c):
        if (c == 'অ' or c == 'আ' or c == 'ই' or c == 'ঈ' or c == 'উ' or c == 'ঊ' or c == 'ঋ' or c == 'ঌ' or c == 'এ' or c == 'ঐ' or c == 'ও' or c == 'ঔ'):
            return True
        return False

    def IsBanglaNukta(self, c):
        if (c == 'ঁ'):
            return True
        return False

    def IsBanglaHalant(self, c):
        if (c == '্'):
            return True
        return False

    def IsSpace(self, c):
        if (c == ' ' or c == '\t' or c == '\n' or c == '\r'):
            return True
        return False

    def reArrangeUnicodeConvertedText(self, str):

        #mb_internal_encoding("UTF-8") # force multi-byte UTF-8 encoding

        #global proConversionMap

        #for (i = 0; i < mb_strlen(str); ++i) 
        i = 0
        while i < util.mb_strlen(str):
            #  Change refs
            if (i < (util.mb_strlen(str) - 1) and util.mbCharAt(str, i) == 'র' and self.IsBanglaHalant(util.mbCharAt(str, i + 1)) and self.IsBanglaHalant(util.mbCharAt(str, i - 1))):
                j = 1
                while (True):
                    if (i - j < 0):
                        break
                    
                    if (self.IsBanglaBanjonborno(util.mbCharAt(str, i - j)) and self.IsBanglaHalant(util.mbCharAt(str, i - j - 1))): 
                        j += 2
                    elif (j == 1 and self.IsBanglaKar(util.mbCharAt(str, i - j))):
                        j += 1
                    else:
                        break
                    
                
                temp = util.subString(str, 0, i - j)
                temp += util.mbCharAt(str, i)
                temp += util.mbCharAt(str, i + 1)
                temp += util.subString(str, i - j, i)
                temp += util.subString(str, i + 2, util.mb_strlen(str))
                str = temp
                i += 1
                continue

            i += 1

        str = util.doCharMap(str, proConversionMap)

        #for (i = 0 i < mb_strlen(str) ++i) 
        i=0
        while i<util.mb_strlen(str):
            if (i < util.mb_strlen(str) - 1 and util.mbCharAt(str, i) == 'র' and self.IsBanglaHalant(util.mbCharAt(str, i + 1)) and not self.IsBanglaHalant(util.mbCharAt(str, i - 1)) and self.IsBanglaHalant(util.mbCharAt(str, i + 2))):
                j = 1
                while (True):
                    if (i - j < 0):
                        break
                    
                    if (self.IsBanglaBanjonborno(util.mbCharAt(str, i - j)) and self.IsBanglaHalant(util.mbCharAt(str, i - j - 1))):
                        j += 2
                    elif (j == 1 and self.IsBanglaKar(util.mbCharAt(str, i - j))):
                        j += 1
                    else:
                        break
                    
                
                temp = util.subString(str, 0, i - j)
                temp += util.mbCharAt(str, i)
                temp += util.mbCharAt(str, i + 1)
                temp += util.subString(str, i - j, i)
                temp += util.subString(str, i + 2, util.mb_strlen(str))
                str = temp
                i += 1
                continue
            

            #  for 'Vowel + HALANT + Consonant' it should be 'HALANT + Consonant + Vowel'
            if (i > 0 and util.mbCharAt(str, i) == '\u09CD' and (self.IsBanglaKar(util.mbCharAt(str, i - 1)) or self.IsBanglaNukta(util.mbCharAt(str, i - 1))) and i < util.mb_strlen(str) - 1):
                temp = util.subString(str, 0, i - 1)
                temp += util.mbCharAt(str, i)
                temp += util.mbCharAt(str, i + 1)
                temp += util.mbCharAt(str, i - 1)
                temp += util.subString(str, i + 2, util.mb_strlen(str))
                str = temp
            

            #  for 'RA (\u09B0) + HALANT + Vowel' it should be 'Vowel + RA (\u09B0) + HALANT'
            if (i > 0 and i < util.mb_strlen(str) - 1 and util.mbCharAt(str, i) == '\u09CD' and util.mbCharAt(str, i - 1) == '\u09B0' and util.mbCharAt(str, i - 2) != '\u09CD' and self.IsBanglaKar(util.mbCharAt(str, i + 1))):
                temp = util.subString(str, 0, i - 1)
                temp += util.mbCharAt(str, i + 1)
                temp += util.mbCharAt(str, i - 1)
                temp += util.mbCharAt(str, i)
                temp += util.subString(str, i + 2, util.mb_strlen(str))
                str = temp            

            #  Change pre-kar to post format suitable for unicode
            if (i < util.mb_strlen(str) - 1 and self.IsBanglaPreKar(util.mbCharAt(str, i)) and self.IsSpace(util.mbCharAt(str, i + 1)) == False):
                
                temp = util.subString(str, 0, i)

                j = 1
                while ((i + j) < util.mb_strlen(str) - 1 and self.IsBanglaBanjonborno(util.mbCharAt(str, i + j))):
                    if ((i + j) < util.mb_strlen(str) and self.IsBanglaHalant(util.mbCharAt(str, i + j + 1))):
                        j += 2
                    else:
                        break                    
                
                temp += util.subString(str, i + 1, i + j + 1)

                l = 0
                if (util.mbCharAt(str, i) == 'ে' and util.mbCharAt(str, i + j + 1) == 'া'):
                    temp += "ো"
                    l = 1
                elif (util.mbCharAt(str, i) == 'ে' and util.mbCharAt(str, i + j + 1) == "ৗ"):
                    temp += "ৌ"
                    l = 1
                else:
                    temp += util.mbCharAt(str, i)
                
                temp += util.subString(str, i + j + l + 1, util.mb_strlen(str))
                str = temp
                i += j
            
            #  nukta should be placed after kars
            if (i < util.mb_strlen(str) - 1 and self.IsBanglaNukta(util.mbCharAt(str, i)) and self.IsBanglaPostKar(util.mbCharAt(str, i + 1))):
                temp = util.subString(str, 0, i)
                temp += util.mbCharAt(str, i + 1)
                temp += util.mbCharAt(str, i)
                temp += util.subString(str, i + 2, util.mb_strlen(str))
                str = temp

            i += 1
        return str

    def reArranceUnicodeTextForASCI(self, str):
        
        cY = 0
        i = 0
        
        #for ($i = 0; $i < util.mb_strlen(str); ++$i) 
        while i<util.mb_strlen(str):

            if(i<util.mb_strlen(str) and self.IsBanglaPreKar(util.mbCharAt(str,i))):
                j=1
                while self.IsBanglaBanjonborno(util.mbCharAt(str,i-j)):
                    if (i-j)<0:
                        break
                    if (i-j)<=cY:
                        break
                    if self.IsBanglaHalant(util.mbCharAt(str,i-j-1)):
                        j+=2
                    else:
                        break

                R = util.subString(str,0, i-j)
                R += util.mbCharAt(str,i)
                R += util.subString(str,i-j, i)
                R += util.subString(str,i+1, util.mb_strlen(str))
                
                str = R
                
                cY= i+1
                continue
            
            
            if i<(util.mb_strlen(str)-1) and self.IsBanglaHalant(util.mbCharAt(str,i)) and util.mbCharAt(str,i-1)=='র' and not self.IsBanglaHalant(util.mbCharAt(str,i-2)):
                j=1
                aZ=0

                while True:
                    if self.IsBanglaBanjonborno(util.mbCharAt(str,i+j)) and self.IsBanglaHalant(util.mbCharAt(str,i+j+1)):
                        j+=2

                    elif self.IsBanglaBanjonborno(util.mbCharAt(str,i+j)) and self.IsBanglaPreKar(util.mbCharAt(str,i+j+1)):
                        aZ=1
                        break
                    
                    else:
                        break

                R  = util.subString(str,0, i-1)
                R += util.subString(str, i+j+1, i+j+aZ+1)
                R += util.subString(str, i+1, i+j+1)
                R += util.mbCharAt(str, i-1)
                R += util.mbCharAt(str, i)
                R += util.subString(str, i+j+aZ+1, util.mb_strlen(str))
                
                str = R
                
                i+=(j+aZ)
                cY=i+1
                continue

            i += 1
        return str

    # main conversion def
    def convertBijoyToUnicode(self, srcString):
        if not srcString:
            return srcString

        srcString = util.doCharMap(srcString, preConversionMap)
        srcString = util.doCharMap(srcString, conversionMap)
        
        srcString = self.reArrangeUnicodeConvertedText(srcString)
        srcString = util.doCharMap(srcString, postConversionMap)
        return srcString

    def convertUnicodeToBijoy(self, srcString):
        if not srcString:
            return srcString

        main_char = {
            "।"   :   "|", 	"‘"   :   "Ô", 	"’"   :   "Õ", 
            "“"   :   "Ò", 	"”"   :   "Ó", 	"্র্য"   :   "ª¨", 
            "ম্প্র"   :   "¤cÖ", 	"র‌্য"   :   "i¨", 	"ক্ষ্ম"   :   "²", 
            "ক্ক"   :   "°", 	"ক্ট"   :   "±", 	"ক্ত"   :   "³", 
            "ক্ব"   :   "K¡", 	"স্ক্র"   :   "¯Œ", 	"ক্র"   :   "µ", 
            "ক্ল"   :   "K¬", 	"ক্ষ"   :   "¶", 	"ক্স"   :   "·", 
            "গু"   :   "¸", 	"গ্ধ"   :   "»", 	"গ্ন"   :   "Mœ", 
            "গ্ম"   :   "M¥", 	"গ্ল"   :   "M­", 	"গ্রু"   :   "Mªy", 
            "ঙ্ক"   :   "¼", 	"ঙ্ক্ষ"   :   "•¶", 	"ঙ্খ"   :   "•L", 
            "ঙ্গ"   :   "½", 	"ঙ্ঘ"   :   "•N", 	"চ্ছ্ব"   :   "”Q¡", 
            "চ্চ"   :   "”P", 	"চ্ছ"   :   "”Q", 	"চ্ঞ"   :   "”T", 
            "জ্জ্ব"   :   "¾¡", 	"জ্জ"   :   "¾", 	"জ্ঝ"   :   "À", 
            "জ্ঞ"   :   "Á", 	"জ্ব"   :   "R¡", 	"ঞ্চ"   :   "Â", 
            "ঞ্ছ"   :   "Ã", 	"ঞ্জ"   :   "Ä", 	"ঞ্ঝ"   :   "Å", 
            "ট্ট"   :   "Æ", 	"ট্ব"   :   "U¡", 	"ট্ম"   :   "U¥", 
            "ড্ড"   :   "Ç", 	"ণ্ট"   :   "È", 	"ণ্ঠ"   :   "É", 
            "ন্স"   :   "Ý", 	"ণ্ড"   :   "Ê", 	"ন্তু"   :   "š‘", 
            "ণ্ব"   :   "Y^", 	"ত্ত্ব"   :   "Ë¡", 	"ত্ত"   :   "Ë", 
            "ত্থ"   :   "Ì", 	"ত্ন"   :   "Zœ", 	"ত্ম"   :   "Z¥", 
            "ন্ত্ব"   :   "š—¡", 	"ত্ব"   :   "Z¡", 	"থ্ব"   :   "_¡", 
            "দ্গ"   :   "˜M", 	"দ্ঘ"   :   "˜N", 	"দ্দ"   :   "Ï", 
            "দ্ধ"   :   "×", 	"দ্ব"   :   "Ø", 
            "দ্ভ"   :   "™¢", 	"দ্ম"   :   "Ù", 	"দ্রু"   :   "`ª“", 
            "ধ্ব"   :   "aŸ", 	"ধ্ম"   :   "a¥", 	"ন্ট"   :   "›U", 
            "ন্ঠ"   :   "Ú", 	"ন্ড"   :   "Û", 	"ন্ত্র"   :   "š¿", 
            "ন্ত"   :   "š—", 	"স্ত্র"   :   "¯¿", 	"ত্র"   :   "Î", 
            "ন্থ"   :   "š’", 	"ন্দ"   :   "›`", 	"ন্দ্ব"   :   "›Ø", 
            "ন্ধ"   :   "Ü", 	"ন্ন"   :   "bœ", 	"ন্ব"   :   "š^", 
            "ন্ম"   :   "b¥", 	"প্ট"   :   "Þ", 	"প্ত"   :   "ß", 
            "প্ন"   :   "cœ", 	"প্প"   :   "à", 	"প্ল"   :   "c­", 
            "প্স"   :   "á", 	"ফ্ল"   :   "d¬", 	"ব্জ"   :   "â", 
            "ব্দ"   :   "ã", 	"ব্ধ"   :   "ä", 	"ব্ব"   :   "eŸ", 
            "ব্ল"   :   "e­", 	"ভ্র"   :   "å", 	"ম্ন"   :   "gœ", 
            "ম্প"   :   "¤ú", 	"ম্ফ"   :   "ç", 	"ম্ব"   :   "¤^", 
            "ম্ভ"   :   "¤¢", 	"ম্ভ্র"   :   "¤£", 	"ম্ম"   :   "¤§", 
            "ম্ল"   :   "¤­", 	"্র"   :   "ª", 	"রু"   :   "i“", 
            "রূ"   :   "iƒ", 	"ল্ক"   :   "é", 	"ল্গ"   :   "ê", 
            "ল্ট"   :   "ë", 	"ল্ড"   :   "ì", 	"ল্প"   :   "í", 
            "ল্ফ"   :   "î", 	"ল্ব"   :   "j¦", 	"ল্ম"   :   "j¥", 
            "ল্ল"   :   "j­", 	"শু"   :   "ï", 	"শ্চ"   :   "ð", 
            "শ্ন"   :   "kœ", 	"শ্ব"   :   "k¦", 	"শ্ম"   :   "k¥", 
            "শ্ল"   :   "k­", 	"ষ্ক"   :   "®‹", 	"ষ্ক্র"   :   "®Œ", 
            "ষ্ট"   :   "ó", 	"ষ্ঠ"   :   "ô", 	"ষ্ণ"   :   "ò", 
            "ষ্প"   :   "®ú", 	"ষ্ফ"   :   "õ", 	"ষ্ম"   :   "®§", 
            "স্ক"   :   "¯‹", 	"স্ট"   :   "÷", 	"স্খ"   :   "ö", 
            "স্ত"   :   "¯—", 	"স্তু"   :   "¯‘", 	"স্থ"   :   "¯’", 
            "স্ন"   :   "mœ", 	"স্প"   :   "¯ú", 	"স্ফ"   :   "ù", 
            "স্ব"   :   "¯^", 	"স্ম"   :   "¯§", 	"স্ল"   :   "¯­", 
            "হু"   :   "û", 	"হ্ণ"   :   "nè", 	"হ্ব"   :   "nŸ", 
            "হ্ন"   :   "ý", 	"হ্ম"   :   "þ", 	"হ্ল"   :   "n¬", 
            "হৃ"   :   "ü", 	"র্"   :   "©",
            "্য"   :   "¨", 	"্"   :   "&", 	"আ"   :   "Av", 
            "অ"   :   "A", 	"ই"   :   "B", 	"ঈ"   :   "C", 
            "উ"   :   "D", 	"ঊ"   :   "E", 	"ঋ"   :   "F", 
            "এ"   :   "G", 	"ঐ"   :   "H", 	"ও"   :   "I", 
            "ঔ"   :   "J", 	"ক"   :   "K", 	"খ"   :   "L", 
            "গ"   :   "M", 	"ঘ"   :   "N", 	"ঙ"   :   "O", 
            "চ"   :   "P", 	"ছ"   :   "Q", 	"জ"   :   "R", 
            "ঝ"   :   "S", 	"ঞ"   :   "T", 	"ট"   :   "U", 
            "ঠ"   :   "V", 	"ড"   :   "W", 	"ঢ"   :   "X", 
            "ণ"   :   "Y", 	"ত"   :   "Z", 	"থ"   :   "_", 
            "দ"   :   "`", 	"ধ"   :   "a", 	"ন"   :   "b", 
            "প"   :   "c", 	"ফ"   :   "d", 	"ব"   :   "e", 
            "ভ"   :   "f", 	"ম"   :   "g", 	"য"   :   "h", 
            "র"   :   "i", 	"ল"   :   "j", 	"শ"   :   "k", 
            "ষ"   :   "l", 	"স"   :   "m", 	"হ"   :   "n", 
            "ড়"   :   "o", 	"ঢ়"   :   "p", 	"য়"   :   "q", 
            "ৎ"   :   "r", 	"০"   :   "0", 	"১"   :   "1", 
            "২"   :   "2", 	"৩"   :   "3", 	"৪"   :   "4", 
            "৫"   :   "5", 	"৬"   :   "6", 	"৭"   :   "7", 
            "৮"   :   "8", 	"৯"   :   "9", 	"া"   :   "v", 
            "ি"   :   "w", 	"ী"   :   "x", 	"ু"   :   "y", 
            "ূ"   :   "~", 	"ৃ"   :   "…", 	"ে"   :   "‡", 
            "ৈ"   :   "‰", 	"ৗ"   :   "Š", 	"ং"   :   "s", 
            "ঃ"   :   "t", 	"ঁ"   :   "u"
        }

        pattern = 'ো'
        replacement = 'ো'
        srcString = util.preg_replace(pattern, replacement, srcString)
	
        pattern = 'ৌ'
        replacement = 'ৌ'
        srcString = util.preg_replace(pattern, replacement, srcString)

        # make correction
        srcString = self.reArranceUnicodeTextForASCI(srcString)

        #inv_conversionMap = {v: k for k, v in conversionMap.items()}
        srcString = util.doCharMap(srcString, main_char)
        
        return srcString

    def __init__(self):
        pass
    #def __init__(self):
    #    self = self
