import seed
import idea
import voice
import gpio


def ideate():
    big_idea = idea.invent()
    print("NEW IDEA: \t" + big_idea)
    voice.say(big_idea)


seed.scheduleDownloader()
gpio.listen(ideate)
