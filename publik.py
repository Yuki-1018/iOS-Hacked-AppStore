#=====================================================================
# ＳＥＬＦＢＯＴNEW PUBLIK 2023 BY DHENZA15
#=====================================================================
from linepy import *
import calculators
from calculators.apself import ApCalculator
from justgood import imjustgood
from random import randint
from thrift.unverting import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from thrift import transport, protocol, server
from thrift.protocol import TCompactProtocol,TMultiplexedProtocol,TProtocol
from thrift.transport import TTransport,TSocket,THttpClient,TTransport,TZlibTransport
from akad.ttypes import IdentityProvider, LoginResultType, LoginRequest, LoginType
from akad.ttypes import TalkException
import time, random, json, codecs, subprocess, re,urllib.request,urllib.error,urllib.parse, os, shutil, requests, timeit, ast, pytz, threading, atexit, traceback, base64, pafy, livejson, timeago, math, argparse
from Liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from gtts import gTTS
from multiprocessing import Pool, Process
from bs4 import BeautifulSoup
from bs4.element import Tag
from datetime import datetime
from googletrans import Translator
from zalgo_text import zalgo
from threading import Thread,Event
import wikipedia as wiki
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
from threading import Thread
from urllib.parse import urlencode, quote
from pathlib import Path
_session = requests.session()
requests.packages.urllib3.disable_warnings()

#=====================================
tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)
Bot_startTime = time.strftime("%H:%M:%S", time.localtime())
#dhenzaSelf = LINE("QR")
dhenzaSelf = LINE("email","paswod")
print("""
\033["""+str(randint(0,1))+""";"""+str(randint(31,36))+"""m[ %s Start Bot ]\033[0m    
"""%(Bot_startTime))  
print("""\033["""+str(randint(0,1))+""";"""+str(randint(31,36))+"""m
███████████████████████████████████
	
▀▀█▀▀ █▀▀ █▀▀█ █▀▄▀█  ╭BOT TYPE - PUBLIK V.3.1
░▒█░░ █▀▀ █▄▄█ █░▀░█  ╠URL - github.com/dhenza1415
░▒█░░ ▀▀▀ ▀░░▀ ▀░░░▀  ╠SOURCE LIB - PYPI/LINEPY
█████████ ██████ ████ ╰TEAM - TBP SILENTKILLER
▒█▀▀█ ▒█▀▀▀█ ▀▀█▀▀       █████████████████
▒█▀▀▄ ▒█░░▒█ ░▒█░░ 
▒█▄▄█ ▒█▄▄▄█ ░▒█░░    ⏤͟͟͞͞SELFBOT NEW BY DHENZA𐂄

▒█▀▀█ █▀▀█ █▀▀█ ▀▀█▀▀ █▀▀ █▀▀ ▀▀█▀▀ 
▒█▄▄█ █▄▄▀ █░░█ ░░█░░ █▀▀ █░░ ░░█░░ 
▒█░░░ ▀░▀▀ ▀▀▀▀ ░░▀░░ ▀▀▀ ▀▀▀ ░░▀░░ 

███████████████████████████████████
.....----------:/++oosssyyyyyyso+/:---:::::::::--:
..-----.:+oydmmNNNNNNNNNNNMMMMMMMMMNdyo/--:::::::/
.-----/shddmmmmmNNNNNNNNNNMMMMMMMMMMMMMMNh+::::///
-----osyhddmmmmmNNNNNNNNNNMMMMMMMMMMMMMMMMMm/-/+/+
----+ssyhdddmmmNNNNNNNNNNNMMMMMMMMMMMMMMMMMMN//+so
:-.:sso+/:::://+ohmNNNNNNNNNNNNmddhysyhmNMMMNh:++o
-../s/.`.....``-/+o+hmNNNNNmdsoo+:::://::sNNMN/+o+
..`++..:++++::-..`.ssodNNmo:..:/oydNMMMNms/NNNs+oo
.``o++yddmmmmmho::/yhmmNNNms+osdNNNMMMMMMMmmNNd/+o
.``ssyhhdhssyhhdds:`-dNNMNs/ymNNmddmdmNNNNNNNNm+oo
.``ssyhh//::---:/o+:-sNMMMNNdhyo+//+osshNNNNNNNooo
.``ys+o:++/:---:/+ososNMMMMNdy/-.````./mdmmmMMmooo
...ysydmdhhhddmmmNNdssNMMMMMMMNNNNNNNNNNNNNNNNmyos
.`.sdmmNNNNNNNNNNNmhsyNMMMMMMMMMMMMMMMMMMMMMNNNh+o
.`-yhmmmmmmmNNNNNNdhyhNMMMMMMMMMMMMMMMMMMMMMMNNhos
.`.yyhhdddmmmmmmdddhsdNMMMMMMMMNNMMMNNNNNNNMNNNhos
```ysoossssso++oohdyshNNMMMMMMMNhyhdmNNNNNNNNNNs+o
.``+s/+/-++oydmhso-:o+oyyhdy+yNMMMmdysssyhdmNNm/+o
```-o:/s/.smmmmdhys+``.--.odmNMMMMMMMm/.shmNNNy-:/
````++o+s+`/hdhyyyo`  :h+``.omNMMMNmo`-hdmNNNN/::/
````-/+s+os-.``````./hmNNh:.```..```:ymdNNNmNh:/+/
`````//+s+/oyhddhyossooosssssdNNNNNNNdmNNmmmN/:::/
```  `+//os++++osssyhdmmNNNNNNmmdmmddNMNmmmNo///++
.``````/+/+hs+osso++/-``../osssmNNmmNNmmmNm+://///
..``````.///yhoshdmmNm- `/NNNNNNNmNMNmmmms///+++//
.`````    .::+dhshmNNm. `-MMMMNNNNNmmNdo-:://+++++
.``````     `-/ydydmNd` ``NMMMMNNNmmy/.-----::////
``````        `-+oshmd`  :NNNNNNmh+..-:---.-::::::
````` ``        `-/oyd: `dNNNNdo-`.-::::---::::::-
`````````         `.-//-yhys+-``.-::::::::::::::::
`````` `             ` ```````..--:::-------------
███████████████████████████████████
Login Time %s \033[0m\n\n"""%(Bot_startTime))
print ("LOGIN SB SUCSES")
dhenzaMid = dhenzaSelf.profile.mid
dhenzaStart = time.time()
dhenzaPoll = OEPoll(dhenzaSelf)
oburl = dhenzaSelf.server.LINE_OBJECT_URL
call = dhenzaSelf
owner = ["ub1c5a71f27b863896e9d44bea857d35b"]
admin = [dhenzaMid, "ub1c5a71f27b863896e9d44bea857d35b"]
staff = ["ub1c5a71f27b863896e9d44bea857d35b"]
Bots = [dhenzaMid]
JoinedGroups = dhenzaSelf.getGroupIdsJoined()
Team = owner + admin + Bots
protectqr = []
protectinvite = []
protectjoin = []
protectkick = []
protectcancel = []


helpMessage ="""        𝗛𝗘𝗟𝗣 𝗣𝗨𝗕𝗟𝗜𝗞 𝗕𝗢𝗧

• Liff
• Me
• Mid
• Midbot
• Reset
• Runtime
• speed
• tarik [jumlah]
• Broadcast: [txt] 
• Logout
━━━━━━━━━━━━━━
• url
• cpv
• cpict
• cgrupict
• cppurl [link ytb]
• changebio: [txt]
• changename: [cmd]
━━━━━━━━━━━━━━
• Sider on/off
• Lurking on/off
• Lurking
• welcome on/off
━━━━━━━━━━━━━━
• ["mentionall"]
• Settagall [cmd]
• cgrupname: [cmd]
━━━━━━━━━━━━━━
• listsmule [id]
• youtube [judul]
━━━━━━━━━━━━━━
• share link 「smule」
• share link 「youtube」
• share link 「tiktok」
━━━━━━━━━━━━━━
• banlist
• clearban
• cekbot
• protectlist
• botlist
• adminadd @
• admindell @
• botsadd @
• botdell @
• protectqr on/off
• protectkick on/off
• protectjoin on/off
• protectcancel on/off
• protectinvite on/off
• allpro on/off
━━━━━━━━━━━━━━



                 𝘚𝘦𝘭𝘧𝘣𝘰𝘵 𝘣𝘺 : 𝘋𝘩𝘦𝘯𝘻𝘢15
                      𝘔𝘰𝘥𝘦 : 𝘍𝘳𝘦𝘦 𝘚𝘦𝘭𝘧𝘣𝘰𝘵
                                         Ver : 3.1
"""
msg_dict = {}
offbot = []
targets = []
settingsOpen = codecs.open("setting.json","r","utf-8")
settings = json.load(settingsOpen)

pro = {
    "protectqr":{},
    "protectinvite":{},
    "protectjoin":{},
    "protectkick":{},
    "protectcancel":{},
    "blacklist":{},
}

read={
    "readPoint":{},
    "readMember":{},
    "ROM":{}
}
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

def restartBot():
    print ("[ INFO ] BOT RESETTED")
    python = sys.executable
    os.execl(python, python, *sys.argv)

def autoRestart():
    if settings["autoRestart"] == True:
        if time.time() - botStart > int(settings["timeRestart"]):
            backupData()
            restartBot()
            
def logError(error, write=True):
    errid = str(random.randint(100, 999))
    filee = open('tmp/errors/%s.txt'%errid, 'w') if write else None
 #   if args.traceback: traceback.print_tb(error.__traceback__)
    if write:
        traceback.print_tb(error.__traceback__, file=filee)
        filee.close()
        with open('errorLog.txt', 'a') as e:
            e.write('\n%s : %s'%(errid, str(error)))
    print ('++ Err :\n {error}'.format(error=error))       
        
def waktu(self,secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))

def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')
    
def delete_log1():
    ndt = datetime.now()
    for data in msg_dict1:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict1[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict1[msg_id]
#delete log if pass more than 24 hours
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]    
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)
            time.sleep(0.1)
            page = page[end_content:]
    return items
    
def linkqr(to,her):
    url =pyqrcode.create(her, error='L', version=8, mode='binary')
    url.png("big-number.png",scale=8) 
    dhenzaSelf.sendImage(to,"big-number.png")  
    
def sq(to, text):
	url = "https://api.chstore.me/line2secondary?appname=line_appname&authtoken=auth_token"
	payload={}
	headers = {}
	response = requests.request("GET", url, headers=headers, data=payload)
	dhenzaSelf.sendMessage(response.text)
          
          
def sendFlex(to, data):
    xyzz = LiffContext(chat=LiffChatContext(to))
    view = LiffViewRequest('1602687308-GXq4Vvk9', context = xyzz)
    token = dhenzaSelf.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Line/8.14.0',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    return requests.post(url, headers=headers, data=json.dumps(data))
    
def sendFlex(to, data):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = dhenzaSelf.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))

def sendTemplate(to, data):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = dhenzaSelf.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
    
    
def sendTemplate(to, data):
    xyzz = LiffContext(chat=LiffChatContext(to))
    view = LiffViewRequest('1602687308-GXq4Vvk9', context = xyzz)
    token = dhenzaSelf.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Line/8.14.0',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    return _session.post(url=url, data=json.dumps(data), headers=headers)
    
def allowLiff():
    url = 'https://access.line.me/dialog/api/permissions'
    data = {
        'on': [
            'P',
            'CM'
        ],
        'off': []
    }
    headers = {
        'X-Line-Access': dhenzaSelf.authToken,
        'X-Line-Application': dhenzaSelf.server.APP_NAME,
        'X-Line-ChannelId': '1602687308',
        'Content-Type': 'application/json'
    }
    requests.post(url, json=data, headers=headers)

def sendFooter(receiver, text):
    label = settings["label"]
    icon = settings["iconUrl"]
    link = settings["linkUrl"]
    data = {
        "type": "text",
        "text": text,
        "sentBy": {
            "label": "{}".format(label),
            "iconUrl": "{}".format(icon),
            "linkUrl": "{}".format(link)
        }
    }
    sendTemplate(receiver, data)   
    
    
def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "Hai ".format(str(mid))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = dhenzaSelf.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+settings["welcomee"]#+"\nDigroup: "+str(ginfo.name)+"\n"
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(dhenzaSelf.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        dhenzaSelf.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        dhenzaSelf.sendMessage(to, "[ INFO ] Error :\n" + str(error))   
    
        
def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    dhenzaSelf.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        

def timeChange(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weeks, days = divmod(days,7)
    months, weeks = divmod(weeks,4)
    text = ""
    if months != 0: text += "%02d Bulan" % (months)
    if weeks != 0: text += " %02d Minggu" % (weeks)
    if days != 0: text += " %02d Hari" % (days)
    if hours !=  0: text +=  " %02d Jam" % (hours)
    if mins != 0: text += " %02d Menit" % (mins)
    if secs != 0: text += " %02d Detik" % (secs)
    if text[0] == " ":
        text = text[1:]
    return text
    
def youtubeMp3(to, link):
    subprocess.getoutput('youtube-dl --extract-audio --audio-format mp3 --output dhenza.mp3 {}'.format(link))
    try:
        dhenzaSelf.sendAudio(to, 'dhenza.mp3')
        time.sleep(2)
        os.remove('dhenza.mp3')
    except Exception as e:
        dhenzaSelf.sendReplyMessage(msg.id, to,'「 ERROR 」\nMungkin Link salah cek lagi coba')
def youtubeMp4(to, link):
    subprocess.getoutput('youtube-dl --format mp4 --output dhenza.mp4 {}'.format(link))
    try:
        dhenzaSelf.sendVideo(to, "dhenza.mp4")
        time.sleep(2)
        os.remove('dhenza.mp4')
    except Exception as e:
        dhenzaSelf.sendReplyMessage(msg.id, to,' 「 ERROR 」\nMungkin Link Nya Salah cek lagi', contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+dhenzaSelf.getContact(dhenzaMid).pictureStatus, 'AGENT_NAME': '「 ERROR 」', 'AGENT_LINK': 'https://line.me/ti/p/~teambotprotect'})
   
def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = dhenzaSelf.genOBSParams({'oid': dhenzaMid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = dhenzaSelf.server.postContent('{}/talk/vp/upload.nhn'.format(str(dhenzaSelf.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        dhenzaSelf.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))
        os.remove("dhenza.mp4")        
def removeCmd(cmd, text):
    key = settings["keyCommand"]
    if settings["setKey"] == False: key = ''
    rmv = len(key + cmd) + 1
    return text[rmv:]        
    
def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            silentk1ller = pesan.replace(settings["keyCommand"],"")
        else:
            silentk1ller = "Undefined command"
    else:
        silentk1ller = text.lower()
    return silentk1ller
    
def dhenzaBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if settings["autoAdd"] == True:
                dhenzaSelf.findAndAddContactsByMid(op.param1)
            dhenzaSelf.sendMention(op.param1, settings["autoAddMessage"], [op.param1])
        if op.type == 13 or op.type == 124:
            if settings["autoJoin"] and dhenzaMid in op.param3:
                group = dhenzaSelf.getGroup(op.param1)
                group.notificationDisabled = False
                dhenzaSelf.acceptGroupInvitation(op.param1)
                dhenzaSelf.sendMessage(op.param1, "THAKS FOR INVITE ME SILENTKILLER")                   
#===================================================================== 
        if op.type == 11 or op.type == 122:
            if op.param1 in protectqr:
                try:
                    if dhenzaSelf.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            dhenzaSelf.reissueGroupTicket(op.param1)
                            X = dhenzaSelf.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            dhenzaSelf.updateGroup(X)
                            pro["blacklist"][op.param2] = True
                            dhenzaSelf.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                except:
                    pass

            if op.param1 in protectinvite:
                if op.param2 in Bots:
                    pass
                if op.param2 in Team:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    inv1 = op.param3.replace('\x1e',',')
                    inv2 = inv1.split(',')
                    for _mid in inv2:
                        dhenzaSelf.cancelGroupInvitation(op.param1,[_mid])
                    if op.param2 in Bots:
                        pass
                    if op.param2 in admin:
                        pass
                    if op.param2 in owner:
                        pass
                    if op.param2 in Team:
                        pass
                    else:
                        pro["blacklist"][op.param2] = True
                        try:
                           dhenzaSelf.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                ka.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass
                return
#____________________________________________________________________
        if op.type == 13 or op.type == 124:
            if op.param2 in pro["blacklist"]:
            	if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    z = dhenzaSelf.getGroup(op.param1)
                    if z.invitee is not None:
                        zl = [a.mid for a in z.invitee]
                        for _mid in zl:
                            if _mid in pro["blacklist"]:
                                dhenzaSelf.cancelGroupInvitation(op.param1,[_mid])
                                dhenzaSelf.kickoutFromGroup(op.param1,[op.param2])
                                
        if op.type == 13 or op.type == 124:
            if op.param2 in pro["blacklist"]:
            	if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    z = ka.getGroup(op.param1)
                    if z.invitee is not None:
                        zl = [a.mid for a in z.invitee]
                        for _mid in zl:
                            if _mid in pro["blacklist"]:
                                ka.cancelGroupInvitation(op.param1,[_mid])
                                ka.kickoutFromGroup(op.param1,[op.param2])
                                
        if op.type == 32 or op.type == 126:
            if op.param2 in pro["blacklist"]:
            	if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    z = dhenzaSelf.getGroup(op.param1)
                    if z.invitee is not None:
                        zl = [a.mid for a in z.invitee]
                        for _mid in zl:
                            if _mid in pro["blacklist"]:
                                dhenzaSelf.cancelGroupInvitation(op.param1,[_mid])
                                dhenzaSelf.kickoutFromGroup(op.param1,[op.param2])
                                
        if op.type == 32 or op.type == 126:
            if op.param2 in pro["blacklist"]:
            	if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    z = ka.getGroup(op.param1)
                    if z.invitee is not None:
                        zl = [a.mid for a in z.invitee]
                        for _mid in zl:
                            if _mid in pro["blacklist"]:
                                ka.cancelGroupInvitation(op.param1,[_mid])
                                ka.kickoutFromGroup(op.param1,[op.param2])       
                    
        if op.type == 17 or op.type == 130:
            if op.param2 in pro["blacklist"]:
                random.choice(AKU).kickoutFromGroup(op.param1,[op.param2])
                time.sleep(0.0001)
            else:
                pass
                            
#____________________________________________________________________
        if op.type == 32 or op.type == 126:
            if op.param1 in protectcancel:
                if op.param3 in Team:
                    if op.param2 not in Bots and op.param2 not in admin and op.param2 not in owner and op.param2 not in staff:
                        pro["blacklist"][op.param2] = True
                        try:
                            if op.param3 not in pro["blacklist"]:
                                dhenzaSelf.findAndAddContactsByMid(op.param1,[op.param3])
                                dhenzaSelf.kickoutFromGroup(op.param1,[op.param2])
                                dhenzaSelf.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            pass

        if op.type == 32 or op.type == 126:
            if op.param3 in Team:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                if op.param2 in Team:
                    pass
                else:
                     pro["blacklist"][op.param2] = True
                     try:
                         dhenzaSelf.kickoutFromGroup(op.param1,[op.param2])
                         dhenzaSelf.inviteIntoGroup(op.param1,[op.param3])
                     except:
                         try:
                             ka.kickoutFromGroup(op.param1,[op.param2])
                             ka.inviteIntoGroup(op.param1,[op.param3])
                         except:
                             pass
                return
#____________________________________________________________________
        if op.type == 19:
            if op.param1 in protectjoin:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                if op.param2 in Team:
                    pass
                else:
                    pro["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in pro["blacklist"]:
                            dhenzaSelf.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in pro["blacklist"]:
                                ka.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            pass
                return

            if op.param1 in protectkick:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                if op.param2 in Team:
                    pass
                else:
                    pro["blacklist"][op.param2] = True
                    try:
                        dhenzaSelf.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ka.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            pass
                return

            if op.type == 19:
                if op.param3 in owner:
                    if op.param2 in Bots:
                        pass
                    if op.param2 in owner:
                        pass
                    if op.param2 in admin:
                        pass
                    if op.param2 in staff:
                        pass
                    if op.param2 in Team:
                        pass
                    else:
                        pro["blacklist"][op.param2] = True
                        try:
                            dhenzaSelf.kickoutFromGroup(op.param1,[op.param2])
                            dhenzaSelf.findAndAddContactsByMid(op.param1,[op.param3])
                            dhenzaSelf.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            pass
                    return

                if op.param3 in admin:
                    if op.param2 in Bots:
                        pass
                    if op.param2 in owner:
                        pass
                    if op.param2 in admin:
                        pass
                    if op.param2 in staff:
                        pass
                    if op.param2 in Team:
                        pass
                    else:
                        pro["blacklist"][op.param2] = True
                        try:
                            dhenzaSelf.kickoutFromGroup(op.param1,[op.param2])
                            dhenzaSelf.findAndAddContactsByMid(op.param,[op.param3])
                            dhenzaSelf.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            pass
                    return

                if op.param3 in staff:
                    if op.param2 in Bots:
                        pass
                    if op.param2 in owner:
                        pass
                    if op.param2 in admin:
                        pass
                    if op.param2 in staff:
                        pass
                    if op.param2 in Team:
                        pass
                    else:
                        pro["blacklist"][op.param2] = True
                        try:
                            dhenzaSelf.kickoutFromGroup(op.param1,[op.param2])
                            dhenzaSelf.findAndAddContactsByMid(op.param1,[op.param3])
                            dhenzaSelf.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            pass
                    return

                if op.param3 in Bots:
                    if op.param2 in Bots:
                        pass
                    if op.param2 in owner:
                        pass
                    if op.param2 in admin:
                        pass
                    if op.param2 in staff:
                        pass
                    if op.param2 in Team:
                        pass
                    else:
                        pro["blacklist"][op.param2] = True
                        try:
                            dhenzaSelf.kickoutFromGroup(op.param1,[op.param2])
                            dhenzaSelf.inviteIntoGroup(op.param1,[op.param3])
                            dhenzaSelf.acceptGroupInvitation(op.param1)
                        except:
                            pass
                    return
                    
        if op.type == 55:
            if op.param2 in pro["blacklist"]:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                if op.param2 in Team:
                    pass
                else:
                    pro["blacklist"][op.param2] = True
                    try:
                        dhenzaSelf.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
                return
#====================================================================
        
#====================================================================
        if op.type == 17 or op.type == 130:
            if op.param1 in settings["welcomee"]:
                ginfo = dhenzaSelf.getGroup(op.param1)
                contact = dhenzaSelf.getContact(op.param2)
                cover = dhenzaSelf.getProfileCoverURL(op.param2)
                tz = pytz.timezone("Asia/Jakarta")
                timeNow = datetime.now(tz=tz)
                gname = dhenzaSelf.getGroup(op.param1)
                data = data = {"type": "flex","altText": "FLEX JOIN","contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "separator",
            "color": "#ff0088"
          }
        ],
        "backgroundColor": "#000000"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/2c0Qrtw/ezgif-com-gif-maker-1.png",
            "size": "full",
            "gravity": "top",
            "aspectMode": "cover",
            "offsetTop": "0px",
            "animated": True
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": " "+datetime.strftime(timeNow,'%d-%m-%Y'), 
                    "size": "xxs",
                    "weight": "bold",
                    "color": "#ffffff"
                  }
                ],
                "backgroundColor": "#88008890"
              }
            ],
            "position": "absolute",
            "backgroundColor": "#ff000077",
            "margin": "sm",
            "offsetTop": "2px",
            "paddingAll": "2px",
            "offsetStart": "3px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://obs.line-scdn.net/{}".format(dhenzaSelf.getContact(op.param2).pictureStatus),
                    "aspectMode": "cover"
                  }
                ]
              }
            ],
            "position": "absolute",
            "backgroundColor": "#ff000077",
            "margin": "sm",
            "offsetTop": "0px",
            "paddingAll": "2px",
            "width": "40px",
            "height": "40px",
            "offsetEnd": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "HALO WELCOME kk...",
                    "size": "xxs",
                    "wrap": True,
                    "align": "center",
                    "weight": "bold",
                    "color": "#ffffff"
                  }
                ],
                "backgroundColor": "#88008890"
              }
            ],
            "position": "absolute",
            "backgroundColor": "#ff000077",
            "margin": "sm",
            "offsetTop": "60px",
            "paddingAll": "2px",
            "offsetStart": "10px",
            "offsetEnd": "10px",
            "borderWidth": "semi-bold",
            "borderColor": "#00000022"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "{}".format(dhenzaSelf.getContact(op.param2).displayName),
                    "size": "xxs",
                    "weight": "bold",
                    "color": "#ffffff",
                    "align": "center"
                  }
                ],
                "backgroundColor": "#88008890"
              }
            ],
            "position": "absolute",
            "backgroundColor": "#ff000077",
            "margin": "sm",
            "offsetTop": "30px",
            "paddingAll": "2px",
            "offsetEnd": "50px",
            "paddingEnd": "2px",
            "offsetStart": "3px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "{}".format(cover),
                    "aspectMode": "cover"
                  }
                ]
              }
            ],
            "position": "absolute",
            "backgroundColor": "#ff000077",
            "margin": "sm",
            "paddingAll": "2px",
            "width": "40px",
            "height": "40px",
            "offsetBottom": "3px",
            "offsetStart": "3px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://i.ibb.co/LNYb0f0/ezgif-com-gif-maker.png",
                    "aspectMode": "cover",
                    "aspectRatio": "10:2",
                    "animated": True
                  }
                ]
              }
            ],
            "position": "absolute",
            "backgroundColor": "#ff000077",
            "margin": "sm",
            "paddingAll": "2px",
            "offsetBottom": "2px",
            "offsetEnd": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "ɬც℘ ʂıƖɛŋɬƙıƖƖɛཞ",
                    "color": "#ffffff",
                    "size": "sm",
                    "position": "relative"
                  }
                ]
              }
            ],
            "position": "absolute",
            "backgroundColor": "#ff000077",
            "margin": "sm",
            "paddingAll": "2px",
            "offsetBottom": "30px",
            "offsetEnd": "5px"
          }
        ],
        "margin": "sm",
        "backgroundColor": "#000000",
        "paddingAll": "0px",
        "action": {
          "type": "uri",
          "label": "action",
          "uri": "https://www.dhenza15.site/"
        }
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "separator",
            "color": "#ff0088"
          }
        ],
        "backgroundColor": "#000000"
      }
    }
  ]
}
}
                dhenzaSelf.postTemplate(op.param1, data)                                                   

        if op.type == 15 or op.type == 128:
            if op.param1 in settings["welcomee"]:
                ginfo = dhenzaSelf.getGroup(op.param1)
                contact = dhenzaSelf.getContact(op.param2)
                cover = dhenzaSelf.getProfileCoverURL(op.param2)
                tz = pytz.timezone("Asia/Jakarta")
                timeNow = datetime.now(tz=tz)
                gname = dhenzaSelf.getGroup(op.param1)
                data = {"type": "flex","altText": "FLEX LEAVE","contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "separator",
            "color": "#ff0088"
          }
        ],
        "backgroundColor": "#000000"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/2c0Qrtw/ezgif-com-gif-maker-1.png",
            "size": "full",
            "gravity": "top",
            "aspectMode": "cover",
            "offsetTop": "0px",
            "animated": True
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": " "+datetime.strftime(timeNow,'%d-%m-%Y'), 
                    "size": "xxs",
                    "weight": "bold",
                    "color": "#ffffff"
                  }
                ],
                "backgroundColor": "#88008890"
              }
            ],
            "position": "absolute",
            "backgroundColor": "#ff000077",
            "margin": "sm",
            "offsetTop": "2px",
            "paddingAll": "2px",
            "offsetStart": "3px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://obs.line-scdn.net/{}".format(dhenzaSelf.getContact(op.param2).pictureStatus),
                    "aspectMode": "cover"
                  }
                ]
              }
            ],
            "position": "absolute",
            "backgroundColor": "#ff000077",
            "margin": "sm",
            "offsetTop": "0px",
            "paddingAll": "2px",
            "width": "40px",
            "height": "40px",
            "offsetEnd": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "yaah kok leave si kk...",
                    "size": "xxs",
                    "wrap": True,
                    "align": "center",
                    "weight": "bold",
                    "color": "#ffffff"
                  }
                ],
                "backgroundColor": "#88008890"
              }
            ],
            "position": "absolute",
            "backgroundColor": "#ff000077",
            "margin": "sm",
            "offsetTop": "60px",
            "paddingAll": "2px",
            "offsetStart": "10px",
            "offsetEnd": "10px",
            "borderWidth": "semi-bold",
            "borderColor": "#00000022"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "{}".format(dhenzaSelf.getContact(op.param2).displayName),
                    "size": "xxs",
                    "weight": "bold",
                    "color": "#ffffff",
                    "align": "center"
                  }
                ],
                "backgroundColor": "#88008890"
              }
            ],
            "position": "absolute",
            "backgroundColor": "#ff000077",
            "margin": "sm",
            "offsetTop": "30px",
            "paddingAll": "2px",
            "offsetEnd": "50px",
            "paddingEnd": "2px",
            "offsetStart": "3px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "{}".format(cover),
                    "aspectMode": "cover"
                  }
                ]
              }
            ],
            "position": "absolute",
            "backgroundColor": "#ff000077",
            "margin": "sm",
            "paddingAll": "2px",
            "width": "40px",
            "height": "40px",
            "offsetBottom": "3px",
            "offsetStart": "3px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://i.ibb.co/LNYb0f0/ezgif-com-gif-maker.png",
                    "aspectMode": "cover",
                    "aspectRatio": "10:2",
                    "animated": True
                  }
                ]
              }
            ],
            "position": "absolute",
            "backgroundColor": "#ff000077",
            "margin": "sm",
            "paddingAll": "2px",
            "offsetBottom": "2px",
            "offsetEnd": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "ɬც℘ ʂıƖɛŋɬƙıƖƖɛཞ",
                    "color": "#ffffff",
                    "size": "sm",
                    "position": "relative"
                  }
                ]
              }
            ],
            "position": "absolute",
            "backgroundColor": "#ff000077",
            "margin": "sm",
            "paddingAll": "2px",
            "offsetBottom": "30px",
            "offsetEnd": "5px"
          }
        ],
        "margin": "sm",
        "backgroundColor": "#000000",
        "paddingAll": "0px",
        "action": {
          "type": "uri",
          "label": "action",
          "uri": "https://www.dhenza15.site/"
        }
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "separator",
            "color": "#ff0088"
          }
        ],
        "backgroundColor": "#000000"
      }
    }
  ]
}
}
                dhenzaSelf.postTemplate(op.param1, data)                        
#=====================================================================          
        if op.type == 55:
            if op.param1 in read["readPoint"]:
                if op.param2 not in read["readMember"][op.param1]:
                    read["readMember"][op.param1].append(op.param2)       
#=====================================================================
        if op.type == 55:
            if op.param2 in settings["blackList"]:
                dhenzaSelf.kickoutFromGroup(op.param1,[op.param2])
            else:
                pass                                
#=====================================================================
        if op.type == 55:
            if op.param1 in cctv['point']:
                    Name = dhenzaSelf.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n• " + Name
                        contact = dhenzaSelf.getContact(op.param2)
                        tz = pytz.timezone("Asia/Jakarta")
                        contact = dhenzaSelf.getContact(op.param2)
                        KATA = ["hallo kk sini gabung chat","hay ngitip mulu","up yuk","ngopi atu ka","hallo sayang","cek pm ka","buka filter","hayo ngintip"]
                        TAG = "@! "
                        TAG += random.choice(KATA)
                        dhenzaSelf.sendMention2(op.param1, str(TAG),' ',[op.param2])
#=====================================================================     
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if sender != dhenzaSelf.profile.mid:
                    to = sender
                else:
                    to = receiver
                if msg.contentType == 6:
                  if settings["nCall"] == True:
                    if msg._from not in Bots:
                        try:
                            contact = dhenzaSelf.getContact(sender)
                            group = dhenzaSelf.getGroup(msg.to)
                            cover = dhenzaSelf.getProfileCoverURL(sender)
                            tz = pytz.timezone("Asia/Bangkok")
                            timeNow = datetime.now(tz=tz)
                            if msg.toType == 2:
                                b = msg.contentMetadata['GC_EVT_TYPE']
                                c = msg.contentMetadata["GC_MEDIA_TYPE"]
                                if c == 'AUDIO' and b == "S":
                                    arg = "• ᴄᴀʟʟ ᴀᴜᴅɪᴏ"
                                    arg += "\n• ᴛʏᴘᴇ {} ᴄᴀʟʟ".format(c) 
                                    arg += "\n• ɴᴍ: {}".format(str(contact.displayName)) 
                                    arg += "\n• ɢᴄ: {}".format(str(group.name))
                                    arg += "\n• ʜʀ: {}".format(timeNow.strftime('%A'))
                                    arg += "\n• ᴊᴍ: {}".format(datetime.strftime(timeNow,'%H:%M:%S'))
                                    arg += "\n• ᴛɢ: {}".format(datetime.strftime(timeNow,'%d-%m-%Y'))
                                    contact = dhenzaSelf.getProfile()
                                    mids = [contact.mid]
                                    status = dhenzaSelf.getContact(sender)
                                    strcl = " 「 Ciee ngajakin Audio Call 」 "
                                    data = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/9gGMNS3/ezgif-com-gif-maker-1.png",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "7:4",
            "gravity": "top",
            "animated": True,
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://youtube.com/channel/UCNLejYy84XyUX8qcDropXMw"
            }
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": " "+ datetime.strftime(timeNow,'%H:%M:%S'),
                "size": "xxl",
                "color": "#ffffff",
                "align": "start",
                "gravity": "center",
                "margin": "xs"
              }
            ],
            "position": "absolute",
            "offsetTop": "10px",
            "offsetStart": "100px"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/dbGrjHT/20220303-211805.png",
                "animated": True,
                "aspectMode": "cover",
                "size": "xxl"
              }
            ],
            "position": "absolute",
            "offsetStart": "90px",
            "action": {
              "type": "uri",
              "label": "Bgdz",
              "uri": "https://youtube.com/channel/UCNLejYy84XyUX8qcDropXMw"
            }
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(dhenzaSelf.getContact(sender).pictureStatus),
                "aspectMode": "cover",
                "size": "sm",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://youtube.com/channel/UCNLejYy84XyUX8qcDropXMw"
                },
                "animated": True
              }
            ],
            "position": "absolute",
            "action": {
              "type": "uri",
              "label": "Foto",
              "uri": "https://youtube.com/channel/UCNLejYy84XyUX8qcDropXMw"
            },
            "offsetTop": "xxl",
            "offsetStart": "md",
            "borderColor": "#ff0088",
            "borderWidth": "medium"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "{}".format(status.displayName),
                "size": "md",
                "align": "center",
                "color": "#ffffff"
              }
            ],
            "position": "absolute",
            "borderWidth": "normal",
            "borderColor": "#ff0088",
            "offsetBottom": "xl",
            "offsetStart": "md"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": " "+format(datetime.strftime(timeNow,'%d-%m-%Y')),
                "size": "md",
                "align": "center",
                "color": "#ffffff"
              }
            ],
            "position": "absolute",
            "borderWidth": "normal",
            "borderColor": "#ff0088",
            "offsetEnd": "lg"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": " "+format(strcl),
                "size": "xxs",
                "align": "center",
                "color": "#ffffff",
                "style": "italic"
              }
            ],
            "position": "absolute",
            "borderWidth": "normal",
            "borderColor": "#ff0088",
            "offsetBottom": "md",
            "offsetEnd": "xl"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/WnLG1rC/ezgif-com-gif-to-apng.png",
                "size": "4xl",
                "animated": True
              }
            ],
            "position": "absolute",
            "width": "100px",
            "offsetTop": "40px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": " "+format(c),
                "size": "xs",
                "align": "center",
                "color": "#ffffff",
                "weight": "bold",
                "style": "italic"
              }
            ],
            "position": "absolute",
            "borderWidth": "normal",
            "borderColor": "#ff0088",
            "offsetBottom": "40px",
            "offsetStart": "5px",
            "backgroundColor": "#000000",
            "paddingAll": "0px"
          }
        ],
        "paddingAll": "0px"
      }
    }
  ]
}
                                    dhenzaSelf.postFlex(msg.to,data)
                                if c == 'VIDEO' and b == "S":
                                    arg = "• ᴄᴀʟʟ ᴠɪᴅᴇᴏ"
                                    arg += "\n• ᴛʏᴘᴇ {} ᴄᴀʟʟ".format(c) 
                                    arg += "\n• ɴᴍ: {}".format(str(contact.displayName)) 
                                    arg += "\n• ɢᴄ: {}".format(str(group.name))
                                    arg += "\n• ʜʀ: {}".format(timeNow.strftime('%A'))
                                    arg += "\n• ᴊᴍ: {}".format(datetime.strftime(timeNow,'%H:%M:%S'))
                                    arg += "\n• ᴛɢ: {}".format(datetime.strftime(timeNow,'%d-%m-%Y'))
                                    contact = dhenzaSelf.getProfile()
                                    mids = [contact.mid]
                                    status = dhenzaSelf.getContact(sender)
                                    vdcl =  "「 Ciee ngajakin Video Call 」"
                                    data = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/9gGMNS3/ezgif-com-gif-maker-1.png",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "7:4",
            "gravity": "top",
            "animated": True,
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://youtube.com/channel/UCNLejYy84XyUX8qcDropXMw"
            }
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": " "+ datetime.strftime(timeNow,'%H:%M:%S'),
                "size": "xxl",
                "color": "#ffffff",
                "align": "start",
                "gravity": "center",
                "margin": "xs"
              }
            ],
            "position": "absolute",
            "offsetTop": "10px",
            "offsetStart": "100px"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/dbGrjHT/20220303-211805.png",
                "animated": True,
                "aspectMode": "cover",
                "size": "xxl"
              }
            ],
            "position": "absolute",
            "offsetStart": "90px",
            "action": {
              "type": "uri",
              "label": "Bgdz",
              "uri": "https://youtube.com/channel/UCNLejYy84XyUX8qcDropXMw"
            }
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(dhenzaSelf.getContact(sender).pictureStatus),
                "aspectMode": "cover",
                "size": "sm",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://youtube.com/channel/UCNLejYy84XyUX8qcDropXMw"
                },
                "animated": True
              }
            ],
            "position": "absolute",
            "action": {
              "type": "uri",
              "label": "Foto",
              "uri": "https://youtube.com/channel/UCNLejYy84XyUX8qcDropXMw"
            },
            "offsetTop": "xxl",
            "offsetStart": "md",
            "borderColor": "#ff0088",
            "borderWidth": "medium"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "{}".format(status.displayName),
                "size": "md",
                "align": "center",
                "color": "#ffffff"
              }
            ],
            "position": "absolute",
            "borderWidth": "normal",
            "borderColor": "#ff0088",
            "offsetBottom": "xl",
            "offsetStart": "md"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": " "+format(datetime.strftime(timeNow,'%d-%m-%Y')),
                "size": "md",
                "align": "center",
                "color": "#ffffff"
              }
            ],
            "position": "absolute",
            "borderWidth": "normal",
            "borderColor": "#ff0088",
            "offsetEnd": "lg"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": " "+format(vdcl),
                "size": "xxs",
                "align": "center",
                "color": "#ffffff",
                "style": "italic"
              }
            ],
            "position": "absolute",
            "borderWidth": "normal",
            "borderColor": "#ff0088",
            "offsetBottom": "md",
            "offsetEnd": "xl"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/WnLG1rC/ezgif-com-gif-to-apng.png",
                "size": "4xl",
                "animated": True
              }
            ],
            "position": "absolute",
            "width": "100px",
            "offsetTop": "40px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": " "+format(c),
                "size": "xs",
                "align": "center",
                "color": "#ffffff",
                "weight": "bold",
                "style": "italic"
              }
            ],
            "position": "absolute",
            "borderWidth": "normal",
            "borderColor": "#ff0088",
            "offsetBottom": "40px",
            "offsetStart": "5px",
            "backgroundColor": "#000000",
            "paddingAll": "0px"
          }
        ],
        "paddingAll": "0px"
      }
    }
  ]
}
                                    dhenzaSelf.postFlex(msg.to,data)
                                if c == 'LIVE' and b == "S":
                                    arg = "• ᴄᴀʟʟ ʟɪᴠᴇ"
                                    arg += "\n• ᴛʏᴘᴇ {} ᴄᴀʟʟ".format(c) 
                                    arg += "\n• ɴᴍ: {}".format(str(contact.displayName)) 
                                    arg += "\n• ɢᴄ: {}".format(str(group.name))
                                    arg += "\n• ʜʀ: {}".format(timeNow.strftime('%A'))
                                    arg += "\n• ᴊᴍ: {}".format(datetime.strftime(timeNow,'%H:%M:%S'))
                                    arg += "\n• ᴛɢ: {}".format(datetime.strftime(timeNow,'%d-%m-%Y'))
                                    dhenzaSelf.sendMessage(msg.to,arg)
                                else:
                                    mills = int(msg.contentMetadata["DURATION"])
                                    seconds = (mills/1000)%60
                                    if c == "AUDIO" and b == "E":
                                        arg = "• ᴄᴀʟʟ ᴀᴜᴅɪᴏ"
                                        arg += "\n• ᴅɪᴀᴋʜɪʀɪ {} ᴄᴀʟʟ".format(c)
                                        arg += "\n• ɴᴍ: {}".format(str(contact.displayName)) 
                                        arg += "\n• ɢᴄ: {}".format(str(group.name))
                                        arg += "\n• ʜʀ: {}".format(timeNow.strftime('%A'))
                                        arg += "\n• ᴊᴍ: {}".format(datetime.strftime(timeNow,'%H:%M:%S'))
                                        arg += "\n• ᴛɢ: {}".format(datetime.strftime(timeNow,'%d-%m-%Y'))
                                        arg += "\n• ᴅʀ: {}".format(seconds)
                                        contact = dhenzaSelf.getProfile()
                                        mids = [contact.mid]
                                        status = dhenzaSelf.getContact(sender)
                                        endac = "「 Yahh Kok Turun Audio Call nya 」 "
                                        data = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/FzvLMfk/ezgif-com-gif-to-apng-1.png",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "7:4",
            "gravity": "top",
            "animated": True,
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://youtube.com/channel/UCNLejYy84XyUX8qcDropXMw"
            }
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": " "+ datetime.strftime(timeNow,'%H:%M:%S'),
                "size": "xxl",
                "color": "#ffffff",
                "align": "start",
                "gravity": "center",
                "margin": "xs",
                "weight": "bold"
              }
            ],
            "position": "absolute",
            "offsetTop": "10px",
            "offsetStart": "100px"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/dbGrjHT/20220303-211805.png",
                "animated": True,
                "aspectMode": "cover",
                "size": "xxl"
              }
            ],
            "position": "absolute",
            "offsetStart": "90px",
            "action": {
              "type": "uri",
              "label": "Bgdz",
              "uri": "https://youtube.com/channel/UCNLejYy84XyUX8qcDropXMw"
            }
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(dhenzaSelf.getContact(sender).pictureStatus),
                "aspectMode": "cover",
                "size": "sm",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://youtube.com/channel/UCNLejYy84XyUX8qcDropXMw"
                },
                "animated": True
              }
            ],
            "position": "absolute",
            "action": {
              "type": "uri",
              "label": "Foto",
              "uri": "https://youtube.com/channel/UCNLejYy84XyUX8qcDropXMw"
            },
            "offsetTop": "xxl",
            "offsetStart": "md",
            "borderColor": "#ff0088",
            "borderWidth": "medium"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": " "+format(endac),
                "size": "xxs",
                "align": "center",
                "color": "#ffffff",
                "style": "italic"
              }
            ],
            "position": "absolute",
            "borderWidth": "normal",
            "borderColor": "#ff0088",
            "offsetEnd": "10px",
            "backgroundColor": "#000000",
            "width": "150px",
            "height": "20px",
            "cornerRadius": "20px",
            "offsetBottom": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "{}".format(status.displayName),
                "size": "md",
                "align": "center",
                "color": "#ffffff"
              }
            ],
            "position": "absolute",
            "borderWidth": "normal",
            "borderColor": "#ff0088",
            "offsetBottom": "sm",
            "offsetStart": "md",
            "backgroundColor": "#000000",
            "width": "150px",
            "height": "25px",
            "cornerRadius": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": " "+format(datetime.strftime(timeNow,'%d-%m-%Y')),
                "size": "xxs",
                "align": "center",
                "color": "#ffffff"
              }
            ],
            "position": "absolute",
            "borderWidth": "normal",
            "borderColor": "#ff0088",
            "offsetEnd": "lg",
            "backgroundColor": "#000000",
            "width": "71px",
            "height": "16px",
            "cornerRadius": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/WnLG1rC/ezgif-com-gif-to-apng.png",
                "size": "4xl",
                "animated": True
              }
            ],
            "position": "absolute",
            "width": "100px",
            "offsetTop": "40px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": " "+format(c),
                "size": "xs",
                "align": "center",
                "color": "#ffffff"
              }
            ],
            "position": "absolute",
            "borderWidth": "normal",
            "borderColor": "#ff0088",
            "offsetBottom": "28px",
            "offsetStart": "10px",
            "backgroundColor": "#000000",
            "width": "70px",
            "height": "20px",
            "cornerRadius": "20px"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/fHg003L/ezgif-com-gif-to-apng-2.png-sparkle-1c61d-star---stern---etoile---animation---gif---anime---animated---glitter---sparkles---etoiles---sterne---stars---deco------tube---effect---sparkle---.gif",
                "animated": True,
                "aspectMode": "cover",
                "size": "4xl"
              }
            ],
            "position": "absolute",
            "offsetStart": "90px",
            "action": {
              "type": "uri",
              "label": "Bg emas",
              "uri": "https://youtube.com/channel/UCNLejYy84XyUX8qcDropXMw"
            }
          }
        ],
        "paddingAll": "0px",
        "offsetTop": "0px",
        "borderWidth": "medium",
        "backgroundColor": "#000000",
        "borderColor": "#ff0088"
      }
    }
  ]
}
                                        dhenzaSelf.postFlex(msg.to,data)
                                    if c == "VIDEO" and b == "E":
                                        arg = "• ᴄᴀʟʟ ᴠɪᴅᴇᴏ"
                                        arg += "\n• ᴅɪᴀᴋʜɪʀɪ {} ᴄᴀʟʟ".format(c)
                                        arg += "\n• ɴᴍ: {}".format(str(contact.displayName)) 
                                        arg += "\n• ɢᴄ: {}".format(str(group.name))
                                        arg += "\n• ʜʀ: {}".format(timeNow.strftime('%A'))
                                        arg += "\n• ᴊᴍ: {}".format(datetime.strftime(timeNow,'%H:%M:%S'))
                                        arg += "\n• ᴛɢ: {}".format(datetime.strftime(timeNow,'%d-%m-%Y'))
                                        arg += "\n• ᴅʀ: {}".format(seconds)
                                        contact = dhenzaSelf.getProfile()
                                        mids = [contact.mid]
                                        status = dhenzaSelf.getContact(sender)
                                        endvc = " 「 Yahh Kok Turun Video Call nya 」"
                                        data ={
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/FzvLMfk/ezgif-com-gif-to-apng-1.png",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "7:4",
            "gravity": "top",
            "animated": True,
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://youtube.com/channel/UCNLejYy84XyUX8qcDropXMw"
            }
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": " "+ datetime.strftime(timeNow,'%H:%M:%S'),
                "size": "xxl",
                "color": "#ffffff",
                "align": "start",
                "gravity": "center",
                "margin": "xs",
                "weight": "bold"
              }
            ],
            "position": "absolute",
            "offsetTop": "10px",
            "offsetStart": "100px"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/dbGrjHT/20220303-211805.png",
                "animated": True,
                "aspectMode": "cover",
                "size": "xxl"
              }
            ],
            "position": "absolute",
            "offsetStart": "90px",
            "action": {
              "type": "uri",
              "label": "Bgdz",
              "uri": "https://youtube.com/channel/UCNLejYy84XyUX8qcDropXMw"
            }
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(dhenzaSelf.getContact(sender).pictureStatus),
                "aspectMode": "cover",
                "size": "sm",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://youtube.com/channel/UCNLejYy84XyUX8qcDropXMw"
                },
                "animated": True
              }
            ],
            "position": "absolute",
            "action": {
              "type": "uri",
              "label": "Foto",
              "uri": "https://youtube.com/channel/UCNLejYy84XyUX8qcDropXMw"
            },
            "offsetTop": "xxl",
            "offsetStart": "md",
            "borderColor": "#ff0088",
            "borderWidth": "medium"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": " "+format(endvc),
                "size": "xxs",
                "align": "center",
                "color": "#ffffff",
                "style": "italic"
              }
            ],
            "position": "absolute",
            "borderWidth": "normal",
            "borderColor": "#ff0088",
            "offsetEnd": "10px",
            "backgroundColor": "#000000",
            "width": "150px",
            "height": "20px",
            "cornerRadius": "20px",
            "offsetBottom": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "{}".format(status.displayName),
                "size": "md",
                "align": "center",
                "color": "#ffffff"
              }
            ],
            "position": "absolute",
            "borderWidth": "normal",
            "borderColor": "#ff0088",
            "offsetBottom": "sm",
            "offsetStart": "md",
            "backgroundColor": "#000000",
            "width": "150px",
            "height": "25px",
            "cornerRadius": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": " "+format(datetime.strftime(timeNow,'%d-%m-%Y')),
                "size": "xxs",
                "align": "center",
                "color": "#ffffff"
              }
            ],
            "position": "absolute",
            "borderWidth": "normal",
            "borderColor": "#ff0088",
            "offsetEnd": "lg",
            "backgroundColor": "#000000",
            "width": "71px",
            "height": "16px",
            "cornerRadius": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/WnLG1rC/ezgif-com-gif-to-apng.png",
                "size": "4xl",
                "animated": True
              }
            ],
            "position": "absolute",
            "width": "100px",
            "offsetTop": "40px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": " "+format(c),
                "size": "xs",
                "align": "center",
                "color": "#ffffff"
              }
            ],
            "position": "absolute",
            "borderWidth": "normal",
            "borderColor": "#ff0088",
            "offsetBottom": "28px",
            "offsetStart": "10px",
            "backgroundColor": "#000000",
            "width": "70px",
            "height": "20px",
            "cornerRadius": "20px"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/fHg003L/ezgif-com-gif-to-apng-2.png-sparkle-1c61d-star---stern---etoile---animation---gif---anime---animated---glitter---sparkles---etoiles---sterne---stars---deco------tube---effect---sparkle---.gif",
                "animated": True,
                "aspectMode": "cover",
                "size": "4xl"
              }
            ],
            "position": "absolute",
            "offsetStart": "90px",
            "action": {
              "type": "uri",
              "label": "Bg emas",
              "uri": "https://youtube.com/channel/UCNLejYy84XyUX8qcDropXMw"
            }
          }
        ],
        "paddingAll": "0px",
        "offsetTop": "0px",
        "borderWidth": "medium",
        "backgroundColor": "#000000",
        "borderColor": "#ff0088"
      }
    }
  ]
}
                                        dhenzaSelf.postFlex(msg.to,data)
                                    if c == "LIVE" and b == "E":
                                        arg = "• ᴄᴀʟʟ ʟɪᴠᴇ"
                                        arg += "\n• ᴅɪᴀᴋʜɪʀɪ {} ᴄᴀʟʟ".format(c)
                                        arg += "\n• ɴᴍ: {}".format(str(contact.displayName)) 
                                        arg += "\n• ɢᴄ: {}".format(str(group.name))
                                        arg += "\n• ʜʀ: {}".format(timeNow.strftime('%A'))
                                        arg += "\n• ᴊᴍ: {}".format(datetime.strftime(timeNow,'%H:%M:%S'))
                                        arg += "\n• ᴛɢ: {}".format(datetime.strftime(timeNow,'%d-%m-%Y'))
                                        arg += "\n• ᴅʀ: {}".format(seconds)
                                        dhenzaSelf.sendMessage(msg.to,arg)
                        except Exception as error:
                             print(error)                
                             
        if op.type in [26]:
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            silentk1ller = command(text)
            to = receiver
            if settings["Danger"] == True:
            	if msg._from not in Bots or msg._from not in admin or msg._from not in owner:
                    if silentk1ller in [".js","!js",".sikat","!sikat","sikat","Bubar",".bubar","!bubar",".cipok","!cupok","Cleanse","!cleanse",".cleanse","Kickall","!kickall",".kickall","mayhem","Ratakan","bubarkan","Nuke","nuke",".nuke","Bypass","bypass",".bypass","hancurkan","!malam",".fuck",".malam"]:
                        dhenzaSelf.kickoutFromGroup(receiver,[sender])
                        dhenzaSelf.sendMessage(receiver, "sorri  sya kick jangan usil ya mau JS room") 
# MEDIA NEW BATAS  •••••••••••••••••••••••••••   
                    
                    elif 'https://vt.tiktok.com/' in silentk1ller:
                      #    if settings["tiktok"] == True:
                            try:
                                spilt = silentk1ller.split(" ")
                                txt = spilt
                                no = 0 + 1
                                no += 1
                                data = "{}".format(str(len(txt)))
                                c=ApCalculator()
                                c.run('{} - 1'.format(data))
                                sm = {"write":""}
                                date = sm["write"] = c.lcd
                                dz = sm["write"]
                                hasil = int(dz)
                                masuk = txt[hasil]
                                url = requests.get("https://api.chstore.me/tiktok?url={}".format(masuk))
                                data = url.text
                                main = json.loads(data)
                                dhenzaSelf.sendVideoWithURL(to, main["result"]["mp4"])
                            except Exception as error:
                                print(error)
                    elif "https://youtu.be/" in silentk1ller:
          #                if settings["yt"] == True:
                            try:
                                spilt = silentk1ller.split(" ")
                                txt = spilt
                                no = 0 + 1
                                no += 1
                                data = "{}".format(str(len(txt)))
                                c=ApCalculator()
                                c.run('{} - 1'.format(data))
                                sm = {"write":""}
                                date = sm["write"] = c.lcd
                                dz = sm["write"]
                                hasil = int(dz)
                                aturan = txt[hasil]
                                url = requests.get("https://api.chstore.me/youtube?url={}".format(aturan))
                                main = url.text
                                main = json.loads(main)
                                sk = "WAIT DONLOAD YT \n\n"
                                sk += "DURATION : {}\n".format(main["result"]["duration"])
                                sk += "TITLE : {}".format(main["result"]["title"])
                                dhenzaSelf.sendReplyMessage(msg.id,to, "{}".format(sk)) 
                                dhenzaSelf.sendVideoWithURL(to, main["result"]["mp4"])
                            except Exception as error:
                                print(error)
                                
                    elif 'https://www.smule.com/' in silentk1ller or 'https://www.smule.com/sing-recording' in silentk1ller:
                      #    if settings["smule"] == True:
                            try:
                                spilt = silentk1ller.split(" ")
                                txt = spilt
                                no = 0 + 1
                                no += 1
                                data = "{}".format(str(len(txt)))
                                c=ApCalculator()
                                c.run('{} - 1'.format(data))
                                sm = {"write":""}
                                date = sm["write"] = c.lcd
                                dz = sm["write"]
                                hasil = int(dz)
                                masuk = txt[hasil]
                                url = requests.get("https://api.chstore.me/smule/post?url={}".format(masuk))
                                xx = url.text
                                res = json.loads(xx)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                contact = dhenzaSelf.getProfile()
                                mids = [contact.mid]
                                status = dhenzaSelf.getContact(sender)                               	
                                cover = dhenzaSelf.getProfileCoverURL(sender)
                                ID = "ID : {}".format(res["result"]["owner"]["handle"])
                                LIKE = "LIKE : {}".format(res["result"]["stats"]["total_loves"])
                                LISTEN = "LISTENS : {}".format(res["result"]["stats"]["total_listens"])
                                COMMENT = "COMMENT : {}".format(res["result"]["stats"]["total_comments"])
                                TITLE = "{}".format(res["result"]["title"])
                                PICT = "{}".format(res["result"]["cover_url"])
                                sk = "WAITING DONLOAD FILE\n\n"
                                sk += "\n {}".format(ID)
                                sk += "\n {}".format(LIKE)
                                sk += "\n {}".format(LISTEN)
                                sk += "\n {}".format(COMMENT)
                                sk += "\n {}".format(TITLE)
                                dhenzaSelf.sendReplyMessage(msg.id,to, str(sk))
                                if res["result"]["type"] == "audio":
                                    dhenzaSelf.sendAudioWithURL(to, "{}".format(res["result"]["media_url"]))
                                else:
                                    dhenzaSelf.sendVideoWithURL(to, "{}".format(res["result"]["video_media_url"]))
                            except Exception as error:
                                print(error)  
#===================================≈=============                                                                

#===================BAGIAN PUBLIK BOT =====================================================                        
        if op.type in [26]:
            if op.type == 26: print ("[26] RECEIVE MESSAGE")
            else: print ("[○] SEND MESSAGE")
            try:
                msg = op.message
                text = str(silentk1ller)
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                silentk1ller = command(text)
                for silentk1ller in silentk1ller.split(" & "):
                    setKey = settings["keyCommand"].title()
                    if settings["setKey"] == False:
                        setKey = ''
                    if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                        if msg.toType == 0:
                            if sender != dhenzaSelf.profile.mid:
                                to = sender
                            else:
                                to = receiver
                        elif msg.toType == 1:
                            to = receiver
                        elif msg.toType == 2:
                            to = receiver
                        if msg.contentType == 0:
                            if to in offbot:
                                return
                            if silentk1ller == "help" or silentk1ller == "sb":
                        #    if msg._from in admin or msg._from in owner:
                                dhenzaSelf.sendReplyMessage(msg.id, to,helpMessage)
                                
                                
                        if silentk1ller == "liff":
                        	if msg._from in dhenzaMid:
                        	  dhenzaSelf.sendMessage(to, "line://app/1602687308-GXq4Vvk9?type=text&text=")
                                
                        if silentk1ller == "logout":
                              if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                dhenzaSelf.sendReplyMessage(msg.id, to, "Your selfbot has been logout ")
                                sys.exit("[ INFO ] BOT SHUTDOWN")
                                
                        elif silentk1ller == "me":
                            if msg._from in admin:
                               contact = dhenzaSelf.getContact(sender)
                               dhenzaSelf.sendMessage(msg.to, None,contentMetadata={'mid': sender}, contentType=13)

                        elif silentk1ller == "mid":
                               dhenzaSelf.sendMessage(msg.to, msg._from)

                       
                        elif silentk1ller  == "midbot":
                          if msg._from in admin:
                              dhenzaSelf.sendMessage(msg.to, mid)
                                
                        elif silentk1ller == "reset":
                              if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                restart = "ˢᵘᶜˢᵉˢˢ ʳᵉᵇᵒᵒᵗ ˢⁱˢᵗᵉᵐ ᵇᵒᵗ ᶠʳᵉˢʰ"
                                contact = dhenzaSelf.getContact(sender)
                                dhenzaSelf.sendReplyMessage(msg.id, to,restart)
                                restartBot()

                        elif silentk1ller == "runtime":
                                timeNow = time.time()
                                runtime = timeNow - dhenzaStart
                                runtime = timeChange(runtime)
                                run = "Bot telah aktif selama {}".format(str(runtime))
                                dhenzaSelf.sendReplyMessage(msg.id, to, run)
                                
                        elif silentk1ller == settings["mentionall"]:
                                  group = dhenzaSelf.getGroup(to);nama = [contact.mid for contact in group.members];nama.remove(dhenzaSelf.getProfile().mid)
                                  dhenzaSelf.datamention(to,'「MENTION MEMBER」',nama)
                                  
                        elif silentk1ller.startswith("settagall "):
                              if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                settings["mentionall"] = "{}".format(txt)
                                dhenzaSelf.sendReplyMessage(msg_id, to, "Succesfully change Mention member with key >> {}".format(settings["mentionall"]))
                             
                        elif silentk1ller.startswith("cgrupname: "):
                              if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                if msg.toType == 2:
                                    sep = text.split(" ")
                                    groupname = text.replace(sep[0] + " ","")
                                    if len(groupname) <= 100:
                                        group = dhenzaSelf.getGroup(to)
                                        group.name = groupname
                                        dhenzaSelf.updateGroup(group)
                                        dhenzaSelf.sendReplyMessage(msg.id, to,"Berhasil mengubah nama group menjadi : {}".format(groupname))
                                        
                        elif silentk1ller == "cpict":
                              if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                settings["changePictureProfile"] = True
                                dhenzaSelf.sendReplyMessage(msg.id, to,"Silahkan kirim gambarnya")
                        elif silentk1ller == "cpv":
                              if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                settings["changeVpProfile"] = True
                                dhenzaSelf.sendReplyMessage(msg.id, to,"Silahkan kirim Videonya")

                        elif silentk1ller == "cgrupict":
                              if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                if msg.toType == 2:
                                    if to not in settings["changeGroupPicture"]:
                                        settings["changeGroupPicture"].append(to)
                                    dhenzaSelf.sendReplyMessage(msg.id, to,"Silahkan kirim gambarnya")               
                                    
                        elif silentk1ller.startswith("changename: "):
                              if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                if len(name) <= 999:
                                    profile = dhenzaSelf.getProfile()
                                    profile.displayName = name
                                    dhenzaSelf.updateProfile(profile)
                                    dhenzaSelf.sendMessage(to, "Berhasil mengubah nama menjadi : {}".format(name))
                              else:
                                  txt = ("Hmmmm gk bsa ya :(","Sorryy :(","Jgn Ubah Namaku :(")
                                  pop = random.choice(txt)
                                  dhenzaSelf.sendMessage(to, pop)
                                  
                        elif silentk1ller == "cdual":
                              if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                settings["changeDual"] = True
                                dhenzaSelf.sendReplyMessage(msg.id, to,"Send Viideo for profile")
                                
                        elif silentk1ller.startswith("cppurl"):
                                if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                        link = removeCmd("cppurl", text)
                                        contact = dhenzaSelf.getContact(sender)
                                        dhenzaSelf.sendReplyMessage(msg.id, to," Type: Profile\n • Detail: Change video url\n • Status: Download...")
                                        print("Sedang Mendownload Data")
                                        pic = "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                                        subprocess.getoutput('youtube-dl --format mp4 --output dhenza.mp4 {}'.format(link))
                                        pict = dhenzaSelf.downloadFileURL(pic)
                                        vids = "dhenza.mp4"
                                        changeVideoAndPictureProfile(pict, vids)
                                        dhenzaSelf.sendReplyMessage(msg.id, to," Type: Profile\n • Detail: Change video url\n • Status: Succes")
                                        os.remove("dhenza.mp4")

                        elif silentk1ller.startswith("changebio: "):
                              if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                sep = text.split(" ")
                                bio = text.replace(sep[0] + " ","")
                                if len(bio) <= 100000:
                                    profile = dhenzaSelf.getProfile()
                                    profile.statusMessage = bio
                                    dhenzaSelf.updateProfile(profile)
                                    dhenzaSelf.sendMessageWithFooter(to, "Berhasil mengubah bio menjadi : {}".format(bio))              
#========================== on / off ================            
                        elif silentk1ller == "lurking on":
                              if msg._from in owner or admin:
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if to in read['readPoint']:
                                    try:
                                        del read['readPoint'][to]
                                        del read['readMember'][to]
                                    except:
                                        pass
                                    read['readPoint'][to] = msg_id
                                    read['readMember'][to] = []
                                    dhenzaSelf.sendReplyMessage(msg.id, to,"Lurking telah diaktifkan")
                                else:
                                    try:
                                        del read['readPoint'][to]
                                        del read['readMember'][to]
                                    except:
                                        pass
                                    read['readPoint'][to] = msg_id
                                    read['readMember'][to] = []
                                    dhenzaSelf.sendReplyMessage(msg.id, to,"Set reading point : \n{}".format(readTime))
                        elif silentk1ller == "lurking off":
                              if msg._from in owner or admin:
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if to not in read['readPoint']:
                                    dhenzaSelf.sendReplyMessage(msg.id, to, "Lurking telah dinonaktifkan")
                                else:
                                    try:
                                        del read['readPoint'][to]
                                        del read['readMember'][to]
                                    except:
                                        pass
                                    dhenzaSelf.sendReplyMessage(msg.id, to,"Menghapus tukang ngintip : \n{}".format(readTime))
                        elif "lurking" in silentk1ller:
                              if msg._from in owner or admin:
                                if to in read['readPoint']:
                                    if read["readMember"][to] == []:
                                        return dhenzaSelf.sendReplyMessage(msg.id, to,"Tidak Ada tukang  ngintip")
                                    else:
                                        no = 0
                                        result = "「 Total Tukang Ngintip 」"
                                        for dataRead in read["readMember"][to]:
                                            no += 1
                                            result += "\n {}. @!".format(str(no))
                                        result += "\n「 Total {} Sider 」".format(str(len(read["readMember"][to])))
                                        dhenzaSelf.sendMention(msg.to, result, read["readMember"][to])
                                        read['readMember'][to] = []                 
         
                        elif silentk1ller == "welcome on":
                              if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                if msg.to in settings["welcomee"]:
                                   dhenzaSelf.sendMessage(to,"「 WELCOME MESSAGE  」")
                                else:
                                	settings["welcomee"][msg.to] = True
                                dhenzaSelf.sendMessage(to,"Baerhasil mengaktifkan Welcome message")
                                
                        elif silentk1ller == "welcome off":
                              if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                if msg.to not in settings["welcomee"]:
                                   dhenzaSelf.sendMessage(to,"「 WELCOM EMESSAGE 」")
                                else:
                                	del settings["welcomee"][msg.to]
                                dhenzaSelf.sendMessage(to,"Berhasil menonaktifkan Welcome message")
                                
                        elif silentk1ller == "sider on":
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  dhenzaSelf.sendMessage(to, "Cek sider diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del settings['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              #settings['cyduk'][msg.to]=True

                        elif silentk1ller == "sider off":
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  del cctv['point'][msg.to]
                                  dhenzaSelf.sendMessage(to, "Cek sider dinonaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                              else:
                                  dhenzaSelf.sendMessage(to, "Sudak tidak aktif")
#°°°°°°°°°                                    
                        elif silentk1ller.startswith("tarik "):
                          if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                            args = silentk1ller.replace("tarik ","")
                            mes = 0
                            try:
                                mes = int(args[1])
                            except:
                                mes = 1
                            M = dhenzaSelf.getRecentMessagesV2(to, 101)
                            MId = []
                            for ind,i in enumerate(M):
                                if ind == 0:
                                    pass
                                else:
                                    if i._from == dhenzaSelf.profile.mid:
                                        MId.append(i.id)
                                        if len(MId) == mes:
                                            break
                            def unsMes(id):
                                dhenzaSelf.unsendMessage(id)
                            for i in MId:
                                thread1 = threading.Thread(target=unsMes, args=(i,))
                                thread1.start()
                                thread1.join()
                            dhenzaSelf.sendMessage(msg.to, "Success unsend {} message".format(len(MId)))
      

                        elif silentk1ller == "speed":
                              if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                 start = time.time()                               
                                 dhenzaSelf.sendMessage(to, "𝚌𝚑𝚎𝚔𝚒𝚗𝚐 𝚜𝚙𝚎𝚎𝚍 𝚋𝚘𝚝𝚜...")                               
                                 elapsed_time = time.time() - start
                                 dhenzaSelf.sendReplyMessage(msg.id, to,"{} sec".format(str(elapsed_time/100)))
                                 
                        elif silentk1ller == "open":
                              if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                if msg.toType == 2:
                                   X = dhenzaSelf.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   dhenzaSelf.updateGroup(X)
                                   dhenzaSelf.sendReplyMessage(msg.id, to, "ᯓ▹ Url Opened")

                        elif silentk1ller == "close":
                              if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                  if msg.toType == 2:
                                     X = dhenzaSelf.getGroup(msg.to)
                                     X.preventedJoinByTicket = True
                                     dhenzaSelf.updateGroup(X)
                                     dhenzaSelf.sendReplyMessage(msg.id, to, "ᯓ▹ Url Closed")

                        elif silentk1ller == "url":
                              if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                  if msg.toType == 2:
                                     x = dhenzaSelf.getGroup(msg.to)
                                     if x.preventedJoinByTicket == True:
                                        x.preventedJoinByTicket = False
                                        dhenzaSelf.updateGroup(x)
                                     gurl = dhenzaSelf.reissueGroupTicket(msg.to)
                                     dhenzaSelf.sendReplyMessage(msg_id, to, "ᯓ▹ Nama : "+str(x.name)+ "\nᯓ▹ Url grup : http://line.me/R/ti/g/"+gurl)                
#=========================================     
                        elif silentk1ller.startswith("yt3"):
                                sep = text.split(" ")
                                txt = silentk1ller.replace(sep[0] + " ","")
                                treding = Thread(target=youtubeMp3,args=(to,txt,))
                                treding.daemon = True
                                treding.start()

                        elif silentk1ller.startswith("yt4"):
                                sep = text.split(" ")
                                txt = silentk1ller.replace(sep[0] + " ","")
                                treding = Thread(target=youtubeMp4,args=(to,txt,))
                                treding.daemon = True
                                treding.start()
                                
                        elif silentk1ller.startswith("listsmule "):
                                sep = text.split(" ")
                                search = text.replace(sep[0] + " ","")
                                r = requests.get("https://smule.com/{}/performances/json".format(str(search)))
                                data = r.text
                                a = json.loads(data)
                                if a["list"] != []:
                                    ret_ = []
                                    yt = []
                                    for music in a["list"]:
                                        ret_.append({
                                            "type": "bubble",
                                            "size": "micro",
                                            "styles": {
                                                "body": {
                                                   "backgroundColor": "#000000",
                                                   "separator": True,
                                                   "separatorColor": "#FF0000"
                                                },
                                                "footer": {
                                                    "backgroundColor": "#000000",
                                                    "separator": True,
                                                   "separatorColor": "#FF0000"
                                               }
                                            },
                                            "hero": {
                                                "type": "image",
                                                "url": "{}".format(music['cover_url']),
                                                "size": "full",
                                                "aspectRatio": "20:13",
                                                "aspectMode": "cover",
                                                "action": {
                                                    "type": "uri",
                                                    "uri": "line://app/1602687308-GXq4Vvk9?type=sticker&stk=noanim&sid=32128231&pkg=3099312"
                                                }
                                            },
                                            "body": {
                                                "type": "box",
                                                "spacing": "md",
                                                "layout": "horizontal",
                                                "contents": [{
                                                    "type": "box",
                                                    "spacing": "none",
                                                    "flex": 1,
                                                    "layout": "vertical",
                                                    "contents": [{
                                                        "type": "image",
                                                        "url": "https://i.ibb.co/7J1FWPc/ei-1624349250118-removebg-preview.png",
                                                        "aspectMode": "cover",
                                                        "gravity": "bottom",
                                                        "size": "sm",
                                                        "aspectRatio": "1:1",
                                                        "action": {
                                                          "type": "uri",
                                                          "uri": "https://smule.com/{}/{}".format(str(search), str(music["web_url"]))
                                                        }
                                                    }]
                                                }, {
                                                    "type": "separator",
                                                    "color": "#FF0000"
                                                }, {
                                                    "type": "box",
                                                    "contents": [{
                                                        "type": "text",
                                                        "text": "title",
                                                        "color": "#FF0000",
                                                        "size": "xxs",
                                                        "weight": "bold",
                                                        "flex": 1,
                                                        "gravity": "top"
                                                    }, {
                                                        "type": "separator",
                                                        "color": "#FF0000"
                                                    }, {
                                                        "type": "text",
                                                        "text": "%s" % music['title'],
                                                        "color": "#00FF00",
                                                        "size": "xxs",
                                                        "weight": "bold",
                                                        "flex": 1,
                                                        "wrap": True,
                                                        "gravity": "top"
                                                    }],
                                                    "flex": 1,
                                                    "layout": "vertical"
                                                }]
                                            },
                                            "footer": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [{
                                                    "type": "box",
                                                    "layout": "horizontal",
                                                    "contents": [{
                                                        "type": "button",
                                                        "flex": 1,
                                                        "style": "primary",
                                                        "color": "#FF0000",
                                                        "height": "sm",
                                                        "action": {
                                                            "type": "uri",
                                                            "label": "🎬",
                                                            "uri": "https://smule.com/{}/{}".format(str(search), str(music["web_url"]))
                                                        }
                                                     }, {
                                                        "flex": 1,
                                                        "type": "button",
                                                        "margin": "sm",
                                                        "style": "primary",
                                                        "color": "#FF0000",
                                                        "height": "sm",
                                                        "action": {
                                                            "type": "uri",
                                                            "label": "🎬",
                                                            "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=.smuleaudio%20https://smule.com/{}/{}".format(str(search), str(music["web_url"]))
                                                        }
                                                    }]
                                                },
                                                {
                                                    "type": "button",
                                                    "margin": "sm",
                                                    "style": "primary",
                                                    "color": "#FF0000",
                                                    "height": "sm",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "🎬",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=.smulevideo%20https://smule.com/{}/{}".format(str(search), str(music["web_url"]))
                                                    }
                                                }]
                                            }
                                        }
                                    )
                                        yt.append("https://smule.com/{}/{}".format(str(search), str(music["web_url"])))
                                    k = len(ret_)//5
                                    for aa in range(k+1):
                                        data = {
                                            "type": "flex",
                                            "altText": "Search Smule Resorting",
                                            "contents": {
                                                "type": "carousel",
                                                "contents": ret_[aa*5 : (aa+1)*5]
                                            }
                                        }
                                        dhenzaSelf.postTemplate(to, data)
                                        
                                        
                        elif silentk1ller.startswith("youtube "):
                                sep = text.split(" ")
                                search = text.replace(sep[0] + " ","")
                                r = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=10&q={}&type=video&key=AIzaSyApzHZ18jUd3BdkhL_xcwAI_zxqwb9fuy4".format(str(search)))
                                data = r.text
                                a = json.loads(data)
                                if a["items"] != []:
                                    ret_ = []
                                    yt = []
                                    for music in a["items"]:
                                        ret_.append({
                                            "type": "bubble",
                                    #        "size": "micro",
                                            "styles": {
                                                "body": {
                                                   "backgroundColor": "#000000",
                                                   "separator": True,
                                                   "separatorColor": "#FF0000"
                                                },
                                                "footer": {
                                                    "backgroundColor": "#000000",
                                                    "separator": True,
                                                   "separatorColor": "#FF0000"
                                               }
                                            },
                                            "hero": {
                                                "type": "image",
                                                "url": "https://i.ytimg.com/vi/{}/maxresdefault.jpg".format(music['id']['videoId']),
                                                "size": "full",
                                                "aspectRatio": "2:1",
                                                "aspectMode": "cover",
                                                "action": {
                                                    "type": "uri",
                                                    "uri": "line://nv/profilePopup/mid=ua797021910f0584e11be56d4a6fa74ed"
                                                }
                                            },
                                            "body": {
                                                "type": "box",
                                                "spacing": "md",
                                                "layout": "horizontal",
                                                "contents": [{
                                                    "type": "box",
                                                    "spacing": "none",
                                                    "flex": 1,
                                                    "layout": "vertical",
                                                    "contents": [{
                                                        "type": "image",
                                                        "url": "https://i.ibb.co/nCwKXJg/ezgif-com-gif-maker-6.png",
                                                        "animated": True,
                                                        "aspectMode": "cover",
                                                        "gravity": "bottom",
                                                        "size": "sm",
                                                        "aspectRatio": "1:1",
                                                        "action": {
                                                          "type": "uri",
                                                          "uri": "https://www.youtube.com/watch?v=%s" % music['id']['videoId']
                                                        }
                                                    }]
                                                }, {
                                                    "type": "separator",
                                                    "color": "#FF0000"
                                                }, {
                                                    "type": "box",
                                                    "contents": [{
                                                        "type": "text",
                                                        "text": "judul Video",
                                                        "color": "#FF0000",
                                                        "size": "xxs",
                                                        "weight": "bold",
                                                        "flex": 3,
                                                        "gravity": "top"
                                                    }, {
                                                        "type": "separator",
                                                        "color": "#FF0000"
                                                    }, {
                                                        "type": "text",
                                                        "text": "%s" % music['snippet']['title'],
                                                        "color": "#00FF00",
                                                        "size": "xxs",
                                                        "weight": "bold",
                                                        "flex": 2,
                                                        "wrap": True,
                                                        "gravity": "top"
                                                    }],
                                                    "flex": 3,
                                                    "layout": "vertical"
                                                }]
                                            },
                                            "footer": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [{
                                                    "type": "box",
                                                    "layout": "horizontal",
                                                    "contents": [{
                                                        "type": "button",
                                                        "flex": 0,
                                                        "style": "primary",
                                                        "color": "#FF0000",
                                                        "height": "sm",
                                                        "action": {
                                                            "type": "uri",
                                                            "label": "Youtube",
                                                            "uri": "https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                        }
                                                     }, {
                                                        "flex": 2,
                                                        "type": "button",
                                                        "margin": "sm",
                                                        "style": "primary",
                                                        "color": "#FF0000",
                                                        "height": "sm",
                                                        "action": {
                                                            "type": "uri",
                                                            "label": "Mp3",
                                                            "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=yt3%20https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                        }
                                                    }]
                                                },
                                                {
                                                    "type": "button",
                                                    "margin": "xs",
                                                    "style": "primary",
                                                    "color": "#FF0000",
                                                    "height": "sm",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Mp4",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=yt4%20https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                    }
                                                }]
                                            }
                                        }
                                    )
                                        yt.append('https://www.youtube.com/watch?v=' +music['id']['videoId'])
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "flex",
                                            "altText": "Youtube",
                                            "contents": {
                                                "type": "carousel",
                                                "contents": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        dhenzaSelf.postTemplate(to, data)
                                                                               
#COMAND HELPER =====================
                        elif silentk1ller.startswith("broadcast: "):
                            if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = dhenzaSelf.getGroupIdsJoined()
                               groups = dhenzaSelf.getGroupIdsJoined()
                               contacts = dhenzaSelf.getAllContactIds()
                               contact = dhenzaSelf.getProfile()
                               mids = [contact.mid]
                               status = dhenzaSelf.getContact(sender)
                               for group in saya:
                                   dhenzaSelf.sendMessage(group, pesan)
#==================================================
                        elif silentk1ller.startswith("adminadd "):
                            if msg._from in owner:
                                sep = text.split(" ")
                                pesan = text.replace(sep[0] + " ","")
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    if target not in admin:
                                        admin.append(target)
                                        dhenzaSelf.sendMessage(msg.to, "✓sᴜᴄᴄᴇss ᴀᴅᴅ ᴀᴅᴍɪɴ")
                                    else:
                                        dhenzaSelf.sendMessage(msg.to, "sudah menjadi anggota ᴀᴅᴍɪɴ")


                        elif silentk1ller.startswith("botsadd "):
                            if msg._from in admin:
                            	sep = text.split(" ")
                            pesan = text.replace(sep[0] + " ","")   
                            key = eval(msg.contentMetadata["MENTION"])
                            key["MENTIONEES"][0]["M"]
                            targets = []
                            for x in key["MENTIONEES"]:
                                 targets.append(x["M"])
                                 for target in targets:
                                    if target not in Bots:
                                       Bots.append(target)
                                       dhenzaSelf.sendMessage(msg.to, "✓sᴜᴄᴄᴇss ᴀᴅᴅ Bots")
                                    else:
                                       dhenzaSelf.sendMessage(msg.to, "sudah menjadi anggota Bots")

                        elif silentk1ller.startswith("admindell "):
                            if msg._from in creator:
                            	sep = text.split(" ")
                            pesan = text.replace(sep[0] + " ","")   
                            key = eval(msg.contentMetadata["MENTION"])
                            key["MENTIONEES"][0]["M"]
                            targets = []
                            for x in key["MENTIONEES"]:
                                 targets.append(x["M"])
                                 for target in targets:
                                   if target not in Team:
                                       try:
                                           admin.remove(target)
                                           dhenzaSelf.sendMessage(msg.to, "✓sᴜᴄᴄᴇss ᴅᴇʟᴇᴛᴇ ᴀᴅᴍɪɴ")
                                       except:
                                           pass


                        elif silentk1ller.startswith("botdell "):
                            if msg._from in admin:
                            	sep = text.split(" ")
                            pesan = text.replace(sep[0] + " ","")   
                            key = eval(msg.contentMetadata["MENTION"])
                            key["MENTIONEES"][0]["M"]
                            targets = []
                            for x in key["MENTIONEES"]:
                                 targets.append(x["M"])
                                 for target in targets:
                                   if target not in Team:
                                       try:
                                           Bots.remove(target)
                                           dhenzaSelf.sendMessage(msg.to, "✓sᴜᴄᴄᴇss ᴅᴇʟᴇᴛᴇ ʙᴏᴛs")
                                       except:
                                           pass

                        elif silentk1ller == "banlist":
                            if msg._from in owner or msg._from in admin:
                              if pro["blacklist"] == {}:
                                dhenzaSelf.sendMessage(msg.to,"Nothing blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in pro["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +dhenzaSelf.getContact(m_id).displayName + "\n"
                                dhenzaSelf.sendMessage(msg.to,"Blacklist\n\n"+ma+"\n %s User" %(str(len(pro["blacklist"]))))
                                       
                        elif silentk1ller == "clearban":
                            if msg._from in owner or msg._from in admin:
                              pro["blacklist"] = {}
                              ragets = dhenzaSelf.getContacts(pro["blacklist"])
                              mc = ""
                              dhenzaSelf.sendMessage(msg.to,"Succes clearall " + mc)
                              
                        elif silentk1ller == "cekbot":
                            if msg._from in admin or msg._from in owner:
                               try:dhenzaSelf.inviteIntoGroup(to, [dhenzaMid]);has = "OK"
                               except:has = "NOT"
                               try:dhenzaSelf.kickoutFromGroup(to, [dhenzaMid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "✅ full 100%"
                               else:sil = "❎. Low 0%"
                               if has1 == "OK":sil1 = "✅ full 100%"
                               else:sil1 = "❎ Low 0%"
                               dhenzaSelf.sendMessage(to, "Status:\n\n♻️ Kick : {} \n♻️ Invite : {}".format(sil1,sil))
                                
                        elif silentk1ller == "protectlist":
                            if msg._from in owner or msg._from in admin:
                                ma = ""
                                mb = ""
                                md = ""
                                me = ""
                                mf = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                e = 0
                                f = 0            
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +dhenzaSelf.getGroup(group).name + "\n"
                                gid = protectinvite
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +dhenzaSelf.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +dhenzaSelf.getGroup(group).name + "\n"
                                gid = protectkick
                                for group in gid:
                                    e = e + 1
                                    end = '\n'
                                    me += str(e) + ". " +dhenzaSelf.getGroup(group).name + "\n"
                                gid = protectjoin
                                for group in gid:
                                    f = f + 1
                                    end = '\n'
                                    mf += str(f) + ". " +dhenzaSelf.getGroup(group).name + "\n"
                                dhenzaSelf.sendMessage(msg.to,"⛎ᴅᴀғᴛᴀʀ ʟɪsᴛ ᴘʀᴏᴛᴇᴄᴛ⛎\n\n🔒ᴘʀᴏᴛᴇᴄᴛ ǫʀ:\n"+ma+"\n🔒ᴘʀᴏᴛᴇᴄᴛ ɪɴᴠɪᴛᴇ:\n"+mb+"\n🔒ᴘʀᴏᴛᴇᴄᴛᴋɪᴄᴋ:\n"+md+"\n🔒ᴘʀᴏᴛᴇᴄᴛᴄᴀɴᴄᴇʟ:\n"+me+"\n🔒ᴘʀᴏᴛᴇᴄᴛᴊᴏɪɴ:\n"+mf+"\n\n⛎ᴘʀᴏᴛᴇᴄᴛ ʟɪsᴛ %s ɢʀᴏᴜᴘ⛎" %(str(len(protectqr)+len(protectinvite)+len(protectcancel)+len(protectkick)+len(protectjoin))))
                            
                        elif silentk1ller == "botlist":
                            if msg._from in admin:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +dhenzaSelf.getContact(m_id).displayName + "\n"
                                dhenzaSelf.sendMessage(msg.to, "-------ʟɪsᴛʙᴏᴛ--------\n\n"+ma+"\nᴛᴏᴛᴀʟ :「%s」ʙᴏᴛs\n---------------------------" %(str(len(Bots))))                                  
                        
                                                         
                        elif silentk1ller.startswith("protectqr "):
                           if msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('protectqr ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = "Protect url sudah aktif"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = dhenzaSelf.getGroup(msg.to)
                                       msgs = "Status : [ ✔ ]\nDi Group : " +str(ginfo.name)
                                  dhenzaSelf.sendMessage(msg.to, "「 Status Protect Url 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = dhenzaSelf.getGroup(msg.to)
                                         msgs = "Status : [ ❌ ]\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect url sudah tidak aktif"
                                    dhenzaSelf.sendMessage(msg.to, "「 Status Protect Url 」\n" + msgs)
                                    
                        elif silentk1ller.startswith("protectkick "):
                           if msg._from in owner or msg._from in admin or msg._from in staff:
                              spl = msg.text.replace('protectkick ','')
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "Protect kick sudah aktif"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = dhenzaSelf.getGroup(msg.to)
                                       msgs = "Status : [ ✔ ]\nDi Group : " +str(ginfo.name)
                                  dhenzaSelf.sendMessage(msg.to, "「 Status Protect kick 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = dhenzaSelf.getGroup(msg.to)
                                         msgs = "Status : [ ❌ ]\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect kick sudah tidak aktif"
                                    dhenzaSelf.sendMessage(msg.to, "「 Status Protect kick 」\n" + msgs)

                        elif silentk1ller.startswith("protectjoin "):
                           if msg._from in owner or msg._from in admin or msg._from in staff:
                              spl = msg.text.replace('protectjoin ','')
                              if spl == 'on':
                                  if msg.to in protectjoin:
                                       msgs = "Protect join sudah aktif"
                                  else:
                                       protectjoin.append(msg.to)
                                       ginfo = dhenzaSelf.getGroup(msg.to)
                                       msgs = "Status : [ ✔ ]\nDi Group : " +str(ginfo.name)
                                  dhenzaSelf.sendMessage(msg.to, "「 Status Protect Join 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                         ginfo = dhenzaSelf.getGroup(msg.to)
                                         msgs = "Status : [ ❌ ]\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect join sudah tidak aktif"
                                    dhenzaSelf.sendMessage(msg.to, "「 Status Protect Join 」\n" + msgs)

                        elif silentk1ller.startswith("protectcancel "):
                           if msg._from in owner or msg._from in admin or msg._from in staff:
                              spl = msg.text.replace('protctcancel ','')
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "Protect cancel sudah aktif"
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = dhenzaSelf.getGroup(msg.to)
                                       msgs = "Status : [ ✔ ]\nDi Group : " +str(ginfo.name)
                                  dhenzaSelf.sendMessage(msg.to, "「 Status Protect Cancel 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = dhenzaSelf.getGroup(msg.to)
                                         msgs = "Status : [ ❌ ]\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect cancel sudah tidak aktif"
                                    dhenzaSelf.sendMessage(msg.to, "「 Status Protect Cancel 」\n" + msgs)

                        elif silentk1ller.startswith("protectinvite "):
                           if msg._from in owner or msg._from in admin or msg._from in staff:
                              spl = msg.text.replace('protectinvite ','')
                              if spl == 'on':
                                  if msg.to in protectinvite:
                                       msgs = "Protect invite sudah aktif"
                                  else:
                                       protectinvite.append(msg.to)
                                       ginfo = dhenzaSelf.getGroup(msg.to)
                                       msgs = "Status : [ ✔ ]\nDi Group : " +str(ginfo.name)
                                  dhenzaSelf.sendMessage(msg.to, "「 Status Protect Invite 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                         ginfo = dhenzaSelf.getGroup(msg.to)
                                         msgs = "Status : [ ❌ ]\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect invite sudah tidak aktif"
                                    dhenzaSelf.sendMessage(msg.to, "「 Status Protect Invite 」\n" + msgs)
                                    
      
                        elif silentk1ller.startswith("allpro "):
                           if msg._from in owner or msg._from in admin or msg._from in staff:
                              spl = msg.text.replace('allpro ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectjoin:
                                      msgs = ""
                                  else:
                                      protectjoin.append(msg.to)
                                  if msg.to in protectinvite:
                                      msgs = ""
                                  else:
                                      protectinvite.append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = dhenzaSelf.getGroup(msg.to)
                                      msgs = "Status : [ ✔ ]\nDi Group : " +str(ginfo.name)
                                      msgs += "\nSemua protecttion sudah diaktifkan"
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = dhenzaSelf.getGroup(msg.to)
                                      msgs = "Status : [ ✔ ]\nDi Group : " +str(ginfo.name)
                                      msgs += "\nSemua protection diaktifkan"
                                  dhenzaSelf.sendMessage(msg.to, "「 Status Protection 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                    else:
                                         msgs = ""                               
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = dhenzaSelf.getGroup(msg.to)
                                         msgs = "Status : [ ❌ ]\nDi Group : " +str(ginfo.name)
                                         msgs += "\nSemua protection sudah dimatikan"
                                    else:
                                         ginfo = dhenzaSelf.getGroup(msg.to)
                                         msgs = "Status : [ ❌ ]\nDi Group : " +str(ginfo.name)
                                         msgs += "\nSemua protection dimatikan"
                                    dhenzaSelf.sendMessage(msg.to, "「 Status Protection 」\n" + msgs)
                              
                        
#==================================================                                
                        elif msg.contentType == 2:
                            if settings["changeDual"] == True:
                                def cvp():
                                    dhenzaSelf.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/cvp.mp4")
                                    dhenzaSelf.sendReplyMessage(msg.id, to,"Send Pict :)")
                                td = Thread(target=cvp)
                                td.daemon = True
                                td.start()

                        elif msg.contentType == 1:
                            if settings["changeDual"] == True:
                                def change():
                                    pict = dhenzaSelf.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-cpp.bin".format(time.time()))
                                    settings["changeDual"] = False
                                    dhenzaSelf.updateVideoAndPictureProfile(pict, "LineAPI/tmp/cvp.mp4")
                                    dhenzaSelf.sendReplyMessage(msg.id, to,"Succesfully change video & picture profile")
                                    dhenzaSelf.deleteFile(pict)
                                    dhenzaSelf.deleteFile("LineAPI/tmp/cvp.mp4")
                                td = Thread(target=change)
                                td.daemon = True
                                td.start()
                            
                            if msg.toType == 2 or msg.toType == 1 or msg.toType == 0:
                              if msg._from in dhenzaMid or msg._from in admin or msg._from in owner:
                                if settings["addImage"]["status"] == True:
                                    path = dhenzaSelf.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-add.bin".format(str(settings["addImage"]["name"])))
                                    images[settings["addImage"]["name"]] = {"IMAGE":str(path)}
                                    f = codecs.open("image.json","w","utf-8")
                                    json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    dhenzaSelf.sendMessage(msg.to, "Succesfully add Image With Keyword {}".format(str(settings["addImage"]["name"])))
                                    settings["addImage"]["status"] = False                
                                    settings["addImage"]["name"] = ""
                             
                            if msg.toType == 2 or msg.toType == 1 or msg.toType == 0:
                                if settings["changePictureProfile"] == True:
                                    path = dhenzaSelf.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-cpp.bin".format(time.time()))
                                    settings["changePictureProfile"] = False
                                    dhenzaSelf.updateProfilePicture(path)
                                    dhenzaSelf.sendReplyMessage(msg.id, to,"Berhasil mengubah foto profile")
                                    dhenzaSelf.deleteFile(path)
                            if msg.toType == 2 or msg.toType == 1 or msg.toType == 0:
                                if to in settings["changeGroupPicture"]:
                                    path = dhenzaSelf.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-cgp.bin".format(time.time()))
                                    settings["changeGroupPicture"].remove(to)
                                    dhenzaSelf.updateGroupPicture(to, path)
                                    dhenzaSelf.sendReplyMessage(msg.id, to,"Berhasil mengubah foto group")
                                    dhenzaSelf.deleteFile(path)
                            if msg.toType == 2:
                                if settings["changeCover"] == True:
                                    path = dhenzaSelf.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-cv.bin".format(time.time()))
                                    settings["changeCover"] = False
                                    dhenzaSelf.updateProfileCover(path)
                                    dhenzaSelf.sendReplyMessage(msg.id, to,"Berhasil mengubah cover profile")
                                    dhenzaSelf.deleteFile(path)
                        elif msg.contentType == 2:
                            if settings["changeVpProfile"] == True:
                                path = dhenzaSelf.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-cvp.mp4".format(time.time()))
                                settings["changeVpProfile"] = False
                                changeVideoAndPictureProfile(path)
                                dhenzaSelf.sendReplyMessage(msg.id, to,"Berhasil mengubah video profile")
                                dhenzaSelf.deleteFile(path)
            except Exception as error:
                logError(error)
    except Exception as error:
        logError(error)
#======================================================
        
#============================================
def runningProgram():
    while True:
        try:
            ops = dhenzaPoll.singleTrace(count=50)
        except TalkException as talk_error:
            logError(talk_error)
            if talk_error.code in [7, 8, 20]:
                sys.exit(1)
            continue
        except KeyboardInterrupt:
            sys.exit('[ SYSTEM MESSAGE : *KEYBOARD INTERRUPT.')
        except Exception as error:
            logError(error)
            continue
        if ops:
            for op in ops:
                dhenzaBot(op)
                dhenzaPoll.setRevision(op.revision)

if __name__ == '__main__':
    print (' [•] SYSTEM MESSAGE : *BOT BERHASIL DI INSTALL\n______________________________\n')
    print (' \n*klik my chanel https://youtube.com/@silentkillerofficial4992\n______________________________\n')
    runningProgram()