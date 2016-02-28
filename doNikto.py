#!/usr/bin/python26
# -*-coding:Latin-1 -*
import codecs,csv,subprocess,sys

__author__ = "Justin Morehouse"
__copyright__ = "Copyright 2010, Justin Morehouse"
__credits__ = ["Justin Morehouse"]
__license__ = "GPL v3"
__version__ = "0.1"
__maintainer__ = "Justin Morehouse"
__email__ = "http://scr.im/mascasa"
__website__ = "http://www.stratumsecurity.com"
__status__ = "beta"

# Default message            
opts_str = \
    '\
    \n\
    USAGE:\n\
    \n\
    python donikto.py [Host File]\n\
    \n\
    Host file should be in IP,Port format, with one host per line.\n\
    (e.g. 192.168.1.1,80)\n\
    '

# Prints opts_str if no arguments are passed
if len(sys.argv)==1:
        print opts_str
        sys.exit(0)

# Assigns file name to the first argument passed at command line
for x in sys.argv:
     filename = x

# Opens the file
hostfile = codecs.open(filename, 'rU', 'utf-8')
csvReader= csv.reader( hostfile )

# Parses csv and for each row executes nikto
for row in csvReader:
    try:
        switches = "-h " + row[0] + " -p "  + row[1] + " -F HTML -o " + "Nikto_" + row[0] + "_" + row[1] + ".html"
        subprocess.call("./nikto.pl " + switches, shell=True)
    # Catches Ctrl+C and moves on to the next host
    except KeyboardInterrupt:
        pass
hostfile.close()
