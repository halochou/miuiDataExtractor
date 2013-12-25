#!/usr/local/bin/python2
'''
Extract info from MIUI Note database file.
Input is node.db, sqlite file from ROM flash.
Output is notes in stdout.
'''

import sqlite3
from datetime import datetime
from time import strftime

cx = sqlite3.connect("note.db")
cu = cx.cursor()
cu.execute("select * from note")
#print "Subject,Start Date,Start Time,End Date,End Time,All Day Event,Description,Location,Private"
note = cu.fetchone()
while note != None:
    print note[8]
    print '-' * 50
    #dtstart,tmstart = datetime.fromtimestamp(event[12]/1000).strftime('%m/%d/%y %H:%H:%S').split()
    #dtend,tmend = datetime.fromtimestamp(event[13]/1000).strftime('%m/%d/%y %H:%H:%S').split()
    #      sub  dts  tms  dte  tme  ade    desc loc
    #print '"%s","%s","%s","%s","%s",False,,"",True' % (event[5],dtstart,tmstart,dtend,tmend)
    note = cu.fetchone()
