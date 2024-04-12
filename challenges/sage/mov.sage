q = 1331169830894825846283645180581
a = -35
b = 98

E = EllipticCurve(GF(q), [a,b])

G = E((479691812266187139164535778017 , 568535594075310466177352868412))
Pa =  E((1110072782478160369250829345256 , 800079550745409318906383650948))
Pb =  E((1290982289093010194550717223760 , 762857612860564354370535420319))



k = 1 
while(q**k-1) % E.order() != 0: 
    k+=1 

e = EllipticCurve(GF(q**k), [a, b])



n = G.order() 

T = e.random_point() 
Q = T.order()//G.order()*T 
   

u = e(G).weil_pairing(Q, n)
v = e(Pa).weil_pairing(Q, n)
     
a = v.log(u)

print(a) 
print((a*Pb).xy()[0]) 



