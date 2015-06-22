from django.shortcuts import render
from imageGen.models import BitcoinInfo
from PIL import Image, ImageFont, ImageDraw
import urllib2, json, time, datetime

fontpath = 'C:\\Users\\chasej\\PycharmProjects\\BTCImageGen\\imageGen\\'
imagepath = 'C:\\Users\\chasej\\PycharmProjects\\BTCImageGen\\imageGen\\static\\'
fontttf = 'Merriweather-Regular.ttf'
fontitalttf = 'Merriweather-Italic.ttf'


def generateImage(PRICE, FONTCOLOR, WIDTH, HEIGHT, IMAGENAME):
    W, H = (WIDTH, HEIGHT)
    # New Transparent Image
    img = Image.new("RGBA", (W, H))
    #Draw Image Data
    draw = ImageDraw.Draw(img)
    #Font for Bitcoin Price
    font = ImageFont.truetype(fontpath + fontttf, 320)
    msg = "1 BTC = " + str(PRICE)
    #Put the font in the direct center of the image
    w, h = font.getsize(msg)
    draw.text(((W - w) / 2, (H - h) / 2), msg, FONTCOLOR, font=font)
    #Font for the Date
    datefont = ImageFont.truetype(fontpath + fontitalttf, 160)
    datestr = str(datetime.datetime.now().strftime("%B %d, %Y - %I:%M:%S%p"))
    #Put the date in the center 25 pixels from the bottom
    fw, fh = datefont.getsize(datestr)
    draw.text(((W - fw) / 2, H - 250), datestr, FONTCOLOR, font=datefont)
    #Take the image, scale it down to 10% of the original size
    im = img
    #Create thumbnail
    im.thumbnail((326, 128), Image.ANTIALIAS)
    #Save the image
    im.save(imagepath + IMAGENAME, "PNG", quality=100)
    return im


def getBitcoinInfo():
    bitinfo = BitcoinInfo.objects.last()
    if (int(time.time()) > bitinfo.last_checked + 10):
        print 'getting new price'
        jsonobject = json.load(urllib2.urlopen('https://api.coinbase.com/v1/prices/spot_rate'))
        bitcoin_price = jsonobject['amount']
        bcinfo = BitcoinInfo()
        bcinfo.last_checked = int(time.time())
        bcinfo.price = bitcoin_price
        bcinfo.save()
        generateImage(bitcoin_price, 'black', 3260, 1280, 'cb_spot_transparent_black_merriweather.png')
        generateImage(bitcoin_price, 'white', 3260, 1280, 'cb_spot_transparent_white_merriweather.png')
        return bcinfo
    return bitinfo


# Home view
# Pre: Takes in a request
# Post: Renders our homepage
def home(request):
    # Get the latest Coinbase Spotrate Information
    bit_info = getBitcoinInfo()
    absolute_uri = request.build_absolute_uri()
    last_checked = datetime.datetime.fromtimestamp(bit_info.last_checked).strftime("%B %d, %Y - %I %H:%M:%S%p")
    return render(request, 'home.html',
                  {'price': bit_info.price, 'last_checked': last_checked, 'absoluteurl': absolute_uri})
