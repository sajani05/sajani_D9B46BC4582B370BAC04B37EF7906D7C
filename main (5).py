#1.1 Implement o recursive function tocalculate the factorial of a given number

"""
1!=1×1
2!=2 x 1! ---> 2 x 1 
3!= 3 ×2! --->3 x 1
.
.
10!=10 x 9! ---> 10 x 9 x... x 1
Formula - n ×(n-1)!
"""


1 fact_rec(n):
      if n==0 or n==1:
         return 1 
      else:
         return n*fact_rec(n-1)ppplk(((k kk(k.))))

number = int(input("Enter a value :"))
res = fact_rec (number)

print("The factorial of {} is{}".format(number,res))