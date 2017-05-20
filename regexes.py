import re

# 'p' is pattern object 
# pattern objects have several methods and attributes
# Method/Attribute	Purpose
# match()			Determine if the RE matches at the beginning of the string.
# search()			Scan through a string, looking for any location where this RE matches.
# findall()			Find all substrings where the RE matches, and returns them as a list.
# finditer()		Find all substrings where the RE matches, and returns them as an iterator.
p = re.compile('ab*')
p = re.compile('ab*', re.I)
print(p.match('abB'))

# 'm' is match object
# match object instances also have several methods and attributes
# Method/Attribute	Purpose
# group()			Return the string matched by the RE
# start()			Return the starting position of the match
# end()				Return the ending position of the match
# span()			Return a tuple containing the (start, end) positions of the match
p = re.compile('[a-z]+')
m = p.match('tempo')
print('\n' + m.group())
print(m.start(), m.end())
print(m.span())

m = p.match(':::message')
print(m)
m = p.search(':::message')
print(m)
print(m.group(), m.start(), m.end(), m.span())

# findall() has to create the entire list before it can be returned as the result
p = re.compile('\d+')
m = p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')
print(m)

# finditer() method returns a sequence of match object instances as an iterator
m = p.finditer('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')
for match in m:
	print(match)

# re module also provides top-level functions called match(), search(), findall(), sub(), and so forth
m = re.match(r'From\s+', 'Fromage amk')
print(m)
m = re.match(r'From\s+', 'From amk Thu May 14 19:12:10 1998')
print(m)

# ^ Matches at the beginning of lines
print(re.search('^From', 'From Here to Eternity'))
print(m)
m = re.search('^From', 'Reciting From Memory')
print(m)

# $ Matches at the end of a line or any location followed by a newline character.
print(re.search('}$', '{block}'))
print(re.search('}$', '{block} '))	
print(re.search('}$', '{block}\n'))

# \b matches only when it’s a complete word; it won’t match when it’s contained inside another word
p = re.compile(r'\bclass\b')
print(p.search('no class at all'))
print(p.search('the declassified algorithm'))

# If you’re not using raw strings, then Python will convert the \b to a backspace
p = re.compile('\bclass\b')
print(p.search('class'))
print(p.search('\b' + 'class' + '\b'))

# (ab)* will match zero or more repetitions of ab
p = re.compile('(ab)*')
print(p.match('ababababab').span())

# Group 0 is always present; it’s the whole RE, so match object methods all have group 0 as their default argument
p = re.compile('(a)b')
m = p.match('ab')
print(m.group(), m.group(0), m.group(1))

# group() can be passed multiple group numbers at a time
p = re.compile('(a(b)c)d')
m = p.match('abcd')
print(m.group(0, 1, 2))
# The groups() method returns a tuple containing the strings for all the subgroups, from 1 up to however many there are
print(m.groups())
