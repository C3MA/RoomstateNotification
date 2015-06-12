import subprocess
from xml.dom import minidom
import smtplib
import time
import os
import os.path

# Definition

absender = ("aaa")
empfaenger = ("bbb")
mailserver = ("ccc")
mailspwd = ("ddd")

curlpath = '/path/curl'
statepath = '/path/state.xml'
timepath='/path/cccma_room_open.time'

# Current yearmonthday to now
now = time.strftime("%Y%m%d")


# Create file with old date
def schreibe_oldfile():
        fobjw = open(timepath, "w")
        fobjw.write ("20000101")
        fobjw.close

# Create file with current yearmonthday
def schreibe_tag():
        fobjw = open(timepath, "w")
        fobjw.write (now)
        fobjw.close

# Read yearmonthday from file
def lese_tag():
        fobjr = open(timepath, "r")
        lastopen = fobjr.readlines()
        fobjr.close
        return lastopen

# If datefile doesn't exist create one with old date
if not os.path.isfile(timepath) or not os.access(timepath, os.R_OK):
        print ("Zeitfile wird geschrieben")
        schreibe_oldfile()

# Read date from file
zeit = lese_tag()


# If date in file isn't the same as the current date
if not now in zeit:
        subprocess.call( curlpath + ' -vvv -o' + statepath + ' https://www.ccc-mannheim.de/roomstate/state.xml', shell=True)

        # xml parser
        doc = minidom.parse(statepath)
        stat = doc.getElementsByTagName("status")[0]
        dopen = stat.firstChild.data

        # Write mail if not closed
        if not "CLOSED" in dopen:

                content = "CCC Mannheim --- Raum ist offen"
                mail = smtplib.SMTP(mailserver,587)
                mail.set_debuglevel(2)

                mail.ehlo()
                mail.starttls()
                mail.login(absender,mailspwd)
                mail.sendmail(absender,empfaenger,content)
                mail.quit

                schreibe_tag()
