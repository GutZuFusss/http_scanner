from urllib2 import *

print "# Enter the range to scan"
print "# i.E.: 111.111"
ip_range = raw_input("> ")
print "# Range set to " + ip_range
print "#"
print "# File for IPs with HTTP server"
print "# i.E.: http_servers.txt"
out_file = raw_input("> ")

url_prefix = "http://" + ip_range +"."

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
			print "[caugh HTTPError] Couldn't find a HTTP server."
			continue
		except URLError, e:
			url = None
			print "[caugh  URLError] Couldn't find a HTTP server."
			continue

		print "[HIT] Found HTTP server: " + url
		text_file = open(out_file, "a")
		text_file.write(url + "\n")
		text_file.close()
