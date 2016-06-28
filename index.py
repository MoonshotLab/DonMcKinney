import os
import urllib2
import markovify

googleDocId = os.environ['GOOGLE_DOC_ID']

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

with open('seed.txt') as f:
  text = f.read()

text_model = markovify.Text(text)

sentence = text_model.make_sentence(tries=100)
print sentence
