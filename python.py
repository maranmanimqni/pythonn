# # print("Mani")

# a = int(input("number"))
# if a <= 4:
#     print ("postive")
# else:
#     print ("negative")


# a=int(input("number:"))
# if a>0:
#     if a % 5 == 0:
#         print("divisible by 5")
#         if a % 10 == 0:
#             print("divisable by 10")
#         else:
#             print("not divisable by 10")
#     else:
#         print("not divisable 5")
# else:
#     print("number is not divisable by 0")


# user_name="mani"
# pas_sword="mani123"
# user=input("user name:")
# pas=input("Enter the passowed:")
# if user_name==user:
#     if pas_sword==pas:
#         print("Login Successful")
#     else:
#         print("incurrect possword")
# else:
#     Print("forget username")


# s= input("enter the value:")
# che = 0
# for ch in s:
#     if ch.lower()in "aeiou":
#         che += 1
# print("vowels:",che)

# string

# s = input()
# n = int(input("Enter times: "))

# for ch in s:
#     print(ch * n, end="")
#     s = input()
# result = ""

# for ch in s:
#     if ch not in result:
#         result += ch

# print(result)s = input()
# count = 0

# for ch in s:
#     if ch.lower() not in "aeiou" and ch.isalpha():
#         count += 1

# print("Consonants:", count)s = input()

# if 'a' <= s[0] <= 'z':
#     s = chr(ord(s[0]) - 32) + s[1:]

# print(s)s = input()

# for ch in s:
#     if ch.lower() in "aeiou":
#         break
#     print(ch, end="")


# t1 = (10,"hema",6.88)
# print(t1)


# t1 = (10,"hema",6.88)
# print(t1[1])

# t1 = (10,"hema",6.88,89)
# print(t1[2:])

# t1 = (1,2)+(3,4) 
# print(t1)

# t1 = (7,9) *3
# print(t1)

t1 =(10,20,30,40,)
print(15 in t1)