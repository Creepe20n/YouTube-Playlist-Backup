import colorama as ca
import pytube

ca.init()

class Loger:
    def FileNotFound(custom_message=""):
        print(ca.Fore.RED+"File not Found 101: "+str(custom_message)+ca.Fore.WHITE)
    def YoutubeError(custom_message = ""):
        print(ca.Fore.RED+"Playlist is either private or was deleted Error: "+str(custom_message)+ca.Fore.WHITE)

class ProgramTests():
    def PytubeApiTest(CustomTestLink = "https://www.youtube.com/watch?v=2Q30KTRk_OU&t=185s"):
        try:
            yt = pytube.YouTube(CustomTestLink)
            print("Test Pytube API\n"+yt.author)
            del yt
        except:
            ErrorMessage("API Error, please contact me under: https://cat-labs.itch.io/youtube-playlist-backup")

def ErrorMessage(message=""):
    print(ca.Fore.RED+message+ca.Fore.RESET)