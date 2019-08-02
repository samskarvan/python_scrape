from selenium import webdriver
from lxml import html
from lxml.etree import fromstring
from cssselect import GenericTranslator, SelectorError
from string import Template
# s = Template('https://www.seasonalfoodguide.org/$state/$season')
# s.substitute(state='california', season='late-october')

def createpath(state, season):
    x = "https://www.seasonalfoodguide.org/%s/%s" % (state, season)
    # print x
    return x
# state = "california"
# season = "late-october"

def createCSVFileName(season, state):
    y = "%s_%s.csv" % (season, state)
    # print y
    return y
# y = "Those who know %s and those who %s." % (binary, do_not)
# print x
# print Template('https://www.seasonalfoodguide.org/$state/$season').substitute(s)
browser = webdriver.Chrome('/Users/samskarvan/Desktop/pythonScrape/chromedriver') #replace with .Firefox(), or with the browser of your choice
# url = createpath('california', 'early-november')
# url = createpath('california', 'early-february')
l = 'late'
s = 'alaska'
m = 'january'
url = "https://www.seasonalfoodguide.org/%s/%s-%s" % (s, l, m)
print (url)
browser.get(url) #navigate to the page

# browser.get("http://example.com/page.php") #navigate to page behind login
innerHTML = browser.execute_script("return document.body.innerHTML") #returns the inner HTML as a string

htmlElem = html.document_fromstring(innerHTML) #make HTML element object
# print htmlElem
# print innerHTML


# tdElems = htmlElem.cssselect("[.card-title]") #list of all td elems
# for elem in tdElems:
#     text = elem.text_content() #text inside each td elem 
#     tdElem1 = htmlElem.cssselect("[.card-title]")[0] #first td elem 
#     text = elem.text_content()
#     splitText = text.split("\n") #returns list of text in between "\n" chars
#     print(splitText)\


# csvFilename = "lateOctober_CA.csv" #what name you want to save your csv as
csvFilename = createCSVFileName('earlyFebruary', 'CA')
# print csvFilename
csv = open(csvFilename, "w") #create or open csv, "w" to write strings
colNames = "Name\n" #column titles
csv.write(colNames)
 
print(htmlElem)
expression = GenericTranslator().css_to_xpath('.card-title')
# print(expression)
# document = fromstring(innerHTML)
# print htmlElem.xpath(expression)
# inner = [e.get('.card-title') for e in htmlElem.xpath(expression)]
async inner = await htmlElem.xpath(expression)
print (inner)
# print inner
for elem in inner:
    # text = elem.nodeValue() #text inside each td elem 
    tdElem1 = inner[0] #first td elem 
    text = elem.text_content()
    # print text
    splitText = text.split("\n")[0] #returns list of text in between "\n" chars
    csv.write(splitText + "\n") #write to csv
    print ('csv file created')
    # print splitText

    # print(etree.tostring(root, pretty_print=True))