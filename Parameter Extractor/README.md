# Parameter Extractor

This isprogram has been updated so that it also extracts path names and parameter names from a url. It has been compiled to work on python3.

USAGE: `python3 parameter-extractor.py <URL List>`

Example:

URL-List.txt:

```
https://google.com/?BigParam=WOAH

https://github.com/?smallparam=woah&HUGEPARAM=BANG

https://yahoo.com/?smallparam=duplicate
```

`./parameter-extractor.py URL-List.txt`

Output saved in 'Parameter Names.txt':

```
BigParam
HUGEPARAM
smallparam
```

