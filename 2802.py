n=  int(input())
combinacao2 = (n*(n-1))/2
combinacao4 = (n*(n-1)*(n-2)*(n-3))/(1*2*3*4)
a = int(1 + combinacao2 + combinacao4)
print(a)