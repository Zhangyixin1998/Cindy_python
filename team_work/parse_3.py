import os
import requests
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq
if __name__ == "__main__":
    url =  "http://www.guoxuedashi.com/zhongyi/"
    raw_url = "http://www.guoxuedashi.com"
    new_word = requests.get(url)
    soup = BeautifulSoup(new_word.content,"html.parser")
    result =soup.find_all("dd")
    if not os.path.exists("zhongyi"):
       os.mkdir("zhongyi/")

    i=0
    for elem in result:
        i=i+1
        if i>60:
            new_url=raw_url+elem.a['href'] #进入典籍各章节
            # print(final_url1)
            reps=requests.get(new_url)
            new_soup = BeautifulSoup(reps.content,"html.parser")
            med_name = new_soup.find("div",class_="info_tree").h1.get_text()
            med_def= new_soup.find("div",class_="info_content zj clearfix").p.get_text()
            print(med_name)
            with open('zhongyi/' + med_name + '.txt', "a", encoding='utf-8') as f:
                f.write(med_name + '\n')
                f.write(med_def + '\n')
        else:
            new_url1=raw_url+elem.a['href'] #进入二级页面（各种中医典籍目录）
            word=requests.get(new_url1)
            final_soup = BeautifulSoup(word.content,"html.parser")
            final_result=final_soup.find_all("li")

            for elem in final_result:
                final_url=raw_url+elem.a['href'] #进入典籍各章节
                print(final_url)
                reps1=requests.get(final_url)
                final_soup1 = BeautifulSoup(reps1.content,"html.parser")
                chapter_name = final_soup1.find("div",class_="info_tree").h1.get_text() #取各个章节名
                chapter_def= final_soup1.find("div",class_="info_txt clearfix").get_text() #取各个章节内容名
                print(chapter_name)
                with open('zhongyi/'+chapter_name+'.txt',"a",encoding='utf-8') as f:
                    f.write(chapter_name+'\n')
                    f.write(chapter_def+'\n')
