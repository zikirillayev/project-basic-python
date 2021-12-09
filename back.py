import random
# list()
# s = "python"
# l = list(s)
# print(type(l))
# print("p" in l)

# r = range(0,101,10)
# for  i in r: print(i , end=" ")

# arr = list("123456")
# arr = [1,2,3,4,5]
# for i in arr:
#     print(i)

# arr = [1,2,4,5,9,6]
# arr2 = [8,9]
# arr.append(6) #oxiriga element qo`shish
# arr.extend(arr2) #siz korsatgan massive bilan kengaytiruvchi
# arr.insert(5, "HI ko`shildim ") #faqat bitta qo`sha olasiz
# arr.pop(5) #siz korsatgan elemni index boyicha ochiradi 
# #POP() ga index korsatmasez oxiridan oxhirvoradi
# del arr[0] #siz korsatgan elemni ochirvoradi tubdan ochiradi yani polni
# arr.remove(4) #ochiradi
# # arr.clear()
# # arr.sort()
# print(arr.count(9))#nechta shu qiymat berilganini qaytaradi
# print(any([1,2,3,0])) #listda 1ta true qiymat bolsa ham qolgani false bolsa ham True qaytaradi 
# print(all([1,2,3,4,5,6,8,9,0])) # bu esa listda 1ta false bolsa ham false qaytaradi
# arr.reverse() #teskari qilib qaytaradi
# print(arr)
# rArr = reversed(arr) #kompni qayerida joylashganini qaytaradi
# print(rArr)
# print(list(rArr))

# import random 
# print(random,random()
# print(random.randint(0,10))
# print(random.randint(0,10,2))
# arr = [1,2,3,4,5,6,7,8,9,]
# random.shuffle(arr)
# print(arr)
# str = "assalomualaykum"
# print(random.sample(str,5))

# arr = [1,2,3,4,5,6,7,8,9]
# # arr.sort(reverse=True)
# sorted(arr, )
# print(arr)
# # print(random.choice(arr))

# strArr = ["python" , "pytHon"]
# mass = []
# for i in range(50):
#     mass.append(i)
# print(mass)

# print(list(random.sample(range(0,100),20))) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# print(list(range(0,50,2)))

# user = int(input("son 0-20"))
# for i in range(10):
#     r = random.choice(range(1,10))
#     if user == r:
#         print("you won")
# else:
#      print("you couldn`t")    

# task suming
# a = 1
# b = 50
# li = list(range(a,b))
# ra = random.sample(li,10)
# print(ra)
# print(sum(ra))

a = [1,2]
b = [1,2]
for i in a:
    if i in b:
       a.remove(i)
else:
    for x in b:
       b.remove(x)
    a.extend(b)
print(a)