This repo provides you with the python script to crawl 2017 state election data from http://eciresults.nic.in

### Setup

+ Install [Python](https://www.python.org/downloads/) 
+ Install [pip](https://pip.pypa.io/en/latest/installing/) 
+ Install [BeatutifulSoup](https://www.crummy.com/software/BeautifulSoup/)
+ Install [Requests](http://docs.python-requests.org/en/latest/)

Once you have all the dependecies installed, run

`python scrape.p`

### Output Data Format

| State         | Constituency  | Candidate  		| Party 		| Votes   |
| ------------- |:-------------:| -----------------:|--------------:|--------:|
| UP			|Agra Cantt.	| DR. GIRRAJ SINGH DHARMESH |Bharatiya Janata Party | 113178 |			
| UP			|Agra Cantt.	| GUTIYARI LAL DUWESH |Bahujan Samaj Party | 66853 |		
| UP			|Agra Cantt.	| MAMTA KAUDAN |BSamajwadi Party | 64683 |		
