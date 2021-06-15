#########adb shell dumpsys window windows | findstr mFocusedApp
###
# driver.current_package
# driver.current_activity
from appium import webdriver
import time
import os


#创建一个字典，包装相应的启动参数
desired_caps=dict()
desired_caps['platformName']='Android'
desired_caps['platformVersion']='7.1'
desired_caps['deviceName']='192.168.4.222:5555'
desired_caps['appPackage']='com.picahealth.yunque'
desired_caps['appActivity']='.activitys.mainpage.home.MainPageActivity'
desired_caps['noReset']='True'

driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

time.sleep(2)
driver.implicitly_wait(10)
# driver.start_activity('com.picahealth.yunque','.activitys.webs.webview.WebViewActivity')
# # time.sleep(5)
zhuanxiang="com.picahealth.yunque:id/img"

search_button=driver.find_element_by_xpath("//*[@text='专项合作']")

search_button.click()

study7h=driver.find_element_by_xpath('//*[contains(@text,"高血压系列")]')

print(study7h)

study7h.click()

time.sleep(3)

#works_title=driver.find_elements_by_xpath('//*[@text="y4cPHnj3+HtTBahjXlEwAAAABJRU5ErkJggg=="]')
#print(works_title)
#print(len(works_title))
def is_element_exist(element):
    source=driver.page_source
    if element in source:
        return True
    else:
        return False
judge=is_element_exist("去复习")
print("去复习：",judge)
judge2=is_element_exist("去学习")
print("去学习：",judge2)



for i in range(1,999):
    unstudy = driver.find_element_by_xpath('//*[@text="去复习"]/parent::*')
    selffff = driver.find_element_by_xpath('//*[@text="去复习"]')
    # if len(unstudy) is :
    #     driver.swipe(444,1750,444,950)
    #     unstudy = driver.find_element_by_xpath('//*[@text="去复习"]/parent::*')
    #     study_father = driver.find_element_by_xpath('//*[@text="去复习"]')
    #     study_father.click()
    #     time.sleep(2)
    time.sleep(2)
    selffff.click()
    study_video = driver.find_element_by_id("com.picahealth.yunque:id/ivStart")
    study_video.click()

    judge3 = is_element_exist("您已完成本课程的学习")

    while judge3 is False:
        judge3 = is_element_exist("您已完成本课程的学习")
        time.sleep(2)

    driver.find_element_by_id("com.picahealth.yunque:id/btn_left").click()
    time.sleep(2)
    i=i+1
    print(i)


# driver.quit()
