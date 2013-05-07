import urllib2
import weatherAnalysis
import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')
url = "http://m.weather.com.cn/data/%s.html"
path = "./conf/codeAPI.txt"

def main():
	# print url % "jjj"
	# stream=urllib2.urlopen(url%"101010100")
	# # print stream.read()
	# weatherAnalysis.xmlBuilder(stream.read())
	for li in open(path, "r"):
		for l in re.findall(r'[\d]+', li):
			try:
				# print url%l.replace('\n', '')
				stream=urllib2.urlopen(url%l.strip())
				weatherAnalysis.xmlBuilder(stream.read())
			except Exception, e:
				continue
		# stream=urllib2.urlopen(url%l)
		# # print stream.read()
		# weatherAnalysis.xmlBuilder(stream.read())
	# for li in open("codeAPI001.txt", "r"):
	# 	for l in re.findall(r'[\d]+', li):
	# 		print l




if __name__ == '__main__':
	main()