# RoomstateNotification

## Why ?

This Pyhon 3 Script was created for receiving an email when the CCC MA room status changes to OPEN.

## Requirement
* Python 3
* curl

In order to get this script working you need to modify the following lines:

* absender = ("aaa")    # sender email
* empfaenger = ("bbb")    # recipent email
* mailserver = ("ccc")    # fqdn for the mailserver
* mailspwd = ("ddd")    # password for the mailbox

* curlpath = '/path/curl'   # location for curl
* statepath = '/path/state.xml'   # path where the state.xml should be downloaded
* timepath='/path/cccma_room_open.time' # path where the timestamp file should be created

## Cronjob
I recommand to create a cronjob in order to start script at your desired time

### Example
*/2	15-22	*	*	5-6	root /usr/local/bin/python3 /path/cccma_room_open.py >/dev/null 2>&1
