import math
from decimal import Decimal, getcontext

#You can't just get the right answer because the sum of the fractions cannot be seperated into the positive and the negative sectors. You
#Nah, that was because of the negative and positives, now that thery are seperated we are trying to get numbers smaller than 1/2 that's all. If not 1/3 and on till we get to the latest...Update, it is actually impossible to seperate individually.
#This is as good as it gets bro.
neg = 0
pos = 1/2
num = 2

tpos = 0
tneg = 0

def test(n,pos1,neg1):
   neg2 = math.floor(neg1*n)
   pos2 = math.floor(pos1*n)

   print(f'{pos2-neg2}')
   return pos2-neg2

def is_perfect_square(n):
    if n < 0:
        return False
    root = math.isqrt(n)  # Efficient integer square root
    return root * root == n
   
def test2(n,pos1,neg1):
   neg2 = math.floor(neg1*n)
   pos2 = math.floor(pos1*n)

   tneg = neg1+pos1/n
   tpos = pos1+1/n
   neg3 = math.floor(tneg*n)
   pos3 = math.floor(tpos*n)
   print(f'pneg:{neg2}, nneg:{neg3} ppos:{pos2}, npos:{pos3}')
   if (neg2==neg3) and (pos2+1==pos3):
      return True


#num = 2
#lastp = 2
#while (num<=100) and (num>=2):
#   if (num*(pos-neg)==math.floor(num*(pos-neg))) and (num>lastp):
#      tnum = num*(pos-neg)+1#+1 added
#      neg += pos/(tnum)
#      pos += 1/(tnum)
#      print(f'New addition: {tnum} Updated pos: {pos}, Updated neg: {neg} Updated Frac: {pos-neg}\n')
#      lastp = num
#   else:
#      print(f'{num} not accepted.\n')
#   num +=1

while (num<=1000) and (num>=1):      
   num = 2*num*(pos-neg)

   #tneg += neg + (pos)/(num)
   #tpos += pos + 1/(num)
   #while ()
   neg += (pos)/(num)
   pos += 1/(num)
   print(f'New addition: {num} Updated pos: {pos}, Updated neg: {neg} Updated Frac: {pos-neg}\n')
   #lastp = num


