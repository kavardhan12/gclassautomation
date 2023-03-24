from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime
from selenium.webdriver.chrome.options import Options



now = datetime.datetime.now()
current_time = now.strftime("%H:%M")
current_day = now.strftime("%A")
print("Current Time-->",current_time)
print(current_day)




opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument('--start-maximized')
opt.add_experimental_option("prefs", { \
 
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 0,
    "profile.default_content_setting_values.notifications": 1
})

def login(mlink):
        driver=webdriver.Chrome(chrome_options=opt, executable_path='C:\Program Files (x86)\chromedriver.exe')
        driver.get(mlink)
        time.sleep(10)
        username=driver.find_element_by_id('identifierId')
        username.send_keys("kandadai21_ug@ece.nits.ac.in")
        username.send_keys(Keys.RETURN)
        time.sleep(3)
        password=driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        password.send_keys("kav12kandadai")
        password.send_keys(Keys.RETURN)
        time.sleep(5000)    
        driver.quit()   





def monday():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    timediff=60-(now.minute)
    rtimediff=(now.minute)-60


    if (now.hour==7 and timediff <=30) or (now.hour==8 and rtimediff<=-30) :
        mlink='https://meet.google.com/vpa-nhos-qcg?authuser=0'   
        print("Joining ENGLISH Class.......")
        login(mlink)

    if (now.hour==8 and timediff <=30) or (now.hour==9 and rtimediff<=-30):
        mlink='https://meet.google.com/hzw-igen-fhy?authuser=0'  
        print("Joining Physics Class.....")
        login(mlink)    


    if (now.hour==10 and timediff <=30) or (now.hour==11 and rtimediff<=-30) :
        mlink='https://meet.google.com/uoy-qxkm-esf?authuser=0'
        print("Joining BasicEE Class.....")
        login(mlink)


    if (now.hour==13 and timediff <=30) or ((now.hour==14 and rtimediff<=-30)):
        mlink='https://meet.google.com/gkp-drof-vro?authuser=0'
        print("Joining ENGLISH(Lab)........")
        login(mlink)
        
    else:        
        print("Current Time-->",current_time)
        print(current_day)
        print("Searching for Classes........")
        time.sleep(3)
        print("<<<<<NO CLASS NOW>>>>>")
        time.sleep(20)


def tuesday():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    timediff=60-(now.minute)
    rtimediff=(now.minute)-60


    if (now.hour==8 and timediff <=30) or (now.hour==9 and rtimediff<=-30):
        mlink='https://meet.google.com/yyg-hazr-jnk?authuser=0'    
        print("Joining MATHS Class.......")
        login(mlink)

    if (now.hour==10 and timediff <=30) or (now.hour==11 and rtimediff<=-30):
        mlink='https://meet.google.com/uoy-qxkm-esf?authuser=0'  
        print("Joining BasicEE Class.....")
        login(mlink)


    if (now.hour==12 and timediff <=30) or (now.hour==13 and rtimediff<=-30):
        mlink='https://meet.google.com/yyg-hazr-jnk?authuser=0'
        print("Joining MATHS(I1) Tut.....")
        login(mlink)


    if (now.hour==13 and timediff <=30) or (now.hour==14 and rtimediff<=-30):
        mlink='https://meet.google.com/uoy-qxkm-esf?authuser=0'
        print("Joining BasicEE(I1) Tut........")
        login(mlink)


    if (now.hour==14 and timediff <=30) or (now.hour==15 and rtimediff<=-30):
        mlink='https://meet.google.com/vpa-nhos-qcg?authuser=0'
        print("Joining ENGLISH Class........")
        login(mlink)    
    else:
        
        print("Current Time-->",current_time)
        print(current_day)
        print("Searching for Classes........")
        time.sleep(3)
        print("<<<<<NO CLASS NOW>>>>>")
        time.sleep(20)


def wednesday():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    timediff=60-(now.minute)
    rtimediff=(now.minute)-60


    if (now.hour==8 and timediff <=30) or (now.hour==9 and rtimediff<=-30):
        mlink='https://meet.google.com/hzw-igen-fhy?authuser=0'    
        print("Joining PHYSICS Class.......")
        login(mlink)

    if (now.hour==9 and timediff <=30) or (now.hour==10 and rtimediff<=-30):
        mlink='https://meet.google.com/yyg-hazr-jnk?authuser=0'    
        print("Joining MATHS Class.......")
        login(mlink)


    if (now.hour==12 and timediff <=30) or (now.hour==13 and rtimediff<=-30):
        mlink='https://meet.google.com/hzw-igen-fhy?authuser=0'
        print("Joining PHYSICS(I2) Tut.....")
        login(mlink)


    if (now.hour==13 and timediff <=30) or (now.hour==14 and rtimediff<=-30):
        mlink='https://meet.google.com/wwm-ezzw-rmb?authuser=0'
        print("Joining PHYSICS(Lab)........")
        login(mlink)
    else:
         
         print("Current Time-->",current_time)
         print(current_day)
         print("Searching for Classes........")
         time.sleep(3)
         print("<<<<<NO CLASS NOW>>>>>")
         time.sleep(20)


def thursday():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    timediff=60-(now.minute)
    rtimediff=(now.minute)-60


    if (now.hour==8 and timediff <=30) or (now.hour==9 and rtimediff<=-30):
        mlink='https://meet.google.com/yyg-hazr-jnk?authuser=0'    
        print("Joining MATHS Class.......")
        login(mlink)

    if (now.hour==9 and timediff <=30) or (now.hour==10 and rtimediff<=-30):
        mlink='https://meet.google.com/uoy-qxkm-esf?authuser=0'  
        print("Joining BasicEE Class.....")
        login(mlink)


    if (now.hour==10 and timediff <=30) or (now.hour==11 and rtimediff<=-30):
        mlink='https://meet.google.com/yjv-nooq-qmb?authuser=0'
        print("Joining EDG Class.....")
        login(mlink)


    if (now.hour==13 and timediff <=30) or (now.hour==14 and rtimediff<=-30):
        mlink='https://meet.google.com/yjv-nooq-qmb?authuser=0'
        print("Joining EDG(Lab)........")
        login(mlink)
    else:
        
        print("Current Time-->",current_time)
        print(current_day)
        print("Searching for Classes........")
        time.sleep(3)
        print("<<<<<NO CLASS NOW>>>>>")
        time.sleep(20)

def friday():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    timediff=60-(now.minute)
    rtimediff=(now.minute)-60


    if (now.hour==7 and timediff <=30) or (now.hour==8 and rtimediff<=-30):
       mlink='https://meet.google.com/uoy-qxkm-esf?authuser=0'    
       print("Joining BasicEE(I2) Tut.......")
       login(mlink)

    if (now.hour==8 and timediff <=30) or (now.hour==9 and rtimediff<=-30):
        mlink='https://meet.google.com/yyg-hazr-jnk?authuser=0'  
        print("Joining MATHS(I2) Tut.....")
        login(mlink)


    if (now.hour==9 and timediff <=30) or (now.hour==10 and rtimediff<=-30):
        mlink='https://meet.google.com/hzw-igen-fhy?authuser=0'
        print("Joining PHYSICS Class.....")
        login(mlink)


    if (now.hour==12 and timediff <=30) or (now.hour==13 and rtimediff<=-30):
        mlink='https://meet.google.com/vpa-nhos-qcg?authuser=0'
        print("Joining ENGLISH Class........")
        login(mlink)

    if (now.hour==13 and timediff <=30) or (now.hour==14 and rtimediff<=-30):
        mlink='https://meet.google.com/wwm-ezzw-rmb?authuser=0'
        print("Joining BasicEE Lab........")
        login(mlink)    
    else:
        
        print("Current Time-->",current_time)
        print(current_day)
        print("Searching for Classes........")
        time.sleep(3)
        print("<<<<<NO CLASS NOW>>>>>")
        time.sleep(20) 

        

while True:

    if current_day=="Monday":
     monday()
    elif current_day=="Tuesday":
     tuesday()
    elif current_day=="Wednesday":
     wednesday()
    elif current_day=="Thursday":
     thursday()
    elif current_day=="Friday":
     friday() 
    else:
     print("------>>>>Hurreeey its weekend<<<<------") 
     break



                    





        
    
    







