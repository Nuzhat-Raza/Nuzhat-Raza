from functools import reduce

f = lambda a,b : a*b

result = f(3,5)
print(result)
#Filters#
nums = [2,4,6,7,8,9,3,1,0,8,10,13]
evens = list(filter(lambda n: n%2==0, nums))
odds = list(filter(lambda n:n%2!=0, nums))
print("Evens are :", evens)
print("Odds are :", odds)

#Map#
doubles = list(map(lambda n: n*2, odds))
print("Doubles of Odds is ", doubles)

#Reduce
sum = reduce(lambda a,b:a+b, doubles)
print("Sum is ", sum)

temp = [1,2,'a','b','c',4,[0,1,2],5]

merge= reduce(lambda a,b:a+b, temp)

print(merge)
