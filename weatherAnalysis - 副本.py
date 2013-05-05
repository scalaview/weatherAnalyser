#coding:utf-8 -*-
import sys
import json
import lxml.etree as etree
import datetime

reload(sys)
sys.setdefaultencoding('utf-8')
root = etree.Element("weatherinfos")
data_xml = "weatherinfo%s.xml"
def xmlBuilder(f):
	# f= file("101010100.js")
	js = json.loads(f)
	# print js
	# print js["weatherinfo"].keys()
	# print js["4"]
	# print js["6"]
	# datetime.datetime.now()+datetime.timedelta(hours=4)
	# element = etree.Element("weatherinfo", city=js["weatherinfo"]["city"], city_en=js["weatherinfo"]["city_en"]\
	# 	, date=js["weatherinfo"]["date"], week=js["weatherinfo"]["week"])
	# element.append(jsonAnalyser(js["weatherinfo"]))
	# etree.SubElement(element, jsonAnalyser(js["weatherinfo"]))
	# el = jsonAnalyser(js["weatherinfo"])
	root.append(jsonAnalyser(js["weatherinfo"]))
	out= open(data_xml%datetime.datetime.now().strftime("%Y-%m-%d %Hh"), "w")
	out.write(etree.tostring(root, pretty_print=True, encoding='utf-8'))


def jsonAnalyser(js):
	# if js["date"]==None or js["date"]=="":
	# 	js["date"]=time.mktime(time.strptime(js["date_y"], "%Y年%m月%d日"))
	# print js["city"]
	element = etree.Element("weatherinfo", city=js["city"], city_en=js["city_en"]\
		, date=js["date"], week=js["week"])

	for x in range(1,6):
		d=datetime.datetime.now()+datetime.timedelta(hours=4*(x-1))
		time_range= etree.Element("time_range")
		element.append(time_range)
		#etree.SubElement(time_range, "time").text=d.strftime("%Y-%m-%d %Hh")
		etree.SubElement(time_range, "time").text=d.strftime("%H")
		etree.SubElement(time_range, "tempC").text=js["temp"+str(x)]
		etree.SubElement(time_range, "tempF").text=js["tempF"+str(x)]
		etree.SubElement(time_range, "weather").text=js["weather"+str(x)]
		etree.SubElement(time_range, "wind").text=js["wind"+str(x)]

	# etree.SubElement(element, "tempC").text=js["temp1"]
	# etree.SubElement(element, "tempF").text=js["tempF1"]
	# etree.SubElement(element, "weather").text=js["weather1"]
	# etree.SubElement(element, "fx").text=js["fx1"]


	# for x in js.keys():
	# 	etree.SubElement(element, x).text=js[x]
		# child=etree.Element(x)
		# child.text = js[x]
		# element.append(child)
	# print etree.tostring(element)
	return element

