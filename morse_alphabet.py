# Mors alfabesi / Morse alphabet
alfabe = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    ' ': ' / ',

# Mors alfabesine ait sayılar. / Morse alphabet numbers
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.'
}


metin = input('Cevirilmesi istenilen metni giriniz: ')
#"Enter the text you want translated"
islem = list(map(lambda x: alfabe[x] if x in alfabe else 'EROR({}) '.format(x), list(metin)))
print(metin+ ' => '+''.join(islem))

while True:
    pass
