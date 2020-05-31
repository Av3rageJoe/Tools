This tool will work out what has changed on a website.

The two things that it will calculate are the status code and the page size, and then save them to a text file. You can then pass in these text files to work out the difference between the files supplied and the new responses at time of running.

example to calculate the differences between the files supplied and the current responses:

`difference.py -urls urls -sizes Page-Sizes-File -codes Status-Codes-List`

Where -urls contains a list of urls beginning with the correct schema.

example to generate a text file containing the status codes of a url list and the page sizes:

`difference.py -urls urls`

