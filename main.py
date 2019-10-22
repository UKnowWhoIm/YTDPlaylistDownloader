from selenium import webdriver

browser = webdriver.Chrome()

def Download(link):
    print("Link",link)

link = input("Playlist Link? ")
browser.get(link)
raw_list = browser.find_element_by_css_selector("ytd-playlist-video-renderer")
for i in range(len(raw)):
    raw_list[i].click()
    Download(browser.current_url)
    browser.get(link)
    raw_list = browser.find_element_by_css_selector("ytd-playlist-video-renderer")
    




