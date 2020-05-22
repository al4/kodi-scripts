import subprocess
import sys
import xbmcaddon
import xbmcgui

addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo('name')


def log(text, level=xbmc.LOGINFO):
    msg = "ZoomLauncher: " + text
    xbmc.log(msg, level=level)


def kodi_notify(text, level=xbmcgui.NOTIFICATION_INFO, title='Zoom Launcher', time=5000):
    xbmcgui.Dialog().notification(title, text, level, time)

    xbmc.log(text.encode('utf-8'), level=xbmc.LOGERROR)


def run_zoom():
    if sys.platform.startswith("linux"):
        kodi_notify("Launching Zoom", xbmcgui.NOTIFICATION_INFO)
        subprocess.Popen(['/usr/bin/zoom'], close_fds=True)
    else:
        log("Can't launch Zoom on this computer")
        kodi_notify(xbmcgui.NOTIFICATION_ERROR, "Sorry, only linux is supported")

run_zoom()
