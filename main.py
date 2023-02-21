import requests
from bs4 import BeautifulSoup

def main():
    title = input('Title: ')
    url = input('URL: ')
    print(f'Title of PDF will be {title}.pdf')
    print(f'Url will pull from {url} and will limit to Subdirectories of that URL.')
    HTML = requests.get(url)
    print(HTML.text)


def clean_HTML(HTML):
    soup = BeautifulSoup(HTML.content, 'html.parser')
    #clean this later


def write_HTML_file(HTML, url, title):
    filename = title
    filename = filename + url.split('/')[-1] + '.html'


if __name__ == '__main__':
    main()


