#! /bin/python

import requests
import bs4
import html2text
import mdv
import re
import os
import sys

URL_PARTERN = os.environ.get('URL_PARTERN')
CONTENT_SELECTOR = os.environ.get('CONTENT_SELECTOR')

def echoDescMarkdown(image):
    image = image.split(':')[0]
    full_image = 'library/'+image if image.find('/') == -1 else image
    url = URL_PARTERN.replace('#IMAGE#', full_image)
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    htmls = soup.select(CONTENT_SELECTOR)
    if len(htmls) < 1:
        print 'No content found!'
        sys.exit(1)
    content = u''.join([unicode(x) for x in htmls[0].contents]).strip()
    #md = html2text.html2text(content)
    h = html2text.HTML2Text()
    h.ignore_links = True
    md = h.handle(content)
    colorText = mdv.main(md, theme='584.2214')
    print re.sub(r'<br\s*/?>', '', colorText)

args = sys.argv[1:]

if __name__ == "__main__":
    if len(args) < 1:
        printUsage()
        sys.exit(1)
    [echoDescMarkdown(arg) for arg in args]
