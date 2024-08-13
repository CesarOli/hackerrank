def reverse_array(arr):
    
    n = print(input('informe o tamanho do array : ', len(arr)))
    
    for i in range(n//2):
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
    
    return arr

if __name__=="__main__":
    size = int(input('Informe um número, este número representará o tamanho do array:'))
    arr = []

for _ in range(size):
    element = int(input('Informe o elemento {_ + 1} :' ))
    arr.append(element)

    