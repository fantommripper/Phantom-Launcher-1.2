import customtkinter as CTk
from PIL import Image
import minecraft_launcher_lib as mll
import os

minecraft_directory = mll.utils.get_minecraft_directory().replace('minecraft', 'PhantomLauncher')
config_file_path = os.path.join(minecraft_directory, 'Client.ini')
versions_directory = os.path.join(minecraft_directory, 'versions')

appearanceMode = "dark"
installed_versions = []
nickname = ""
versions = mll.utils.get_version_list()

bar_COLOR = "#202125"
btn_COLOR = "#6301B0"
textVersion_COLOR = "#5B5C60"
btnHover_COLOR = "#45007B"
btnDonat_COLOR = "#B00189"
btnDonatHover_COLOR = "#680051"
white_COLOR = "#ffffff"
whiteHover_COLOR = "#e6e6e6"
downloadBtn_COLOR = "#141414"
downloadBtnHover_COLOR = "#0D0D0D"
canvas_COLOR = "#333333"

home_ICO = CTk.CTkImage(dark_image=Image.open("image/home.png"), size=(20,20))
account_ICO = CTk.CTkImage(dark_image=Image.open("image/Acaunt.png"), size=(20,20))
donat_ICO = CTk.CTkImage(dark_image=Image.open("image/Donat.png"), size=(20,20))
help_ICO = CTk.CTkImage(dark_image=Image.open("image/Help.png"), size=(20,20))
news_ICO = CTk.CTkImage(dark_image=Image.open("image/news.png"), size=(20,20))
seting_ICO = CTk.CTkImage(dark_image=Image.open("image/seting.png"), size=(20,20))
version_ICO = CTk.CTkImage(dark_image=Image.open("image/Version.png"), size=(20,20))
play_ICO = CTk.CTkImage(dark_image=Image.open("image/Play.png"), size=(20,20))
boosty_ICO = CTk.CTkImage(dark_image=Image.open("image/Boosty.png"), size=(20,25))
bg_IMAGE = CTk.CTkImage(dark_image=Image.open("image/BG.png"), size=(836,493))

release_versions = None
snapshot_versions = None
nicknameEnt_SEVE = None
config_FAIL = None
louding_PB = None
bosty = "https://boosty.to/__fantomm__"