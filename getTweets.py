from selenium import webdriver
import logininfo
import time

browser = webdriver.Firefox(executable_path = "C:\\Users\\hp\\Desktop\\Selenium Python\\geckodriver.exe")

browser.get("https://twitter.com")

time.sleep(3)
 
first_login = browser.find_element_by_xpath("/html/body/div/div/div/div/main/div/div/div/div[1]/div/a[2]/div")
first_login.click()
 
time.sleep(2)
 
username = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input") 
password = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input")
 
username.send_keys(logininfo.my_username)
password.send_keys(logininfo.my_password)
 
time.sleep(2)
 
login = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div")
login.click()
 
time.sleep(2)
 
searchArea = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input")
searchArea.send_keys("fityemek")
searchArea.send_keys(u'\ue007')

tweets = []

lenOfPage = browser.execute_script("window.scrollTo(0,document.body.scrollHeight); var lenOfPage = document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(2)
    tweetField = browser.find_elements_by_css_selector(".css-901oao.r-hkyrab.r-1qd0xha.r-a023e6.r-16dba41.r-ad9z0x.r-bcqeeo.r-bnwqim.r-qvutc0")
    for tweet in tweetField:
        tweets.append(tweet.text)
    lenOfPage = browser.execute_script("window.scrollTo(0,document.body.scrollHeight); var lenOfPage = document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match=True
time.sleep(2)

tweetCount = 1
with open("tweets.txt","w", encoding= "UTF-8") as file:
    for tweet in tweets\
            :
        file.write(str(tweetCount) +"\n"+ tweet +"\n")
        file.write("**************************************************\n")
        tweetCount+=1
time.sleep(1)

 
browser.close()
