import requests

URL = 'http://api.wordreference.com/1/json/enfr/tall'

HEADERS = {
    'Referer': 'http://www.wordreference.com/docs/api.aspx'
}

def main():
    r = requests.get(URL, headers=HEADERS)
    print(r.status_code)

if __name__ == '__main__':
    main()
