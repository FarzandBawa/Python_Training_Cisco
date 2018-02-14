import re
s = "abc123"
r = re.compile(r'[a-z][0-9]')
print(re.findall(r, s))
r = re.compile(r'[a-z]+[0-9]+')
print(re.findall(r, s))
s = '123'
r = re.compile(r'[a-z]*[0-9]+')
print(re.findall(r, s))
s = 'ABC123'
r = re.compile(r'[A-Z]*[0-9]+')
print(re.findall(r, s))
s = 'aAbC123'
r = re.compile(r'[A-Za-z]*[0-9]+')
print(re.findall(r, s))
s = '3Python'
r = re.compile(r'[A-Za-z]+')
print(re.findall(r, s))
s = 'Python3.0'
r = re.compile(r'^[A-Za-z]+[0-9]')
print(re.findall(r, s))
s = 'Python3'
r = re.compile(r'^[A-Za-z]+[0-9]$')
print(re.findall(r, s))
s = 'Python3.0'
r = re.compile(r'[^A-Za-z][0-9]+')
print(re.findall(r, s))
s = 'Python3.0'
r = re.compile(r'[0-9]+\.*[0-9]*')
# r = re.compile(r'\d')
print(re.findall(r, s))
s = "abcde1243"
r = re.compile(r'[a-z]{1,3}')  # range
print(re.findall(r, s))
s = "Python 123"
r = re.compile(r'[^Python\s]+')
print(re.findall(r, s))
p = "AAAAA1234A"
pan = re.compile(r'^[A-Z]{5}[0-9]{4}[A-Z]$')
print(re.findall(pan, p))
