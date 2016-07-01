import threading
import feedparser
import os
import urllib2
from bs4 import BeautifulSoup


def scheduleDownloader():
    download()


def download():
    print 'downloading new seed...'

    # overwrite the old seed file
    f = open('seed.txt', 'w+')
    f.write('')
    f.close()
    f = open('seed.txt', 'a')

    # fetch new seed from rss feed
    while True:
        print('retrieving page ' + str(page) + ' from rss feed')
        url = os.environ['RSS_LINK'] + str(page)

        feed = feedparser.parse(url)
        if(len(feed['entries'])):
            content = urllib.urlopen(feed['entries'][0]['link']).read()
            soup = BeautifulSoup(content, 'html.parser')
            entry = soup.select('.entry-content')
            text = entry[0].getText()
            f.write(text.encode('utf-8'))

            page+=1
        else:
            print('done fetching rss feed')
            break

    # close the file
    f.close()

    # recurse, download new file every hour
    threading.Timer(3600, download).start()
    print "scheduling new seed download for one hour into the future"
