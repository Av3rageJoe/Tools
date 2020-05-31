#!/usr/bin/python3

import requests
import argparse

parser = argparse.ArgumentParser(description='Parse the arguments')
parser.add_argument('-urls', help='The list containing all of the urls', required=True)
parser.add_argument('-sizes', help='The list containing all of the response sizes', required=False)
parser.add_argument('-codes', help='The list containing all of the status codes', required=False)

args = parser.parse_args()

originalCodes = []
originalSizes = []
newCodes = []
newSizes = []
urls = []
extendedUrls = []

# Populate the url array
urlList = open(args.urls, "r+")
for url in urlList:
		url = url.rstrip('\n')
		if url != '':
			urls.append(url)
urlList.close()

#Populate the status code and page sizes arrays
if (args.sizes != None and args.codes != None):
	statusCodeFile = open(args.codes, 'r+')
	sizesFile = open(args.sizes, 'r+')

	# populate the orignal codes and sizes array
	for i in statusCodeFile:
		if i != '':
			i = i.rstrip('\n')
			originalCodes.append(i)
	statusCodeFile.close()
	for i in sizesFile:
		if i != '':
			i = i.rstrip('\n')
			originalSizes.append(i)
	sizesFile.close()

	if(len(urls) > len(originalCodes)):
		extendedUrls = urls[-(len(urls) - len(originalCodes)):]
		urls = urls[:(len(originalCodes))]




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
	if(originalSize != newSize and (originalSize == "error" or newSize == "error")):
		return True
	originalSize = int(originalSize)
	newSize = int(newSize)
	minus10= newSize * 0.9
	plus10 = newSize * 1.1
	if(minus10 < originalSize and plus10 > originalSize):
		return False
	else: 
		return True

def codeDifference(originalCode, newCode):
	if(originalCode == "error" and newCode != "error"):
		return True
	elif(newCode == "error" and newCode != "error"):
		return True
	elif(originalCode == "error" and newCode == "error"):
		return False
	newCode = int(newCode)
	originalCode = int(originalCode)
	if(originalCode == newCode):
		return False
	else:
		return True


def createLists():
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

def updateUrlList(url):
	statusCodeFile = open(args.codes, "a+")
	sizesFile = open(args.sizes, "a+")
	try:
		response = requests.get(url)
		statusCodeFile.write(str(getCode(response)) + '\n')
		sizesFile.write(str(getSize(response)) + '\n')
	except:
		statusCodeFile.write("error" + '\n')
		sizesFile.write("error" + '\n')
	statusCodeFile.close()
	sizesFile.close()


# If there is no codes and sizes supplied, then create a list of them
if (args.sizes == None or args.codes == None):
	# Create all the original arrays
	createLists()

else:
	differencesFile = open("Differences.txt", "w")
	# Get the new and updated responses details
	for i in range(0,len(originalCodes)):
		try:
			response = requests.get(urls[i])
			newCodes.append(getCode(response))
			newSizes.append(getSize(response))
		except:
			newCodes.append("error")
			newSizes.append("error")
		# Works out if there are differences and then writes them to a file
		if codeDifference(originalCodes[i], newCodes[i]):
			if PercentageDifference(originalSizes[i], newSizes[i]):
				differencesFile.write(urls[i] + ": \n\nPrevious status code: " + str(originalCodes[i]) + "\t\t New status code: " + str(newCodes[i]) + "\n")
				differencesFile.write("Previous page size: " + str(originalSizes[i]) + "\t\t New page size: " + str(newSizes[i]) + '\n\n')
			else:
				differencesFile.write(urls[i] + ": \n\nPrevious status code: " + str(originalCodes[i]) + "\t\t New status code: " + str(newCodes[i]) + "\n\n")
		elif PercentageDifference(originalSizes[i], newSizes[i]):
			differencesFile.write(urls[i] + ": \n\nPrevious page size: " + str(originalSizes[i]) + "\t\t New page size: " + str(newSizes[i]) + "\n\n")
	if(extendedUrls):
		for i in extendedUrls:
			i = i.rstrip('\n')
			updateUrlList(i)
