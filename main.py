from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options  

chrome_options = Options()
# chrome_options.add_argument("--headless") -> Buggy

browser = webdriver.Chrome(options=chrome_options)

def Download(r_link):
    # Website Used : https://youtubedownload.video/youtube-to-mp3-downloader.php
    
    browser.get("https://youtubedownload.video/youtube-to-mp3-downloader.php")
    while True:
        # Keep On Trying Until element loads
        print("Waiting For DDoSCheck")
        try:
            target1 = browser.find_element_by_css_selector("#urlYoutube")
            break
        except:
            sleep(1)
            pass
    browser.execute_script("arguments[0].value=arguments[1]",target1,r_link)
    browser.find_element_by_css_selector("#submit1").click()
    while True:
        # Keep On Trying Until element loads
        print("Waiting For Search Result")
        try:
            browser.find_element_by_css_selector("input[type=button]").click()
            break
        except Exception as E:
            sleep(1)
            pass
    while True:
        # Keep On Trying Until element loads
        print("Waiting For Conversion")
        try:
            browser.find_element_by_css_selector("input[value=Download]").click()
            break
        except:
            sleep(1)
            pass
    
    
    
link = input("Playlist Link? ")
browser.get(link)
raw_list = browser.find_elements_by_css_selector("ytd-playlist-video-renderer")
for i in range(len(raw_list)):
    raw_list[i].click()
    Download(browser.current_url)
    print("%i Done "%(i+1))
    sleep(5)
    browser.get(link)
    raw_list = browser.find_elements_by_css_selector("ytd-playlist-video-renderer")
    




