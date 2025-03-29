#Función para convertir caracteres (números o letras) en subíndices
def convertir_a_subindice(texto):
    #Relaciones de los caracteres con sus subíndices Unicode correspondientes
    subindices = {
        '0': '\u2080',
        '1': '\u2081',
        '2': '\u2082',
        '3': '\u2083',
        '4': '\u2084',
        '5': '\u2085',
        '6': '\u2086',
        '7': '\u2087',
        '8': '\u2088',
        '9': '\u2089',
        'a': '\u2090',
        'e': '\u2091',
        'i': '\u1D62',
        'j': '\u2C7C',
        'm': '\u2098',
        'p': '\u209A',
        'r': '\u1D63',
        's': '\u209B',
        't': '\u209C',
        'u': '\u1D64'
        
    }
    #Se genera una nueva cadena reemplazando cada carácter por su subíndice 
    return ''.join(subindices.get(c, c) for c in texto)

