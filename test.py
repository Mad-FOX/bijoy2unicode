#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bijoy2unicode import converter

test = converter.Unicode()
bijoy_text = 'Dfq cv‡k av‡bi kx‡l †ewóZ cvwb‡Z fvmgvb RvZxq dzj kvcjv| Zvi gv_vq cvUMv‡Qi ci¯úi mshy³ wZbwU cvZv Ges Dfh cv‡k `ywU K‡i ZviKv|'

print(bijoy_text)
toPrint=test.convertBijoyToUnicode(bijoy_text)
print(toPrint)
toPrint=test.convertUnicodeToBijoy(bijoy_text)
print(toPrint)