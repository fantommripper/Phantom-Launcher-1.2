import configparser
from typing import Optional, Tuple, Union
import customtkinter as CTk
import tkinter as Tk
import data as d
import logic as l 

class App(CTk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("900x550")
        self.title("Phantom Launcher")
        self.resizable(False, False)
        CTk.set_appearance_mode(d.appearanceMode)

        def test():
            self.play_BTN.place_forget()

        self.config = configparser.ConfigParser()
        self.config.read(d.config_file_path)
        if 'Player' in self.config:
            saved_nickname = self.config['Player'].get('nickname', '')
            self.nickname_ENT.insert(0, d.nickname)

        self.left_BAR = CTk.CTkFrame(master=self, width=64, height=550, bg_color=d.bar_COLOR)
        self.left_BAR.place(x=0, y=0)

        self.down_BAR = CTk.CTkFrame(master=self, width=900, height=64, bg_color=d.bar_COLOR)
        self.down_BAR.place(x=0, y=486)


        self.home_BTN = CTk.CTkButton(
                                 master=self.left_BAR,
                                 width=36, height=36,
                                 fg_color=d.btn_COLOR,
                                 text="", corner_radius=7,
                                 hover_color=d.btnHover_COLOR,
                                 image=d.home_ICO
                                 )
        self.home_BTN.place(x=13, y= 70)

        self.version_BTN = CTk.CTkButton(
                                 master=self.left_BAR,
                                 width=36, height=36,
                                 fg_color=d.btn_COLOR,
                                 text="", corner_radius=7,
                                 hover_color=d.btnHover_COLOR,
                                 image=d.version_ICO
                                 )
        self.version_BTN.place(x=13, y= 125)

        self.account_BTN = CTk.CTkButton(
                                 master=self.left_BAR,
                                 width=36, height=36,
                                 fg_color=d.btn_COLOR,
                                 text="", corner_radius=7,
                                 hover_color=d.btnHover_COLOR,
                                 image=d.account_ICO
                                 )
        self.account_BTN.place(x=13, y= 180)

        self.help_BTN = CTk.CTkButton(
                                 master=self.left_BAR,
                                 width=36, height=36,
                                 fg_color=d.btn_COLOR,
                                 text="", corner_radius=7,
                                 hover_color=d.btnHover_COLOR,
                                 image=d.help_ICO
                                 )
        self.help_BTN.place(x=13, y= 235)

        self.seting_BTN = CTk.CTkButton(
                                 master=self.left_BAR,
                                 width=36, height=36,
                                 fg_color=d.btn_COLOR,
                                 text="", corner_radius=7,
                                 hover_color=d.btnHover_COLOR,
                                 image=d.seting_ICO
                                 )
        self.seting_BTN.place(x=13, y= 290)

        self.news_BTN = CTk.CTkButton(
                                 master=self.left_BAR,
                                 width=36, height=36,
                                 fg_color=d.btn_COLOR,
                                 text="", corner_radius=7,
                                 hover_color=d.btnHover_COLOR,
                                 image=d.news_ICO
                                 )
        self.news_BTN.place(x=13, y= 345)

        self.donat_BTN = CTk.CTkButton(
                                 master=self.left_BAR,
                                 width=36, height=36,
                                 fg_color=d.btnDonat_COLOR,
                                 text="", corner_radius=7,
                                 hover_color=d.btnDonatHover_COLOR,
                                 image=d.donat_ICO
                                 )
        self.donat_BTN.place(x=13, y= 450)

        self.nickname_ENT = CTk.CTkEntry(master=self.down_BAR, placeholder_text="nickname", height=36, width=150)
        self.nickname_ENT.place(x=70, y=17)

        self.downloadedVersion_CBB = CTk.CTkComboBox(master=self.down_BAR, values=d.installed_versions, state="disabled", height=36, width=194)
        self.downloadedVersion_CBB.place(x=374, y=17)

        self.play_BTN = CTk.CTkButton(
                                 master=self.down_BAR,
                                 width=170, height=36,
                                 fg_color=d.btn_COLOR,
                                 text="Play", corner_radius=7,
                                 hover_color=d.btnHover_COLOR,
                                 image=d.play_ICO,
                                 command=test
                                 )
        self.play_BTN.place(x=718, y= 17)

        self.bg_leadl = CTk.CTkLabel(master=self, text="", image=d.bg_IMAGE, width=836, height=492)
        self.bg_leadl.place(x=64, y=0)

        l.updateVersionsList(self.downloadedVersion_CBB)
    
if __name__ == "__main__":
    app = App()
    app.mainloop()