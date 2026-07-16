import mpmath as mp

mp.mp.dps = 200

def fac(n):
    if n == 0 or n == 1:
        return 1
    return n * fac(n-1)

series = mp.mpf('0')
n = -1

print("math.pi =", mp.nstr(mp.pi, 100), end = "\n"*2)

while n < 0:
    n = int(input("How many terms?\n"))
    if n < 0:
        print("Try again")

for i in range(n):
    i_mpf = mp.mpf(i)
    term = ((-1)**i * fac(6*i) * (mp.mpf('545140134')*i_mpf + mp.mpf('13591409'))) / (fac(3*i) * fac(i)**3 * mp.power(mp.mpf('640320'), (3*i_mpf + mp.mpf('1.5'))))
    series += term

series *= mp.mpf('12')
mp.nprint(1/series, 100)
