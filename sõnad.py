def teesõnadjatähed(tekstifail):
    f = open(tekstifail)
    def num_there(s):
        for i in s:
            if i.isdigit():
                return True
        return False
    
    temp = []
    for rida in f:
        rida = rida.strip()
        temp.append(rida)
    f.close()
    sõnad = []
    for i in temp:
        try:
            if (not num_there(i) and not i[0].isupper()
                and len(i) > 3
                and "-" not in i and ","not in i
                and "." not in i and "'" not in i
                and "&" not in i and "\n" not in i
                and "ž" not in i and " " not in i
                and "é" not in i and "!" not in i
                and "š" not in i and "x" not in i
                and "y" not in i and "w" not in i):
                sõnad.append(i)
        except:
            pass
    
    tähestik = set()
    for sõna in sõnad:
        for täht in sõna.strip():
            tähestik.add(täht.lower())

    sõnade_maatriks = [[]]
    for sõna in sõnad:
        while True:
            try:
                sõnade_maatriks[len(sõna)].append(sõna)
                break
            except IndexError:
                sõnade_maatriks.append([])

    return (sõnade_maatriks, sorted(list(tähestik)))
