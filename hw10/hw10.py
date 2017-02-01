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
    
def main():
    text = extract('tomat.htm')
    checked = find(text)
    print (checked)

main()
