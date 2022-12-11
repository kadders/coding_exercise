import requests

urlFile = "urls.file"
outputFile = "shortUrls.out"

# Clear the output file
outputHeader = open(outputFile, 'w')
outputHeader.write("Shortened URLs: \n")
outputHeader.close()

# file open for read
soureFile = open(urlFile, 'r')
Lines = soureFile.readlines()

count = 0
for line in Lines:
	count += 1
	# print(line.strip())

	# run the request
	r = requests.post('https://cleanuri.com/api/v1/shorten', data={'url': line.strip()})
	# shortResponse = r.json()
	# print(r.json()['result_url'])

	shortenFile = open(outputFile, 'a')
	shortenFile.write(r.json()['result_url'] + "\n")
	shortenFile.close()
