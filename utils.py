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
meme = "https://ronreiter-meme-generator.p.mashape.com/meme?bottom=%s&font=%s&font_size=%s&meme=%s&top=%s"


unirest.default_header('X-Mashape-Key', api_key)


def generate(line, meme):
    return 0


def translate(line, meme):
    line = line.replace(" ", "+")
    print line
    stringer = unirest.get(translator[int(meme)] % (line), headers = {"Accept": "text/plain"})
    return stringer.body
