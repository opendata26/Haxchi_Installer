import os
import sys
import urllib
import shutil
import os.path

""" WELCOME """
print"******************************"
print"*    Haxchi Installer 1.1    *"
print"******************************\n"
print"******************************"
print"*    (FIX94  Haxchi v1.7)    *"
print"*                            *"
print"*       16-nov-2016          *"
print"*                            *"
print"*   Script by Vickdu31       *"
print"* email : vickdu31@yahoo.fr  *"
print"******************************"
raw_input("Press enter to start...")
os.system('cls' if os.name == 'nt' else 'clear') 
print"**************************************"
print"*         DISCLAIMER :               *"
print"**************************************\n"
print"**************************************"
print"*  I AM NOT RESPONSIBLE FOR BRICK    *"
print"*    DO NOT MODIFY THIS TOOL         *"
print"*                                    *"
print"*  This tool have been tested a lot  *"
print"*          It should be safe         *"
print"**************************************"
raw_input("Press enter to continue...")
os.system('cls' if os.name == 'nt' else 'clear') 


""" ASK REGION """
print"******************************"
print"*    Haxchi Installer 1.1    *"
print"******************************\n"
for retry in range(5):
    creg = raw_input("What is your console region ? (eur/us/jap)  ")
    if (creg == 'eur' or creg == 'us' or creg == 'jap'):
        ansr = raw_input("Your console region is " + creg + ". Is that correct ? (y/n)  ")
        if (ansr == 'y' or ansr == 'Y' or ansr == 'yes'):
            break
    print "\nPlease enter values correctly.\n"
else:
    sys.exit(1)


""" ASK WCHICH NDS GAME """
for retry in range(5):
    print "\nWhat NDS (eShop) game do you want to hack ?"
    print "1) Dr. Kawashima : Brain Age   2) Kirby Squeak Squad"
    print "3) WarioWare: Touched          4) Yoshi's Island DS "
    print "5) Maroi Kart DS               6) New Super Mario Bros DS "
    print "7) Star Fox Command            8) Zelda Phantom Hourglass"
    print "9) Super Mario 64 DS           10) Yoshi Touch and Go \n"
    game_number = raw_input("Enter a number :  ")
    if (game_number == '1' or game_number == '2' or game_number == '3' or game_number == '4' or game_number == '5' or game_number == '6' or game_number == '7' or game_number == '8' or game_number == '9' or game_number == '10'):
        ansr = raw_input("Your NDS eShop game is the game number " + game_number + ". Is that correct ? (y/n)  ")
        if (ansr == 'y' or ansr == 'Y' or ansr == 'yes'):
            break
    print "\nPlease enter number from 1 to 10.\n"
else:
    sys.exit(1)


""" CALCULATING TITLEID """
print "\n*We will replace the necessary files...* \n"
if game_number == '1':
    game_name = 'Dr. Kawashima : Brain Age'
    shutil.copy2('files/haxchi/brainage.zip', 'rom.zip')
    if creg == 'eur':
        game_id = "10179C00"
    if creg == 'us':
        game_id = "10179B00"
    if creg == 'jap':
        game_id = "10179A00"    
if game_number == '2':
    game_name = "Kirby : Mouse Attack"
    shutil.copy2('files/haxchi/kirby.zip', 'rom.zip')
    if creg == 'eur':
        game_id = "101A5700"
    if creg == 'us':
        game_id = "101A5600"
    if creg == 'jap':
        game_id = "101A5500"            
if game_number == '3':
    game_name = "WarioWare: Touched"
    shutil.copy2('files/haxchi/wwtouched.zip', 'rom.zip')
    if creg == 'eur':
        game_id = "101A2000"
    if creg == 'us':
        game_id = "101A1F00"
    if creg == 'jap':
        game_id = "101A1E00"            
if game_number == '4':
    game_name = "Yoshi's Island DS"
    shutil.copy2('files/haxchi/yoshids.zip', 'rom.zip')
    if creg == 'eur':
        game_id = "10198A00"
    if creg == 'us':
        game_id = "10198900"
    if creg == 'jap':
        game_id = "10198800"         
if game_number == '5':
    game_name = "Mario Kart DS"
    shutil.copy2('files/haxchi/mariokartds.zip', 'rom.zip')
    if creg == 'eur':
        game_id = "10195800"
    if creg == 'us':
        game_id = "10195700"
    if creg == 'jap':
        game_id = "10195600"      
if game_number == '6':
    game_name = "New Super Mario Bros"
    shutil.copy2('files/haxchi/newsmb.zip', 'rom.zip')
    if creg == 'eur':
        game_id = "10195B00"
    if creg == 'us':
        game_id = "10195A00"
    if creg == 'jap':
        game_id = "10195900"      
if game_number == '7':
    game_name = "Star Fox Command"
    shutil.copy2('files/haxchi/sfcommand.zip', 'rom.zip')
    if creg == 'eur':
        game_id = "101AC200"
    if creg == 'us':
        game_id = "101AC100"
    if creg == 'jap':
        game_id = "101AC000"      
if game_number == '8':
    game_name = "Zelda Phantom Hourglass"
    shutil.copy2('files/haxchi/zeldaph.zip', 'rom.zip')
    if creg == 'eur':
        game_id = "101C3800"
    if creg == 'us':
        game_id = "101C3700"
    if creg == 'jap':
        game_id = "101C3600"                                         
if game_number == '9':
    game_name = "Super Mario 64 DS"
    shutil.copy2('files/haxchi/sm64ds.zip', 'rom.zip')
    if creg == 'eur':
        game_id = "101C3500"
    if creg == 'us':
        game_id = "101C3400"
    if creg == 'jap':
        game_id = "101C3300"        
if game_number == '10':
    game_name = "Yoshi Touch and Go"
    shutil.copy2('files/haxchi/yoshitouchandgo.zip', 'rom.zip')
    if creg == 'eur':
        game_id = "10179F00"
    if creg == 'us':
        game_id = "10179E00"
    if creg == 'jap':
        game_id = "10179D00"                

raw_input("Please check that you now have a rom.zip file and please press enter to continue...")


""" ASK GAME LOCATION """
os.system('cls' if os.name == 'nt' else 'clear') 
print"******************************"
print"*    Haxchi Installer 1.1    *"
print"******************************\n"
for retry in range(15):
    gloc = raw_input("Where is your game located ?\n  1) USB   2) NAND/REDNAND/INTERNAL MEMORY  ")
    if (gloc == '1'):
        game_storage = 'USB'
        storage_code = 'usb01'
        ansr = raw_input("Are you sure it is on USB ? (y/n)  ")
        if (ansr == 'y' or ansr == 'Y' or ansr == 'yes'):
            break
        break
    if (gloc == '2'):
        game_storage = 'NAND'
        storage_code = 'mlc01'
        ansr = raw_input("Are you sure it is on SYSNAND or REDNAND ? (y/n)  ")
        if (ansr == 'y' or ansr == 'Y' or ansr == 'yes'):
            break
        break       
    print "\nPlease enter 1 or 2.\n"
else:
    sys.exit(1)

""" DEFINE LOGO """
for retry in range(10):
    hmode = raw_input("\nWhich icon do you want to use for " + game_name + " stored on  " + game_storage + " ?\n  1) Haxchi Icon   2) Hombrew Launcher\n   3) CFW Booter  4) Keep the current icon and name  ")
    if (hmode == '1' or hmode == '2' or hmode == '3' or hmode == '4'):
        ansr = raw_input("Are you sure ? (y/n)  ")
        if (ansr == 'y' or ansr == 'Y' or ansr == 'yes'):
            break
    print "\nPlease enter 1, 2, 3 or 4.\n"
else:
    sys.exit(1)

""" DEFINE BOOTSOUND """
for retry in range(10):
    sound = raw_input("\n Do you want to use the nice Hombrew Channel Boot Sound (from Wii) ? (y/n)  ")
    if (sound == 'y' or sound == 'YES' or sound == 'yes' or sound == 'Y' or sound == 'n' or sound == 'no' or sound == 'NO'):
        ansr = raw_input("Are you sure ? (y/n)  ")
        if (ansr == 'y' or ansr == 'Y' or ansr == 'yes'):
            if (sound == 'y' or sound == 'Y' or sound == 'yes'):
                sound = "1"
            break
    print "\nPlease decide if you want it.\n"
else:
    sys.exit(1)


""" IP FINDER FOR USER """
for retry in range(10):
    know_ip = raw_input("\nDo you have your Wii U IP adress somewhere ? (y/n)  ")
    if (know_ip == 'y' or know_ip == 'Y' or know_ip == 'yes' or know_ip == 'YES'):
        wiiuip = raw_input("Please write the Wii U Ip adress Ex :(192.168.x.x)\n").replace('\n', '')
        f = open('Your_Wii_U_IP.txt', 'w')
        f.write(wiiuip)
        f.close()
        break
    if (know_ip == 'n' or know_ip == 'N' or know_ip == 'no' or know_ip == 'NO'):
        print "Downloading WNetwatcher...(800KB)"
        urllib.urlretrieve('http://www.nirsoft.net/utils/wnetwatcher.zip', "wnetwatcher.zip")
        print "Please open the .exe and try to find the IP address of a Nintendo device Ex.(192.168.X.X)\nOnce you found it, press enter to continue\n"
        os.startfile('wnetwatcher.zip')
        raw_input("")
        wiiuip = raw_input("Please write the Wii U IP adress (192.168.x.x)\n").replace('\n', '')
        f = open('Your_Wii_U_IP.txt', 'w')
        f.write(wiiuip)
        f.close()
        break
    print "\nChoose beetween yes or no...\n"
else:
    sys.exit(1)

""" IP CHECK """
for retry in range(10):
    with open('Your_Wii_U_IP.txt', 'r') as ipfile:
        ipcheck = ipfile.read().replace('\n', '')
    ansr = raw_input("Your console IP adress is -->" + ipcheck + "<--  Is that correct ? (y/n)  ")
    if (ansr == 'y' or ansr == 'Y' or ansr == 'yes'):
        break
    wiiuip = raw_input("Please write the Wii U Ip adress. Use correct format : 192.168.x.x\n").replace('\n', '')
    f = open('Your_Wii_U_IP.txt', 'w')
    f.write(wiiuip)
else:
    sys.exit(1)

""" ASK CONFIG """
os.system('cls' if os.name == 'nt' else 'clear')
for retry in range(30):
    print "Would you like to use current config.txt ? (default configuration as below) (Apply when you start your NDS game) \n"
    print "Default (Press nothing) : /wiiu/apps/homebrew_launcher/homebrew_launcher.elf"
    print "Button A : fw.img"
    print "Button B : /rednand/fw.img"
    print "Button Y : wiiu/apps/loadiine_gx2/loadiine_gx2.elf"
    print "Button X : wiiu/apps/ftpiiu/ftpiiu.elf"
    print "Down : wiiu/apps/snes9x2010_libretro/snes9x2010_libretro.elf"
    ansr = raw_input("\nYes to continue, no to edit the config file. (y/n)")
    if (ansr == 'y' or ansr == 'Y' or ansr == 'yes' or ansr == 'YES'):
        break
    if (ansr == 'n' or ansr == 'N' or ansr == 'no' or ansr == 'NO'):
        os.startfile('config.txt')
        raw_input("Please modify the file, SAVE IT and press enter continue")
        raw_input("Are you sure your config file is OK and you saved it ? (y/n)  ")
        if (ansr == 'y' or ansr == 'Y' or ansr == 'yes'):
            break
        break
    print "Please answer by yes or no..."
else:
    sys.exit(1)

""" wupclient INIT """
os.system('cls' if os.name == 'nt' else 'clear')
print "*  Initialize connection :  *\n"
print "\nWe will now try to connect to the your Wii U via Wupserver.\n\n Please make sure that :\n- Your Wii U is turned ON and connected to internet\n- You started CFW Booter using Wupserver fw.img\n- You are currently on Rednand (only if you have one)"
print "\nYour Wii U region is " + creg
print "Your Wii U IP adress is " + ipcheck
print "The game you are hacking is " + game_name + " (Game ID : " + game_id + ")"
print "Your game is stored on " + game_storage + "\n"
raw_input("Make sure this is correct, press enter when you are ready!")


print "\n*  Initialise connexion  *\n"

from wupclient import wupclient
wupclient = wupclient()

print "*  If an error is displayed, your IP adress is wrong or the Wii U is not reachable  *\n"
raw_input("We are now connected to WUPServer on your Wii U, press enter when you are ready!")
os.system('cls' if os.name == 'nt' else 'clear')




""" REPLACING META.XML """
if (hmode == '1' or hmode == '2' or hmode == '3'):
    print "\n* Installing files, please wait.. (Takes a while if you change logo or Boot sound...) *\n"
    PATH8 = "/vol/storage_" + storage_code + "/usr/title/00050000/" + game_id + "/meta/meta.xml"
    wupclient.dl(PATH8)
    print "\n\n* meta.xml downloaded ! *"
    from shutil import copyfile
    copyfile('meta.xml', 'meta.xml.bak')
    print "* meta.xml backup created ! *"
    if (hmode == '1'):
        channel_name = "Haxchi"
    if (hmode == '2'):
        channel_name = "Hombrew Launcher"
    if (hmode == '3'):
        channel_name = "CFW Booter" 
    import xml.etree.ElementTree as ET
    import codecs
    tree = ET.parse("meta.xml")
    root = tree.getroot()
    for child in root:
        if(child.tag.startswith("longname_") or child.tag.startswith("shortname_")):
            child.text = channel_name
    with codecs.open("meta.xml", "w", "utf-8-sig") as f:
        f.write('<?xml version="1.0" encoding="utf-8"?>\n')
        tree.write(f, encoding="utf-8", method="html")
    wupclient.up("meta.xml", PATH8)

""" FLASHING ROM AND CONFIG """


PATH1 = "/vol/storage_" + storage_code + "/usr/title/00050000/" + game_id + "/content/0010/rom.zip"
wupclient.up("rom.zip", PATH1)


""" FLASHING BOOTSOUND"""

if sound == '1':
    PATH6 = "/vol/storage_" + storage_code + "/usr/title/00050000/" + game_id + "/meta/bootSound.btsnd"
    wupclient.up("files/icon/hbl/bootSound.btsnd", PATH6)


""" FLASHING ICONS """
if hmode == '1':
    PATH2 = "/vol/storage_" + storage_code + "/usr/title/00050000/" + game_id + "/meta/iconTex.tga"
    PATH3 = "/vol/storage_" + storage_code + "/usr/title/00050000/" + game_id + "/meta/bootDrcTex.tga"
    PATH4 = "/vol/storage_" + storage_code + "/usr/title/00050000/" + game_id + "/meta/bootTvTex.tga"
    wupclient.up("files/icon/hax/iconTex.tga", PATH2)
    wupclient.up("files/icon/hax/bootDrcTex.tga", PATH3)
    wupclient.up("files/icon/hax/bootTvTex.tga", PATH4)
if hmode == '2':
    PATH2 = "/vol/storage_" + storage_code + "/usr/title/00050000/" + game_id + "/meta/iconTex.tga"
    PATH3 = "/vol/storage_" + storage_code + "/usr/title/00050000/" + game_id + "/meta/bootDrcTex.tga"
    PATH4 = "/vol/storage_" + storage_code + "/usr/title/00050000/" + game_id + "/meta/bootTvTex.tga"
    wupclient.up("files/icon/hbl/iconTex.tga", PATH2)
    wupclient.up("files/icon/hbl/bootDrcTex.tga", PATH3)
    wupclient.up("files/icon/hbl/bootTvTex.tga", PATH4)
if hmode == '3':
    PATH2 = "/vol/storage_" + storage_code + "/usr/title/00050000/" + game_id + "/meta/iconTex.tga"
    PATH3 = "/vol/storage_" + storage_code + "/usr/title/00050000/" + game_id + "/meta/bootDrcTex.tga"
    PATH4 = "/vol/storage_" + storage_code + "/usr/title/00050000/" + game_id + "/meta/bootTvTex.tga"
    wupclient.up("files/icon/cfb/iconTex.tga", PATH2)
    wupclient.up("files/icon/cfb/bootDrcTex.tga", PATH3)
    wupclient.up("files/icon/cfb/bootTvTex.tga", PATH4) 
PATH5 = "/vol/storage_" + storage_code + "/usr/title/00050000/" + game_id + "/content/config.txt"       
wupclient.up("files/config.txt", PATH5)        
wupclient.chmod(PATH5, 0x644)        
wupclient.kill()
print "\n* Success ! *\n"


""" GOODBYE """  
print"******************************"
print"*    Haxchi Installer 1.1    *"
print"******************************\n"
print"******************************"
print"*  You now have Haxchi v1.7  *"
print"*       On your Wii U        *"
print"******************************\n"
print"******************************"
print"*    SHUTDOWN YOUR WII U     *"
print"*   Once program is closed   *"
print"*                            *"
print"*                            *"
print"*   Script by Vickdu31       *"
print"* email : vickdu31@yahoo.fr  *"
print"******************************"
raw_input("Press enter to continue...")
os.system('cls' if os.name == 'nt' else 'clear') 

""" CREDITS """ 
print"******************************"
print"*    Haxchi Installer 1.1    *"
print"******************************\n"        
print "* Your game is now replaced by Haxchi ! *\n"
print"**************************************"
print"*            CREDITS :               *"
print"**************************************\n"
print"**************************************"
print"*   @smealum for original Haxchi     *"
print"*   @smealum for iosuhax/wupserver   *"
print"*   @FIX94   for forked Haxchi       *"
print"*  @FIX94 helping me with the script *"
print"*       @FIX94 IS THE BEST <3        *"
print"  Everyone contribuing to WII U HACK *"
print"**************************************"
raw_input("Press enter to exit program...")
sys.exit()