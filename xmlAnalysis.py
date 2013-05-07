from lxml import etree
from StringIO import StringIO
import sys
import rules

reload(sys)
sys.setdefaultencoding('GBK')
part1 = ['time', 'weather', 'wind']
part2 = ['tempFL', 'tempFH']
#----------------------------------------------------------------------
def parseWeatherXML(xmlFiles):
    weather = []
    utf8_parser = etree.XMLParser(encoding='utf8')
    for xmlFile in xmlFiles.split(','):
    	f = open(xmlFile)
    	xml = f.read()
    	f.close()
    	doc = etree.parse(StringIO(xml), parser=utf8_parser)
    	
    	for df in doc.xpath('//time_range'):
    		time_range=[]
    		for sf in df.getchildren():
    			if not sf.text:
    				text = "None"
    			elif '' != sf.text.strip() and not sf.tag.startswith('tempF'):
                # elif '' != sf.text.strip() and (not sf.tag in part2):
    				time_range.append(partition(sf))
    		weather.append(time_range)
    return weather

def partition(elem):
    if not elem.tag in part1:
        return rules.rule(elem.text)
    else:
        return elem.text




# if __name__ == "__main__":
# 	print parseWeatherXML("weatherinfo.xml")
