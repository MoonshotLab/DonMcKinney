import markovify
import seed

seed.scheduleDownloader()

with open('seed.txt') as f:
    text = f.read()

text_model = markovify.Text(text)

sentence = text_model.make_sentence(tries=100)
print sentence
