import configparser
from typing import Optional, Tuple, Union
import customtkinter as CTk
import tkinter as Tk
import data as d
import logic as l 
import minecraft_launcher_lib as mll
import subprocess
from uuid import uuid1
from random_username.generate import generate_username
import sys
import threading

class App(CTk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("895x550")
        self.title("Phantom Launcher")
        self.resizable(False, False)
        CTk.set_appearance_mode(d.appearanceMode)


        self.left_BAR = CTk.CTkFrame(master=self, width=64, height=550, bg_color=d.bar_COLOR)
        self.left_BAR.place(x=0, y=0)

        self.down_BAR = CTk.CTkFrame(master=self, width=900, height=64, bg_color=d.bar_COLOR)
        self.down_BAR.place(x=0, y=486)

        self.main_FRAME = CTk.CTkFrame(master=self, width=830, height=490)
        self.main_FRAME.place(x=64, y=0)

        l.start(self.main_FRAME)

        self.home_BTN = CTk.CTkButton(
                                 master=self.left_BAR,
                                 width=36, height=36,
                                 fg_color=d.btn_COLOR,
                                 text="", corner_radius=7,
                                 hover_color=d.btnHover_COLOR,
                                 image=d.home_ICO,
                                 command=lambda: l.openHomeWindow(self.main_FRAME),
                                 )
        self.home_BTN.place(x=13, y= 70)

        self.version_BTN = CTk.CTkButton(
                                 master=self.left_BAR,
                                 width=36, height=36,
                                 fg_color=d.btn_COLOR,
                                 text="", corner_radius=7,
                                 hover_color=d.btnHover_COLOR,
                                 image=d.version_ICO,
                                 command=lambda: l.openVersionWindow(self.main_FRAME),
                                 )
        self.version_BTN.place(x=13, y= 125)

        self.account_BTN = CTk.CTkButton(
                                 master=self.left_BAR,
                                 width=36, height=36,
                                 fg_color=d.btn_COLOR,
                                 text="", corner_radius=7,
                                 hover_color=d.btnHover_COLOR,
                                 image=d.account_ICO,
                                 command=lambda: l.openAccountWindow(self.main_FRAME),
                                 )
        self.account_BTN.place(x=13, y= 180)

        self.help_BTN = CTk.CTkButton(
                                 master=self.left_BAR,
                                 width=36, height=36,
                                 fg_color=d.btn_COLOR,
                                 text="", corner_radius=7,
                                 hover_color=d.btnHover_COLOR,
                                 image=d.help_ICO,
                                 command=lambda: l.openHelpWindow(self.main_FRAME),
                                 )
        self.help_BTN.place(x=13, y= 235)

        self.seting_BTN = CTk.CTkButton(
                                 master=self.left_BAR,
                                 width=36, height=36,
                                 fg_color=d.btn_COLOR,
                                 text="", corner_radius=7,
                                 hover_color=d.btnHover_COLOR,
                                 image=d.seting_ICO,
                                 command=lambda: l.openSetingWindow(self.main_FRAME),
                                 )
        self.seting_BTN.place(x=13, y= 290)

        self.news_BTN = CTk.CTkButton(
                                 master=self.left_BAR,
                                 width=36, height=36,
                                 fg_color=d.btn_COLOR,
                                 text="", corner_radius=7,
                                 hover_color=d.btnHover_COLOR,
                                 image=d.news_ICO,
                                 command=lambda: l.openNewsWindow(self.main_FRAME),
                                 )
        self.news_BTN.place(x=13, y= 345)

        self.donat_BTN = CTk.CTkButton(
                                 master=self.left_BAR,
                                 width=36, height=36,
                                 fg_color=d.btnDonat_COLOR,
                                 text="", corner_radius=7,
                                 hover_color=d.btnDonatHover_COLOR,
                                 image=d.donat_ICO,
                                 command=lambda: l.openDonatWindow(self.main_FRAME),
                                 )
        self.donat_BTN.place(x=13, y= 450)

        self.nickname_ENT = CTk.CTkEntry(master=self.down_BAR, placeholder_text="nickname", height=36, width=150)
        self.nickname_ENT.place(x=70, y=17)

        self.config = configparser.ConfigParser()
        self.config.read(d.config_file_path)

        if 'Player' in self.config:
            saved_nickname = self.config['Player'].get('nickname', '')
            self.nickname_ENT.insert(0, d.nickname)

        self.downloadedVersion_CBB = CTk.CTkComboBox(master=self.down_BAR, values=d.installed_versions, state="disabled", height=36, width=194)
        self.downloadedVersion_CBB.place(x=374, y=17)

        def launchMinecraft(version):
            username = self.nickname_ENT.get()
            if username == "":
                username = generate_username()[0]

            if 'Player' not in self.config:
                self.config['Player'] = {}
            self.config['Player']['nickname'] = username

            with open(d.config_file_path, 'w') as configfile:  # Відкриваємо новий файл для запису
                self.config.write(configfile)

            options = {
                'username': username,
                'uuid': str(uuid1()),
                'token': ''
            }

            mll.install.install_minecraft_version(versionid=version, minecraft_directory=d.minecraft_directory)

            l.updateVersionsList()

            d.louding_PB.start()
            subprocess.call(mll.command.get_minecraft_command(version=version, minecraft_directory=d.minecraft_directory, options=options))
            d.louding_PB.stop()
            d.louding_PB.configure(mode="determinate")
            d.louding_PB.set(0)
            d.louding_PB.configure(mode="indeterminate")

            interfaceControl(True)

        def startGame():

            interfaceControl(False)
            threading.Thread(target=launchMinecraft, args=(self.downloadedVersion_CBB.get(),)).start()
            l.openHomeWindow(self.main_FRAME)


        self.play_BTN = CTk.CTkButton(
                                 master=self.down_BAR,
                                 width=170, height=36,
                                 fg_color=d.btn_COLOR,
                                 text="Play", corner_radius=7,
                                 hover_color=d.btnHover_COLOR,
                                 image=d.play_ICO,
                                 command=startGame
                                 )
        self.play_BTN.place(x=718, y= 17)

        def interfaceControl(bool):
            if bool == False:
                self.downloadedVersion_CBB.configure(state="disabled")
                self.nickname_ENT.configure(state="disabled")
                self.donat_BTN.configure(state="disabled")
                self.news_BTN.configure(state="disabled")
                self.seting_BTN.configure(state="disabled")
                self.help_BTN.configure(state="disabled")
                self.account_BTN.configure(state="disabled")
                self.home_BTN.configure(state="disabled")
                self.version_BTN.configure(state="disabled")
                self.play_BTN.configure(state="disabled")
            elif bool == True:
                self.downloadedVersion_CBB.configure(state="normal")
                self.nickname_ENT.configure(state="normal")
                self.donat_BTN.configure(state="normal")
                self.news_BTN.configure(state="normal")
                self.seting_BTN.configure(state="normal")
                self.help_BTN.configure(state="normal")
                self.account_BTN.configure(state="normal")
                self.home_BTN.configure(state="normal")
                self.version_BTN.configure(state="normal")
                self.play_BTN.configure(state="normal")

        self.bg_leadl = CTk.CTkLabel(master=self.main_FRAME, text="", image=d.bg_IMAGE, width=836, height=492)
        self.bg_leadl.place(x=0, y=0)

        l.updateVersionsComdoBox(self.downloadedVersion_CBB)

    
if __name__ == "__main__":
    app = App()
    l.set_app_instance(app)
    app.mainloop()