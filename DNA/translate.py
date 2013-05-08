#-*- encoding:utf8 -*-

'''
Created on 2013. 3. 30.

@author: stmkmk
'''
from microsofttranslator import Translator
translator = Translator('GSI_CHECK', 'm1ZX2yz3UVbmx7s2TVoaonjIsSqLvNjUtSd0VL1peBw=')

print translator.translate('합침 SR no.: SLAO-1303075-1 / 총 이체가: 30829.69 $ / 합쳐진 CI NO.: SLAO-1303078-1번과 합쳐진 SR입니다.', "en")
