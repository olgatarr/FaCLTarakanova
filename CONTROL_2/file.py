import re
import csv

def opening(name):
    f = open(name, 'r', encoding='utf-8')
    lines = f.readlines()
    f.close()
    return lines

def writing(name, text, mode):
    f = open(name, 'w', encoding='utf-8')
    if mode == 5:
        f.write(str(len(text)))
    if mode == 8:
        f.write('\n'.join(text))
    if mode == 10:
        tow = []
        for item in text:
            tow.append(item + ', ' + str(text[item]))
        f.write('\n'.join(tow))
    if mode == 102:
        output = csv.writer(f, delimiter=',')
        header = ['лемма', 'разбор', 'словоформа']
        output.writerow(header)
        for item in text:
            row = item.split(', ')
            output.writerow([row[0], row[1], row[2]])
    f.close()

def counting(lines):
    dic = {}
    notags_arr = []
    for line in lines:
        match = re.search(".*<w lemma=.*?type=\"(.*?)\".*", line)
        if match:
            match = match.group(1)
            if match not in dic:
                dic[match] = 1
            else:
                dic[match] += 1
            notags_arr.append(re.sub(".*<w lemma=\"(.*?)\" type=\"(.*?)\">(.*?)</w>\n", "\\1, \\2, \\3", line))
    return dic, notags_arr

def adj(dic):
    dic_adj = {}
    for item in dic:
        if re.search('l.f.*', item):
            if item not in dic_adj:
                dic_adj[item] = 1
            else:
                dic_adj[item] += 1
    return dic_adj

def main():
    lines = opening('island.xml')
    writing('lines.txt', lines, 5)
    dic_arr = counting(lines)
    writing('freq.txt', dic_arr[0], 8)
    dic_adj = adj(dic_arr[0])
    writing('freq_adj.txt', dic_adj, 10)
    writing('notags.csv', dic_arr[1], 102)
    
main()
 
