import seed
import idea
import voice
import gpio
import time


def ideate():
    big_idea = idea.invent()
    print(big_idea)
    voice.say(big_idea)


seed.scheduleDownloader()
gpio.listen(ideate)
