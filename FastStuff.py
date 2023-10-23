import os
import pytube
import ErrorLoger as EL
import colorama as ca
ca.init()
class FastFile:
    def LookForExiting(path, create_file=False):
        if os.path.exists(str(path)):
            return True
        elif not create_file:
            return False
        else:
            try:
                f= open(path,"x")
                f.close()
                return True
            except:
                EL.Loger.FileNotFound()
    def RebuildSaveFile(WriteData,Path,FileName,CreateBackup=True):
        TotalPath = Path+FileName+".sav"
        if CreateBackup:
            os.rename(TotalPath,Path+FileName+".old")
        for x in WriteData:
            pass
class FastYT:
    def GetVideosFromPlaylist(url):
        try:
            yt = pytube.Playlist(url)
            i = yt.video_urls
            del yt
            return i
        except:
            return False
    def ShowInfos(url,IsVideo = False):
        try:
            if IsVideo:
                yt = pytube.YouTube(url)
            else:
                yt = pytube.Playlist(url)
            return '\nTitle: '+str(yt.title)+'\nOwner: '+str(yt.owner)+'\nVideos: '+str(yt.length)+'\n'
        except:
            return EL.Loger.YoutubeError("Couldnt get infos from Playlist:"+url)
    def ControllExistence(url,IsVideo = False):
        try:
            if IsVideo:
                yt = pytube.YouTube(url)
                yt.author
                print(ca.Fore.GREEN+'Video exist'+ca.Fore.WHITE)
            else:
                yt = pytube.Playlist(url)
                yt.owner
                print(ca.Fore.GREEN+'Playlist exist'+ca.Fore.WHITE)
            del yt
            return True
        except:
            EL.Loger.YoutubeError("Playlist or Video dosent Exist ")
            return False