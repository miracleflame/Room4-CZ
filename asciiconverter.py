from unidecode import unidecode

with open('.\\English-resources-puv.assets-894.txt', mode='r', encoding='utf8') as fin:
    deaccented = unidecode(fin.read())
    open('.\\deaccentedEnglish-resources.assets-894.txt', mode='w', encoding='utf8').write(deaccented)
