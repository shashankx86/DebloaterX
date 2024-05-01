import os
import time
import colorama
from colorama import Back, Fore, Style

os.system("title = DebloaterX Made by @shashankx86")

colorama.init(autoreset=True)
os.system("@echo off")
print(Fore.CYAN + "Debloater Script for NON ROOTED Users")
print(Fore.CYAN + "Build by"+ Fore.RED +" @shashankx86\n")

while True:
    print(Fore.CYAN +"[Mode Menu] Select Mode to continue : \n" + Fore.RED + "1. Auto\n"+ Fore.RED +"2. Quit\n"+ Fore.RED +"3. clear\n"+ Fore.RED +"4. Manual[disable]\n"+ Fore.RED +"5. Manual[uninstall]")
    starto = input(Fore.CYAN + ">>> ")
    start = (starto.lower())
    if start == "1":
        print(Fore.CYAN + "[+]" + Fore.GREEN + "Starting....")
        break
    elif start == "2":
        print(Fore.CYAN + "[+]" + Fore.RED + "Quiting....")
        quit()
    elif start == "3":
        os.system("cls")
        continue
    elif start == "4":
        while True:
            print(Fore.CYAN + "[+] " + Fore.GREEN + "Manual Mode[disable]") 
            print(Fore.CYAN + "[S] " + Fore.GREEN + "Santax : <service/app name> [ Ex: com.facebook.services ]  /  help  /  clear")
            mulmo1 = input(Fore.CYAN + ">> ")
            mulm = (mulmo1.lower())
            if mulm == "help":
                print(Fore.CYAN + "[H] " +Fore.GREEN + "1. = Mode Menu")
                print(Fore.CYAN + "[H] " +Fore.GREEN + "2. = Quit")
                print(Fore.CYAN + "[H] " +Fore.GREEN + "3. = Clear\n")
                continue
            elif mulm == "2":
                quit()
            elif mulm == "3":
                os.system("cls")
                continue
            elif mulm == "1":
                print(Fore.CYAN + "[+]" +Fore.GREEN + "Mode Menu\n")
                break
            else:
                os.system("powershell.exe res/adb.exe shell pm disable-user --user 0 " + mulmo1)
                pass
    elif start == "5":
        while True:
            print(Fore.CYAN + "[+] " + Fore.GREEN + "Manual Mode[uninstall]") 
            print(Fore.CYAN + "[S] " + Fore.GREEN + "Santax : <service/app name> [ Ex: com.facebook.services ]  /  help  /  clear")
            mulmo2 = input(Fore.CYAN + ">> ")
            mulm = (mulmo2.lower())
            if mulm == "help":
                print(Fore.CYAN + "[H] " +Fore.GREEN + "1. = Mode Menu")
                print(Fore.CYAN + "[H] " +Fore.GREEN + "2. = Quit")
                print(Fore.CYAN + "[H] " +Fore.GREEN + "3. = Clear\n")
                continue
            elif mulm == "2":
                quit()
            elif mulm == "3":
                os.system("cls")
                continue
            elif mulm == "1":
                print(Fore.CYAN + "[+]" +Fore.GREEN + "Mode Menu")
                break
            else:
                os.system("powershell.exe res/adb.exe shell pm uninstall -k " + mulmo2)
                pass

    else:
        print(Fore.RED + "Invalid Input: " + start)
        continue
    
        

os.system("powershell.exe res/adb.exe kill-server")
os.system("powershell.exe res/adb.exe devices")
os.system("timeout /t 5 /nobreak > nul")

os.system("@echo off")
print(Fore.RED + "Note : it will show you error if you dont have that app installed, so ignore it\n")
os.system("timeout /t 5 /nobreak > nul")

print("######################################################")
print("#  To uninstall user apps : pm uninstall -k --user 0 #")
print("#  To disable them : pm disable-user --user 0        #")
print("######################################################")
print(Fore.RED + "Removing below services/apps")


print (Fore.CYAN + "Facebook apps")

os.system("powershell.exe res/adb.exe shell pm uninstall -k com.facebook.services")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.facebook.katana")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.facebook.system")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.facebook.appmanager")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.vanced.android.youtube")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.facebook.system")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.facebook.appmanager")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.facemoji.lite.xiaomi")
os.system("powershell.exe res/adb.exe shell pm uninstall –k ––user 0 com.facebook.appmanager")
os.system("powershell.exe res/adb.exe shell pm uninstall –k ––user 0 com.facebook.services")
os.system("powershell.exe res/adb.exe shell pm uninstall –k ––user 0 com.facebook.system")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.sec.android.app.DataCreate")
os.system("timeout /t 2 /nobreak > nul")
print (Fore.CYAN + "Google apps")

os.system("powershell.exe res/adb.exe shell pm uninstall -k com.android.chrome ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.google.android.youtube ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.google.android.tts ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.google.android.googlequicksearchbox ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.google.android.apps.tachyon ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.google.android.apps.docs ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.google.android.gm ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.google.android.videos ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.google.android.music ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.google.android.tts ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.google.android.apps.maps ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.google.android.apps.photos ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.google.android.youtube ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.google.ar.lens ")
os.system("powershell.exe res/adb.exe shell pm disable-user --user 0 com.google.ar.lens ")
os.system("powershell.exe res/adb.exe shell pm disable-user --user 0 com.google.android.youtube ")
os.system("powershell.exe res/adb.exe shell pm disable-user --user 0 com.google.android.gm ")
os.system("powershell.exe res/adb.exe shell pm disable-user --user 0 com.google.android.googlequicksearchbox ")
os.system("powershell.exe res/adb.exe shell pm disable-user --user 0 com.google.android.apps.maps ")
os.system("timeout /t 2 /nobreak > nul ")

print (Fore.CYAN + "Microsoft apps")

os.system("powershell.exe res/adb.exe shell pm uninstall -k com.microsoft.office.powerpoint ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.microsoft.office.excel ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.microsoft.office.word ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.microsoft.skydrive ")
os.system("timeout /t 2 /nobreak > nul ")

print (Fore.CYAN + "Linkedin Apps")

os.system("powershell.exe res/adb.exe shell pm uninstall -k com.linkedin.android ")
os.system("timeout /t 2 /nobreak > nul ")

print (Fore.CYAN + "Samsung Apps")

os.system("powershell.exe res/adb.exe shell pm uninstall -k com.sec.android.app.sbrowser ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.sec.android.email.provider ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.sec.android.app.voicenote ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.sec.android.beaconmanage")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.sec.android.dynamiclock ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.sec.android.dynsystem ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.sec.android.app.samsungapps ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.sec.android.game.gameho ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.sec.android.game.gametool ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.sec.android.service.health")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.sec.android.icecone ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.sec.android.keyguardmgsup ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.sec.android.sprotect ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.sec.android.securefolder ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.sec.android.app.camera.sticker.facear.preload ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.sec.android.themecenter ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.sec.android.themestore ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.sec.android.app.sbrowser.lite ")
os.system("timeout /t 2 /nobreak > nul ")

print (Fore.CYAN + "Bixby apps")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.samsung.android.bixby.wakeup ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.samsung.android.bixby.service ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.samsung.android.visionintelligence ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.samsung.android.bixby.agent ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.samsung.android.bixby.agent.dummy ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.samsung.android.bixbyvision.framework ")
os.system("timeout /t 2 /nobreak > nul ")

print (Fore.CYAN + "Realme apps, ignore if u dont have realme device and wait")

os.system("powershell.exe res/adb.exe shell pm uninstall -k com.coloros.compass2")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.heytap.market ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.redteamobile.roaming ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.heytap.market ")
os.system("powershell.exe res/adb.exe shell pm disable–user ––user 0 com.heytap.market ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k --user 0 com.heytap.browser ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k --user 0 com.heytap.market ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k --user 0 com.redteamobile.roaming ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k --user 0 com.heytap.usercenter ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k --user 0 com.heytap.cloud ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k --user 0 com.oppo.quicksearchbox ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k --user 0 com.coloros.backuprestore ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k --user 0 com.coloros.weather2 ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k --user 0 com.coloros.weather.service ")
os.system("powershell.exe res/adb.exe shell pm disable-user --user 0 com.nearme.gamecenter ")
os.system("timeout /t 2 /nobreak > nul ")

print (Fore.CYAN + "Redmi-apps, ignore if u dont have redmi device and wait")

os.system("powershell.exe res/adb.exe shell pm uninstall -k com.miui.cleanmaster ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.xiaomi.mipicks ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.xiaomi.payment ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.mipay.wallet.in ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.xiaomi.midrop ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.miui.miservice ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.miui.daemon ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.miui.msa.global ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.mi.webkit.core ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.xiaomi.joyose ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.facebook.services")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.facebook.appmanager ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.facebook.system ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.miui.analytics ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.miui.android.fashiongallery ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.xiaomi.midrop ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.android.browser ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.android.calendar ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.miui.bugreport")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.xiaomi.glgm ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.miui.yellowpage ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.miui.weather2")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.miui.miservice ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.miui.player ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.mipay.wallet.id ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.mipay.wallet.in ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.xiaomi.payment ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.miui.hybrid ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.miui.hybrid.accessory ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.miui.videoplayer ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.xiaomi.mipicks ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.miui.translation.kingsoft ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.miui.translation.youdao ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.miui.translation.xmcloud ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.miui.translationservice ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k cn.wps.xiaomi.abroad.lite ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.wps.xiaomi.abroad.lite ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.xiaomi.mirecycle ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.xunmeng.pinduoduo ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.xiaomi.midrop ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.tencent.mtt ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.eg.android.alipayGphone ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.dragon.read ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.taobao.taobao ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.tencent.qqlive ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.qiyi.video ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.ss.android.article.news ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.wps.moffice_eng ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.sina.weibo ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.xiaomi.jr ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.ss.android.ugc.aweme ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.baidu.BaiduMap ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.xiaomi.youpin ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.duokan.reader")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.xiaomi.vipaccount ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.mipay.wallet ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.miui.miservice ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.android.email ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k com.miui.global.packageinstaller ")
os.system("powershell.exe res/adb.exe shell pm uninstall -k android.autoinstalls.config.Xiaomi.ginkgo ")
os.system("powershell.exe res/adb.exe shell pm disable-user --user 0 com.xiaomi.mipicks ")
os.system("powershell.exe res/adb.exe shell pm disable-user --user 0 com.mipay.wallet.in ")
os.system("powershell.exe res/adb.exe shell pm disable-user --user 0 com.xiaomi.midrop ")
os.system("powershell.exe res/adb.exe shell pm disable-user --user 0 com.miui.miservice")
os.system("timeout /t 2 /nobreak > nul ")

print (Fore.CYAN + "Exiting script, Now reboot/restart and enjoy debloated Device")
os.system("powershell.exe res/adb.exe kill-server")
time.sleep(5)



