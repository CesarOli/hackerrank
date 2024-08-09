def statement():
    print('''
     
    ''')

def breakingRecords(scores):
    
    maximo_score = scores[0]
    minimo_score = scores[0]
    maximo_breaks = 0
    minimo_breaks = 0

    for score in scores[1:]:
        if score > maximo_score:
            maximo_score = score
            maximo_score += 1
        elif score < minimo_score:
            minimo_score = score
            minimo_breaks += 1

    return [maximo_breaks, minimo_breaks]

if __name__ == '__main__':

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)
