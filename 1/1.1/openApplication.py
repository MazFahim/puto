import webbrowser


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