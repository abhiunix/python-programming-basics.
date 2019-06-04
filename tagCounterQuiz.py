#Quiz: Tag Counter
#Write a for loop that iterates over a list of strings, tokens, and counts how many of them are XML tags. 
#XML is a data language similar to HTML. You can tell if a string is an XML tag if it begins with a left angle bracket "<" and ends with a right angle bracket ">". 
#Keep track of the number of tags using the variable count.
#You can assume that the list of strings will not contain empty strings.

#NOT_CORRECT
tokens = ['<greeting>', 'Hello World!>', '<greeting>']
count = 0
for token in tokens:
	if '<' and '>' in token:
		count+=1
print(count)

#CoRRECT

tokens = ['<greeting>', '<Hello World!>', '<greeting>']
count =0

for token in tokens:
	if token[0]=='<' and token[-1]=='>':
		count+=1
print(count)

#Quiz2
#Quiz: Create a HTML List
#Write some code, including a for loop, that iterates over a list of strings and creates a single string, html_str, which is an HTML list.
#For example, if the list is items = ['first string', 'second string'], printing html_str should output:

#<ul>
#<li>first string</li>
#<li>second string</li>
#</ul>
#That is, the string's first line should be the opening tag <ul>.
#Following that is one line per element in the source list, surrounded by <li> and </li> tags.
#The final line of the string should be the closing tag </ul>.

items = ['first string', 'second string']
html_str = "<ul>\n"  
# "\ n" is the character that marks the end of the line, it does
# the characters that are after it in html_str are on the next line

# write your code here
for item in items:
    html_str += "<li>{}</li>\n".format(item)
html_str += "</ul>"

print(html_str)