# Coding Exercise: The URL Shortener

## First Pass - in BASH

## Goals and Objectives
The goal of this exercise is to be able to shorten a list from a file.
This list would then be output to a different list using the following curl call:
`curl -XPOST -d '${LONG_URL}' 'https://cleanuri.com/api/v1/shorten'`

## Using the code
The script requires one (1) argument, the file for reading.  This file path is relative to the execution path (`./`) from the script.
The output from reading the file will be available in `results.out`
