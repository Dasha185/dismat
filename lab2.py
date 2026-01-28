a = [[0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]]

while True:
    binary = '01'
    f = input('Введите число: ')
    
    if len(f) != 16:
        print('число должно содержать 16 символов')
        continue
    
    is_binary = True
    for digit in f:
        if digit not in binary:
            is_binary = False
            break
    
    if not is_binary:
        print('число не двоичное')
        continue
    else:
        break

a[0][0] = int(f[0])
a[0][1] = int(f[1])
a[0][2] = int(f[3])  
a[0][3] = int(f[2])  
a[1][0] = int(f[4])
a[1][1] = int(f[5])
a[1][2] = int(f[7]) 
a[1][3] = int(f[6]) 
a[2][0] = int(f[12])  
a[2][1] = int(f[13]) 
a[2][2] = int(f[15]) 
a[2][3] = int(f[14]) 
a[3][0] = int(f[8]) 
a[3][1] = int(f[9]) 
a[3][2] = int(f[11]) 
a[3][3] = int(f[10]) 

print(a)