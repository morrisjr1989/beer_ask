import requests
import json
from collections import namedtuple


class QueryForBeer:
    def __init__(self, city, state):
        #self.search_term = search_term
        self.city = city
        self.state = state

    # def GeneralQuery(self):
    #     data = requests.get(''.join(['https://api.openbrewerydb.org/breweries/?query=',self.search_term]))
    #     data = data.json()
    #     results = []
    #     for each_brewery in data:
    #         data = json.dumps(each_brewery)
    #         results.append(json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values())))
    #     return results

    def LocationQuery(self):
        data = requests.get('https://api.openbrewerydb.org/breweries?by_city={}&by_state={}'.format(self.city, self.state))
        data = data.json()
        results = []
        for each_brewery in data:
            data = json.dumps(each_brewery)
            results.append(json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values())))
        return results

    

# city = 'Harrisonburg'
# state = 'Virginia'

# breweries = QueryForBeer(city, state).LocationQuery()

# print('I have found {} breweries for {}, {}'.format(len(breweries), city, state))

# for brewery in breweries:
#     print('{}, on {}'.format(brewery.name, brewery.street))
#     print('{} is a {}'.format(brewery.name, brewery.brewery_type))

def main():
    pass

if __name__ == '__main__':
    main()

