import json
import logging

import scrapy

API_URL = 'http://api.wordreference.com/1/json/enfr/{}'

HEADERS = {
    'Referer': 'http://www.wordreference.com/docs/api.aspx'
}

class EnglishToFrench(scrapy.Spider):
    name = "english-to-french"

    def start_requests(self):
        with open('wordlists/english-20k.txt') as f:
            words = [raw.strip() for raw in f.readlines()]
        
        urls = [API_URL.format(word) for word in words]

        for word in words:
            meta = {'word': word}
            url = API_URL.format(word)

            yield scrapy.Request(url=url, callback=self.parse, headers=HEADERS, meta=meta)
    
    def parse(self, response):
        server_response = json.loads(response.text)

        if 'Error' in server_response:
            logging.warning('Error response')
        elif response.status != 200:
            logging.warning('Non 200 response')
        else:
            yield {
                'url': response.request.url,
                'word': response.meta['word'],
                'body': json.loads(response.text)
            }
