def parse(s):
    regex = ''
    d = {
        '(': '(?:',
        '+': '|',           # or
        ' ': '',            # strip the whitespace
        'e': '.{0}',        # empty string
        '.': ''             # concatenation
    }
    for ch in s:
        if ch in d:
            regex += d[ch]
        else:
            regex += ch
    return '^(' + regex + ')$'


if __name__ == '__main__':
    print(parse('(  (12) + (((11)1*) ((22)2*))* )   (121)    ((  ((11)1*) ((22)2*)   )*  + (21) )'))
