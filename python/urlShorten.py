import requests
import fileinput

outputFile = "shortUrls.out"

# Clear the output file
outputHeader = open(outputFile, 'w')
outputHeader.write("Shortened URLs: \n")
outputHeader.close()

count = 0
for line in fileinput.input():
	count += 1

	# run the request
	r = requests.post('https://cleanuri.com/api/v1/shorten', data={'url': line.strip()})
	# print(r.json()['result_url'])

	shortenFile = open(outputFile, 'a')
	shortenFile.write(r.json()['result_url'] + "\n")
	shortenFile.close()
