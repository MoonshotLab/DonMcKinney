import markovify

def invent():
    # open the seed text and create a model
    with open('seed.txt') as f:
        seed_text = f.read()
    text_model = markovify.Text(seed_text)

    # create the idea
    idea = text_model.make_sentence(tries=100)
    return idea
