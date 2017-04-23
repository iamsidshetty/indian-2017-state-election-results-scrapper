import requests
from BeautifulSoup import BeautifulSoup


# get the base page
url = "http://eciresults.nic.in/ConstituencywiseS0510.htm?ac=10"
response = requests.get(url)
html = response.content


# all the states that went to election in 2017
states = ['HdnGA', 'HdnMR', 'HdnUP', 'HdnUT', 'HdnPB']


# function to get the Constituency
def get_constituencies(state):
	soup = BeautifulSoup(html)
	const = soup.find('input', attrs={'id': state})

	ac = const['value'].encode("ascii")
	aclist = ac.split(";")

	for i in aclist:
		if i is not '':
			print i.split(',')[1]

for each_state in states:
	get_constituencies(each_state)
	print "-------------------------------------------------"