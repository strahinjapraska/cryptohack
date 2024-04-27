px = 2582928974243465355371953056699793745022552378548418288211138499777818633265 #x1 
py = 2421683573446497972507172385881793260176370025964652384676141384239699096612 #y1 
gx = 8742397231329873984594235438374590234800923467289367269837473862487362482 # x2 
gy = 225987949353410341392975247044711665782695329311463646299187580326445253608 # y2 
p = 4368590184733545720227961182704359358435747188309319510520316493183539079703


Zn = Integers(p) 
x1_sub_x2 = Zn(px - gx) 
x1_sub_x2_inv =  x1_sub_x2 ^-1

a = (((py**2 - gy**2) - (px**3 - gx**3))*x1_sub_x2_inv) %p
b = (py**2 - px**3 - a*px)%p

#E = EllipticCurve(GF(p), [a,b]) # will lead to error that we are trying to define a singular curve 

var('x y a_s b_s') 
curve_eq = x^3 + a_s*x + b_s - y^2  
dx = diff(curve_eq, x)
dy = diff(curve_eq, y)

#solution = solve([dx == 0, dy == 0], x, y)[0][0].rhs()
#print(solution) 
x_singular = mod((-pow(3,-1,p)*a)%p,p).sqrt()

P.<x> = GF(p)[] 
f = x^3 + a*x + b 
P = (px, py) 
Q = (gx, gy) 

f_ = f.subs(x = x+x_singular) 
P_ = (P[0] - x_singular, P[1]) 
Q_ = (Q[0] - x_singular, Q[1])

#print(f_.factor())
r = 305179796174210822247618473361747316085422620437271958999235012896334193460
t = GF(p)(r).square_root() 

v = (P_[1] + t*P_[0])/(P_[1] - t*P_[0]) % p
u = (Q_[1] + t*Q_[0])/(Q_[1] - t*Q_[0]) % p

print(discrete_log(v,u)) 