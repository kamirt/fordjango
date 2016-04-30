
"""
There is a log of web-server, each line is request for this server. Log format is:
...
127.0.0.1 - frank [10/Oct/2000:13:55:36 -0700] "GET /index.php HTTP/1.0" 200 2326
...
We must find five IP, who gives most requests.

"""

filepath = "/home/kamirt/list"
iplist= []
def getListIp(filepath):
	with open(filepath) as f:
		for line in f:
			lineDivider = line.split(" - ")
			iplist.append(lineDivider[0])
	from collections import Counter
	ipdict = Counter(iplist).most_common(5)
	return ipdict

print(getListIp(filepath))

