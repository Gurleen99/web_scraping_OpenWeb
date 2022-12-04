from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
import time, ctypes, sys
from csv import writer

import user_agent
import fileHandling

url = 'https://rladies.org/canada-rladies/'


options = webdriver.ChromeOptions()
options.add_argument(user_agent.userAgent)
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("--disable-extensions")
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
# driver = webdriver.Chrome(service=Service(ChromeDriverManger().install()), options=options)
driver = webdriver.Chrome(executable_path=user_agent.executablePath)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
         Object.defineProperty(navigator, 'webdriver', {
         get: () => undefined
         })
      """
})

driver.get(url)
driver.implicitly_wait(10)
time.sleep(4)

source=driver.page_source
soup=BeautifulSoup(source,'html.parser')
with open('index.html','w', encoding='utf-8') as f :
    f.write(source)

list_user=soup.find_all('span',class_='cn-image-style')
#print(list_user)

users=[]
for user in list_user:
    link=user.find('a').get('href')
    users.append(link)
print(len(users))

given_name_list=[]
family_name_list=[]
profession_list=[]
organization_list=[]
locality_list=[]
region_list=[]
country_list=[]
personal_website_list=[]
social_media_list=[]
interests_list=[]
contact_method_list=[]

print(given_name_list,family_name_list,profession_list,organization_list,locality_list,region_list,country_list,profession_list,social_media_list)

for i in range(0,len(users),1):
    driver.get(users[i])
    driver.implicitly_wait(10)
    time.sleep(4)

    isource = driver.page_source
    iuser=BeautifulSoup(isource,'html.parser')
    with open('individual_user.html', 'w', encoding='utf-8') as f:
        f.write(isource)

    print('---------------user {}--------------'.format(i))

    # find websites
    if iuser.find_all('span', class_='link cn-link website'):
        links= iuser.find_all('a', class_='url')
        web_list=[]
        for web in links:
            personal_web=web.get('href')
            web_list.append(personal_web)
        #print('personal websites: ', web_list)
        personal_website_list.insert(0,web_list)
    else:
        #print("Nan")
        personal_website_list.insert(0,'[Nan]')

    # find given name
    if iuser.find_all('span',class_='given-name'):
        firstname=iuser.find('span',class_='given-name').text
        #print('firstname:',firstname)
        given_name_list.insert(0,firstname)
    else:
        #print("Nan")
        given_name_list.insert(0,"Nan")

    #find family name
    if iuser.find_all('span', class_='family-name'):
        familyname = iuser.find('span', class_='family-name').text
        family_name_list.insert(0,familyname)
        #print('familyname:',familyname)
    else:
        #print("Nan")
        family_name_list.insert(0,'Nan')


    #find profession
    if iuser.find_all('span', class_='title notranslate'):
        Profession=iuser.find('span', class_='title notranslate').text
        profession_list.insert(0,Profession)
        #print('profession:',Profession)
    else:
        #print("Nan")
        profession_list.insert(0,"Nan")


    #find organization
    if iuser.find_all('span', class_='organization-name notranslate'):
        organization=iuser.find('span', class_='organization-name notranslate').text
        organization_list.insert(0,organization)
        #print('organization:',organization)
    else:
        #print("Nan")
        organization_list.insert(0,'Nan')

    # find locality
    if iuser.find_all('span', class_='locality'):
        locality = iuser.find('span', class_='locality').text
        locality_list.insert(0,locality)
        #print('locality:',locality)
    else:
        #print("Nan")
        locality_list.insert(0,'Nan')

    # find region
    if iuser.find_all('span', class_='region'):
        region = iuser.find('span', class_='region').text
        region_list.insert(0,region)
        #print('region:',region)
    else:
        #print("Nan")
        region_list.insert(0,'Nan')

    # find country
    if iuser.find_all('span', class_='country-name'):
        country= iuser.find('span', class_='country-name').text
        country_list.insert(0,country)
        #print('country:',country)
    else:
        #print("Nan")
        country_list.insert(0,'Nan')


    # find social media
    if iuser.find_all('span', class_='social-media-network cn-social-media-network'):
       social_media = iuser.find('span', class_='social-media-network cn-social-media-network').find('a').get('href')
       social_media_list.insert(0,social_media)
       #print('social media: ',social_media)
    else:
       #print("Nan")
       social_media_list.insert(0,'Nan')

    values=[personal_website_list[0],given_name_list[0],family_name_list[0],profession_list[0],organization_list[0],locality_list[0],region_list[0],country_list[0],social_media_list[0]]
    with open(r'C:\Users\Lenovo\PycharmProjects\pythonProject\R_ladies_global1_demo.csv', 'a', encoding='utf8', newline='') as f:
        write_data=writer(f)
        write_data.writerow(values)


    # find contact
    #if iuser.find_all('div',class_='cn-biography'):
     #   contact = iuser.find('div',class_='cn-biography').find('ul')
      #  contact=contact.select_one("li:nth-child(3)")
       # print('contact: ',contact)
        #contact_method_list.append(organization)
   # else:
    #    print('Nan')


# find interest
    #if iuser.find_all('div',class_='cn-biography'):
     #   interest=iuser.find('div',class_='cn-biography').find('ul')
      #  interest=interest.select_one("li:nth-child(2)").text
        #interests_list.append(organization)
       # print(interest)
    #else:
     #   print("Nan")

