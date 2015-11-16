from os import urandom
import unirest

secret_key = urandom(32)

# X-Mashape-Key
api_key = "frXllSpx5amshUV29IPWvrEiIk3Tp1qJGikjsnhgwldpgnfGEO"

# Translating API Links
yoda = "https://yoda.p.mashape.com/yoda?sentence=%s"
l33t = "https://montanaflynn-l33t-sp34k.p.mashape.com/encode?text=%s"
translator = [yoda, l33t]

# Meme Generator Link
memeURL = "http://apimeme.com/meme?meme=%(mem)s&top=%(top)s&bottom=%(bottom)s"
memes = ["Advice+Yoda", "Grandma+Finds+The+Internet", "Condescending+Wonka", "Grumpy+Cat+Table", "Hipster+Barista"]

unirest.default_header('X-Mashape-Key', api_key)


def generate(line, meme):
    if (meme == 0 or meme == 1):
        line = translate(line, meme)
    return memeURL%{'bottom': "Filler", 'mem': memes[meme], 'top': line}


def translate(line, meme):
    line = line.replace(" ", "+")
    print line
    stringer = unirest.get(translator[meme] % (line), headers = {"Accept": "text/plain"})
    return stringer.body
