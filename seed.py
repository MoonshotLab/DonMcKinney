import threading
import os
import urllib2


googleDocId = os.environ['GOOGLE_DOC_ID']

url = ''.join([
    'https://docs.google.com/document/d/',
    googleDocId,
    '/export?format=txt'
])


def scheduleDownloader():
    download()


def download():
    print "downloading new seed..."

    response = urllib2.urlopen(url)
    html = response.read()

    text_file = open('seed.txt', 'w')
    text_file.write(html)
    text_file.close()

    print "seed downloaded!"
    # recurse, download new file every hour
    threading.Timer(3600, download).start()
    print "scheduling new seed download for one hour into the future"
