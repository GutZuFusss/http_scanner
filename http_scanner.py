from urllib2 import *

url_prefix = "http://212.224." # "http://172.217."

for x1 in range(0, 255):
	for x2 in range(0, 255):
		url = url_prefix + str(x1) + "." + str(x2)
		print "Trying: " + url + "..."

		req = Request(url)

		# Try to open the url
		try: 
			reponse = urlopen(req, timeout=1)
		except HTTPError, e:
			url = None
			print "[caugh HTTPError] (hier keine, bruder)"
			continue
		except URLError, e:
			url = None
			print "[caugh  URLError] (hier keine, bruder)"
			continue

		print "HARRRR!!!! URL: " + url
		text_file = open("twf_possibru_ips.txt", "a")
		text_file.write(ip + "\n")
		text_file.close()