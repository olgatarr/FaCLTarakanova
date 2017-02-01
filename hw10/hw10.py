import re

def extract(name):
    f = open(name, 'r', encoding='utf-8')
    text = f.read().strip()
    f.close()
    return text       

def find(text):
    res = re.search("Семейство:(?:.*\n)*?.*?<a.*?>(.*?)</a>", text)
    if res:
        res = res.group(1)
    return res

def writing(name, checked):
    f = open(name, 'a', encoding='utf-8')
    f.write(checked + '\n')
    f.close()
    
def main():
    text = extract('tomat.htm')
    checked = find(text)
    writing('res.txt', checked)

main()
