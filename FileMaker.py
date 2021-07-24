"""
Base 데이터
"""
Base_layer = {'ㄱ':100,'ㄲ':101,'ㅋ':102,'ㄴ':110,'ㄹ':120,'ㄷ':130,'ㄸ':131,'ㅌ':132,'ㅂ':140,'ㅃ':141,'ㅍ':142,'ㅅ':150,'ㅆ':151,'ㅎ':160,'ㅈ':170,
              'ㅉ':171,'ㅊ':172,'ㅇ':180,'ㅁ':190,'ㅡ':300,'ㅣ':300,'ㅏ':301,'ㅗ':301,'ㅜ':302,'ㅓ':302,'ㅑ':303,'ㅛ':303,'ㅕ':304,'ㅠ':304,'ㅐ':300.5,
                          'ㅒ':301.5,'ㅔ':301,'ㅖ':302,'ㅘ':301,'ㅙ':300.75,'ㅚ':300.5,'ㅝ':302,'ㅞ':301.5,'ㅟ':301,'ㅢ':300}

"""
layer raw 데이터
"""
Seem_layer_raw = {'/': ('ㅣ', '1.5'), '|': ('ㅣ', '0'), '1': ('ㅣ', '0.5'), 'r': ('ㅏ', '2'), '^': ('ㅅ', '1'), '•': ('ㅇ', '2'), '○': ('ㅇ', '0.5'),
                  '●': ('ㅇ', '2'), '0': ('ㅇ', '1'), 'O': ('ㅇ', '1'), 'o': ('ㅇ', '1'), '@': ('ㅇ', '3'), '°': ('ㅇ', '2.5'), '¤': ('ㅇ', '2.5'),
                  '□': ('ㅁ', '1'), '■': ('ㅁ', '1.5'), '◇': ('ㅇ', '3'), 'H': ('ㅐ', '1'), 'F': ('ㅑ', '1'), 'l': ('ㅣ', '0.5'), '*': ('ㅇ', '3')}

KeyBoard_layer_raw = {'q': ('ㅂ', 0), 'Q': ('ㅃ', 0), 'w': ('ㅈ', 0), 'W': ('ㅉ', 0), 'e': ('ㄷ', 0), 'E': ('ㄸ', 0), 'r': ('ㄱ', 0), 'R': ('ㄲ', 0),
                      't': ('ㅅ', 0), 'T': ('ㅆ', 0), 'y': ('ㅛ', 0), 'Y': ('ㅛ', 0), 'u': ('ㅕ', 0), 'U': ('ㅕ', 0), 'i': ('ㅑ', 0), 'I': ('ㅑ', 0),
                      'o': ('ㅐ', 0), 'O': ('ㅒ', 0), 'p': ('ㅔ', 0), 'P': ('ㅖ', 0), 'a': ('ㅁ', 0), 'A': ('ㅁ', 0), 's': ('ㄴ', 0), 'S': ('ㄴ', 0),
                      'd': ('ㅇ', 0), 'D': ('ㅇ', 0), 'f': ('ㄹ', 0), 'F': ('ㄹ', 0), 'g': ('ㅎ', 0), 'G': ('ㅎ', 0), 'h': ('ㅗ', 0), 'H': ('ㅗ', 0),
                      'j': ('ㅓ', 0), 'J': ('ㅓ', 0), 'k': ('ㅏ', 0), 'K': ('ㅏ', 0), 'l': ('ㅣ', 0), 'L': ('ㅣ', 0), 'z': ('ㅋ', 0), 'Z': ('ㅋ', 0),
                      'x': ('ㅌ', 0), 'X': ('ㅌ', 0), 'c': ('ㅊ', 0), 'C': ('ㅊ', 0), 'v': ('ㅍ', 0), 'V': ('ㅍ', 0), 'b': ('ㅠ', 0), 'B': ('ㅠ', 0),
                      'n': ('ㅜ', 0), 'N': ('ㅜ', 0), 'm': ('ㅡ', 0), 'M': ('ㅡ', 0)}

Pro_layer_raw = {'a': ('ㅏ', 0), 'A': ('ㅏ', 0), 'o': ('ㅗ', 0), 'O': ('ㅗ', 0), 'u': ('ㅜ', 0), 'U': ('ㅜ', 0), 'i': ('ㅣ', 0), 'I': ('ㅣ', 0),
                 'e': ('ㅔ', 0), 'E': ('ㅔ', 0), 'g': ('ㄱ', 0), 'G': ('ㄱ', 0), 'k': ('ㅋ', 0), 'K': ('ㅋ', 0), 'd': ('ㄷ', 0), 'D': ('ㄷ', 0),
                 't': ('ㅌ', 0), 'T': ('ㅌ', 0), 'b': ('ㅂ', 0), 'B': ('ㅂ', 0), 'p': ('ㅍ', 0), 'P': ('ㅍ', 0), 'j': ('ㅈ', 0), 'J': ('ㅈ', 0),
                 's': ('ㅅ', 0), 'S': ('ㅅ', 0), 'h': ('ㅎ', 0), 'H': ('ㅎ', 0), 'n': ('ㄴ', 0), 'N': ('ㄴ', 0), 'm': ('ㅁ', 0), 'M': ('ㅁ', 0),
                 'r': ('ㄹ', 0), 'R': ('ㄹ', 0), 'l': ('ㄹ', 0), 'L': ('ㄹ', 0)}


"""
raw 데이터를 base 데이터로 코딩
"""

Seem_layer = {}
KeyBoard_layer = {}
Pro_layer = {}

for i in Seem_layer_raw:
    Seem_layer[i]=Base_layer[Seem_layer_raw[i][0]]+float(Seem_layer_raw[i][1])
for i in KeyBoard_layer_raw:
    KeyBoard_layer[i]=Base_layer[KeyBoard_layer_raw[i][0]]+float(KeyBoard_layer_raw[i][1])
for i in Pro_layer_raw:
    Pro_layer[i]=Base_layer[Pro_layer_raw[i][0]]+float(Pro_layer_raw[i][1])




import pickle

with open('WDLD.txt', 'wb') as file:
        pickle.dump(Base_layer, file)
        pickle.dump(Seem_layer, file)
        pickle.dump(KeyBoard_layer, file)
        pickle.dump(Pro_layer, file)