import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        json_list = []
        items = json.loads(self.get_response_body())
        # for item in items:
        #     json_list.append(item["name"])
            
        return items
    
# items = GetRequester(url="https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json").get_response_body()
# print(items)
  
get_requester = GetRequester(url="https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json")
people = get_requester.load_json()
print(people)
