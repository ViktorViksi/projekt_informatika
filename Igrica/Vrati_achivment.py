def vrati_achivment(skok, gubitak, Pigra, Tzvez, SveTzvez, high): #omogućuje da se postigne achivment. Radi tako da se na stavi potrebna mjesta (npr. funkicju za skokove) i onda ona to ovdje vraća i mijenja achivmente u točne
    global achivment_skok
    global achivment_gubitak
    global achivment_1pobjeda
    global achivment_3zvez
    global achivment_sve3zvez
    global achivment_high_score
    global high_score
    if skok == 1:
        achivment_skok = 1
    if gubitak == 1:
        achivment_gubitak = 1
    if Pigra == 1:
        achivment_1pobjeda = 1
    if Tzvez == 1:
        achivment_3zvez = 1
    if SveTzvez == 1:
        achivment_sve3zvez = 1
    if high == 1:
        achivment_high_score = 1