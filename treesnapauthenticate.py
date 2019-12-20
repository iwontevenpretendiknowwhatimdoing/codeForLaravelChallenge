import requests
import json
import sqlite3
token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjRlNzYwMWUxMTk0NWE5MTA1NmUyYzhiOTg4MmJhODgxMjhhZTM2ZTE0NzI0NzZkYWQ0YjIzZWFmMjgyZDBjYWIzMDYyMDQwMGFjMGZhMjA2In0.eyJhdWQiOiIxIiwianRpIjoiNGU3NjAxZTExOTQ1YTkxMDU2ZTJjOGI5ODgyYmE4ODEyOGFlMzZlMTQ3MjQ3NmRhZDRiMjNlYWYyODJkMGNhYjMwNjIwNDAwYWMwZmEyMDYiLCJpYXQiOjE1NzY3Nzg5MTcsIm5iZiI6MTU3Njc3ODkxNywiZXhwIjoxNjA4NDAxMzE3LCJzdWIiOiI1MTc4Iiwic2NvcGVzIjpbXX0.mHZvXl02omEOQaiuOEB0KqEuaXJrqsYqCf8zJewBBSJQsi_XA9qg9VUel85GkmHoJcG0XKfEVfMsK3xEq8DO4OMKfFuEGxWVseI5t_EHPOcEGY9tDUoGs8Qn1dh_og5VOL25fIEeY52RE54UJbEEjFPLaRw3zZB5tZgFewjo2MVyV8jf2mjGZr9iuqtPam-GXmEZcszx3akteYMMVG0B7bTISIRLwyL7lLk_Y-x8-7AXksgREpGm3GWSg24WgKMbYbCjjmhlpDSpCRm0Cv522_sBugYkWt08Uop_vFFRBm9vexxdJPupfhUtwJPPhxPOt-HzMEsJsG0ZgwAHgKSt4HLNFNedixCUIarPpSlO25nWb4oJJQlQErTCc3UdCCfx5fac33fEeZ02By8EbRazVuMoB6K3xysjW-y4QMnuXJIXPfg5l48qUkW8w1eVM8LwASs3jJnf1Wg5k64lHaHq0J5aEsYmjfFY_iZNeMFXQ7InKWuqNRw2gpvDGPa6Eemj8Isu1-DRVYRA7EUQcu0GywFD1BncI6n37kx2LJedEtG1SA6d9cymVse16kwv6sSJHN519PGC31GkgPcxiJDoTlrYtTI_ofLcMT6D_ojSpaae61Q_sT_9qX5n6d_vrWv7lTVxiNuoO8V9LSoZZWKLhdHqxahdWF4vamfsCUzmiH8'
headers = {'Authorization': 'Bearer ' + token}
url = 'https://treesnap.org/web-services/v1/observations'
querystring ={"page":"1"}
r = requests.request("GET", url, headers=headers, params=querystring)
splittext=json.loads(r.text)
print(splittext)
try:
    sqlCon=sqlite3.connect('database.sqlite')
    print('Connected to SQLite')
    createTable='''CREATE TABLE TreesnapInfo( id INTEGER PRIMARY KEY, custom_id TEXT NOT NULL, category TEXT NOT NULL,
genus TEXT NOT NULL, species TEXT NOT NULL, submitter TEXT NOT NULL, thumbnail IMAGE,
images IMAGE, longitude TEXT NOT NULL, latitude TEXT NOT NULL, location_accuracy TEXT NOT NULL, collection_date TEXT NOT NULL,
meta_data TEXT NOT NULL, locationCharacteristics TEXT NOT NULL, diameterNumeric_confidence TEXT NOT NULL, url TEXT NOT NULL);'''
    cursor=sqlCon.cursor()
    cursor.execute(createTable)
    sqlCon.commit()
    print('table created')
except sqlite3.Error as error:
    print('Error Connecting', error)
finally:
    sqlCon.close()


    
    
    