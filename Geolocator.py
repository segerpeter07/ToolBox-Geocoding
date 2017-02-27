from urllib.request import urlopen
import json
from pprint import pprint


def read_data(url):
    """
    Given a valid location URL, reads the data into a JSON module
    """
    f = urlopen(url)
    response_text = f.read()
    response_data = json.loads(str(response_text, 'utf-8'))
    # pprint(response_data)
    return response_data


def address_name(data):
    """
    Given a valid JSON module, returns the vernacular name of the location
    """
    return data['results'][0]['formatted_address']


def lng_lat(data):
    """
    Given a vaid JSON module, returns the latitude and longitude of the location
    """
    lat = data['results'][0]['geometry']['location']['lat']
    lng = data['results'][0]['geometry']['location']['lng']
    return lat, lng


def url_maker(location):
    """
    Given a string query, converts to URL that can be used to find location
    """
    query = location
    words = []
    base = 'https://maps.googleapis.com/maps/api/geocode/json?address='
    words = query.split(' ')
    res = base
    i = 0
    while i < len(words):
        if i == 0:
            res = res + words[i]
        else:
            res = res + '%' + words[i]
        i += 1
    return res


if __name__ == '__main__':
    url = url_maker(input('Location: '))
    data = read_data(url)
    print(address_name(data))
    print(lng_lat(data))
