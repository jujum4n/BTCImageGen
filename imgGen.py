__author__ = 'juju'

from PIL import Image, ImageFont, ImageDraw
import urllib2, json, datetime

def getCoinbaseSpot():
    data = json.load(urllib2.urlopen('https://api.coinbase.com/v1/prices/spot_rate'))
    return data['amount']

def generateImage(PRICE, BGCOLOR, FONTCOLOR, WIDTH, HEIGHT):
    W, H = (WIDTH, HEIGHT)
    img = Image.new("RGBA", (W, H))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Merriweather-Regular.ttf", 36)
    msg = "1 BTC = " + str(PRICE)
    w, h = font.getsize(msg)
    draw.text(((W-w)/2, (H-h)/2), msg, FONTCOLOR, font=font)
    datefont = ImageFont.truetype("Merriweather-Italic.ttf", 18)
    datestr = str(datetime.datetime.now().strftime("%B %d, %Y - %H:%M:%S%p"))
    fw, fh = datefont.getsize(datestr)
    draw.text(((W-fw)/2, H-25), datestr, FONTCOLOR, font=datefont)
    img.save('cb_spot_rate.png', 'PNG')
    img.show()
    return img

def newCBImage():
    price = getCoinbaseSpot()
    generateImage(price, 'black', 'white', 326, 128)

newCBImage()

#https://blockchain.info/q/avgtxnumber
#https://blockchain.info/stats?format=json
#https://blockchain.info/q/getblockcount