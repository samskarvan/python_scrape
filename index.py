from selenium import webdriver
from lxml import html
from lxml.etree import fromstring
from cssselect import GenericTranslator, SelectorError
from string import Template
from threading import Timer
import asyncio
# s = Template('https://www.seasonalfoodguide.org/$state/$season')
# s.substitute(state='california', season='late-october')

seasonList = ['early', 'late']
monthList = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
stateList = []

states = ['Alaska']
# , 'Alabama', 'Arkansas', 'Arizona',] 

# 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Guam', 'Hawaii', 'Iowa', 'Idaho', 'Illinois', 'Indiana', 'Kansas', 'Kentucky', 'Louisiana', 'Massachusetts', 'Maryland', 'Maine', 'Michigan', 'Minnesota', 'Missouri', 'Mississippi', 'Montana', 'North Carolina', 'North Dakota', 'Nebraska', 'New Hampshire', 'New Jersey', 'New Mexico', 'Nevada', 'New York', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Puerto Rico', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Virginia', 'Virgin Islands', 'Vermont', 'Washington', 'Wisconsin', 'West Virginia', 'Wyoming']
for s in states:
    stateList.append(s.lower())

# stateList = stateList[]

# for s in stateList:
#     for m in monthList:
    # for l in seasonList:
l = 'late'
s = 'alaska'
m = 'january'
url = "https://www.seasonalfoodguide.org/%s/%s-%s" % (s, l, m)
print (url)
browser = webdriver.Chrome('/Users/samskarvan/Desktop/pythonScrape/chromedriver') 
browser.get(url)
csvFilename = "%s_%s_%s.csv" % (l, m, s) #what name you want to save your csv as
csv = open(csvFilename, "w") #create or open csv, "w" to write strings
colNames = "Name\n" #column titles
csv.write(colNames)

innerHTML = browser.execute_script("return document.body.innerHTML") #returns the inner HTML as a string
htmlElem = html.document_fromstring(innerHTML) #make HTML element object
print (htmlElem)

expression = GenericTranslator().css_to_xpath('.card-title')
print(expression)
# print htmlElem
# document = fromstring(innerHTML)
# print htmlElem.xpath(expression)
# inner = [e.get('.card-title') for e in htmlElem.xpath(expression)]

# @asyncio.coroutine 
# async def print_sum(html):
    # return await html.xpath(expression)

def twoArgs(arg1,arg2):
    print (arg1)
    print (arg2)
    print ("")
async def inner(expression): 
    await asyncio.sleep(3) 
    return htmlElem.xpath(expression)
# print inner
inner = inner(expression)
# r = Timer(5.0, twoArgs, ('hello', 'world'))
# r.start()
print(inner)
for elem in inner:
    print ('scraping text...')
    # text = elem.nodeValue() #text inside each td elem 
    tdElem1 = inner[0] #first td elem 
    text = elem.text_content()
    # print text
    splitText = text.split("\n")[0] #returns list of text in between "\n" chars
    csv.write(splitText + "\n") #write to csv
    print ('csv file created')
    # print splitText
# browser.close()


# state = "california"
# season = "late-july"
# # x = "https://www.seasonalfoodguide.org/%s/%s" % (state, season)
# # y = "Those who know %s and those who %s." % (binary, do_not)
# # print x
# def createCSVFileName(season, month, state):
#     y = "%s%s_%s.csv" % (season, month, state)
#     print y
#     return y

# # print Template('https://www.seasonalfoodguide.org/$state/$season').substitute(s)
# browser = webdriver.Chrome('/Users/samskarvan/Desktop/pythonScrape/chromedriver') 
# url = "https://www.seasonalfoodguide.org/%s/%s" % (state, season)
# browser.get(url) #navigate to the page

# browser.get("http://example.com/page.php") #navigate to page behind login
# innerHTML = browser.execute_script("return document.body.innerHTML") #returns the inner HTML as a string
# htmlElem = html.document_fromstring(innerHTML) #make HTML element object
# # print htmlElem


# # tdElems = htmlElem.cssselect("[.card-title]") #list of all td elems
# # for elem in tdElems:
# #     text = elem.text_content() #text inside each td elem 
# #     tdElem1 = htmlElem.cssselect("[.card-title]")[0] #first td elem 
# #     text = elem.text_content()
# #     splitText = text.split("\n") #returns list of text in between "\n" chars
# #     print(splitText)\



 

# expression = GenericTranslator().css_to_xpath('.card-title')
# # print(expression)
# # print htmlElem
# # document = fromstring(innerHTML)
# # print htmlElem.xpath(expression)
# # inner = [e.get('.card-title') for e in htmlElem.xpath(expression)]
# inner = htmlElem.xpath(expression)
# for elem in inner:
#     print 'scraping text...'
#     # text = elem.nodeValue() #text inside each td elem 
#     tdElem1 = inner[0] #first td elem 
#     text = elem.text_content()
#     # print text
#     splitText = text.split("\n")[0] #returns list of text in between "\n" chars
#     csv.write(splitText + "\n") #write to csv
# print 'csv file created'
#     # print splitText
# browser.close()
    # print(etree.tostring(root, pretty_print=True))

