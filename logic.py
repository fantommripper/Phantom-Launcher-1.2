import data as d
import customtkinter as CTk
import os
import webbrowser
import tkinter
import threading
import minecraft_launcher_lib as mll
import subprocess
from uuid import uuid1
from random_username.generate import generate_username
import os
from tkinter import messagebox


app_instance = None

def interfaceControl(bool):
    global app_instance
    if bool == False:
        app_instance.downloadedVersion_CBB.configure(state="disabled")
        app_instance.nickname_ENT.configure(state="disabled")
        app_instance.donat_BTN.configure(state="disabled")
        app_instance.news_BTN.configure(state="disabled")
        app_instance.seting_BTN.configure(state="disabled")
        app_instance.help_BTN.configure(state="disabled")
        app_instance.account_BTN.configure(state="disabled")
        app_instance.home_BTN.configure(state="disabled")
        app_instance.version_BTN.configure(state="disabled")
        app_instance.play_BTN.configure(state="disabled")
    elif bool == True:
        app_instance.downloadedVersion_CBB.configure(state="normal")
        app_instance.nickname_ENT.configure(state="normal")
        app_instance.donat_BTN.configure(state="normal")
        app_instance.news_BTN.configure(state="normal")
        app_instance.seting_BTN.configure(state="normal")
        app_instance.help_BTN.configure(state="normal")
        app_instance.account_BTN.configure(state="normal")
        app_instance.home_BTN.configure(state="normal")
        app_instance.version_BTN.configure(state="normal")
        app_instance.play_BTN.configure(state="normal")

def set_app_instance(app):
    global app_instance
    app_instance = app

def launchMinecraft(version):
    global app_instance

    if not os.path.exists(os.path.dirname(d.config_file_path)):
        os.makedirs(os.path.dirname(d.config_file_path))

    username = app_instance.nickname_ENT.get()
    if username == "":
        username = generate_username()[0]

    if 'Player' not in app_instance.config:
        app_instance.config['Player'] = {}
    app_instance.config['Player']['nickname'] = username

    with open(d.config_file_path, 'w') as configfile:
        app_instance.config.write(configfile)

    options = {
        'username': username,
        'uuid': str(uuid1()),
        'token': ''
    }

    mll.install.install_minecraft_version(versionid=version, minecraft_directory=d.minecraft_directory)

    d.louding_PB.start()
    subprocess.call(mll.command.get_minecraft_command(version=version, minecraft_directory=d.minecraft_directory, options=options))
    d.louding_PB.stop()
    d.louding_PB.configure(mode="determinate")
    d.louding_PB.set(0)
    d.louding_PB.configure(mode="indeterminate")

    interfaceControl(True)

def updateVersionsComdoBox(ComboBox):
    if os.path.exists(d.versions_directory):
        versions = os.listdir(d.versions_directory)
        ComboBox.configure(state="normal")
        d.installed_versions = []

        for version in versions:
            d.installed_versions.append(version)
        # Обновляем значения выпадающего списка
            
        ComboBox.configure(values= d.installed_versions)
    else:
       ComboBox.configure(state="disabled")

def hide_objects_on_main_frame(frame):
    for child in frame.winfo_children():
        child.destroy()

def updateVersionsList():
    if os.path.exists(d.versions_directory):
        versions = os.listdir(d.versions_directory)
        d.installed_versions = []

        for version in versions:
            d.installed_versions.append(version)
        # Обновляем значения выпадающего списка

def openHomeWindow(frame):
    global louding_PB

    hide_objects_on_main_frame(frame)
    bg_leadl = CTk.CTkLabel(master=frame, text="", image=d.bg_IMAGE, width=836, height=492)
    bg_leadl.place(x=0, y=0)

    d.louding_PB = CTk.CTkProgressBar(master=frame, width=836, height=17, mode="indeterminate",progress_color=d.btn_COLOR)
    d.louding_PB.place(x=0, y=475)

def openVersionWindow(frame):
    #messagebox.showinfo("Ok", "Ok")
    hide_objects_on_main_frame(frame)
    bg_leadl = CTk.CTkLabel(master=frame, text="", image=d.bg_IMAGE, width=836, height=492)
    bg_leadl.place(x=0, y=0)



    def _on_mousewheel(event):
        versionCanvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        snapshotСanvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    tabview = CTk.CTkTabview(master=frame, width=836, height=492)
    tabview.place(x= 0, y=0)
    tabview.add("release")
    tabview.add("snapshot")
    tabview.add("my version")

    versionCanvas = CTk.CTkCanvas(master=tabview.tab("release"), width=820, bg=d.canvas_COLOR,  height=492, highlightthickness=0)
    versionCanvas.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)

    snapshotСanvas = CTk.CTkCanvas(master=tabview.tab("snapshot"), width=820, bg=d.canvas_COLOR,  height=492, highlightthickness=0)
    snapshotСanvas.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)

    VersionCanvasFrame = CTk.CTkFrame(versionCanvas, bg_color=d.canvas_COLOR)
    versionCanvas.create_window((0, 0), window=VersionCanvasFrame, anchor=tkinter.NW, width=800, height=3200)

    SnapshotCanvasFrame = CTk.CTkFrame(snapshotСanvas, bg_color=d.canvas_COLOR)
    snapshotСanvas.create_window((0, 0), window=SnapshotCanvasFrame, anchor=tkinter.NW, width=800, height=22000)

    version_x_offset = 15
    version_y_offset = 15
    version_row_count = 0

    snapshot_x_offset = 15
    snapshot_y_offset = 15
    snapshot_row_count = 0

    def launch_game(version):
        updateVersionsList()
        interfaceControl(False)
        threading.Thread(target=launchMinecraft, args=(version,)).start()
        openHomeWindow(frame)


    for version in d.release_versions:
        bgVersion_FRAME = CTk.CTkFrame(master=VersionCanvasFrame, bg_color=d.bar_COLOR, width=250, height=70)
        bgVersion_FRAME.place(x=version_x_offset, y=version_y_offset)

        textVersion_FRAME = CTk.CTkFrame(master=VersionCanvasFrame, bg_color=d.textVersion_COLOR, width=250, height=35)
        textVersion_FRAME.place(x=version_x_offset, y=version_y_offset)
 
        version_label = CTk.CTkLabel(textVersion_FRAME, text=version, fg_color="transparent")
        version_label.place(x=109, y=3)
 
        if version not in d.installed_versions:
            install_button = CTk.CTkButton(width=131, height=23, master=bgVersion_FRAME, text="download",fg_color= d.downloadBtn_COLOR, hover_color= d.downloadBtnHover_COLOR, command=lambda version=version: launch_game(version))
            install_button.place(x=57, y=40)
        else:
            play_button = CTk.CTkButton(width=131, height=23, master=bgVersion_FRAME, text="play", command=lambda version=version: launch_game(version))
            play_button.place(x=57, y=40)
 
        version_row_count += 1
        if version_row_count >= 3:
            version_row_count = 0
            version_x_offset = 15
            version_y_offset += 110
        else:
            version_x_offset += 260

    VersionCanvasFrame.update_idletasks()
    versionCanvas.config(scrollregion=versionCanvas.bbox(tkinter.ALL))
    versionCanvas.bind_all("<MouseWheel>", _on_mousewheel)

    for version in d.snapshot_versions:
        bgSnapshot_FRAME = CTk.CTkFrame(master=SnapshotCanvasFrame, bg_color=d.bar_COLOR, width=250, height=70)
        bgSnapshot_FRAME.place(x=snapshot_x_offset, y=snapshot_y_offset)

        textSnapshot_FRAME = CTk.CTkFrame(master=SnapshotCanvasFrame, bg_color=d.textVersion_COLOR, width=250, height=35)
        textSnapshot_FRAME.place(x=snapshot_x_offset, y=snapshot_y_offset)
 
        version_label = CTk.CTkLabel(textSnapshot_FRAME, text=version, fg_color="transparent")
        version_label.place(x=109, y=3)
 
        if version not in d.installed_versions:
            install_button = CTk.CTkButton(width=131, height=23, master=bgSnapshot_FRAME, text="download",fg_color= d.downloadBtn_COLOR, hover_color= d.downloadBtnHover_COLOR, command=lambda version=version: launch_game(version))
            install_button.place(x=57, y=40)
        else:
            play_button = CTk.CTkButton(width=131, height=23, master=bgSnapshot_FRAME, text="play", command=lambda version=version: launch_game(version))
            play_button.place(x=57, y=40)
 
        snapshot_row_count += 1
        if snapshot_row_count >= 3:
            snapshot_row_count = 0
            snapshot_x_offset = 15
            snapshot_y_offset += 110
        else:
            snapshot_x_offset += 260

    SnapshotCanvasFrame.update_idletasks()
    snapshotСanvas.config(scrollregion=snapshotСanvas.bbox(tkinter.ALL))
    snapshotСanvas.bind_all("<MouseWheel>", _on_mousewheel)

def openAccountWindow(frame):
    hide_objects_on_main_frame(frame)
    bg_leadl = CTk.CTkLabel(master=frame, text="", image=d.bg_IMAGE, width=836, height=492)
    bg_leadl.place(x=0, y=0)


def openHelpWindow(frame):
    hide_objects_on_main_frame(frame)
    bg_leadl = CTk.CTkLabel(master=frame, text="", image=d.bg_IMAGE, width=836, height=492)
    bg_leadl.place(x=0, y=0)


def openSetingWindow(frame):
    hide_objects_on_main_frame(frame)
    bg_leadl = CTk.CTkLabel(master=frame, text="", image=d.bg_IMAGE, width=836, height=492)
    bg_leadl.place(x=0, y=0)


def openNewsWindow(frame):
    hide_objects_on_main_frame(frame)
    bg_leadl = CTk.CTkLabel(master=frame, text="", image=d.bg_IMAGE, width=836, height=492)
    bg_leadl.place(x=0, y=0)


def openDonatWindow(frame):
    hide_objects_on_main_frame(frame)
    bg_leadl = CTk.CTkLabel(master=frame, text="", image=d.bg_IMAGE, width=836, height=492)
    bg_leadl.place(x=0, y=0)

    boosty_BTN = CTk.CTkButton(
                             master=frame,
                             width=36, height=36,
                             fg_color=d.white_COLOR,
                             text="", corner_radius=7,
                             hover_color=d.whiteHover_COLOR,
                             image=d.boosty_ICO,
                             command=openBoosty,
                             )
    boosty_BTN.place(x=382, y=210)

def openBoosty():
    webbrowser.open(d.bosty)

def start(frame):
    openHomeWindow(frame)
    d.release_versions = [version['id'] for version in d.versions if version['type'] == 'release']
    d.snapshot_versions = [version['id'] for version in d.versions if version['type'] == 'snapshot']
