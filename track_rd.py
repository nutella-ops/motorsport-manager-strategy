#!/usr/bin/python3

#track attributes
hspc = "high speed corners"
mspc = "medium speed corners"
lspc = "low speed corners"
dcl = "deceleration"
acl = "acceleration"
tsp = "top speed"

#fuel & tyre attributes
vl = "very low "
l = "low "
m = "medium "
h = "high "
vh = "very high "
fb = "fuel burn"
tw = "tyre wear"

#track info 
ita = [tsp, dcl, hspc, m+fb, l+tw]
chi = [tsp, acl, lspc, l+fb, m+tw] //favored
qat = [acl, lspc, tsp, l+fb, m+tw] //favored
usa = [tsp, lspc, hspc, l+fb, vh+tw] //mayb
can = [acl, lspc, mspc, m+fb, h+tw] //mayb
jap = [dcl, lspc, mspc, vl+fb, m+tw] //unlikely
uae = [tsp, dcl, hspc, m+fb, vl+tw]  //unlikely
bra = [tsp, hspc, acl, vh+fb, m+tw] //mayb
aus = [acl, lspc, tsp, m+fb, h+tw] //favored

//trying to trick it into search by attribute -_____-
hspc = [ita, usa, uae, bra] //4 
mspc = [can, jap] //2
lspc = [chi, qat, usa, can, jap, aus] //6 lspc
dcl = [ita, jap, uae] //3 
acl = [chi, qat, can, bra, aus] //5 acl
tsp = [ita, chi, qat, usa, uae, bra, aus] //7 tsp

vlfb = [jap]
lfb = [chi, qat, usa] //3 lfb
mfb = [ita, can, uae, aus] //4 mfb
hfb = []
vhfb = [bra]

vltw = [uae]
ltw = [ita]
mtw = [chi, qat, jap, bra] //4 mtw
htw = [can, aus] //2 htw
vhtw = [usa]

#track list
tr = [ita, chi, qat, usa, can, jap, uae, bra, aus]
tr_dict = {"ita":0, "chi":1, "qat":2, "usa":3, "can":4, "jap":5, "uae":6, "bra":7, "aus":8}


def search(q):
  key = tr_dict[q]
  print(tr[key])
  

#main code
while True:
  q = input("track: ")
  search(q)
   