import requests
from bs4 import BeautifulSoup

def main():
    # title = input('Title: ')
    # url = input('URL: ')
    title = 'RP-1'
    url = 'https://github.com/KSP-RO/RP-0/wiki'
    print(f'Title of PDF will be {title}.pdf')
    print(f'Url will pull from {url} and will limit to Subdirectories of that URL.')
    html = requests.get(url)
    write_HTML_file(html, url, title)

def clean_HTML(html):
    soup = BeautifulSoup(html.content, 'html.parser')
    #clean this later


def write_HTML_file(html, url, title):
    filename = title
    filename = filename + url.split('/')[-1] + '.html'
    with open(f'data/HTML/{filename}', 'w+') as file:
        file.write(html.text)


if __name__ == '__main__':
    main()


# TODO
# Reorganize based on relative link system. files should match urling.
