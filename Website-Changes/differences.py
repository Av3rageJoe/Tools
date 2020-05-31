#!/usr/bin/python3

import requests
import argparse

parser = argparse.ArgumentParser(description='Parse the arguments')
parser.add_argument('-urls', help='The list containing all of the urls', required=True)
parser.add_argument('-sizes', help='The list containing all of the response sizes', required=False)
parser.add_argument('-codes', help='The list containing all of the status codes', required=False)

args = parser.parse_args()

# Populate the url array
urlList = open(args.urls, "r+")
urls = []
for url in urlList:
		url = url.rstrip('\n')
		if url != '':
			urls.append(url)
urlList.close()

originalCodes = []
originalSizes = []
newCodes = []
newSizes = []

# Gets the size of the url
def getSize(url):
	size = len(url.content)
	return size

# Gets the response status code
def getCode(url):
	code = url.status_code
	return code	

def PercentageDifference(originalSize, newSize):
	if(originalSize == newSize):
		return False
	originalSize = int(originalSize)
	newSize = int(newSize)
	minus10= newSize * 0.9
	plus10 = newSize * 1.1
	if(minus10 < originalSize and plus10 > originalSize):
		return False
	else: 
		return True

def codeDifference(originalCode, newCode):
	if(originalCode == newCode):
		return False
	originalCode = int(originalCode)
	newCode = int(newCode)
	if(originalCode == newCode):
		return False
	else:
		return True


def createLists(urlList):
	for url in urls:
		if url != '':
			try:
				response = requests.get(url)
				originalCodes.append(getCode(response))
				originalSizes.append(getSize(response))
			except:
				originalCodes.append("error")
				originalSizes.append("error")
	statusCodeFile = open("Status-Codes-List", "w")
	sizesFile = open("Page-Sizes-File", "w")

	for i in range(0,len(originalCodes)):
		statusCodeFile.write(str(originalCodes[i]) + '\n')
	statusCodeFile.close()

	for i in range(0,len(originalSizes)):
		sizesFile.write(str(originalSizes[i]) + '\n')
	sizesFile.close()

# If there is no codes and sizes supplied, then create a list of them
if (args.sizes == None or args.codes == None):
	# Create all the original arrays
	createLists(urlList)

else:
	statusCodeFile = open(args.codes, 'r+')
	sizesFile = open(args.sizes, 'r+')

	# populate the orignal codes and sizes array
	for i in statusCodeFile:
		i = i.rstrip('\n')
		originalCodes.append(i)
	statusCodeFile.close()
	for i in sizesFile:
		i = i.rstrip('\n')
		originalSizes.append(i)
	sizesFile.close()

	differencesFile = open("Differences.txt", "w")
	# Get the new and updated responses details
	for i in range(0,len(urls)):
		try:
			response = requests.get(urls[i])
			newCodes.append(getCode(response))
			newSizes.append(getSize(response))
		except:
			newCodes.append("error")
			newSizes.append("error")

		if codeDifference(originalCodes[i], newCodes[i]):
			if PercentageDifference(originalSizes[i], newSizes[i]):
				differencesFile.write(urls[i] + ": \n\nPrevious status code: " + str(originalCodes[i]) + "\t\t New status code: " + str(newCodes[i]) + "\n")
				differencesFile.write("Previous page size: " + str(originalSizes[i]) + "\t\t New page size: " + str(newSizes[i]) + '\n\n')
			else:
				differencesFile.write(urls[i] + ": \n\nPrevious status code: " + str(originalCodes[i]) + "\t\t New status code: " + str(newCodes[i]) + "\n\n")
		elif PercentageDifference(originalSizes[i], newSizes[i]):
			differencesFile.write(urls[i] + ": \n\nPrevious page size: " + str(originalSizes[i]) + "\t\t New page size: " + str(newSizes[i]) + "\n\n")


