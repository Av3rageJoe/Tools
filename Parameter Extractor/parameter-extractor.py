from sys import argv
import re

url = argv[1]
urlList = open(url, 'r')

foundParameters = []
PathNames = []

# Extract the parameters
def ParameterExtracter(url):
	if "?" in url:
		allParametersUrl = url.split('?')[1]
		parameterList = allParametersUrl.split('&')
		for parameter in parameterList:
			param = parameter.split('=')[0]
			if param not in foundParameters:
				foundParameters.append(param) 

def PathExtracter(url):
	
	if "://" in url:
		url = url.split("://")[1]
	if '/' not in url:
		url = url + '/'
	if '?' not in url:
		url = url + '?'
	paths = re.search('/(.*)?', url)
	paths = paths.group(1)
	if paths == '':
		return None
	if (paths[0] != '?'):
		paths = paths[:-1]
	
	if '?' in paths:
		paths = paths.split('?')[0]

	if paths != '':
		if '/' not in paths and paths not in PathNames:
			PathNames.append(paths)
		else:
			for path in paths.split('/'):
				if path not in PathNames:
					PathNames.append(path)

userChoice = ''

while userChoice == '':
	userChoice = input('What would you like to do? \n\n \t\t (1) Extract all Parameter names \n\t\t (2) Extract all path names\n\n')
	userChoice = userChoice.rstrip('\n')
	if userChoice == '1' or userChoice == '2':
		None
	else:
		print('The input you entered is not correct. Please try again')
		userChoice = ''

if userChoice == '1':
	print("Writing to \'Parameter Names.txt\'...")
	for url in urlList:
		url=url.rstrip('\n')
		ParameterExtracter(url)

	paramFile = open('Parameter Names.txt', 'w')
	foundParameters.sort()
	for param in foundParameters:
		paramFile.write(param + '\n')
	paramFile.close()
	print("done")

elif userChoice == '2':
	print("Writing to \'Path Names.txt\'...")

	for url in urlList:
		url=url.rstrip('\n')
		PathExtracter(url)

	pathFile = open('Path Names.txt', 'w')
	PathNames.sort()
	for path in PathNames:
		pathFile.write(path + '\n')
	pathFile.close()
	print("done")

urlList.close()
