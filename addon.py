import subprocess
import sys
import xbmcaddon
import xbmcgui

addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo('name')


def log(text, level=xbmc.LOGINFO):
    msg = "SkypeLauncher: " + text
    xbmc.log(msg, level=level)


def kodi_notify(text, level=xbmcgui.NOTIFICATION_INFO, title='Skype Launcher', time=5000):
    xbmcgui.Dialog().notification(title, text, level, time)

    xbmc.log(log_text.encode('utf-8'), level=xbmc.LOGERROR)


def run_skype():
    if sys.platform.startswith("linux"):
        subprocess.Popen(['/usr/bin/skypeforlinux'], close_fds=True)
    else:
        log("Can't launch Skype on this computer")
        kodi_notify(xbmcgui.NOTIFICATION_ERROR, "Sorry, only linux is supported")


run_skype()
