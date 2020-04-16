s1= ['Ahmad', 18, 17, 19.5, 8, 25]
s2= ['Sami', 20, 20, 19, 9, 28]
s3= ['Faris', 14.5, 16, 13, 7, 23]

s = input("Enter student's name: ")

if s in s1:
    print(s, sum(s1[1:]))
elif s in s2:
    print(s, sum(s2[1:]))
elif s in s3:
    print(s, sum(s3[1:]))

else:
    print("student is not recorded", 0)
