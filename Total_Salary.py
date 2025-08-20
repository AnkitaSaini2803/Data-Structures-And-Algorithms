'''                                                      20-08-2025
Ninja just got an offer letter from a reputable company. The company sent him an offer letter along with the salary bifurcation.

In that bifurcation,Total Salary was not mentioned but instead a ‘basicSalary’ and an upper case character representing grade was mentioned, depending on which the Total Salary is calculated.

Help Ninja in calculating his total salary, where total salary is defined as:

‘totalSalary’ = ‘basic’ + ‘hra’ + ‘da’ + ‘allowance’ - ‘pf’
The above terms are as follows:

‘hra’ = 20% of ‘basic’
‘da’ = 50% of ‘basic’
‘allowance’ = 1700 if grade = ‘A’
‘allowance’ = 1500 if grade = ‘B’
‘allowance’ = 1300 if grade = ‘C' or any other character
‘pf’ = 11% of ‘basic’.
'x.5' type values will always be round up, for example, 1.5, 2.5 will be round off to 2, 3 respectively.

'''
from math import floor
basic=int(input('Enter:'))
grade=input('Enter: ')
def totalSalary(basic, grade):
	
	hra=(20/100)*basic
	da=(50/100)*basic
	if grade=='A':
		allowance=1700
	elif grade=='B':
		allowance=1500
	else:
		allowance=1300
	pf=(11/100)*basic
    
	res=basic+hra+da+allowance-pf
	return floor(res+0.5)

print(totalSalary(basic,grade))