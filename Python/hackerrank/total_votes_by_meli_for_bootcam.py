import requests


def get_vote_count(city_name, estimated_cost):
    
    url = f"https://jsonmock.hackerrank.com/api/food_outlets?city={city_name}&estimated_cost={estimated_cost}"
    total_votes = 0
    page = 1 
    
    while True:
        response = requests.get(url + f'&page={page}')
        data = response.json()

        if not data['data']:
            break

        for outlet in data['data']:
            if 'user_rating' in outlet and 'votes' in outlet['user_rating']:
                total_votes += outlet['user_rating']['votes']
        
        page += 1
        if page > data['total_pages']:
            break
    return total_votes if total_votes > 0 else -1

if __name__ == '__main__':
    city_name = input('Informe o nome da cidade: ')
    estimated_cost = int(input('Informe o custo estimado: '))

    result = get_vote_count(city_name, estimated_cost)
    print(f'Total de votos: {result}')

