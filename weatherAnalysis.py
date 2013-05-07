#coding:utf-8 -*-
import sys
import json
import lxml.etree as etree
import datetime

reload(sys)
sys.setdefaultencoding('utf-8')
root = etree.Element("weatherinfos")
data_xml = "data/weatherinfo%s.xml"
splitor='~'
subffixlow='L'
subffixhigh='H'
def xmlBuilder(f):
	js = json.loads(f)
	root.append(jsonAnalyser(js["weatherinfo"]))
	out= open(data_xml%datetime.datetime.now().strftime("%Y-%m-%d-%Hh"), "w")
	out.write(etree.tostring(root, pretty_print=True, encoding='utf-8'))


def jsonAnalyser(js):
	element = etree.Element("weatherinfo", city=js["city"], city_en=js["city_en"]\
		, date=js["date"], week=js["week"])

	for x in range(1, 6):
		d=datetime.datetime.now()+datetime.timedelta(hours=4*(x-1))
		time_range= etree.Element("time_range")
		element.append(time_range)
		etree.SubElement(time_range, "time").text=d.strftime("%H")
		tempC=js["temp"+str(x)].split(splitor)
		etree.SubElement(time_range, "tempCL").text=tempC[0]+subffixlow
		etree.SubElement(time_range, "tempCH").text=tempC[1]+subffixhigh
		tempC=js["tempF"+str(x)].split(splitor)
		etree.SubElement(time_range, "tempFL").text=tempC[0]+subffixlow
		etree.SubElement(time_range, "tempFH").text=tempC[1]+subffixhigh
		etree.SubElement(time_range, "weather").text=js["weather"+str(x)]
		etree.SubElement(time_range, "wind").text=js["wind"+str(x)]
	return element
