from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
import random
from selenium.common.exceptions import NoSuchElementException
from GoogleAPI import ConnectToAPI #Function I created to grab data from my Google Sheets through the use of an API
import datetime, time
from datetime import timedelta
from datetime import datetime

#Xpaths Below

CalmDown = [7, 1, 3, 2, 5, 3, 2] #Slowing Down the Refresh Rate; Was 1, 3, 2, 5, 3, 2
xpath_of_comment_section = "//div/form[*[local-name()='textarea']]" 
CaptionXpath = "//div[3]/div[1]/div/div[1]/div/span[2][*[local-name()='span']]"
BlogNameXpath = "//div/span[1][*[local-name()='a']]"
Post = "//div/form/button[contains(text(),'Post')]"

print ('Go to @accs_to_f0llow and follow who that account follows for best performance of this bot.')

#What the bot looks for on the first post on its timeline so it knows if to comment or not
RecentPost = ['1 SECONDS AGO', '2 SECONDS AGO', '3 SECONDS AGO', '4 SECONDS AGO', '5 SECONDS AGO', '6 SECONDS AGO', '7 SECONDS AGO', '8 SECONDS AGO', '9 SECONDS AGO']

#---------------------- Below Connects to a Spread Sheet on Google's API that Has a List of Comments---------
Login = []
RandomComments = []
Boosie = []
Six9 = []
NBAYoungBoy = []
PopSmoke = []
MeekMill = []
NLEChoppa = []
DonaldTrump = []
KanyeWest = []
Drake = []
LilUzi = []
LilBaby = []
Future = []
JuiceW = []
DaBaby = []
Megan = []
Gunna = []
YoungThug = []
GHerbo = []
NickiMinaj = []
TI = []
FifCent = []
theshaderoom = []
CardiB = []
domislivenews = []
four2dug = []
Takeoff = []
Beirut = []
Coronavirus = []
Snapchat = [' snapchat plugin belongs here']
Instagram = ['instagram plugin belongs here']
FBGDuck = []
RichTheKid = []
FamousDex = []
YBAcc = []
Six9ineAcc = []
KylieJennerAcc = []
cnnacc = []
LilBabyacc = []
KingVonacc = []
LilReeseAcc = []
KimKAcc = []
MoneyBagYoAcc = []
Fivio = []
MeganAcc = []
WillSmithAcc = []
TrippieRedd = []
lilyatchy = []
torylanes = []
ABoogie = []
NickCannon = []
Stunna4Vegas = []
iamcardibAcc = []
OffsetAcc = []
Akon = []
DojaCatAcc = []
YBN = []
daquanAcc = []
Nipsey = []
Quando = []
LilReese = []
PNBRock = []
TravisScott = []
LilPump = []
KodakBlack = []
ChiefKeef = []
Statistic = [] #Comments related to Political Issues
ShaunKingacc = []
LilDurk = []
SmokePurp = []
Tupac = []
AsianDoll = []
YFNLucci = []
Blueface = []
Breezy600 = []
AdrBroner = []
CelinaPowell = []
Plies = []
PoloG = []
LilWayne = []
LilTjay = []
Savage21 = []
Diddy =[]
PoppHunna = []
Vaccine = []
vladtv =[]
BobbyShmurda=[]
RoddyRich =[]
PoohShiesty = []
Druski = []
BhadBhabie = []
YoungDolph = []
Charlamagne = []
Southside = []
DMX = []

print ('Connecting to Google API to Extract Comments')
ConnectToAPI('A', RandomComments)
ConnectToAPI('B', Boosie)
ConnectToAPI('C', Six9)
ConnectToAPI('D', NBAYoungBoy)
ConnectToAPI('E', PopSmoke)
ConnectToAPI('F', MeekMill)
ConnectToAPI('G', NLEChoppa)
ConnectToAPI('H', DonaldTrump)
ConnectToAPI('I', KanyeWest)
ConnectToAPI('J', Drake)
ConnectToAPI('K', Login)
ConnectToAPI('L', LilUzi)
ConnectToAPI('M', LilBaby)
ConnectToAPI('N', Future)
ConnectToAPI('O', JuiceW)
ConnectToAPI('P', DaBaby)
ConnectToAPI('Q', Megan)
ConnectToAPI('R', Gunna)
ConnectToAPI('S', YoungThug)
ConnectToAPI('T', GHerbo)
ConnectToAPI('U', NickiMinaj)
ConnectToAPI('V', TI)
ConnectToAPI('W', FifCent)
ConnectToAPI('X', theshaderoom)
ConnectToAPI('Y', CardiB)
ConnectToAPI('Z', domislivenews)
ConnectToAPI('AA', four2dug)
ConnectToAPI('AB', Takeoff)
ConnectToAPI('AC', Beirut)
ConnectToAPI('AD', Coronavirus)
ConnectToAPI('AE', FBGDuck)
ConnectToAPI('AF', RichTheKid)
ConnectToAPI('AG', FamousDex)
ConnectToAPI('AH', YBAcc)
ConnectToAPI('AI', Six9ineAcc)
ConnectToAPI('AJ', KylieJennerAcc)
ConnectToAPI('AK', cnnacc)
ConnectToAPI('AL', LilBabyacc)
ConnectToAPI('AM', KingVonacc)
ConnectToAPI('AN', LilReeseAcc)
ConnectToAPI('AO', KimKAcc)
ConnectToAPI('AP', MoneyBagYoAcc)
ConnectToAPI('AQ', Fivio)
ConnectToAPI('AR', MeganAcc)
ConnectToAPI('AS', WillSmithAcc)
ConnectToAPI('AT', TrippieRedd)
ConnectToAPI('AU', lilyatchy)
ConnectToAPI('AV', torylanes)
ConnectToAPI('AW', ABoogie)
ConnectToAPI('AX', NickCannon)
ConnectToAPI('AY', Stunna4Vegas)
ConnectToAPI('AZ', iamcardibAcc)
ConnectToAPI('BA', OffsetAcc)
ConnectToAPI('BB', Akon)
ConnectToAPI('BC', DojaCatAcc)
print ('Pausing for 101 Seconds... Then will continue to Pull data from the Google API')
sleep(101)
ConnectToAPI('BD', YBN)
ConnectToAPI('BE', daquanAcc)
ConnectToAPI('BF', Nipsey)
ConnectToAPI('BG', Quando)
ConnectToAPI('BH', LilReese)
ConnectToAPI('BI', PNBRock)
ConnectToAPI('BJ', TravisScott)
ConnectToAPI('BK', LilPump)
ConnectToAPI('BL', KodakBlack)
ConnectToAPI('BM', ChiefKeef)
ConnectToAPI('BN', Statistic)
ConnectToAPI('BO', ShaunKingacc)
ConnectToAPI('BP', LilDurk)
ConnectToAPI('BQ', SmokePurp)
ConnectToAPI('BR', Tupac)
ConnectToAPI('BS', AsianDoll)
ConnectToAPI('BT', YFNLucci)
ConnectToAPI('BU', Blueface)
ConnectToAPI('BV', Breezy600)
ConnectToAPI('BW', AdrBroner)
ConnectToAPI('BX', CelinaPowell)
ConnectToAPI('BY', Plies)
ConnectToAPI('BZ', PoloG)
ConnectToAPI('CA', LilWayne)
ConnectToAPI('CB', LilTjay)
ConnectToAPI('CC', Savage21)
ConnectToAPI('CD', Diddy)
ConnectToAPI('CE', PoppHunna)
ConnectToAPI('CF', Vaccine)
ConnectToAPI('CG', vladtv)
ConnectToAPI('CH', BobbyShmurda)
ConnectToAPI('CI', RoddyRich)
ConnectToAPI('CJ', PoohShiesty)
ConnectToAPI('CK', Druski)
ConnectToAPI('CL', BhadBhabie)
ConnectToAPI('CM', YoungDolph)
ConnectToAPI('CN', Charlamagne)
ConnectToAPI('CO', YoungDolph)
ConnectToAPI('CP', Charlamagne)





#Cleaning the list from any None values.
RandomComments = list(filter(None, RandomComments))
Boosie = list(filter(None, Boosie))
Six9 = list(filter(None, Six9))
NBAYoungBoy = list(filter(None, NBAYoungBoy))
PopSmoke = list(filter(None, PopSmoke))
MeekMill = list(filter(None, MeekMill))
NLEChoppa = list(filter(None, NLEChoppa))
DonaldTrump = list(filter(None, DonaldTrump))
KanyeWest = list(filter(None, KanyeWest))
Drake = list(filter(None, Drake))
#Login = list(filter(None, Login))
LilUzi = list(filter(None, LilUzi))
LilBaby = list(filter(None, LilBaby))
Future = list(filter(None, Future))
JuiceW = list(filter(None, JuiceW))
DaBaby = list(filter(None, DaBaby))
Megan = list(filter(None, Megan))
Gunna = list(filter(None, Gunna))
YoungThug = list(filter(None, YoungThug))
GHerbo = list(filter(None, GHerbo))
NickiMinaj = list(filter(None, NickiMinaj))
TI = list(filter(None, TI))
FifCent = list(filter(None, FifCent))
theshaderoom = list(filter(None, theshaderoom))
CardiB = list(filter(None, CardiB))
domislivenews = list(filter(None, domislivenews))
four2dug = list(filter(None, four2dug))
Takeoff = list(filter(None, Takeoff))
Beirut = list(filter(None, Beirut))
Coronavirus = list(filter(None, Coronavirus))
FBGDuck = list(filter(None, FBGDuck))
RichTheKid = list(filter(None, RichTheKid))
FamousDex = list(filter(None, FamousDex))
YBAcc = list(filter(None, YBAcc))
Six9ineAcc = list(filter(None, Six9ineAcc))
KylieJennerAcc = list(filter(None, KylieJennerAcc))
cnnacc = list(filter(None, cnnacc))
LilBabyacc = list(filter(None, LilBabyacc))
KingVonacc = list(filter(None, KingVonacc))
LilReeseAcc = list(filter(None, LilReeseAcc))
KimKAcc = list(filter(None, KimKAcc))
MoneyBagYoAcc = list(filter(None, MoneyBagYoAcc))
Fivio = list(filter(None, Fivio))
MeganAcc = list(filter(None, MeganAcc))
WillSmithAcc = list(filter(None, WillSmithAcc))
TrippieRedd = list(filter(None, TrippieRedd))
lilyatchy = list(filter(None, lilyatchy))
torylanes = list(filter(None, torylanes))
ABoogie = list(filter(None, ABoogie))
NickCannon = list(filter(None, NickCannon))
Stunna4Vegas = list(filter(None, Stunna4Vegas))
iamcardibAcc = list(filter(None, iamcardibAcc))
OffsetAcc = list(filter(None, OffsetAcc))
Akon = list(filter(None, Akon))
DojaCatAcc = list(filter(None, DojaCatAcc))
YBN = list(filter(None, YBN))
daquanAcc = list(filter(None, daquanAcc))
Nipsey = list(filter(None, Nipsey))
Quando = list(filter(None, Quando))
LilReese = list(filter(None, LilReese))
PNBRock = list(filter(None, PNBRock))
TravisScott = list(filter(None, TravisScott))
LilPump = list(filter(None, LilPump))
KodakBlack = list(filter(None, KodakBlack))
ChiefKeef = list(filter(None, ChiefKeef))
Statistic = list(filter(None, Statistic))
ShaunKingacc = list(filter(None, ShaunKingacc))
LilDurk = list(filter(None, LilDurk))
SmokePurp = list(filter(None, SmokePurp))
Tupac = list(filter(None, Tupac))
AsianDoll = list(filter(None, AsianDoll))
YFNLucci = list(filter(None, YFNLucci))
Blueface = list(filter(None, Blueface))
Breezy600 = list(filter(None, Breezy600))
AdrBroner = list(filter(None, AdrBroner))
CelinaPowell = list(filter(None, CelinaPowell))
Plies = list(filter(None, Plies))
PoloG = list(filter(None, PoloG))
LilWayne = list(filter(None, LilWayne))
LilTjay = list(filter(None, LilTjay))
Savage21= list(filter(None, Savage21))
Diddy = list(filter(None, Diddy))
PoppHunna= list(filter(None, PoppHunna))
Vaccine = list(filter(None, Vaccine))
vladtv= list(filter(None, vladtv))
BobbyShmurda= list(filter(None, BobbyShmurda))
RoddyRich= list(filter(None, RoddyRich))
PoohShiesty = list(filter(None, PoohShiesty))
Druski= list(filter(None, Druski))
BhadBhabie = list(filter(None, BhadBhabie))
YoungDolph= list(filter(None, YoungDolph))
Charlamagne= list(filter(None, Charlamagne))
Southside= list(filter(None, Southside))
DMX= list(filter(None, DMX))

def veonslogin(username, password):
    driver.execute_script("window.open('https://login.veonpanel.com/account/login');")
    #Opens new tab with the URL included; Opens Tab for Veons Panel
    driver.implicitly_wait(20)
    windows = driver.window_handles
    #A List of handles for both window tabs
    driver.switch_to.window(windows[1])
    print ('Switched to',driver.title)
    #The code above allows the program to switch between tabs
    driver.find_element_by_name('username').send_keys(username)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_name('submit').click()
    driver.get('https://login.veonpanel.com/p/comment-likes')
    driver.implicitly_wait(20)
    driver.switch_to.window(windows[0])
    print ('Switched Back to',driver.title)



#------------------------------------------Browser Opens and Starts Below

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.instagram.com/')
driver.implicitly_wait(10)
sleep(2)

if Login[4] == 'no' or Login[4] == 'No' or Login[4] == None: #If no account is made on Veon's Panel is made or put in the excel sheet, it runs without the comment likes
    print ('Running without Comment Likes...')
else: #If account is made and info is provided, it logs into veon's panel real quick then switches back to instagram
    veonslogin(Login[4], Login[5]) #Will login with login credentials extracted from the Login(k) from the Excel Sheet
#Username = 'xxxxxxxx'
#Password = 'xxxxxxxx'
driver.find_element_by_name('username').send_keys(Login[0]) #Login[0]
driver.find_element_by_name('password').send_keys(Login[1]) #Login[1]
LoginButton = "//button[@type='submit']"
sleep(2)
driver.find_element_by_xpath(LoginButton).submit()
sleep(1)
#Logs into Instagram
'''
if driver.current_url != 
Add if link = instagram/reactivated then driver.refresh()
'''
'''Load = 0
while Load == 0:
    if driver.current_url != 'https://www.instagram.com/#reactivated':
        sleep(1)
    else:
        driver.refresh()
        print ('Link Changed')
        Load = Load + 2'''
print ('Logged In')

#------------------------ATTENTION

NotNow = "//button[contains(text(),'Not Now')]"
driver.find_element_by_xpath(NotNow).click()
#Clicks Pop Up
print ('Close Pop Up')

NotNow = "//button[contains(text(),'Not Now')]"
try:
    driver.find_element_by_xpath(NotNow).click()
    #Clicks Pop Up
    print ('Close Pop Up')
except NoSuchElementException:
    print ('No Pop Up was Found.')


    #----------------------------------- #Comment Likes Function Using Veons Panel
def veonspanel(user, postlink):
    driver.switch_to.window(driver.window_handles[1])
    print ('Switched to',driver.title)
    driver.implicitly_wait(20)
    driver.find_element_by_name('url').send_keys(postlink)
    driver.find_element_by_name('username').send_keys(user)
    driver.find_element_by_name('total').send_keys('123')
    driver.find_element_by_name('submit').submit()
    wait = WebDriverWait(driver, 15)
    element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="salsakp8"]/div'))) #This results in an error, next time record the data
    LikeResults = driver.find_element_by_xpath('//*[@id="salsakp8"]/div')
    if 'Success' in (LikeResults.text):
        print ('Comments Likes Being Sent...')
        #current_time = f'{datetime.now():%H:%M:%S%z}' #Prints the current hour, min and second of day
        #8 minutes if not do 9 min 40 seconds
    else:
        print ('Comment Likes Panel is still on Cool Down Mode.')
        #If LikeResults.text == success we will record current time of day, and make it so this function cant be used until after 7 - 10 minute limit
    driver.switch_to.window(driver.window_handles[0])
    print ('Switched Back to',driver.title)
    #make an if statement with veonspanel, if exceet sheet has yes or no, make veonspanel function the code above or make veonspanel function empty code

#------------------------------------------------------------

def LeavingComments(comment):
    LeaveComment = driver.find_element_by_xpath(xpath_of_comment_section)
    LeaveComment.click()
    LeaveComment2 = driver.find_element_by_tag_name('textarea')
    LeaveComment2.send_keys(comment)#, Snapchat[0])
    Post2 = driver.find_element_by_xpath(Post).click()
    print ('Under: ', (BlogName.text))
    print ('Comment Left: ', comment)

#------------------------------------------------------------


#NewPost = []




while True:
    print ('Refreshing Timeline')
    driver.refresh()


    #This randomizes the list of comments extracted from the spread sheet, from up above
    temp = list(zip(Boosie, Six9, NBAYoungBoy, PopSmoke, MeekMill, NLEChoppa,
                    DonaldTrump, KanyeWest, Drake))
    random.shuffle(temp)
    random.shuffle(CalmDown)
    random.shuffle(RandomComments)
    Boosie2, Six9ine, NBAYoungBoy2, PopSmoke2, MeekMill2, NLEChoppa2, DonaldTrump2, KanyeWest2, Drake2 = zip(*temp)
    random.shuffle(LilUzi)
    random.shuffle(LilBaby)
    random.shuffle(Future)
    random.shuffle(JuiceW)
    random.shuffle(DaBaby)
    random.shuffle(Megan)
    random.shuffle(Gunna)
    random.shuffle(YoungThug)
    random.shuffle(GHerbo)
    random.shuffle(NickiMinaj)
    random.shuffle(TI)
    random.shuffle(FifCent)
    random.shuffle(theshaderoom)
    random.shuffle(CardiB)
    random.shuffle(domislivenews)
    random.shuffle(four2dug)
    random.shuffle(Takeoff)
    random.shuffle(Beirut)
    random.shuffle(Coronavirus)
    random.shuffle(Snapchat)
    random.shuffle(FBGDuck)
    random.shuffle(RichTheKid)
    random.shuffle(FamousDex)
    random.shuffle(YBAcc)
    random.shuffle(Six9ineAcc)
    random.shuffle(KylieJennerAcc)
    random.shuffle(cnnacc)
    random.shuffle(LilBabyacc)
    random.shuffle(KingVonacc)
    random.shuffle(LilReeseAcc)
    random.shuffle(KimKAcc)
    random.shuffle(MoneyBagYoAcc)
    random.shuffle(Fivio)
    random.shuffle(MeganAcc)
    random.shuffle(WillSmithAcc)
    random.shuffle(TrippieRedd)
    random.shuffle(lilyatchy)
    random.shuffle(torylanes)
    random.shuffle(ABoogie)
    random.shuffle(NickCannon)
    random.shuffle(Stunna4Vegas)
    random.shuffle(iamcardibAcc)
    random.shuffle(OffsetAcc)
    random.shuffle(Akon)
    random.shuffle(DojaCatAcc)
    random.shuffle(YBN)
    random.shuffle(daquanAcc)
    random.shuffle(Nipsey)
    random.shuffle(Quando)
    random.shuffle(LilReese)
    random.shuffle(Instagram)
    random.shuffle(PNBRock)
    random.shuffle(TravisScott)
    random.shuffle(LilPump)
    random.shuffle(KodakBlack)
    random.shuffle(ChiefKeef)
    random.shuffle(Statistic)
    random.shuffle(ShaunKingacc)
    random.shuffle(LilDurk)
    random.shuffle(SmokePurp)
    random.shuffle(Tupac)
    random.shuffle(AsianDoll)
    random.shuffle(YFNLucci)
    random.shuffle(Blueface)
    random.shuffle(Breezy600)
    random.shuffle(AdrBroner)
    random.shuffle(Plies)
    random.shuffle(CelinaPowell)
    random.shuffle(PoloG)
    random.shuffle(LilWayne)
    random.shuffle(LilTjay)
    random.shuffle(Savage21)
    random.shuffle(Diddy)
    random.shuffle(PoppHunna)
    random.shuffle(Vaccine)
    random.shuffle(vladtv)
    random.shuffle(BobbyShmurda)
    random.shuffle(RoddyRich)
    random.shuffle(PoohShiesty)
    random.shuffle(Druski)
    random.shuffle(BhadBhabie)
    random.shuffle(YoungDolph)
    random.shuffle(Charlamagne)
    random.shuffle(Southside)
    random.shuffle(DMX)
    


    try: #Incase connection is ever lost while running the bot
        PostCaption = driver.find_element_by_xpath(CaptionXpath) #Xpath for the caption of our current post
    except NoSuchElementException:
        print ('Error Webpage; Refreshing')
        driver.refresh()

    LinkHolder = 0

    def LinkExtraction(postlink):
        postlink = driver.find_element_by_xpath("//article[1]/div[3]/div[2]/a").get_attribute('href')
        #Correct xpath: "//article[1]/div[3]/div[1]/div/div[2]/div[1]/a"
        #
        return (postlink)

    def veonrefresh(): #Function made to refresh the comment like tab so it doesnt expire and log out after sitting idle
        driver.switch_to.window(driver.window_handles[1])
        driver.refresh()
        driver.switch_to.window(driver.window_handles[0])


    if Login[4] == 'no' or Login[4] == 'No' or Login[4] == None: #Incase their is no longer a veonpanel account, all functions will have no worth
        def LinkExtraction(postlink):#                            and will be re-defined. Things will run normal without comment likes tab
            return 0;
        def veonspanel(user, postlink):
            return 0;
        def veonrefresh():
            return 0;
        
    BlogName = driver.find_element_by_xpath(BlogNameXpath)
    Time = driver.find_element_by_xpath("//div[3]/div[2]/a[*[local-name()='time']]") #XPATH for the time of day the Instagram Post was made
    #May need to add a try statement here for NoSuchElementException, if (New Post) becomes an issue
    print ('Last Post Was: ', Time.text)

    #The bot chooses what to comment based on what the caption is about or what the account name is. Comments are pulled from a spread sheet and randomized.
    if (Time.text) in RecentPost:
        if 'Boosie' in (PostCaption.text) or 'boosie' in (PostCaption.text):
            LeavingComments(Boosie2[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0]) #Statistic
        elif 'Blueface' in (PostCaption.text) or 'blueface' in (PostCaption.text) or 'BlueFace' in (PostCaption.text):
            LeavingComments(Blueface[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'Roddy' in (PostCaption.text) or 'roddy' in (PostCaption.text):
            LeavingComments(RoddyRich[0]), LinkExtraction(LinkHolder), veonspanel(Username, LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'Pooh' in (PostCaption.text) or 'pooh' in (PostCaption.text):
            LeavingComments(PoohShiesty[0]), LinkExtraction(LinkHolder), veonspanel(Username, LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'Bhad' in (PostCaption.text) or 'bhad' in (PostCaption.text):
            LeavingComments(BhadBhabie[0]), LinkExtraction(LinkHolder), veonspanel(Username, LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'dolph' in (PostCaption.text) or 'Dolph' in (PostCaption.text):
            LeavingComments(YoungDolph[0]), LinkExtraction(LinkHolder), veonspanel(Username, LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'Charlamagne' in (PostCaption.text) or 'charlamagne' in (PostCaption.text):
            LeavingComments(Charlamagne[0]), LinkExtraction(LinkHolder), veonspanel(Username, LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif '600B' in (PostCaption.text) or '600b' in (PostCaption.text):
            LeavingComments(Breezy600[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'Broner' in (PostCaption.text) or 'broner' in (PostCaption.text):
            LeavingComments(AdrBroner[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'Popp' in (PostCaption.text) or 'popp' in (PostCaption.text):
            LeavingComments(PoppHunna[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'vladtv' in (PostCaption.text) or 'Vladtv' in (PostCaption.text):
            LeavingComments(vladtv[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'vaccine' in (PostCaption.text) or 'Vaccine' in (PostCaption.text):
            LeavingComments(Vaccine[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'Diddy' in (PostCaption.text) or 'diddy' in (PostCaption.text):
            LeavingComments(Diddy[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif '21 Savage' in (PostCaption.text) or '21 savage' in (PostCaption.text) or '21savage' in (PostCaption.text) or '21Savage' in (PostCaption.text):
            LeavingComments(Savage21[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'tjay' in (PostCaption.text) or 'TJay' in (PostCaption.text):
            LeavingComments(LilTjay[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'lilwayne' in (PostCaption.text) or 'LilWayne' in (PostCaption.text) or 'Lil Wayne' in (PostCaption.text) or 'lil wayne' in (PostCaption.text):
            LeavingComments(LilWayne[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'Polo' in (PostCaption.text) or 'polo' in (PostCaption.text):
            LeavingComments(PoloG[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'Powell' in (PostCaption.text) or 'powell' in (PostCaption.text):
            LeavingComments(CelinaPowell[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'YFNLucci' in (PostCaption.text) or 'YFN Lucci' in (PostCaption.text) or 'YFN' in (PostCaption.text)or 'yfn' in (PostCaption.text):
            LeavingComments(YFNLucci[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'asiandoll' in (PostCaption.text) or 'AsianDoll' in (PostCaption.text) or 'Asian Doll' in (PostCaption.text)or 'asiandabrat' in (PostCaption.text):
            LeavingComments(AsianDoll[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'chauvin' in (PostCaption.text) or 'Chauvin' in (PostCaption.text):
            LeavingComments(Statistic[0]), LinkExtraction(LinkHolder), veonspanel(Username, LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'dmx' in (PostCaption.text) or 'DMX' in (PostCaption.text):
            LeavingComments(DMX[0]), LinkExtraction(LinkHolder), veonspanel(Username, LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'Southside' in (PostCaption.text) or 'southside' in (PostCaption.text) or '808mafia' in (PostCaption.text):
            LeavingComments(Southside[0]), LinkExtraction(LinkHolder), veonspanel(Username, LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'kodakblack' == (BlogName.text) or 'KodakBlack' in (PostCaption.text) or 'kodakblack' in (PostCaption.text) or 'kodak' in (PostCaption.text) or 'Kodak' in (PostCaption.text):
            LeavingComments(KodakBlack[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'ChiefKeef' in (PostCaption.text) or 'chiefkeef' in (PostCaption.text) or 'Chief Keef' in (PostCaption.text) or 'chief keef' in (PostCaption.text)or 'sosa' in (PostCaption.text) or 'Sosa' in (PostCaption.text):
            LeavingComments(ChiefKeef[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'lilpump' in (PostCaption.text) or 'LilPump' in (PostCaption.text) or 'lil pump' in (PostCaption.text) or 'Lil Pump' in (PostCaption.text):
            LeavingComments(LilPump[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'Travis' in (PostCaption.text) or 'travis' in (PostCaption.text) or 'TRAVIS' in (PostCaption.text):
            LeavingComments(TravisScott[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'PNB' in (PostCaption.text) or 'pnb' in (PostCaption.text):
            LeavingComments(PNBRock[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif '69' in (PostCaption.text) or '6ix9ine' in (PostCaption.text) or 'Tekashi' in (PostCaption.text) or 'tekashi' in (PostCaption.text):
            LeavingComments(Six9ine[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'Nipsey' in (PostCaption.text) or 'nipsey' in (PostCaption.text) or 'NIPSEY' in (PostCaption.text):
            LeavingComments(Nipsey[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'NBAYoungboy' in (PostCaption.text) or 'NBA Youngboy' in (PostCaption.text) or 'NBAYoungBoy' in (PostCaption.text) or 'NBA YoungBoy' in (PostCaption.text)  or 'nbayoungboy' in (PostCaption.text)  or 'youngboy' in (PostCaption.text):
            LeavingComments(NBAYoungBoy2[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'PopSmoke' in (PostCaption.text) or 'Pop Smoke' in (PostCaption.text) or 'popsmoke' in (PostCaption.text):
            LeavingComments(PopSmoke2[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'Meek' in (PostCaption.text) or 'meek' in (PostCaption.text) or 'meekmill' == (BlogName.text):
            LeavingComments(MeekMill2[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'NLE Choppa' in (PostCaption.text) or 'NLEChoppa' in (PostCaption.text)or '#nlech' in (PostCaption.text):
            LeavingComments(NLEChoppa2[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'Trump' in (PostCaption.text) or 'DonaldTrump' in (PostCaption.text):
            LeavingComments(DonaldTrump2[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'Kanye' in (PostCaption.text) or 'kanye' in (PostCaption.text):
            LeavingComments(KanyeWest2[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'Drake' in (PostCaption.text) or 'drake' in (PostCaption.text) or '@champagnepapi' in (PostCaption.text):
            LeavingComments(Drake2[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'LilUziVert' in (PostCaption.text) or 'liluzivert' in (PostCaption.text):
            LeavingComments(LilUzi[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'Lil Baby' in (PostCaption.text) or 'LilBaby' in (PostCaption.text) or 'lil baby' in (PostCaption.text) or 'lilbaby' in (PostCaption.text) or 'lilbaby' == (BlogName.text):
            LeavingComments(LilBaby[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'Future' in (PostCaption.text) or 'future' in (PostCaption.text):
            LeavingComments(Future[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'JuiceWRLD' in (PostCaption.text) or 'wrld' in (PostCaption.text) or 'WRLD' in (PostCaption.text) or 'JuiceWrld' in (PostCaption.text):
            LeavingComments(JuiceW[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'Da Baby' in (PostCaption.text) or 'DaBaby' in (PostCaption.text)or 'da baby' in (PostCaption.text) or 'dababy' in (PostCaption.text):
            LeavingComments(DaBaby[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'MegTheeStallion' in (PostCaption.text) or 'Stallion' in (PostCaption.text) or 'Meganthe' in (PostCaption.text)or 'meganthe' in (PostCaption.text)or 'megthe' in (PostCaption.text)or 'Megthe' in (PostCaption.text):
            LeavingComments(Megan[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'Gunna' in (PostCaption.text) or 'gunna' in (PostCaption.text):
            LeavingComments(Gunna[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'Young Thug' in (PostCaption.text) or 'young thug' in (PostCaption.text)  or 'Youngthug' in (PostCaption.text) or 'YoungThug' in (PostCaption.text) or 'youngthug' in (PostCaption.text) or 'thugga' in (PostCaption.text):
            LeavingComments(YoungThug[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'GHerbo' in (PostCaption.text) or 'gherbo' in (PostCaption.text) or 'G Herbo' in (PostCaption.text) or 'Gherbo' in (PostCaption.text) or 'g herbo' in (PostCaption.text) or (BlogName.text) == 'nolimitherbo':
            LeavingComments(GHerbo[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder)) #This one looks for herbo's hashtag or his username
            sleep(CalmDown[0])
        elif 'Nicki Minaj' in (PostCaption.text) or 'nickiminaj' in (PostCaption.text) or 'nicki minaj' in (PostCaption.text) or 'NickiMinaj' in (PostCaption.text):
            LeavingComments(NickiMinaj[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif '#TI' in (PostCaption.text) or '#ti' in (PostCaption.text) or '#TIP' in (PostCaption.text) or '#tip' in (PostCaption.text):
            LeavingComments(TI[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif '50 Cent' in (PostCaption.text) or '50Cent' in (PostCaption.text) or '50cent' in (PostCaption.text) or '50 cent' in (PostCaption.text):
            LeavingComments(FifCent[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'CardiB' in (PostCaption.text) or 'cardib' in (PostCaption.text) or 'Cardi B' in (PostCaption.text) or 'Cardib' in (PostCaption.text) or 'CARDIB' in (PostCaption.text):
            LeavingComments(CardiB[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif '42dug' in (PostCaption.text) or '42 dug' in (PostCaption.text) or '42D' in (PostCaption.text) or '42 D' in (PostCaption.text):
            LeavingComments(four2dug[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'Takeoff' in (PostCaption.text) or 'takeoff' in (PostCaption.text):
            LeavingComments(Takeoff[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'Beirut' in (PostCaption.text) or 'beirut' in (PostCaption.text)or 'BEIRUT' in (PostCaption.text):
            LeavingComments(Beirut[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0]) 
        elif 'Durk' in (PostCaption.text) or 'lildurk' == (BlogName.text) or 'durk' in (PostCaption.text) or 'DURK' in (PostCaption.text):
            LeavingComments(LilDurk[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0]) 
        elif 'epurp' in (PostCaption.text) or 'ePurp' in (PostCaption.text):
            LeavingComments(SmokePurp[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0]) 
        elif '2pac' in (PostCaption.text) or '2Pac' in (PostCaption.text) or 'Tupac' in (PostCaption.text) or '2PAC' in (PostCaption.text) or 'tupac' in (PostCaption.text):
            LeavingComments(Tupac[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0]) 
        elif 'lilreese' in (PostCaption.text) or 'LilReese' in (PostCaption.text) or 'Lil Reese' in (PostCaption.text) or 'lil reese' in (PostCaption.text):
            LeavingComments(LilReese[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'quandorondo' in (PostCaption.text) or 'QuandoRondo' in (PostCaption.text) or 'lul' in (PostCaption.text) or 'Lul' in (PostCaption.text) or 'Quando Rondo' in (PostCaption.text) or 'quando_rondo' == (BlogName.text) or 'quando rondo' in (PostCaption.text):
            LeavingComments(Quando[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'Convid' in (PostCaption.text) or 'CONVID' in (PostCaption.text) or 'Corona' in (PostCaption.text) or 'CORONA' in (PostCaption.text):
            LeavingComments(Coronavirus[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'FBGDUCK' in (PostCaption.text) or 'fbgduck' in (PostCaption.text) or 'FBGDuck' in (PostCaption.text) or 'FBG Duck' in (PostCaption.text) or 'fbg duck' in (PostCaption.text):
            LeavingComments(FBGDuck[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'RichTheKid' in (PostCaption.text) or 'Rich The Kid' in (PostCaption.text) or 'richthekid' in (PostCaption.text) or 'rich the kid' in (PostCaption.text) or 'richthekid' == (BlogName.text):
            LeavingComments(RichTheKid[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder)) #Looks for Riches hashtag and his username
            sleep(CalmDown[0])
        elif 'FivioForeign' in (PostCaption.text) or 'fivioforeign' in (PostCaption.text) or 'fiviofor' in (PostCaption.text) or 'fivio foreign' in (PostCaption.text)or 'Fivio Foreign' in (PostCaption.text):
            LeavingComments(Fivio[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'FamousDex' in (PostCaption.text) or 'Famous Dex' in (PostCaption.text) or 'famousdex' in (PostCaption.text) or 'famous dex' in (PostCaption.text):
            LeavingComments(FamousDex[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'trippieredd' in (PostCaption.text) or 'TrippieRedd' in (PostCaption.text) or 'trippie redd' in (PostCaption.text) or 'Trippie Redd' in (PostCaption.text):
            LeavingComments(TrippieRedd[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0]) 
        elif 'lilyachty' in (PostCaption.text) or 'LilYachty' in (PostCaption.text) or 'lil yachty' in (PostCaption.text) or 'Lil Yachty' in (PostCaption.text):
            LeavingComments(lilyatchy[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'NickCannon' in (PostCaption.text) or 'Nick Cannon' in (PostCaption.text) or 'nickcannon' in (PostCaption.text) or 'nick cannon' in (PostCaption.text):
            LeavingComments(NickCannon[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'stunna4vegas' in (PostCaption.text) or 'Stunna4Vegas' in (PostCaption.text) or 'tunna4' in (PostCaption.text):
            LeavingComments(Stunna4Vegas[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'ABoogie' in (PostCaption.text) or 'aboogie' in (PostCaption.text) or 'a boogie' in (PostCaption.text) or 'A Boogie' in (PostCaption.text):
            LeavingComments(ABoogie[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'torylanez' in (PostCaption.text) or 'tory lanez' in (PostCaption.text) or 'ToryLanez' in (PostCaption.text) or 'Tory Lanez' in (PostCaption.text):
            LeavingComments(torylanes[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'YBN' in (PostCaption.text) or 'ybn' in (PostCaption.text):
            LeavingComments(YBN[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'offsetyrn' == (BlogName.text):
            LeavingComments(OffsetAcc[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'Akon' in (PostCaption.text) or 'akon' in (PostCaption.text) or 'AKON' in (PostCaption.text):
            LeavingComments(Akon[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0]) 
        elif 'theshaderoom' == (BlogName.text) or 'hollywoodunlocked' == (BlogName.text):
            LeavingComments(theshaderoom[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0]) #BobbyShmurda, Plies
        elif 'realbobbyshmurdags9' == (BlogName.text) or 'Shmurda' in (PostCaption.text) or 'shmurda' in (PostCaption.text)  or 'rebel' in (PostCaption.text) or 'Rebel' in (PostCaption.text):
            LeavingComments(BobbyShmurda[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'plies' == (BlogName.text):
            LeavingComments(Plies[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'shaunking' == (BlogName.text):
            LeavingComments(ShaunKingacc[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'druski2funny' == (BlogName.text):
            LeavingComments(Druski[0]), LinkExtraction(LinkHolder), veonspanel(Username, LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif '6ix9ine' == (BlogName.text):
            LeavingComments(Six9ineAcc[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'nba_youngboy' == (BlogName.text):
            LeavingComments(YBAcc[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'kyliejenner' == (BlogName.text):
            LeavingComments(KylieJennerAcc[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'domislivenews' == (BlogName.text):
            LeavingComments(domislivenews[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'cnn' == (BlogName.text) or 'nytimes' == (BlogName.text) or 'foxnews' == (BlogName.text) or 'donaldjtrumpjr' == (BlogName.text) or 'whitehouse' == (BlogName.text) or 'realdonaldtrump' == (BlogName.text):
            LeavingComments(cnnacc[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'lilbaby_1' == (BlogName.text):
            LeavingComments(LilBabyacc[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'kingvonfrmdao' == (BlogName.text) or 'king von' in (PostCaption.text) or 'King Von' in (PostCaption.text) or 'kingvon' in (PostCaption.text)or 'KingVon' in (PostCaption.text):
            LeavingComments(KingVonacc[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'reesemoney300' == (BlogName.text):
            LeavingComments(LilReeseAcc[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'kimkardashian' == (BlogName.text):
            LeavingComments(KimKAcc[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'moneybaggyo' == (BlogName.text):
            LeavingComments(MoneyBagYoAcc[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'willsmith' == (BlogName.text):
            LeavingComments(WillSmithAcc[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'theestallion' == (BlogName.text):
            LeavingComments(MeganAcc[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'iamcardib' == (BlogName.text):
            LeavingComments(iamcardibAcc[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'daquan' == (BlogName.text):
            LeavingComments(daquanAcc[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0])
        elif 'dojacat' == (BlogName.text):
            LeavingComments(DojaCatAcc[0]), LinkExtraction(LinkHolder), veonspanel(Login[0], LinkExtraction(LinkHolder))
            sleep(CalmDown[0]) 
        elif 'saycheesetv' == (BlogName.text) and 'visuals' or 'drops' in (PostCaption.text):
            print ('SayCheese Promo; Skipping')
            sleep(CalmDown[0]) 
        else:
            LeavingComments(RandomComments[0])
            sleep(CalmDown[0])
    else:
        sleep(CalmDown[0]), veonrefresh()


        









