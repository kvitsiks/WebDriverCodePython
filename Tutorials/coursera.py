# hrs = raw_input("Enter Hours:")
# pay_rate = raw_input("Enter Rate:")
# try:
# 	h = float(hrs)
# except:
# 	h = 1
# try:
#     p_r = float(pay_rate)
# except:
# 	p_r = 1
# if (h <= 40):
# 	print "You don't have an overtime"
# elif (h > 40):
#     over = h - 40
#     over_pay = over*(p_r * 1.5)
# print 40*p_r + over_pay


# score = raw_input("Enter Score: ")
# try:
#     s = float(score)
# except:
#     s = 0
# if (1.0>= s >=0.9):
#     print "A"
# elif (0.89>= s >=0.8):
#     print "B"
# elif (0.79>= s >=0.7):
#     print "C"
# elif (0.69>= s >=0.6):
#     print "D"
# elif (0.59>= s >=0.0):
#     print "F"
# else:
#     print "Value is out of range"

# def addtwo(a, b):
#     added = a + b
#     return a
#
# x = addtwo(2, 7)
# print x
#
# def stuff():
#     print 'Hello'
#     return 'World1'
#     print 'World'
#
# print stuff()


# def computepay(h, r):
#     hrs = raw_input("Enter Hours:")
#     pay_rate = raw_input("Enter Rate:")
#     try:
#         h = float(hrs)
#     except:
#         h = 0
#     try:
#         r = float(pay_rate)
#     except:
#         r = 0
#     if (h <= 40):
#         print "You don't have an overtime"
#     elif (h > 40):
#         over = h - 40
#         gross_pay = (40 * r) + (over * (r * 1.5))
#     return gross_pay
#
# print computepay(1234234,232423234324234)


# largest = None
# smallest = None
# while True:
#     num = raw_input("Enter a number: ")
#     try:
#         s_num = int(num)
#     except:
#         print "Invalid input"
#     if num == "done": break
#     print num
#     for value in num:
#         if smallest is None:
#           smallest = value
#         elif value < smallest:
#             smallest = value
#     for value1 in num:
#         if largest is None:
#             largest = value
#         elif value > largest:
#             largest = value
#
# print "Maximum is", largest
# print "Minimum is", smallest

# word = 'banana'
# count = 0
# for letter in word:
#     if letter == 'n':
#         count = count+1
# print count

# text = "X-DSPAM-Confidence:    0.8475";
# zero_pos = text.find("0")
# print zero_pos
# five_pos = text.find("5")
# print five_pos
# number = text[zero_pos:five_pos+1]
# print float(number)


# fh = open("ChromeDriver.txt", "r")
#
# count = 0
# for line in fh:
#     print line.strip()
#     count = count + 1
#
# print count,"Lines"

# fname = raw_input("Enter the file name:")
# try:
#     fhand = open(fname)
# except:
#     print "File",fname,"doesn't exist"
#     quit()
# count = 0
# for line in fhand:
#     if line.startswith('Subject'):
#         count=count+1
# print "There were", count, "lines in",fname

# Use words.txt as the file name
# fname = raw_input("Enter file name: ")
# fh = open(fname)
# for line in fh:
#     line = line.rstrip()
#     print line.upper()





# fname = raw_input("Enter file name: ")
# try:
#     fhand = open(fname)
# except:
#     print "File",fname,"doesn't exist"
#     quit()
# fh = open(fname)
# count=0
# total = 0
# res = 0
# for line in fh:
#     if not line.startswith("X-DSPAM-Confidence:") : continue
#     count = count + 1
#     zero_pos = line.find("0")
#     last_pos = line.find("\n")
#     numbers = line[zero_pos:last_pos]
#     numbers = float(numbers)
#     print numbers
#     total = total + numbers
#     res = total / count
# #mbox-short.txt
# print "Average spam confidence:",res

#the same =>

# fname = raw_input("Enter file name: ")
# fh = open(fname)
# tot = 0
# ans = 0
# count =0
# for line in fh:
#     if not line.startswith("X-DSPAM-Confidence:"): continue
#     count = count + 1
#     num = float(line[21:])
#     tot = tot + num
#     ans = tot / count
# print "Average spam confidence:", ans


# fname = raw_input("Enter file name: ")
# fh = open(fname)
# lst = list()
# for line in fh:
#     split = line.split()
#     for i in split:
#         if i not in lst:
#             lst.append(i)
#             lst.sort()
# print lst


# fname = raw_input("Enter file name: ")
# text = open(fname)
# count = 0
# for line in text:
#     if not line.startswith("From "): continue
#     elem = line.split()
#     count = count+1
#     #mbox-short.txt
#     print elem[1]
# print "There were", count, "lines in the file with From as the first word"


# name = raw_input("Enter file:")
# handle = open(name, 'r')
# counts = dict()
# lst = list()
# for line in handle:
#     if not line.startswith("From "): continue
#     words = line.split()
#     words1=words[1]
#     lst.append(words1)
# for word in lst:
#     counts[word] = counts.get(word,0)+1
#
# bigcount = None
# bigword = None
# for word,count in counts.items():
#     if bigcount is None or count > bigcount:
#         bigword = word
#         bigcount = count
# print bigword, bigcount


# name = raw_input("Enter file name: ")
# handle = open(name, 'r')
# lst = list()
# counts = dict()
# for line in handle:
#     if not line.startswith("From "): continue
#     words = line.split()
#     words1 = words[1]
#     lst.append(words1)
# print lst
# for word in lst:
#     counts[word] = counts.get(word,0)+1
# print counts
#
# maxcount = None
# maxword = None
# for word, count in counts.items():
#     if maxcount is None or count > maxcount:
#         maxword = word
#         maxcount = count
# print maxword, maxcount


# name = raw_input("Enter file:")
# handle = open(name)
# lst = list()
# lst1 = list()
# counts = dict()
# for line in handle:
#     if not line.startswith("From "): continue
#     words = line.split()
#     words1 = words[5]
#     etc = words1.split(':')
#     etc = etc[0]
#     lst.append(etc)
# for word in lst:
#     counts[word] = counts.get(word,0)+1
# #print sorted([(k,v) for k,v in counts.items()])
# for key, value in counts.items():
#     lst1.append((key, value))
#
# lst1.sort()
# print lst1
#
# for key, value in lst1:
#     print key, value


#mbox-short.txt


# s = 'sfdsf 10 30 20 40 sdfsd 60 fwfwef'
# lst = list()
# tot = 0
# for word in s:
#     words = s.split()
# for word in words:
#     if word.__contains__("0"):
#         lst.append(word)
# lst = map(int, lst)
# for i in lst:
#     tot = tot + i
# print "Total is:", tot


# import re
# tot = 0
# s = 'sfdsf 15 30 243 412 sdfsd 78 fwfwef'
# print s
# y = re.findall('[0-9]+', s)
# y = map(int, y)
# for i in y:
#     tot = tot + i
# print "Total is:", tot



# import re
# tot = 0
# inputs = raw_input("Enter file name: ")
# opens = open(inputs)
# text = opens.read()
# y = re.findall('[0-9]+', text)
# x = map(int, y)
# for i in x:
#     tot = tot + i
# print tot
# regex_sum_315600.txt


# import socket
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('www.data.pr4e.org', 80))
# mysock.send('GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n')
# while True:
#     data = mysock.recv(512)
#     if (len(data) < 1):
#         break
#     print data
# mysock.close()

# import urllib
# fhand = urllib.urlopen('http://py4inf.com/code/romeo.txt')
# for line in fhand:
#     print line.split()

#
# import urllib
# from BeautifulSoup import *
# url = raw_input('Enter - ')
# html = urllib.urlopen(url).read()
# soup = BeautifulSoup(html)
# tags = soup('span')
# tot = 0
# lst = list()
# for tag in tags:
#     a = int(tag.contents[0])
#     lst.append(a)
# for num in lst:
#     tot = num + tot
# print tot



# import urllib
# from BeautifulSoup import *
#
# URL = raw_input("Enter the URL:") #Put insurance
# link_line = int(raw_input("Enter the line of the desired link:")) - 1 #Put insurance
# count = int(raw_input("Enter the loop repeat times:")) #Put insurance
#
# while count >= 0:
#     html = urllib.urlopen(URL).read()
#     soup = BeautifulSoup(html)
#     tags = soup('a')
#     print URL
#     URL = tags[link_line].get("href", None)
#     count = count - 1


# import urllib
# import xml.etree.ElementTree as ET
# url = 'http://python-data.dr-chuck.net/comments_315602.xml'
# data = urllib.urlopen(url).read()
# tree = ET.fromstring(data)
# counts = tree.findall('comments/comment/count')
# total = 0
# for count in counts:
#     total += int(count.text)
# print 'total: ', total


# w = int(raw_input("Enter w:"))
# h = int(raw_input("Enter h:"))
# r = int(raw_input("Enter radius:"))
# perim = (w+h)*2
# area = w*h
# circumference = 2*3.14*r
# area_of_a_circle = 3.14*r**2
# print perim
# print area
# print circumference
# print area_of_a_circle

# import sqlite3
#
# conn = sqlite3.connect('emaildb.sqlite')
# cur = conn.cursor()
#
# cur.execute('''
# DROP TABLE IF EXISTS Counts''')
#
# cur.execute('''
# CREATE TABLE Counts (org TEXT, count INTEGER)''')
#
# fname = raw_input('Enter file name: ')
# if ( len(fname) < 1 ) : fname = 'mbox.txt'
# fh = open(fname)
# for line in fh:
#     if not line.startswith('From: ') : continue
#     pieces = line.split()
#     email = pieces[1]
#     #print email
#     parts = email.split('@')
#     org = parts[-1]
#     cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
#     row = cur.fetchone()
#     if row is None:
#         cur.execute('''INSERT INTO Counts (org, count)
#                 VALUES ( ?, 1 )''', ( org, ) )
#     else :
#         cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?',
#             (org, ))
#     # This statement commits outstanding changes to disk each
#     # time through the loop - the program can be made faster
#     # by moving the commit so it runs only after the loop completes
#     conn.commit()
#
# # https://www.sqlite.org/lang_select.html
# sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
#
# print
# print "Counts:"
# for row in cur.execute(sqlstr) :
#     print str(row[0]), row[1]
#
# cur.close()


# str = "12345"
# print str[::-1]

#########################Extracting Data from XML############################
# import urllib
# import xml.etree.ElementTree as ET
#
# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'
#
# while True:
#     address = raw_input('Enter location: ')
#     if len(address) < 1 : break
#
#     url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
#     print 'Retrieving', url
#     uh = urllib.urlopen(url)
#     data = uh.read()
#     print 'Retrieved',len(data),'characters'
#     print data
#     tree = ET.fromstring(data)
#
#
#     results = tree.findall('result')
#     lat = results[0].find('geometry').find('location').find('lat').text
#     lng = results[0].find('geometry').find('location').find('lng').text
#     location = results[0].find('formatted_address').text
#
#     print 'lat',lat,'lng',lng
#     print location

#########################Extracting Data from JSON############################
# import urllib
# import json
#
# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
#
# while True:
#     address = raw_input('Enter location: ')
#     if len(address) < 1 : break
#
#     url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
#     print 'Retrieving', url
#     uh = urllib.urlopen(url)
#     data = uh.read()
#     print 'Retrieved',len(data),'characters'
#
#     try: js = json.loads(str(data))
#     except: js = None
#     if "status" not in js or js["status"] !="OK":
#         print "Failure to retrieve"
#         print data
#         continue
#
#     print json.dumps(js, indent=4)
#
#     lat = js["results"][0]["geometry"]["location"]["lat"]
#     lng = js["results"][0]["geometry"]["location"]["lng"]
#     print "lat", lat, "lng", lng
#     location = js["results"][0]["formatted_address"]
#     print location


# import urllib
# import json
# ############http:// python-data.dr-chuck.net/comments_315606.json
# while True:
#     url = raw_input('Enter location: ')
#     if len(url) < 1 : break
#
#     #open url
#     url_open = urllib.urlopen(url)
#
#     #extract data
#     data = url_open.read()
#     uh = urllib.urlopen(url)
#     data = uh.read()
#     print 'Retrieved',len(data),'characters'
#
#     #put the data into a dictionary
#     data_parsed = json.loads(data)
#
#     total = 0
#     for item in data_parsed['comments']:
#         total += int(item['count'])
#
#     print 'Total: ', total


import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'

    try: js = json.loads(str(data))
    except: js = None
    if "status" not in js or js["status"] !="OK":
        print "Failure to retrieve"
        print data
        continue

    # print json.dumps(js, indent=4)

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    place_id = js["results"][0]["place_id"]
    location = js["results"][0]["formatted_address"]
    print "Place id:", place_id
    break