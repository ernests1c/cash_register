#
# Kases aparāts
#
# 0.5pt pievienot jaunu preci - nosaukumu un cenu^^^^^^
#     0.5pt preces nosaukumam jābūt no 2 līdz 120 simboliem (jābūt validācijai, rādīt paziņojumu ja neder)^^^^^
#     0.5pt preces cenai jābūt veselam skaitlim vai daļskaitlim ar vērtību no 0 līdz 9999 (jābūt validācijai, rādīt paziņojumu ja neder)^^^^^
# 0.5pt dzēst preci pēc kārtas numura^^^^
# 0.5pt atcelt ievadu / iztukšot preču sarakstu
# 0.5pt piemērot atlaidi, ievadīt summu procentos^^^^
# 0.5pt samaksāt, ja iedota lielāka summa - izdrukāt atlikumu ^^^^
# 0.5pt izdrukāt čeku uz ekrāna - preces nosaukumus un summas ^^^^
#     0.5pt izdrukāt piemēroto atlaidi (ja ir) ^^^^^
#     0.5pt izdrukāt kopējo summu ^^^^^

# 1pt programmas stāvoklis tiek glabāts JSON faila un programmas sākumā tiek ielasīts un beigās saglabāts
# 1pt kodam ir jēdzīgi komentāri, pirms "if, for, while" koda konstrukcijam
# 1pt koda palaišanas brīdī nerādās kļūdas
# 1pt mainīgo un funkciju nosaukumi atspoguļo izmantošanas būtību, bez saisinājumiem, rakstīti snake_case stilā
# 1pt izmaiņas saglabātas versiju vadības sistēmā Git, savs fork
#
# Dokumentācija
# Mainīgie - https://www.w3schools.com/python/python_variables.asp
# Operācijas ar mainīgiem - https://www.w3schools.com/python/python_operators.asp
# Mainīgo drukāšana - https://www.w3schools.com/python/python_variables_output.asp
# Nosacījumi, zarošana, if ... else - https://www.w3schools.com/python/python_conditions.asp
# For cikls - https://www.w3schools.com/python/python_for_loops.asp
# Github Fork (repozitorija kopija) - https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
# Saraksti - https://www.w3schools.com/python/python_lists.asp
# Vārdnīcas - https://www.w3schools.com/python/python_dictionaries.asp
# Klonēt repozitoriju - hhttps://code.visualstudio.com/docs/sourcecontrol/intro-to-git
#
import json

kases_aparats = []
sakuma_atlaide = 1.00
sakuma_atlikums = 0.00
beigu_atlikums = 0
kopeja_summa = 0

with open('kases_aparats.json', 'r') as openfile:
    kases_aparats = json.load(openfile)

while True:
    print("         ~~~~~~Kases aparāts~~~~~~           ")
    print("1. Pievienot preci")
    print("2. Esmu gatavs maksāt")
    print("3. Dzēst preci pēc kārtas numura")
    print("4. Iztukšot preču sarakstu")
    print("5. Izdrukāt čeku uz ekrāna")

    print("         ~~~~~~Kases aparāts~~~~~~           ")
    kases_izvele = input("Izvēlies ko tu vēlies darīt: ")

    if kases_izvele == "1": # ja izvele ir 1 tad lietotajs var pievienot preci
        prece = input("Ievadiet preces nosaukumu: ")
        preces_cena = float(input("Ievadiet preces cenu: "))
        atlaide_precei = float(input("Ievadit atlaidi ja tāda ir: "))
        atlaide_preceisumma = atlaide_precei / 100
        beigu_atlaide = sakuma_atlaide - atlaide_preceisumma

        if len(prece) > 120: # pārbauda, vai simboli ir vairāk nekā 120
            print("Preces garumam jābūt līdz 120 simboliem!")
        elif len(prece) < 2: # pārbauda, vai simboli ir mazāk nekā 2
            print("Preces garumam jābūt starp 2 līdz 120 simboliem!")
        if preces_cena > 9999: # pārbauda, vai ievadītā cena ir virs 9999
            print("Prece nevar būt dārgāka par 9999!")
        elif preces_cena < 0: # pārbauda, vai ievadītā cena nav zem 0
            print("Prece nevar būt lētāka par 0!")
        if atlaide_precei > 100: # pārbauda, vai ievadita atlaide ir virs 100
            print("Atlaide nevar būt tik liela! Ievadi skaitli starp 0 un 100.")
        elif atlaide_precei < 0: # pārbauda, vai ievadītā atlaide ir zem 0
            print("Atlaide nevar būt zem 0! Ievadi skaitli starp 0 un 100.")
        pievienot_kasei = {
                "Prece": prece,
                "Cena": preces_cena,
                "Atlaide %": atlaide_precei,
                }
        kases_aparats.append(pievienot_kasei)
        pass
    elif kases_izvele == "2":
        iedota_nauda = (input("Ievadiet, cik jūs dosiet naudu kasierim: "))
        for x in kases_aparats:
            if "Cena" in x:
                kopeja_summa = sum(preces_cena)
                beigu_atlikums = kopeja_summa - iedota_nauda
        print("Jūsu atlikums ir: ", float(beigu_atlikums))
        


    elif kases_izvele == "3": # ja izvele ir 3 tad lietotajs var izdzest preci pec kartas skaitļa
        saraksta_id = int(input("Ievadi pēc kārtas skaitļa kuru preci tu vēlies noņemt: "))
        del kases_aparats[saraksta_id] 
    elif kases_izvele == "4": # ja izvele ir 4 tad lietotajs var iztukšot visu preču sarakstu
        del(kases_aparats)
    elif kases_izvele == "5": # izdrukā čeku uz ekrāna
        print(kases_aparats)
        with open("kases_aparats.json", "w") as kases_aparatsfails:
            json.dump(kases_aparats, kases_aparatsfails)
