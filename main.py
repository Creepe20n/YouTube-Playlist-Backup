import os
from FastStuff import FastFile as FF
from FastStuff import FastYT as FYT
import ErrorLoger as EL
import colorama as ca
ca.init()
PlaylistNames = []
PlaylistUrls = []
MainFileName = 'YSS2.sav'
def main():
    print('Welcome to Charlie2.0')
    StartActions()
def StartActions():
    if not EL.ProgramTests.PytubeApiTest():
        print('Failure')
        while True:
            pass
    print("Looking for Savefile (o_0)")
    MainFilePath =os.path.expanduser("~\\"+MainFileName)
    if not FF.LookForExiting(MainFilePath,True):
        EL.Loger.FileNotFound("Main Savefile Error")
        return
    print("Found Savefile i(0u0)i")
    TempFile = open(MainFilePath,"r")
    TempInt = 1
    for x in TempFile:
        x = x.replace("\n","")
        if TempInt == 2:
            PlaylistUrls.append(x)
            TempInt =1
        else:
            PlaylistNames.append(x)
        TempInt = TempInt +1
    TempFile.close()
    MainMenu()

def MainMenu():
    print("\n__Main_Menu_V0.1__")
    color = ca.Fore.RESET
    if len(PlaylistUrls) <= 0:
        color = ca.Fore.RED
    print(color+"1) Control Save files\n"+ca.Fore.RESET+"2)Playlist Options")
    inp = str(input())
    if inp == "1":
        print("Not Existing LOL")
    elif inp == "2":
        PlaylistMenu()

def PlaylistMenu():
    print("\n__Playlist_Options_V1.0__\n1)Add/Remove Playlist\n2)Update Savefile")
    Inp = str(input())
    if Inp == "1":
        print("1)Add Playlist\n2)Remove Playlist")
        Inp = str(input())
        if Inp == "1":
            AddPlaylist()
def AddPlaylist():
    print(ca.Fore.RED+"Remember that this Action will fail when the Playlist is private"+ca.Fore.RESET)
    Inp = str(input("Copy Playlist Url here:"))
    if not FYT.ControllExistence(Inp):
        MainMenu()
        return
    print(FYT.ShowInfos(Inp))
main()