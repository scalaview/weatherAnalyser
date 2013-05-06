# -*- coding: UTF-8 -*-

import re
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
interval = 5
def parseToInt(str):
	pattern = re.compile(r'[\d]+')
	if str and str.strip() != '':
		match = pattern.match(str)
		if match:
			try:
				return int(match.group())
			except Exception, e:
				raise e
	return None


def convert(temperature):
	return int(temperature/interval)*interval

def rule(text):
	temperature = parseToInt(text)
	if temperature:
		return text.replace(str(temperature), str(convert(temperature)))
	else:
		return text


def main():
	print rule('25HL')

if __name__ == '__main__':
	main()