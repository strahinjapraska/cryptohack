

# This file was *autogenerated* from the file micro-transmissions.sage
from sage.all_cmdline import *   # import sage library

_sage_const_99061670249353652702595159229088680425828208953931838069069584252923270946291 = Integer(99061670249353652702595159229088680425828208953931838069069584252923270946291); _sage_const_1 = Integer(1); _sage_const_4 = Integer(4); _sage_const_43190960452218023575787899214023014938926631792651638044680168600989609069200 = Integer(43190960452218023575787899214023014938926631792651638044680168600989609069200); _sage_const_20971936269255296908588589778128791635639992476076894152303569022736123671173 = Integer(20971936269255296908588589778128791635639992476076894152303569022736123671173); _sage_const_87360200456784002948566700858113190957688355783112995047798140117594305287669 = Integer(87360200456784002948566700858113190957688355783112995047798140117594305287669); _sage_const_6082896373499126624029343293750138460137531774473450341235217699497602895121 = Integer(6082896373499126624029343293750138460137531774473450341235217699497602895121); _sage_const_0 = Integer(0); _sage_const_2 = Integer(2); _sage_const_64 = Integer(64); _sage_const_5174653704092763360796229829845257205073345937937186983729251250965927323427 = Integer(5174653704092763360796229829845257205073345937937186983729251250965927323427); _sage_const_16 = Integer(16)
p = _sage_const_99061670249353652702595159229088680425828208953931838069069584252923270946291 
a = _sage_const_1  
b = _sage_const_4 
E = EllipticCurve(GF(p), [a,b]) 

G = E(_sage_const_43190960452218023575787899214023014938926631792651638044680168600989609069200 ,_sage_const_20971936269255296908588589778128791635639992476076894152303569022736123671173 )
A = E.lift_x(_sage_const_87360200456784002948566700858113190957688355783112995047798140117594305287669 )
B = E.lift_x(_sage_const_6082896373499126624029343293750138460137531774473450341235217699497602895121 )

a = discrete_log(A,G, operation = '+', bounds = (_sage_const_0 ,_sage_const_2 **_sage_const_64 )) 
ss = (a*B).xy()[_sage_const_0 ]

import hashlib 
from Crypto.Cipher import AES 
from Crypto.Util.Padding import unpad

flag =  {'iv': 'ceb34a8c174d77136455971f08641cc5', 'encrypted_flag': 'b503bf04df71cfbd3f464aec2083e9b79c825803a4d4a43697889ad29eb75453'}

ss = _sage_const_5174653704092763360796229829845257205073345937937186983729251250965927323427 
sha1 = hashlib.sha1() 
sha1.update(str(ss).encode('ascii'))
key = sha1.digest()[:_sage_const_16 ]

iv = bytes.fromhex(flag['iv'])
c = bytes.fromhex(flag['encrypted_flag'])

cipher = AES.new(key, AES.MODE_CBC, iv)
unpad(cipher.decrypt(c),_sage_const_16 ) 

