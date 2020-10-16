tamB=0
tamA=0
K=0

print("Insira o tamanho da string:")
n = int(input())
print("Insira os valores em binário para a string1:")
s1 = input()
print("Insira os valores em binário para a string2:")
s2 = input()

for i in range(n):
    if(s1[i]!=s2[i]):
        tamA=tamA+(i+1)
        # print("Tamanho de A = ",tamA)
        
if(tamA%2==0):
    tamB=tamA/2
    # print("Tamanho de A e B = ",tamA, tamB)
    
else:
    K=int(tamA/2)
    tamB=(K+2)
    # print("tamanho de A e B = ",tamA, tamB)
    # print("K = ",K)

print(int(tamB))
