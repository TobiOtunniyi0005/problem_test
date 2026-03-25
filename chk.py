import math
from decimal import Decimal, getcontext

iRoundPres = 10
iDecPres = 50
getcontext().prec = iDecPres
frac = Decimal(0)
num = 2
lastp = Decimal(1)
id = Decimal(-1)
#prev

def is_perfect_square(n):
    if n < 0:
        return False
    root = math.isqrt(n)  # Efficient integer square root
    return root * root == n


def fracer(frac,n):
   r1 = frac*(n)
   if (-1)**(n-1)==1:
      r2 = math.floor(r1)
   else:
      r2 = math.ceil(r1)
   r3 = (r1-r2)/n# Get the excess
   r1 = n*(frac-r3)#Remove the excess
   print(r1)
   return r1

def test(pre, cur):
   print('Mango')

while (num<1000):
   print(f'num = {num}')
   pre = fracer(frac, num+1)
   cur = fracer(frac, num )

   pre = fracer(frac, num-1)
   
   if (round((10**iRoundPres)*pre) == round((10**iRoundPres)*cur)):# and not(is_perfect_square(num)):
      frac = frac-frac/(num)+Decimal(1/(num))
      print(f'\n +-+-+-+-+-+-+-+- \nNew addition: {num} The updated fraction: {frac}')
      lastp = num
   else:
      print('Not found')
   num=num+1
   id *=-1