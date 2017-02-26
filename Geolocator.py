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
    return data['results'][0]['geometry']['location']


if __name__ == '__main__':
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address=Fenway%20Park'
    data = read_data(url)
    print(address_name(data))
    print(lng_lat(data))
