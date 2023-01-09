from json import dumps

from httplib2 import Http

from urllib.request import urlopen
from urllib.error import URLError
from urllib.error import HTTPError
from http import HTTPStatus
import time

def get_website_status(url):
    try:
        with urlopen(url) as connection:
            code = connection.getcode()
            return code
    except HTTPError as e:
        return e.code
    except URLError as e:
        return e.reason
    


def main():
    url = 'https://chat.googleapis.com/v1/spaces/AAAAyEJPTXc/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=dgZhpyZhjRgCQCglaKsirMfrALsV8D87sUMKcNegSSk%3D'
    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
    file = open("D:\webmonitoring\webs.txt", "r")
    l=[]
    bot={}
    for i in file:
        l.append(i)
    for i in range(len(l)):
        code = get_website_status(l[i])
        if code!=200:
            bot['text']="The website {} is down".format(l[i])
        
    http_obj = Http()
    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot),
    )
    print(response)


if __name__ == '__main__':
    main()