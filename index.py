import os
import urllib2

googleDocId = os.environ['GOOGLE_DOC_ID']
print googleDocId

url = ''.join([
  'https://docs.google.com/document/d/',
  googleDocId,
  '/export?format=txt'
])

response = urllib2.urlopen(url)
html = response.read()

text_file = open('seed.txt', 'w')
text_file.write(html)
text_file.close()
