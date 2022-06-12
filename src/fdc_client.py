import json

import requests

from fdc_parse_utils import parse_search_result, parse_get_results
from objects.diet import Diet


class FdcClient:
    url = 'https://api.nal.usda.gov/fdc/v1'

    def __init__(self, api_key):
        self.api_key = api_key

    def call(self, params, url_suffix):
        target_url = self.url + url_suffix
        call_params = dict(params, api_key=self.api_key)
        return json.loads(requests.get(url=target_url, params=call_params).text)

    def search_foods(self, phrase, pageNumber=1):
        params = dict(
            query=' '.join(map(lambda s: '+' + s, phrase.split(' '))),
            pageNumber=pageNumber
        )
        return parse_search_result(self.call(params, '/foods/search'))

    def get_foods(self, id_amount_dict, name='Default'):
        params = dict(
            fdcIds=id_amount_dict.keys()
        )
        query_result = self.call(params, '/foods')
        return parse_get_results(query_result, id_amount_dict.values(), name)

    def get_meals(self, meals):
        mea = [self.get_foods(ingredients, name) for meal in meals for name, ingredients in meal.items()]
        return Diet(mea)
