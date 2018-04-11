import os, sys
import subprocess
from time import sleep

usage_string = """
Usage: python3 control_chrome.py <COMMAND>

<COMMAND>s available:
	>> goto URL - Navigates the tab to 'URL' specified
	>> previous - Go back in history
	>> forward - Go forward in history
	>> reload - Reloads current tab
	>> close - Closes current tab
	>> pin - Pins current tab
	>> unpin - Unpins current tab
	>> scrollDown N, smoothScrollDown N - Scrolls down by 'N' pixels
	>> scrollUp N, smoothScrollUp N - Scrolls up by 'N' pixels
	>> duplicate - Duplicates current tab and switches to it
	>> bookmark - Bookmarks current tab
	>> openLink N - Clicks on the 'N'th link of Google Search Results page
	>> details - Displays some details about the current tab (tid, title, url)
	>> speak - Speaks the title of the current tab
"""


def convert(url):
    if url.startswith('www.'):
        return 'https://' + url[len('www.'):]
    if not url.startswith('http://') and not url.startswith('https://'):
        return 'https://' + url
    return url


args = sys.argv
del args[0]

try:
	command = args[0]
except IndexError:
	command = "iDontKnowWhatIAmDoing"

print("-" * 40)
print("No. of Arguments:", len(args))
print("Args:", str(args))
print("-" * 40)


current_tid = int(subprocess.getoutput("""chromix-too raw chrome.tabs.getSelected null | grep -Po '"id":.*?[^\\\],"' """)[5:-2])
current_title = subprocess.getoutput("""chromix-too raw chrome.tabs.getSelected null | grep -Po '"title":.*?[^\\\],"' """)[9:-3]
current_url = subprocess.getoutput("""chromix-too raw chrome.tabs.getSelected null | grep -Po '"url":.*?[^\\\],"' """)[7:-3]

if command == "iDontKnowWhatIAmDoing":
	print(usage_string)
	exit()

elif command == "back" or command == "previous":
	os.system("""chromix-too raw chrome.tabs.executeScript null '{"code":"window.history.back()"}' """)

elif command == "forward" or command == "next":
	os.system("""chromix-too raw chrome.tabs.executeScript null '{"code":"window.history.forward()"}' """)

elif command == "pin":
	os.system("""chromix-too raw chrome.tabs.update """ + str(current_tid) + """ '{"pinned":true}' """)

elif command == "unpin":
	os.system("""chromix-too raw chrome.tabs.update """ + str(current_tid) + """ '{"pinned":false}' """)

elif command == "openLink":
	try:
		n = int(args[1])
	except IndexError:
		n = 1
	cStr = """chromix-too raw chrome.tabs.executeScript null '{"code":"document.querySelectorAll(\\".g > div > .rc > .r > a\\")[""" + str(n-1) + """].click()"}' """
	os.system(cStr)

elif command == "scrollDown" or command == "down":
	try:
		n = int(args[1])
	except IndexError:
		n = 50
	os.system("""chromix-too raw chrome.tabs.executeScript null '{"code":"window:scrollBy(0,""" + str(n) + """)"}' """)

elif command == "scrollUp" or command == "up":
	try:
		n = int(args[1])
	except IndexError:
		n = 50
	os.system("""chromix-too raw chrome.tabs.executeScript null '{"code":"window:scrollBy(0,-""" + str(n) + """)"}' """)

elif command == "smoothScrollDown" or command == "sDown":
	try:
		n = int(args[1])
	except IndexError:
		n = 50
	for i in range(n//4):
		os.system("""chromix-too raw chrome.tabs.executeScript null '{"code":"window:scrollBy(0,4)"}' """)
		sleep(0.001)

elif command == "smoothScrollUp" or command == "sUp":
	try:
		n = int(args[1])
	except IndexError:
		n = 50
	for i in range(n//4):
		os.system("""chromix-too raw chrome.tabs.executeScript null '{"code":"window:scrollBy(0,-4)"}' """)
		sleep(0.001)

elif command == "bookmark":
	os.system("chromix-too raw chrome.bookmarks.create '{\"title\":\"" + str(current_title) + "\", \"url\":\"" + str(current_url) + "\"}'")

elif command == "reload":
	os.system("chromix-too raw chrome.tabs.reload")

elif command == "remove" or command == "close":
	os.system("chromix-too raw chrome.tabs.remove " + str(current_tid))

elif command == "details":
	print("-" * 40)
	print("Current tab ID:", current_tid)
	print("Title:", current_title)
	print("URL:", current_url)
	print("-" * 40)

elif command == "remove" or command == "close":
	os.system("chromix-too raw chrome.tabs.remove " + str(current_tid))

elif command == "duplicate" or command == "clone":
	os.system("chromix-too raw chrome.tabs.duplicate " + str(current_tid))

elif command == "say" or command == "speak":
	print("Title:", current_title)
	os.system("chromix-too raw chrome.tabs.executeScript null '{\"code\":\"window.speechSynthesis.speak(new SpeechSynthesisUtterance(\\\"" + str(current_title) + "\\\"))\"}'")

elif command == "goto":
	try:
		goto_url = convert(str(args[1]))
	except IndexError:
		goto_url = "https://www.google.co.in"
	os.system("chromix-too raw chrome.tabs.update " + str(current_tid) + " '{\"url\":\"" + goto_url + "\"}'")

else:
	print("No such command available.")
	print(usage_string)
	exit()
  
