from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
list_xpath=[]#存放第2-10页按钮的xpath路径
def click_xpath(xpath):
    driver.find_element_by_xpath(xpath).click()
def get_xpath():
    for i in range(9):
        page='//*[@id="Page_Container_267733"]/a['+str(i+3)+']'
        list_xpath.append(page)
    return list_xpath
def get_image(soup):
    aa=soup.find_all(class_='p_newhero_item')#使用了BeautifulSoup的方法选择器进行解析
    list1=[]#存放图片的url
    list2=[]#存放图片的名字
    for p in aa:
        for vv in p.find_all(name='img'):
            list1.append(vv['data-src'])
            list2.append(vv['alt'])
    for mm in range(len(list1)):
        image_content=requests.get(list1[mm]).content
        path='E:\\study\\爬虫\\高清壁纸\\'+list2[mm]+'.jpg'
        with open(path,'wb') as file1:
            file1.write(image_content)
if __name__=='__main__':
    driver = webdriver.Firefox()
    url = 'https://pvp.qq.com/web201605/wallpaper.shtml'
    driver.get(url)
    js = "var q=document.documentElement.scrollTop=10000"
    driver.execute_script(js)#滑动滚动条到最底部
    source1 = driver.page_source
    get_xpath()
    source_add=[]
    for i in list_xpath:
        click_xpath(i)
        time.sleep(1)
        source = driver.page_source
        source_add.append(source)
    driver.close()
    source_add.append(source1)
    string_source=''.join(source_add)#将存放所有网页源码的列表转化为字符串
    soup = BeautifulSoup(string_source, 'html.parser')
    get_image(soup)
    print('OK!')