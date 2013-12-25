#!/usr/local/bin/python2
import sqlite3
from datetime import datetime
from time import strftime

cx = sqlite3.connect("calendar.db")
cu = cx.cursor()
cu.execute("select * from Events")
print "Subject,Start Date,Start Time,End Date,End Time,All Day Event,Description,Location,Private"
event = cu.fetchone()
while event != None:
    dtstart,tmstart = datetime.fromtimestamp(event[12]/1000).strftime('%m/%d/%y %H:%H:%S').split()
    dtend,tmend = datetime.fromtimestamp(event[13]/1000).strftime('%m/%d/%y %H:%H:%S').split()
    #      sub  dts  tms  dte  tme  ade    desc loc
    print '"%s","%s","%s","%s","%s",False,,"",True' % (event[5],dtstart,tmstart,dtend,tmend)
    event = cu.fetchone()
