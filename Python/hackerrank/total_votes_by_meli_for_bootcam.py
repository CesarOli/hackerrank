def get_vote_count(city_name, estimated_cost):
    
    url = f"https://jsonmock.hackerrank.com/api/food_outlets?city={city_name}&estimated_cost={estimated_cost}"
    total_votes = 0
    page = 1 
    
    while True:
        response = request.get(url + f'&page={page}')
        data = response.json()

        if not data['data']:
            break

        for outlet in data['data']:
            total_votes += outlet['user_rating']['vote']
        
        page += 1
        if page > data['total_pages']:
            break
    return total_votes if total_votes > 0 else -1

if