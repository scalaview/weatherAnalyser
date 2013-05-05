# #coding:GBK -*-
# import sys
# import lxml.etree as etree


# reload(sys)
# sys.setdefaultencoding('utf-8')
# infile = 'weatherinfo.xml'


# def main():
#       root = etree.Element("root")
#       for element in root.iter():
#               print("%s - %s" % (element.tag, element.text))
#       # build_text_list = etree.XPath("//text()")
#       # # time_range=etree.Element("weatherinfo")
#       # # print time_range.xpath("//text()")
#       # context=etree.iterparse(infile, encoding="GBK", events=("end", ), tag='weatherinfo')
#       # for elem in context:
#       #       # print build_text_list(elem)
#       #       for elrange in elem:
#       #               print elrange
#       # root = etree.parse("weatherinfo.xml")
#       # etree.Element("weatherinfo")


# if __name__ == '__main__':
#       main()

from lxml import etree
from StringIO import StringIO
import sys
reload(sys)
sys.setdefaultencoding('GBK')
#----------------------------------------------------------------------
def parseWeatherXML(xmlFile):

	f = open(xmlFile)
	xml = f.read()
	f.close()

     #    # tree = etree.parse(StringIO(xml))
     #    # print tree.docinfo.doctype
     #    context = etree.iterparse(StringIO(xml), encoding="GBK")
     #    weatherinfo = []
     #    time_range = []
     #    for actions, weatherElem in context:
	    # # time_range = []
	    # # for action, elem in weatherElem:
	    #       if not weatherElem.text:
	    #               text = "None"
	    #       elif '' != weatherElem.text.strip():
	    #               time_range.append(weatherElem.text)
	    # weatherinfo.append(time_range)
	    # text = elem.text
	    # print elem.tag + " => " + text.encode('utf8')
	    # book_dict[elem.tag] = text
	    # if elem.tag == "book":
	    #     books.append(book_dict)
	    #     book_dict = {}
	# return time_range

	gbk_parser = etree.XMLParser(encoding='GBK')
	doc = etree.parse(StringIO(xml), parser=gbk_parser)
	weather = []
	for df in doc.xpath('//time_range'):
	    # print df.attrib
		time_range=[]
	for sf in df.getchildren():
		if not sf.text:
			text = "None"
		elif '' != sf.text.strip() and not sf.tag.startswith('tempF'):
			time_range.append(sf.text)
	# print time_range
	weather.append(time_range)
	return weather



if __name__ == "__main__":
	print parseWeatherXML("weatherinfo.xml")
