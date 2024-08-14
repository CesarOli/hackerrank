def reverse_array(arr):
    
    n = len(arr)
    
    for i in range(n//2):
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
    
    return arr

if __name__=="__main__":
    size = int(input('Informe um número, este número representará o tamanho do array:'))
    arr = []

    for i in range(size):
        element = int(input(f'Informe o elemento {i + 1} :' ))
        arr.append(element)

reversed_array = reverse_array(arr)
print('O array no formato reverso/invertido é: ', reversed_array)