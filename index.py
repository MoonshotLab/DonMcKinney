import markovify
import seed
import pyttsx

# schedule the seed updater
seed.scheduleDownloader()

# configure the voice
voice = pyttsx.init()
voice.setProperty('rate', 170)
voice.setProperty('voice', 'default')

# open the seed text and create a model
with open('seed.txt') as f:
    seed_text = f.read()
text_model = markovify.Text(seed_text)

# make an idea
idea = text_model.make_sentence(tries=100)
voice.say(idea)

# say it
print idea
voice.runAndWait()
