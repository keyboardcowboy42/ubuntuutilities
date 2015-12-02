#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# Written By Hades.y2k
# Nov 5 2015
# GNU GPL v<2.0>

import os
import sys


def aptupdate():
    os.system("sudo apt-get update")

def essentials():
    os.system("clear")
    print("[!] Going to install essentials programs for Ubuntu")
    print("    Programs below are going to install")
    print("     - Ubuntu Restriected Extras")
    print("     - Unity Tweak Tool")
    print("     - Dconf-Editor")
    print("     - Compiz Config Settings Manager")
    print("     - HTop")
    print("     - Java Runtime 8")
    print("     - Virtual Box")
    print("     - Wine")
    print("     - Play On Linux")
    print("     - Steam")
    print("     - VLC Media Player")
    print("     - Pinta")
    print("     - UGet")
    print("     - Chromium Web Browser")
    print("		- dict <Online Dictionary>")
    print("		- tlp")
    os.system("sudo apt-get install -y ubuntu-restricted-extras unity-tweak-tool dconf-editor compizconfig-settings-manager htop openjdk-8-jdk virtualbox wine playonlinux steam vlc pinta uget chromium-browser dict tlp")
    print("[+] Installation Complete")
    
def ccsm():
    print("[!] Compiz Config Settings Manager Installation")
    os.system("sudo apt-get install -y compizconfig-settings-manager compiz-plugins-extra")
    print("[+] Installation Complete")
    
def gnome_tweak_tool():
    print("[!] Gnome Tweak Tool")
    os.system("sudo apt-get install -y gnome-tweak-tool")
    print("[+] Installation Complete")
    
def sublime3():
    print("[!] Sublime Text Editor")
    os.system("sudo add-apt-repository ppa:webupd8team/sublime-text-3 && sudo apt-get update")
    os.system("sudo apt-get install sublime-text-installer")
    print("[+] Installation Complete")
    
def networktools():
    print("[!] Network Tools")
    print("    Wireshark & Zenmap")
    os.system("sudo apt-get install -y zenmap wireshark")
    print("[+] Installation Complete")

def install_network_driver():
    print("[!] Network Driver Installation")
    os.system("wget https://github.com/Hadesy2k/ubuntunetworkdriver/raw/master/bcmwl-kernel-source_6.30.223.248%2Bbdcom-0ubuntu7_amd64.deb")
    os.system("wget https://github.com/Hadesy2k/ubuntunetworkdriver/raw/master/dkms_2.2.0.3-2ubuntu6_all.deb")
    os.system("sudo dpkg -i *.deb")
    os.system("rm *.deb")
    print("[+] Driver Installation Complete")
    os.system("sudo service network-manager restart")
    
def pyidgsu():
    print("[!] Install Pyi Daung Su ZawGyi Decode Font")
    print("    You can view both Unicode and Zawgyi with this font")

    os.system("wget https://github.com/Hadesy2k/pyidgsufont/raw/master/ZawDecode1.0_for_Windows.ttf")
    os.system("mkdir ~/.fonts")
    os.system("cp *.ttf ~/.fonts")
    print("[+] Pyi Daung Su Zawgyi decode font installed")

def gimp():
	print("[!] GIMP photo editor")
	os.system("sudo apt-get install -y gimp")
	print("[+] Installation Complete")

def synaptic():
    print("[!] Synaptic Packages Manager")
    os.system("sudo apt-get install -y synaptic")
    print("[+] Installation Complete")

def sysupdate():
    print("[!] Update/Upgrade Software Repositories")
    os.system("sudo apt-get update && sudo apt-get upgrade")
    print("[+] Update/Upgrade Complete")

def remove_guest():
    print("[!] This will remove guest login from Ubuntu Logan")
    conf = open("/etc/lightdm/lightdm.conf", "w")
    conf.write("[SeatDefaults]\n")
    conf.write("greeter-session=unity-greeter\n")
    conf.write("allow-guest=false\n")
    conf.close()
    print("[+] Process Complete")
    print("[+] Guest login will disappear after you reboot the computer")

def fix_brightness_control():
    print("[!] Fixing the Brightness Shortcut in Ubuntu")
    print("[!] Works only for Intel")
    intel = open("/usr/share/X11/xorg.conf.d/20-intel.conf", "w")
    intel.write('Section "Device"')
    intel.write('             Identifier "card0"')
    intel.write('             Driver "intel"')
    intel.write('             Option "Backlight" "intel_backlight"')
    intel.write('             BusID "PCI:0:2:0"')
    intel.write('EndSection')
    intel.close()
    print("[+] Fixing Complete")
    print("[+] Reboot the computer")

def quit():
    print("[!] Exiting...")
    exit()

if __name__ == "__main__":
    if 'linux' not in sys.platform:
        print("[-] Works only on Linux")
        exit(1)
    if os.geteuid() != 0:
        print("[-] Root access is needed to run")
        print("[!] Use 'sudo'")
        exit(1)

    logo = """
  ▄• ▄▌▄▄▄▄· ▄• ▄▌ ▐ ▄ ▄▄▄▄▄▄• ▄▌    ▄• ▄▌▄▄▄▄▄▪  ▄▄▌  ▄▄▄▄▄▪  ▄▄▄ ..▄▄ · 
  █▪██▌▐█ ▀█▪█▪██▌•█▌▐█•██  █▪██▌    █▪██▌•██  ██ ██•  •██  ██ ▀▄.▀·▐█ ▀. 
  █▌▐█▌▐█▀▀█▄█▌▐█▌▐█▐▐▌ ▐█.▪█▌▐█▌    █▌▐█▌ ▐█.▪▐█·██▪   ▐█.▪▐█·▐▀▀▪▄▄▀▀▀█▄
  ▐█▄█▌██▄▪▐█▐█▄█▌██▐█▌ ▐█▌·▐█▄█▌    ▐█▄█▌ ▐█▌·▐█▌▐█▌▐▌ ▐█▌·▐█▌▐█▄▄▌▐█▄▪▐█
   ▀▀▀ ·▀▀▀▀  ▀▀▀ ▀▀ █▪ ▀▀▀  ▀▀▀      ▀▀▀  ▀▀▀ ▀▀▀.▀▀▀  ▀▀▀ ▀▀▀ ▀▀▀  ▀▀▀▀ 
                                                  Hades.y2k   Nov 5 2015
 """

    menu = """
0: Exit                             1: Install Must Have Programs
2: Compiz Config Setting Manager    3: Gnome Tweak Tool
4: Sublime v<3.0>                   5: Network Tools
6: Install Network Driver           7: PyiDaungSu Zawgyi Decode Font
8: Remove Guest Login               9: Fix Brightness Control Shortcut
10: Synaptic                       11: GIMP
12: SYS Update
"""

    cmdTable = {
        "0":quit,
        "1":essentials,
        "2":ccsm,
        "3":gnome_tweak_tool,
        "4":sublime3,
        "5":networktools,
        "6":install_network_driver,
        "7":pyidgsu,
        "8":remove_guest,
        "9":fix_brightness_control,
        "10":synaptic,
        "11":gimp,
        "12":sysupdate }
    
    try:
        while True:
            print logo
            print menu
            usr = input("[=] Enter the option: ")
            if usr != '':
                cmdTable[str(usr)]()

    except KeyboardInterrupt:
        print("[!] Ctrl + C detected")
        print("[!] Exiting")
        exit()