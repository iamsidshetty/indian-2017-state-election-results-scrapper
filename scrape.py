import requests
from BeautifulSoup import BeautifulSoup
import csv

# function to get the Constituency
def get_constituencies(html, stateID):
	mainpage = BeautifulSoup(html)
	
	parse_constituency = mainpage.find('input', attrs={'id': stateID})

	all_constituency_info = parse_constituency['value'].encode("ascii")
	
	all_constituency_info_list = all_constituency_info.split(";")
	
	return all_constituency_info_list

def get_constituency_result_info(filetowrite, constituency_url, constituency_name, state):

	getinfo = BeautifulSoup(requests.get(constituency_url).content)

	parse_table = getinfo.find('table', attrs={'border' : 1})

	all_candidates = []
	for row in parse_table.findAll('tr', attrs={'style' : 'font-size:12px;'}):
		candidate = [state, constituency_name]
		for cell in row.findAll('td'):
			candidate.append(cell.text.encode("utf8"))
		# print candidate
		all_candidates.append(candidate)
	
	# write to a file
	writer = csv.writer(filetowrite)
	writer.writerows(all_candidates)



def main():

	# get the base page
	base_url = "http://eciresults.nic.in/Constituencywise"
	url = "http://eciresults.nic.in/ConstituencywiseS0510.htm?ac=10"
	html = requests.get(url).content

	# all the states that went to election in 2017
	states = { 'GA' : 'S05', 'MR' : 'S14', 'PB' : 'S19', 'UP' : 'S24', 'UT' : 'S28' }

	# open a file to write
	datafile = open("./election_results_data.csv", "wb")

	# get all constituencies
	for each_state, code in states.iteritems():
		all_constituency_info_list = get_constituencies(html, 'Hdn' + each_state)
		print "LOG: Starting with state --" + each_state

		# examples
			# 34 Wangjing tentha 
			# 15 Wangkhei 
			# 32 Wangkhem 
			# 22 Wangoi 
			# 14 Yaiskul 
			
		for constituency_data in all_constituency_info_list:
			if constituency_data is not '':
				constituency_data_split = constituency_data.split(',')
				print "\t Starting with constituency --" + constituency_data_split[1]
				get_constituency_result_info(datafile, base_url + code + constituency_data_split[0] + ".htm?ac=" + constituency_data_split[0], constituency_data_split[1], each_state)

if __name__ == "__main__": 
	main()
	

