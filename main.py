import password_checker as checker

f = open('./dict.txt','r')

list = []
i = 1
while i < 5:
    i+=1
    list.append(f.readline())

print(list)