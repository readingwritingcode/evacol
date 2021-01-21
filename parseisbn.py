#!/usr/bin/python3
#  this program read ISBD data an split fields
#   end of info
# # # # # # # # # # # # # # # # # # # # # #  #
import sys
import unidecode
a = 'Física : campos y ondas. v.2. Marcelo Alonso; Edward J. Finn. edición revisada y aumentada.. México : Addison Wesley, 1987, 1989 reimpresión. V.2 (xxi, páginas 454-1068). ISBN 9686630023, ISBN 0201002809 (530/A454 v2 e21) - (Btca Carlos G)'

#isbn=sys.arv[1]

def parseisbn(isbn):
    tit=unidecode.unidecode(isbn.split('. ')[0]).lower()
    aut=unidecode.unidecode(isbn.split('. ')[2].split(';')[0]).lower()
    edt=unidecode.unidecode(isbn.split('. ')[5]).lower()
    return [tit,aut,edt]

if __name__=="__main__":
    isbn=sys.argv[1]
    tit=parseisbn(isbn)[0]
    aut=parseisbn(isbn)[1]
    edt=parseisbn(isbn)[2]
        
    print(tit, aut, edt)


