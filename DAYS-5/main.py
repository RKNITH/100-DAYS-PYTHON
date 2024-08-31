#  FOR LOOP
a =['1','2','3']
for i in a:
    print(i)

# 
score =[120,123,190,112,100]
sum =0
for i in score:
    sum+=i
print(sum)  

print(max(score))

#  FINDING MAX VALUE USING FOR LOOP
maxi =0
for i in score:
    if i>maxi:
        maxi=i
print(maxi)        


# sum n natural number(1 to 100)
#  range(a, b) , starts from a and end with b-1, not include b
sum =0
for i in range(101):
    sum +=i
print(sum)   




