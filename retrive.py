import urllib.request

import pyrebase
import time

config = {
    "apiKey": "AIzaSyCK4wd9Eb2zFhZh6LTpJh_A9F_Rcg6e8lM",
    "authDomain": "connectdbtofb.firebaseapp.com",
    "projectId": "connectdbtofb",
    "databaseURL": "https://connectdbtofb-default-rtdb.firebaseio.com/",
    "storageBucket": "connectdbtofb.appspot.com",
    "messagingSenderId": "766913817740",
    "appId": "1:766913817740:web:1afcaedfa98b43e1675fa9",
    "measurementId": "G-QCXTG2L8RK",
    "serviceAccount": "serviceAccount.json"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

#  read
path = input("enter the path to file in the firebase")
url = storage.child(path).get_url(None)
f = urllib.request.urlopen(url).read()
print(f)