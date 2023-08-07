import requests

def get_url_content(url:str):
    try:
        r = requests.get(url)
        write_file(r.text)
    except Exception as error:
        print(error)


def write_file(content:str):
    with open('./html/content.html','+w') as file:
        file.write(content)