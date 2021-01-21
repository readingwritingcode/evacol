#!/usr/bin/python3
tw="Física : campos y ondas. v.2.".strip(':').split(' ') 
lr=[ "Física", "Física", "Campos y ondas", "Física. Vol. 2, Campos y ondas", "Física.", "Campos y ondas : v.2.", "Física : campos y ondas", "Física", "Física", "Física. Vol. 2, Campos y ondas" ]

idx=[]
for j in lr:
    s=0
    for i in range(len(tw)):
        if tw[i] in j:
            s+=1
    if s >= len(tw)-2:
        idx.append(lr.index(j))


import Levenshtein as lv

lvr=[]
lri=[]
tw="Física : campos y ondas. v.2.".replace('.','').replace(' ','').replace(':','').lower()
for j in lr:
    jt=j.replace('.','').replace(' ','').replace(':','').lower()
    print(jt,'----',tw,'---',lv.ratio(jt,tw))
    if lv.ratio(tw,jt) >= 0.75:
        lri.append(j)
        
    lvr.append(lv.ratio(tw,jt))
lvm=max(lvr)
print(lr[lvr.index(lvm)],lvr.index(lvm))

//form/table/tbody/tr

# titulo: $x('//form/table/tbody/tr/td[4]/div[3]/a/strong/text()')
# author: $x('//form/table/tbody/tr/td[4]/div[4]/text()')
# type  : $x('//form/table/tbody/tr/td[4]/div[5]')
# lang  : $x('//form/table/tbody/tr/td[4]/div[6]')
# publ  : $x('//form/table/tbody/tr/td[4]/div[7]/span/text()')
# eds   : $x('//form/table/tbody/tr/td[4]/ul/li/a')
