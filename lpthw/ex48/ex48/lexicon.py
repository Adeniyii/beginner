d = 'direction'
v = 'verb'
s = 'stop'
n = 'noun'


pairs = {'north': d, 'south': d, 'east': d, 'west': d, 'down': d, 'up': d,
        'go': v, 'kill': v, 'run': v,'eat': v,'the': s, 'to': s, 'and': s,
        'in': s, 'of': s, 'now': s, 'bear': n, 'princess': n}


def word_type(word):
    word_s = word.strip(',').strip('.')
    word_l = word_s.lower()
    lex = pairs.get(word_l)
    if word_l in pairs:
        return (lex, word_s)
    elif word_l not in pairs and word_l.isalpha():
        return ('error', word_s)
    elif word_s.isdigit():
        raise ValueError
    else:
        return ('error', word_s)


def scan(word):
    sentence = []
    word_list = word.split()

    for words in word_list:
        try:
            t = word_type(words)
            sentence.append(t)
        except ValueError:
            word_n = words.strip('.').strip(',')
            sentence.append(('number', int(word_n)))
    return sentence
