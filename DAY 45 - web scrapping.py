
import requests
from bs4 import BeautifulSoup

respond=requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
data=respond.text
soup=BeautifulSoup(data,'html.parser')
best = soup.find_all(class_="title",name='h3')

best_of_best=[]
for i in best:
    yet=i.getText()
    best_of_best.append(yet)
    #print(yet)
#best_of_best.reverse()
#print(best_of_best)
with open('file.text',mode='w',encoding='utf-8') as file:
    for lit in range(len(best_of_best)-1,-1,-1):
        movie=best_of_best[lit]
        file.write(f'{movie}\n')
        print(best_of_best[lit])

