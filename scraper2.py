import requests
import re
from bs4 import BeautifulSoup

urls = [
"https://books.toscrape.com/catalogue/category/books/travel_2/index.html",
"https://books.toscrape.com/catalogue/category/books/mystery_3/index.html",
"https://books.toscrape.com/catalogue/category/books/mystery_3/page-2.html",
"https://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html",
"https://books.toscrape.com/catalogue/category/books/historical-fiction_4/page-2.html",
"https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html",
"https://books.toscrape.com/catalogue/category/books/sequential-art_5/page-2.html",
"https://books.toscrape.com/catalogue/category/books/sequential-art_5/page-3.html",
"https://books.toscrape.com/catalogue/category/books/sequential-art_5/page-4.html",
"https://books.toscrape.com/catalogue/category/books/classics_6/index.html",
"https://books.toscrape.com/catalogue/category/books/philosophy_7/index.html",
"https://books.toscrape.com/catalogue/category/books/romance_8/index.html",
"https://books.toscrape.com/catalogue/category/books/romance_8/page-2.html",
"https://books.toscrape.com/catalogue/category/books/womens-fiction_9/index.html",
"https://books.toscrape.com/catalogue/category/books/fiction_10/index.html",
"https://books.toscrape.com/catalogue/category/books/fiction_10/page-2.html",
"https://books.toscrape.com/catalogue/category/books/fiction_10/page-3.html",
"https://books.toscrape.com/catalogue/category/books/fiction_10/page-4.html",
"https://books.toscrape.com/catalogue/category/books/childrens_11/index.html",
"https://books.toscrape.com/catalogue/category/books/childrens_11/page-2.html",
"https://books.toscrape.com/catalogue/category/books/religion_12/index.html",
"https://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html",
"https://books.toscrape.com/catalogue/category/books/nonfiction_13/page-2.html",
"https://books.toscrape.com/catalogue/category/books/nonfiction_13/page-3.html",
"https://books.toscrape.com/catalogue/category/books/nonfiction_13/page-4.html",
"https://books.toscrape.com/catalogue/category/books/nonfiction_13/page-5.html",
"https://books.toscrape.com/catalogue/category/books/nonfiction_13/page-6.html",
"https://books.toscrape.com/catalogue/category/books/music_14/index.html",
"https://books.toscrape.com/catalogue/category/books/default_15/index.html",
"https://books.toscrape.com/catalogue/category/books/default_15/page-2.html",
"https://books.toscrape.com/catalogue/category/books/default_15/page-3.html",
"https://books.toscrape.com/catalogue/category/books/default_15/page-4.html",
"https://books.toscrape.com/catalogue/category/books/default_15/page-5.html",
"https://books.toscrape.com/catalogue/category/books/default_15/page-6.html",
"https://books.toscrape.com/catalogue/category/books/default_15/page-7.html",
"https://books.toscrape.com/catalogue/category/books/default_15/page-8.html",
"https://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html",
"https://books.toscrape.com/catalogue/category/books/sports-and-games_17/index.html",
"https://books.toscrape.com/catalogue/category/books/add-a-comment_18/index.html",
"https://books.toscrape.com/catalogue/category/books/add-a-comment_18/page-2.html",
"https://books.toscrape.com/catalogue/category/books/add-a-comment_18/page-3.html",
"https://books.toscrape.com/catalogue/category/books/add-a-comment_18/page-4.html",
"https://books.toscrape.com/catalogue/category/books/fantasy_19/index.html",
"https://books.toscrape.com/catalogue/category/books/fantasy_19/page-2.html",
"https://books.toscrape.com/catalogue/category/books/fantasy_19/page-3.html",
"https://books.toscrape.com/catalogue/category/books/new-adult_20/index.html",
"https://books.toscrape.com/catalogue/category/books/young-adult_21/index.html",
"https://books.toscrape.com/catalogue/category/books/young-adult_21/page-2.html",
"https://books.toscrape.com/catalogue/category/books/young-adult_21/page-3.html",
"https://books.toscrape.com/catalogue/category/books/science_22/index.html",
"https://books.toscrape.com/catalogue/category/books/poetry_23/index.html",
"https://books.toscrape.com/catalogue/category/books/paranormal_24/index.html",
"https://books.toscrape.com/catalogue/category/books/art_25/index.html",
"https://books.toscrape.com/catalogue/category/books/psychology_26/index.html",
"https://books.toscrape.com/catalogue/category/books/autobiography_27/index.html",
"https://books.toscrape.com/catalogue/category/books/parenting_28/index.html",
"https://books.toscrape.com/catalogue/category/books/adult-fiction_29/index.html",
"https://books.toscrape.com/catalogue/category/books/humor_30/index.html",
"https://books.toscrape.com/catalogue/category/books/horror_31/index.html",
"https://books.toscrape.com/catalogue/category/books/history_32/index.html",
"https://books.toscrape.com/catalogue/category/books/history_32/index.html",
"https://books.toscrape.com/catalogue/category/books/history_32/page-2.html",
"https://books.toscrape.com/catalogue/category/books/food-and-drink_33/index.html",
"https://books.toscrape.com/catalogue/category/books/food-and-drink_33/page-2.html",
"https://books.toscrape.com/catalogue/category/books/christian-fiction_34/index.html",
"https://books.toscrape.com/catalogue/category/books/business_35/index.html",
"https://books.toscrape.com/catalogue/category/books/biography_36/index.html",
"https://books.toscrape.com/catalogue/category/books/thriller_37/index.html",
"https://books.toscrape.com/catalogue/category/books/contemporary_38/index.html",
"https://books.toscrape.com/catalogue/category/books/spirituality_39/index.html",
"https://books.toscrape.com/catalogue/category/books/academic_40/index.html",
"https://books.toscrape.com/catalogue/category/books/self-help_41/index.html",
"https://books.toscrape.com/catalogue/category/books/historical_42/index.html",
"https://books.toscrape.com/catalogue/category/books/christian_43/index.html",
"https://books.toscrape.com/catalogue/category/books/suspense_44/index.html",
"https://books.toscrape.com/catalogue/category/books/short-stories_45/index.html",
"https://books.toscrape.com/catalogue/category/books/novels_46/index.html",
"https://books.toscrape.com/catalogue/category/books/health_47/index.html",
"https://books.toscrape.com/catalogue/category/books/politics_48/index.html",
"https://books.toscrape.com/catalogue/category/books/cultural_49/index.html",
"https://books.toscrape.com/catalogue/category/books/erotica_50/index.html",
"https://books.toscrape.com/catalogue/category/books/crime_51/index.html"
]

cats = [
"travel",
"mystery",
"historical-fiction",
"sequential-art",
"classics",
"philosophy",
"romance",
"womens-fiction",
"fiction",
"childrens",
"religion",
"nonfiction",
"music",
"default",
"science-fiction",
"sports-and-games",
"add-a-comment",
"fantasy",
"new-adult",
"young-adult",
"science",
"poetry",
"paranormal",
"art",
"psychology",
"autobiography",
"parenting",
"adult-fiction",
"humor",
"horror",
"history",
"food-and-drink",
"christian-fiction",
"business",
"biography",
"thriller",
"contemporary",
"spirituality",
"academic",
"self-help",
"historical",
"christian",
"suspense",
"short-stories",
"novels",
"health",
"politics",
"cultural",
"erotica",
"crime"
]


for url in urls:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find('div', class_='col-sm-8 col-md-9')
    
    if results is None:
        continue
    books = results.find_all('article', class_='product_pod')
    for book in books:
        name = book.find('h3')
        name = name.find('a')['title']
        rating=0
        r1 = book.find('p', class_='star-rating One')
        r2 = book.find('p', class_='star-rating Two')      
        r3 = book.find('p', class_='star-rating Three')
        r4 = book.find('p', class_='star-rating Four')
        r5 = book.find('p', class_='star-rating Five')
        
        if r1 is not None:
            rating=1
        if r2 is not None:
            rating=2
        if r3 is not None:
            rating=3
        if r4 is not None:
            rating=4
        if r5 is not None:
            rating=5
        
        price = book.find('p', class_='price_color').text
        availability = book.find('p', class_='instock availability')
        
        
        availability = availability.text.strip()
        for cat in cats:
            if re.search(cat, url) is not None:
                f = open(cat+".csv", "a")
                f.write('"'+name+'"'+','+str(rating)+','+price+','+availability+'\n')
                f.close()