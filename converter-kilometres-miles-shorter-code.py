# -*- coding: utf-8 -*-.

answer="yes"
while answer == "yes":

    print "Hello. With this programme, you can convert kilometres to miles."

    kilometres=int(raw_input("Number of kilometres:"))
    miles = kilometres * 0.621371192
    print "This is %s miles." % miles

    answer= raw_input("Do you want another conversion? Yes/No").lower()


    if answer == "no":
        print "Thank you and bye bye."




