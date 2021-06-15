# -*- coding:utf-8 -*- 

"""
作者：luoyu
日期：2021年06月12日
"""
import uiautomator2 as u2
import time



def try_click(elem):
    try:
        elem.click()
        time.sleep(1)
    except:
        pass

def check_box():
    statue = False
    while True:
        try:
            statue = d(text="恭喜！您已完成本课程的学习").exists(1)
        except:
            pass
        try:
            d(text="学习未学完的章节").click()
        except:
            pass
        if statue:
            return True


def start_studing():
    # 点击开始
    d.xpath('//*[@resource-id="com.picahealth.yunque:id/ivStart"]').click()
    time.sleep(3)
    # 学习列表
    class_ = d(className="android.widget.TextView",resourceId="com.picahealth.yunque:id/tv_sub_title")
    print("学习列表：")
    for each in class_:
        print(each.get_text())
    if check_box():
        d(text="我知道了").click()
        time.sleep(2)
    d.press("back")
    time.sleep(2)

def select_class_to():
    s = d(scrollable=True).scroll.to(description="去学习")
    time.sleep(1)
    if s:
        d.swipe_ext("down", scale=0.1)
        while True:
            try:
                print("尝试点击 去学习")
                d(description="去学习").click()
                break
            except:
                d.swipe_ext("up", scale=0.3)
        time.sleep(2)
        start_studing()
        return True
    else:
        print("没有去学习了，寻找继续学习！")
        return select_class_continue()

def select_class_review():
    s = d(scrollable=True).scroll.to(description="去复习")
    time.sleep(1)
    if s:
        d.swipe_ext("down", scale=0.2)
        d(description="去复习").click()
        time.sleep(2)
        start_studing()
        return True
    else:
        print("没有去复习了，寻找继续学习！")
        return select_class_continue()


def select_class_continue():
    s = d(scrollable=True).scroll.to(description="继续学习")
    time.sleep(1)
    if s:
        d.swipe_ext("down", scale=0.1)
        while True:
            try:
                print("尝试点击 继续学习")
                d(description="继续学习").click()
                break
            except:
                d.swipe_ext("up", scale=0.3)
        time.sleep(2)
        start_studing()
        return True
    else:
        print("没有继续学习了，学习完成！")
        return False

def main():

    # qidong
    d(text="云鹊医").click()
    time.sleep(5)
    ignore_elem = d(resourceId="com.picahealth.yunque:id/btn_ignore")
    close_ads = d(resourceId="com.picahealth.yunque:id/notice_close")
    try_click(ignore_elem)
    try_click(close_ads)
    time.sleep(1)
    # 进入专项合作
    d.xpath('//*[@text="专项合作"]').click()
    time.sleep(4)
    d.xpath('//*[@content-desc="2021年重庆市基层卫生人员能力培训"]').click()
    time.sleep(4)
    while True:
        statue = select_class_to()
        if not statue:
            print("学习全部完成！")
            time.sleep(10)
            break


if __name__ == '__main__':
    d = u2.connect_usb()
    main()








