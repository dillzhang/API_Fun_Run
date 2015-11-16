from os import urandom
import unirest

secret_key = urandom(32)

# X-Mashape-Key
api_key = "frXllSpx5amshUV29IPWvrEiIk3Tp1qJGikjsnhgwldpgnfGEO"

# Translating API Links
yoda = "https://yoda.p.mashape.com/yoda?sentence=%s"
l33t = "https://montanaflynn-l33t-sp34k.p.mashape.com/encode?text=%s"
translator = [l33t]

# Meme Generator Link
memeURL = "http://apimeme.com/meme?meme=%(mem)s&top=%(top)s&bottom=%(bottom)s"
memes = ["Grandma+Finds+The+Internet", "Condescending+Wonka", "Grumpy+Cat+Table", "Hipster+Barista"]

fillertexts = ["1'll+wReCk+y0u+m8t3", "That's+Nice,+tell+me+more", "I+hate+you", "Been+there,+done+that"] 

unirest.default_header('X-Mashape-Key', api_key)


def generate(line, meme):
    if (meme == 0):
        line = translate(line, meme)
    return memeURL%{'bottom': fillertexts[meme], 'mem': memes[meme], 'top': line}


def translate(line, meme):
    line = line.replace(" ", "+")
    print line
    stringer = unirest.get(translator[meme] % (line), headers = {"Accept": "text/plain"})
    return stringer.body
