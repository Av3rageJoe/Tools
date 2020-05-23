# Parameter Extractor

This is a small bash program that will take a list of urls, and extract all the parameters used inside the urls. 
It will then save these parameters to a file.

USAGE: `parameter-extractor.sh <URL List>`

Example:

URL-List.txt:

```
https://google.com/?BigParam=WOAH

https://github.com/?smallparam=woah&HUGEPARAM=BANG

https://yahoo.com/?smallparam=duplicate
```

`./parameter-extractor.sh URL-List.txt`

Output saved in parameters.txt:

```
BigParam
smallparam
HUGEPARAM
```

