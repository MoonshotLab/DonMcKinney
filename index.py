import seed
import idea
import voice
import gpio
import printer


def ideate():
    big_idea = idea.invent()
    print("NEW IDEA: \t" + big_idea)
    printer.output(big_idea)
    voice.say(big_idea)


seed.scheduleDownloader()
gpio.listen(ideate)
