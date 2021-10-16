#TOOLS FIND JOBS
#AUTHOR : Cx0plaz A.K.A 7RU5H7
#Version : 2021.01

from bs4 import BeautifulSoup
import requests
import time
import os

#key = input("Keywords : ")
def jobSearch():
    url = 'https://bogorloker.com/'

    req = requests.get(url).text

    soup = BeautifulSoup(req, 'lxml')

    jobs= soup.find_all('div', class_='job-title-wrap')

    for job in jobs:
    
        nameJob = job.find('h2', class_='entry-title').text.strip()
        nameCompany = job.find('div', class_='company-name').text.strip()
        jobType = job.find('li', class_='job-type').text
        moreInfo = job.h2.a["href"]
        with open(f'/storage/emulated/0/belajarpython/jobs.txt', 'a') as f:
            f.write (f"\n[#] Company Name : {nameCompany}\n")
            f.write (f"[#] Job Name : {nameJob.capitalize()}\n")
            f.write (f"[#] Type Job : {jobType}\n")
            f.write (f"[#] More Info : {moreInfo}\n")
            f.write ("="*50)
        print ('[+] File save successfuly')
        time.sleep(0.2)
        
        
if __name__ == '__main__':
    while True:
        os.system('clear')
        jobSearch()
        time_wait = 1
        input("[Exit] Press enter...")
        os.system('clear')
        print (f"[!] Waiting {time_wait} seconds...")
        time.sleep(time_wait*10)
        exit()