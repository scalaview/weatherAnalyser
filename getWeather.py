import urllib2
import weatherAnalysis
import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')
url = "http://m.weather.com.cn/data/%s.html"
path = "./conf/codeAPI.txt"

def main():
	for li in open(path, "r"):
		for l in re.findall(r'[\d]+', li):
			try:
				# print url%l.replace('\n', '')
				stream=urllib2.urlopen(url%l.strip())
				weatherAnalysis.xmlBuilder(stream.read())
			except Exception, e:
				continue




if __name__ == '__main__':
	main()