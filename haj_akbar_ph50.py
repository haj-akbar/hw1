#delta!!!
a = float(input ("enter a : "))
b = float(input ("enter b : "))
c = float(input ("enter c : "))
delta = (b ** 2 +(-4 * a * c))
x = (delta ** (1 / 2))
if delta > 0 :
    d = (((-1 * (b)) + x) / (2 * a))
    e = ( ((-1 * (b)) - x) / (2 * a))
    print(d , e)
if delta == 0 :
    s = ((-1 * (b)) / (2 * a))
    print(s)
if delta < 0 :
    print (" There is no quota")
                      
