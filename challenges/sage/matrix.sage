from Crypto.Util.number import long_to_bytes

P = 2
N = 50 
e = 31337


FLAG = b'crypto{??????????????????????????}'

def load_matrix(fname):
    data = open(fname, 'r').read().strip()
    rows = [list(map(int, row)) for row in data.splitlines()]
    return Matrix(GF(P), rows)


c = load_matrix("../data/matrix.enc")
d =  pow(e, -1, c.multiplicative_order()) 
flag_matrix = c^d



s = ''.join(str(flag_matrix[j][i]) for i in range(N) for j in range(N))

s = s[:len(FLAG) * 8]
print(long_to_bytes(int(s,2)))
