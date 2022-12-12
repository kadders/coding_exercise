# Coding Exercise: The URL Shortener

## First Pass - in Python

## Goals and Objectives
The goal of this exercise is to be able to shorten a list from one or more files given as arguments. 
This list would then be shortened using the following requests call:
`requests.post('https://cleanuri.com/api/v1/shorten', data={'url': line.strip()})`

And then output to this defined output file:
`outputFile = "shortUrls.out"`

## Execution
script can be run with `python3 urlShorten.py urls.txt`
