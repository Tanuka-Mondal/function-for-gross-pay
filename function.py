#Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. The function should return a value. 


def computepay(h,r):
   if h<=40:
       Pay=hr
       return Pay
   else:
       Pay=(40*r)+((h-40)*1.5*r)
       return Pay
hrs = input('Enter Hours:')
h=float(hrs)
rate = input('Enter Rate:')
r=float(rate)
pay=computepay(h,r)
print("Pay", pay)
