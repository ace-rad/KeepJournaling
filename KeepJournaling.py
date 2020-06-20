#Without script: each day I duplicate a Dailytemplate of preset questions as part of a journaling process, this template is usually tweaked at monthly intervals
#Intended outcome: automate the duplication and proivide more dynamic questions to improve the journaling process  


import gkeepapi #Following instructions from https://gkeepapi.readthedocs.io/en/latest/#setting-note-content
# import emoji 
from datetime import date

#job() script: Daily update of a custom journal template
keep = gkeepapi.Keep()
success = keep.login('@gmail.com', '...')

#Get contents of daily note
DailyJournalID = '1a8jSU-gNQd6Izud5Eu6yQnGbAXlrHSv55LbIyLNmckTglwgwyhi_ThT0DqG0nE2l7pIH'
WIPDailyJournal = keep.get(DailyJournalID)

    #To Do: 
    #Analyse how day gone went by inspecting latest entry on WIPDailyJournal
        #Effort - measure by number of characters? 
        #Effectiveness - how many of the questions attempted 

    #Use effort and Effectiveness measures to make adjustment to the DailyTemplateNoteText

#Define the daily template text and Append to the DailyJournal
DailyTemplateNoteText = str(date.today().month) + '.' + str(date.today().day) + ':' + '\nMM: streak is 🔥❄️ FOOT: ✔️❌ \nDMED0630: 🌅👨‍⚖️🌱🌇 “Today, I shall judge nothing that occurs,”\nDL: #\n💰 Money Direct rate? Amount?\nProductivity: Target 5+ hours on daily productivity\n   1. 🥇 One Thing: Ruthlessly closedown goals that are not working.\n   2. 🧘‍♂️Activate focus mode and turn my phone off\n   3. 💧🧶⚡ flow state achieved \n\n'
WIPDailyJournal.text = DailyTemplateNoteText + WIPDailyJournal.text


keep.sync()


# SCHEDULING - to be setup on Heroku server once job() script  is tested https://pypi.org/project/schedule/
    #import schedule
    #import time

    #def job(): 
    #    <daily keep update to go here> #job() script: Daily update of a custom journal template

    #schedule.every().day.at("05:30").do(job)

    #while True:
    #    schedule.run_pending()
    #    time.sleep(1)
