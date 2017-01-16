def opening(name):
    f = open(name, 'r', encoding='utf-8')
    text = f.read()
    f.close()
    text = text.strip()
    return text

def splitting(text):
    words = []
    words = text.split()
    return words

def counting(words):
    count = 0
    count2 = 0
    for word in words:
        checked = word.strip('.,":;?*()')
        if checked.endswith('ed'):
            count += 1
            if checked.endswith('ied'):
                count2 += 1
    return str(count), str(count2)

def final():
    text = opening('jane.txt')
    words = splitting(text)
    print(' '.join(counting(words)))

final()
    
