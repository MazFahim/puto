import webbrowser
import os
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")


def openCommand(command):
    print(command)
    if "gmail" in command:
        print("gmail")
        url = 'https://mail.google.com/mail/u/0/#inbox'
        webbrowser.register('chrome',
                            None,
                            webbrowser.BackgroundBrowser(
                                "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
        webbrowser.get('chrome').open(url)
    elif "linkedin" in command:
        print("linkedin")
        url = 'https://www.linkedin.com/in/maz-fahim-a401351a3/'
        webbrowser.register('chrome',
                            None,
                            webbrowser.BackgroundBrowser(
                                "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
        webbrowser.get('chrome').open(url)
    elif "github" in command:
        print("github")
        url = 'https://github.com/'
        webbrowser.register('chrome',
                            None,
                            webbrowser.BackgroundBrowser(
                                "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
        webbrowser.get('chrome').open(url)
    elif "youtube" in command:
        print("youtube")
        url = 'https://www.youtube.com/'
        webbrowser.register('chrome',
                            None,
                            webbrowser.BackgroundBrowser(
                                "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
        webbrowser.get('chrome').open(url)
    elif "colour code" in command:
        print("color codes")
        url = 'https://htmlcolorcodes.com/'
        webbrowser.register('chrome',
                            None,
                            webbrowser.BackgroundBrowser(
                                "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
        webbrowser.get('chrome').open(url)
    elif "drive" in command:
        localFolder(command)


def localFolder(folderName):
    elements = folderName.split(' ')
    print(elements)
    try:
        drive_index = elements.index('drive')
        drive_path = elements[drive_index-1]
        filename = ""
        for i in range(1, drive_index-1):
            if elements[i] == 'in' or elements[i] == 'ine':
                break
            filename = filename + elements[i] + " "
        print(filename)
        os.startfile(r'%s:\%s' % (drive_path, filename))
        #os.startfile(r'D:\Senior Project')
    except Exception as e:
        print("Can't find the folder")


def searchOnline(q):
    q2 = q.replace("search", '')
    print(q2)
    for j in search(q2, tld="co.in", num=3, stop=5, pause=2):
        print(j)