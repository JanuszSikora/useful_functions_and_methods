#To jest moduł zawierający
#funkcje rozwiązujące proste zapytania
#"kalendarzowe" - dotyczące dat, dni
#tygodnia, upływu czasu, itp.""")

#sprawdza, czy podany rok jest przestępny i zwraca True (jeżeli jest) lub False
def CzyPrzestępny(rok):
    if rok%4==0 and rok%100!=0 or rok%400==0:
        return True    
    else:
        return False

#wczytuje zadany parametrem element daty 1=>(RRR)R,
#2=>(M)M, 3=>(D)D, wymagając podania go w postaci
#liczby całk.; zwraca tak wczytany element
def Wczytaj(rmd):
    if rmd==1:
        tekst='rok'
    elif rmd==2:
        tekst='miesiąc'
    else:
        tekst='dzień'
    print(tekst)
    for i in range(9999999):
        try:
            liczba=int(input('- podaj go w postaci liczby całkowitej:'))
            break
        except:
            continue
    return liczba

#Sprawdza, czy podana data jest prawidłowa
#pod kątem lat przastępnych i długości miesięcy
#zwraca True, jeżeli ok lub None, jeżeli błędna
def Czy_dni_w_mscu_i_roku_ok(rok,miesiąc,dzień):
    if miesiąc>0 and miesiąc<13:
        if dzień>0 and dzień<32:        
            if (miesiąc==1 or miesiąc==3 or miesiąc==5 or miesiąc==7 or miesiąc==8 or miesiąc==10 or miesiąc==12):
                return True
            elif (miesiąc==4 or miesiąc==6 or miesiąc==9 or miesiąc==11) and dzień>30:
                return None
            elif CzyPrzestępny(rok)==True and miesiąc==2 and dzień>29:
                return None
            elif CzyPrzestępny(rok)==False and miesiąc==2 and dzień>28:
                return None
            else:
                return True
        else:
            return None
    else:
        return None

#sprawdza na podst. zadanej daty,
#który to dzień roku i go zwraca
def DzieńWRoku(rok,miesiąc,dzień):
    dzień_roku=30*(miesiąc-1)
    for i in range(miesiąc):
        if i==1 or i==3 or i==5 or i==7 or i==8 or i==10:
            dzień_roku+=1
        if i==2:
            dzień_roku-=2
    if CzyPrzestępny(rok)==True and miesiąc>2:
        dzień_roku+=1
    dzień_roku=dzień_roku+dzień
    return dzień_roku

#Na podst. 2-ch dat zadanych w formacie rok,dzień roku
#wylicza, ile dni jest pomiędzy nimi i zwraca wynik
def DniMiędzyDatami(rok1,dzień_roku1,rok2,dzień_roku2):
    if rok1>rok2 or rok1==rok2 and dzień_roku1>dzień_roku2:
        rok1,rok2=rok2,rok1
        dzień_roku1,dzień_roku2=dzień_roku2,dzień_roku1
    dni_między_datami=365*(rok2-rok1)
    if rok1==rok2 and CzyPrzestępny(rok1)==True and dzień_roku1<60 and dzień_roku2>60:
        dni_między_datami+=1
    else:
        for i in range(rok1,rok2):
            if CzyPrzestępny(i)==True:
                dni_między_datami+=1
    dni_między_datami=dni_między_datami+(dzień_roku2-dzień_roku1)
    return dni_między_datami
    
#na podst. zadanej daty wylicza, jaki to dzień tygodnia - zwraca od 0(niedziela)
#do 6 (sobota)
def Dzień_tygodnia(rok,miesiąc,dzień):
    YY=(rok-1)%100
    C=(rok-1)-YY
    G=YY+YY//4
    dz_tyg_dla_1_stycz=(((((C//100)%4)*5)+G)%7)
    DZ_TYG=DzieńWRoku(rok,miesiąc,dzień)%7+dz_tyg_dla_1_stycz
    if DZ_TYG>6:
        DZ_TYG=DZ_TYG-7
    return DZ_TYG

#z daty podaje, który to tydzień roku
def TydzieńWRoku(rok,miesiąc,dzień):
    dzień_roku=funkcje_kalendarzowe.DzieńWRoku(rok,miesiąc,dzień)
    Dz_tyg_1_st=funkcje_kalendarzowe.Dzień_tygodnia(rok,1,1)
    if (dzień_roku-Dz_tyg_1_st)<=7:
        nr_tyg=2
    else:
        nr_tyg=(abs((dzień_roku-Dz_tyg_1_st)))//7+1
    if funkcje_kalendarzowe.Czy_dni_w_mscu_i_roku_ok(rok,miesiąc,dzień)==True:
        return nr_tyg
    else:
        return None


#przekształcam numer miesiąca na jego nazwę
def nazwa_miesiąca(nr_miesiąca):
    if nr_miesiąca==1:
        miesiąc='styczeń'
    elif nr_miesiąca==2:
        miesiąc='luty'
    elif nr_miesiąca==3:
        miesiąc='marzec'
    elif nr_miesiąca==4:
        miesiąc='kwiecień'
    elif nr_miesiąca==5:
        miesiąc='maj'
    elif nr_miesiąca==6:
        miesiąc='czerwiec'
    elif nr_miesiąca==7:
        miesiąc='lipiec'
    elif nr_miesiąca==8:
        miesiąc='sierpień'
    elif nr_miesiąca==9:
        miesiąc='wrzesień'
    elif nr_miesiąca==10:
        miesiąc='październik'
    elif nr_miesiąca==11:
        miesiąc='listopad'
    else:
        miesiąc='grudzień'
    return miesiąc

#Sprawdza, czy podany nr miesiąca jest prawidłowy
#zwraca None, jeżeli błędna;
#zwraca liczbę dni w miesiącu z uwzględnieniem
#lat przestępnych
def Ile_dni_w_mscu(miesiąc):
    if miesiąc>0 and miesiąc<13:
        if miesiąc==1 or miesiąc==3 or miesiąc==5 or miesiąc==7 or miesiąc==8 or miesiąc==10 or miesiąc==12:
            return 31
        elif miesiąc==4 or miesiąc==6 or miesiąc==9 or miesiąc==11:
            return 30
        elif CzyPrzestępny(rok)==True and miesiąc==2:
            return 29
        elif CzyPrzestępny(rok)==False and miesiąc==2:
            return 28
        else:
            return None
    else:
        return None

        
