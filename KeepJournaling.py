
#Following instructions from https://gkeepapi.readthedocs.io/en/latest/#setting-note-content

import schedule
import time

def job():
    print("I'm working...")

schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)


#import gkeepapi

#keep = gkeepapi.Keep()
#success = keep.login('aceradness@gmail.com', 'Decathlete2010')

##Simple example to create a note
#note = keep.createNote('Todo', 'Be more like simon! Eat bagels for breakfast and move house each week to keep it fresh')
#note.pinned = True
##note.color = keep.node.ColorValue.Red

#keep.sync()

#print(note.title)
#print(note.text)

