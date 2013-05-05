from lxml import etree
from StringIO import StringIO
import sys
reload(sys)
sys.setdefaultencoding('GBK')
#----------------------------------------------------------------------
def parseWeatherXML(xmlFiles):
    weather = []
    gbk_parser = etree.XMLParser(encoding='utf8')
    for xmlFile in xmlFiles.split(','):
    	f = open(xmlFile)
    	xml = f.read()
    	f.close()
    	doc = etree.parse(StringIO(xml), parser=gbk_parser)
    	
    	for df in doc.xpath('//time_range'):
    		time_range=[]
    		for sf in df.getchildren():
    			if not sf.text:
    				text = "None"
    			elif '' != sf.text.strip() and not sf.tag.startswith('tempF'):
    				time_range.append(sf.text)
    		weather.append(time_range)
    return weather




# if __name__ == "__main__":
# 	print parseWeatherXML("weatherinfo.xml")
