#!/usr/bin/python

# MIT License

# Copyright (c) [2017] [Harvey Cary]

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import sys
from optparse import OptionParser
import ConfigParser
import nntplib
import socket
import yenc


HOMEDIR = os.getenv("HOME") + "/"



parser = OptionParser("usage: %prog [options] ",
    version="%prog 1.0")

parser.add_option("-c", "--config",
    action="store",
    type="string",
    dest="config",
    default=HOMEDIR + "/ubinc.cnf",
    help="configuration file name")

parser.add_option("-g", "--group",
    action="store",
    type="string",
    dest="group",
    default="*",
    help="By default " + sys.argv[0] + " will process every subscribed group in the .newsrc. This option specifies the name of one group to be processed. Note that group must exist in the .newsrc and must be subscribed.")

parser.add_option("-l", "--long",
    action="store_true",
    dest="long",
    default=False,
    help="Long filenames - uses the article subject as the filename. This makes life easier because many folks encode their files with terribly vague filenames.")

parser.add_option("-s", "--search",
    action="store",
    type="string",
    dest="search",
    default="*",
    help="")
 

(opts, args) = parser.parse_args()


config = ConfigParser.ConfigParser()
config.read(opts.config)

# Ensure download path is terminated with a / to allow appending filename withour breaking path
download_path = config.get('nntp', 'download_path')
if download_path[-1] != "/":
    download_path = download_path + "/"


x = yenc


def str_rem_spaces(mystr):

    mystr = mystr.replace(" ", "_")
    mystr = mystr.replace("/", "_")
    mystr = mystr.replace(":", "_")
    mystr = mystr.replace("__", "_")
    
    return mystr

def read_newsrc():
    print "read_newsrc"
    
    
    
conn = nntplib.NNTP(config.get('nntp', 'server'), \
    config.get('nntp', 'port'), \
    config.get('nntp', 'user'), \
    config.get('nntp', 'passwd'))

    
#group, last, first, flag
#conn.list("newsrc.txt")

resp, count, first, last, name = conn.group(opts.group)
print count, first, last, name


resp, subs = conn.xhdr('subject', first + '-' + last)
for id, subject in subs:
    #print id, subject

    print id
    
    if subject.find(opts.search) > 0:
        
        subject = str_rem_spaces(subject)
        
        print "SUBJECT: " + subject
        #conn.body(id, download_path + subject + ".txt")
        body_result = conn.body(id)
        print body_result
        
        for ln in body_result:
            print ln
    
    else:

        subject = str_rem_spaces(subject)
        
        print "SUBJECT: " + subject
        #conn.body(id, download_path + subject + ".txt")
        body_result = conn.body(id)
        print body_result
        
        for ln in body_result:
            print ln       
#response, number, id, list = conn.head()


exit()

#>>> resp, count, first, last, name = conn.group('gmane.comp.python.committers')

#>>> print 'Group', name, 'has', count, 'articles, range', first, 'to', last
#Group gmane.comp.python.committers has 1071 articles, range 1 to 1071
#>>> resp, subs = s.xhdr('subject', first + '-' + last)


