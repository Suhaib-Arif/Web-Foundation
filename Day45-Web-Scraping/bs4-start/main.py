from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
markup = response.text

soup = BeautifulSoup(markup , "html.parser")
title = [tag.string for tag in soup.select(selector="h3")][::-1]
print(title)
for movie in title:
    with open("list.txt","a",encoding="utf-8") as Movie_list:
            Movie_list.write(movie.encode() + "\n")






























#
# response=requests.get(url="https://news.ycombinator.com/news")
# HTML_Code=response.text
# soup = BeautifulSoup(HTML_Code,"html.parser")
#
# # print(soup.prettify())
# article_text=[item.get_text() for item in soup.select(selector=".titleline a")]
# article_link=[item.get("href") for item in soup.select(selector=".titleline a")]
# article_points=[int((item.string).split()[0]) for item in soup.select(selector=".score")]
#
# print(article_points)
# print(len(article_points))
# max_point=max(article_points)
# max_point_index=article_points.index(max_point)
# print(article_text[max_point_index])
# print(article_text)
# print(len(article_text))
# print(article_link[max_point_index])
# print(len(article_link))
































# with open("website.html",encoding='cp850') as file:
#     contents=file.read()
#
# soup = BeautifulSoup(contents,"html.parser")
# a_tag=soup.find(name="h1", id="name")
# # print(a_tag)
# # for tag in a_tag:
#     # print(tag.get("href"))
#
# print(soup.find(name="h3", class_="heading"))
# print(soup.select_one(selector="#name"))
# print(soup.select(selector=".heading"))