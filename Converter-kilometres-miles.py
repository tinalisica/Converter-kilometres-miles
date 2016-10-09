# -*- coding: utf-8 -*-.

"""Program pozdravi uporabnika in predstavi kaj počne.
Program prosi uporabnika, naj vnese število kilometrov.
Uporabnik vnese številko.
Program pretvori kilometre v milje in izpiše rezultat v terminalu.
Program vpraša uporabnika, če želi narediti novo pretvorbo.
Če uporabnik odgovori z "da", potem se proces ponovi.
Če ne, se program poslovi in konča."""



print "Hello. With this programme, you can convert kilometres to miles."

kilometres = int(raw_input("Number of kilometres:"))

miles = kilometres * 0.621371192
print "This is %s miles." % miles


answer=1
while True:


    answer = raw_input("Do you want another conversion? Yes/No").lower()
    if answer == "no":
        print "Thank you and bye bye."
        break

    elif answer == "yes":
        kilometres = int(raw_input("Number of kilometres:"))
        miles = kilometres * 0.621371192
        print "This is %s miles." % miles



























