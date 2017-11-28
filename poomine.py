import operator

# Vajalikud muutujad
sonade_fail = open("eesti_keel.txt", encoding="UTF-8")
sonade_matriks = [[], [], [], []] # suurendan seda vastavalt vajadusele
arvatud_tahed = []
vihje = input()


# vaatab, millist tahte esineb enim vaadeltatavates voimalustes vaadeltatavatel positsioonidel
def tahe_arv(jarjend, alakriipsud):
    # Muutujad
    tahed = {}
    enim = set()
    enim_list = []
    # Teen dictionary, kus tahed on keyd ja tahtede esinemis sagedus on vaartus
    for i in jarjend:
        for taht in alakriipsud:
            try:
                tahed[i[taht]] = tahed[i[taht]] + 1
            except KeyError:
                tahed[i[taht]] = 1
            except IndexError:
                return []
    # Teen listi, kus enim esinevad tahed on ees pool
    enim = sorted(tahed.items(), key=operator.itemgetter(1))
    enim.reverse()
    # Ei pane siia listi arvatud tahti
    for a in enim:
        if all(a[0] != x for x in arvatud_tahed):
            enim_list.append(a[0])
    return enim_list


def uued_voimalused(hetkesed_voimalused, vihje_p):
    global sonade_matriks
    global arvatud_tahed
    uued_voimalused_m = hetkesed_voimalused.copy()

    if len(arvatud_tahed) == 0 and all("_" == x for x in vihje_p):
        uued_voimalused_m = sonade_matriks[len(vihje_p)].copy()

    if len(arvatud_tahed) >= 1:
        if arvatud_tahed[-1] in vihje_p:

            if vihje_p.count(arvatud_tahed[-1]) == 1:
                positsioon = vihje_p.index(arvatud_tahed[-1])
                element = arvatud_tahed[-1]

                for i in hetkesed_voimalused:
                    if i[positsioon] != element:
                        uued_voimalused_m.remove(i)
                        continue
                    for a in range(len(vihje_p)):
                        if vihje_p[a] == "_" and i[a] == arvatud_tahed[-1]:
                            uued_voimalused_m.remove(i)
                            break

            if vihje_p.count(arvatud_tahed[-1]) > 1:

                for i in hetkesed_voimalused:
                    for a in range(len(vihje_p)):
                        if vihje_p[a] == "_" and i[a] == arvatud_tahed[-1]:
                            uued_voimalused_m.remove(i)
                            break
                        if vihje_p[a] == arvatud_tahed[-1] and i[a] != arvatud_tahed[-1]:
                            uued_voimalused_m.remove(i)
                            break

        if arvatud_tahed[-1] not in vihje_p:
            for e in hetkesed_voimalused:
                if arvatud_tahed[-1] in e:
                    uued_voimalused_m.remove(e)
                    continue

    return uued_voimalused_m


# Loen sonad maatriksisse, kus erinevate pikkustega sonad on eri ridades
for i in sonade_fail:
    i = i.strip().upper()
    pikkus = len(i)
    try:
        sonade_matriks[pikkus].append(i)
    except IndexError:
        while len(sonade_matriks) <= pikkus:
            sonade_matriks = sonade_matriks + [[]]
        sonade_matriks[pikkus].append(i)

sonade_fail.close()


# Sorteerin maatriksite read tahestikulises jarjekorras
for i in range(len(sonade_matriks)):
    sonade_matriks[i].sort()


def alakriipsu_pos(vihje_p):
    kriipsud = []
    for i in range(len(vihje_p)):
        if vihje_p[i] == "_":
            kriipsud.append(i)
    return kriipsud


def automaat(taht_p, vihje_p, sona):
    uus_vihje = ""
    if taht_p in sona:
        for i in range(len(sona)):
            if sona[i] == taht_p:
                uus_vihje += taht_p
            else:
                uus_vihje += vihje_p[i]
        return uus_vihje
    else:
        return vihje_p


voimalused = uued_voimalused(sonade_matriks, vihje)
arv = 0



while len(voimalused) != 1:
    pakkumine = tahe_arv(voimalused, alakriipsu_pos(vihje))[0]
    arvatud_tahed.append(pakkumine)
    print(pakkumine)
    vihje = automaat(pakkumine, vihje, "URGITSEMA")
    #vihje = input()
    voimalused = uued_voimalused(voimalused, vihje)
    arv += 1

print(voimalused[0])
