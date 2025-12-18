#DEIMOS Version 1
#Auth: Titanite01
#For Java Edition 1.21.10 + (not tested on bedrock)
#Big incompressible packet bomb Data generator
# 1023 characters per page

import secrets, pyperclip


def get_secret_unicode(length):

    get_char = chr
    # Update this to include code point ranges to be sampled
    include_ranges = [
        ( 0x2100, 0x214F ), #letter symbols
        ( 0x2150, 0x218F ), #number forms
        ( 0x2190, 0x21FF ), #Arrows
        ( 0x1F800, 0x1F8FF ), #supplement arrows
        ( 0x2200, 0x22FF ), #math operators
        ( 0x2980, 0x29FF ), #misc math
        ( 0x2300, 0x23FF ), #tech misc
        ( 0x2460, 0x24FF ), #alpha numerics
        ( 0x2500, 0x257F ), #box frames
        ( 0x25A0, 0x25FF ), #geometric shapes
        ( 0x2600, 0x26FF ), #misc emoji
        ( 0x2700, 0x27BF ), #Dingbats
        ( 0x2800, 0x28FF )  #Braille1
    ]

    alphabet = [
        get_char(code_point) for current_range in include_ranges
            for code_point in range(current_range[0], current_range[1]+ 1)
    ]
    return ''.join(secrets.choice(alphabet) for i in range(length))

    #print('A secret string: ' + get_secret_unicode(1023))


counter = 0
for loop in range(100):
    counter = counter + 1

    pyperclip.copy(get_secret_unicode(1023))
    print("Data copied to clipboard!")
    print("Page number: ", counter, "printed.")
    clickcheck = input("")

print("End.")