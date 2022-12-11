#!/bin/bash

FILE_INPUT=./${1}
# Clear the reults file
echo "" > results.out

# Function for API call for shortening
shortenUrl(){
	# This is for making the calls for shortening the URLs from a file
	LONG_URL="$(echo ${1} | sed -e 's/\\n//g')"
	# echo "curl -XPOST -d 'url=${LONG_URL}' 'https://cleanuri.com/api/v1/shorten'"
	API_RESULT=$(curl -XPOST -d url=${LONG_URL} 'https://cleanuri.com/api/v1/shorten' 2> /dev/null)
	# echo ${API_RESULT}
	SHORT_URL=$(echo -e ${API_RESULT} | cut -d':' -f2-)
	echo -e ${SHORT_URL} | sed -e 's/\"//g' -e 's/}//g' -e 's/\\\//\//g' >> results.out
}

while read -r URL
do
	shortenUrl ${URL}
done < ${FILE_INPUT}
