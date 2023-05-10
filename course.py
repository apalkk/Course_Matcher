#!/usr/bin/env python

import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import requests
import sys

if (len(sys.argv) > 2):
    raise Exception("Incorrect arg number (>2) {}", sys.argv[-1])

def get_raw_ann(link) -> list:
    chromedriver_path = '/path/to/chromedriver'
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(
        options=options, executable_path=chromedriver_path)
    driver.get(link)
    html = driver.find_element(By.CLASS_NAME, 'sections-container')
    # .get_attribute("links")
    links = html.find_elements(By.CLASS_NAME, 'open-seats-count')
    return get_text(links)


def get_text(list) -> list[str]:
    ls = []
    for x in list:
        ls.append(x.text)
    return ls

text : str = sys.argv[1]
start : int = text.find('courseId=')
end : int = text.find('&sectionId')
text = text[int(start)+9:int(end)]

def main():
    try:
        i = 0
        while (True):
            i += 1
            for x in get_raw_ann(sys.argv[1]):
                # print(x)
                if (x != '0'):
                    os.system('afplay Downloads/Goat-Bah-A-www.fesliyanstudios.com.mp3')
                    os.system('curl -d "text=We found that {} just opened up on Testudo." -d "channel=C05713SSRUK" -H "Authorization: Bearer xoxb-5262894251488-5224790812039-bBeGZ9mfg1YrVZKcAolpEh1i" -X POST https://slack.com/api/chat.postMessage --http1.1'.format(text))
                    sys.exit()
            print("Loop ", i)
            time.sleep(30)
    except Exception as e:
        print(e)
        main()

main()
