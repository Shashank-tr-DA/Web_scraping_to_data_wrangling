from bs4 import BeautifulSoup
import requests

urls = ['https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off', 
      'https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page=2', 
      'https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page=3', 
      'https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page=4', 
      'https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page=5', 
      'https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page=6', 
      'https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page=7', 
      'https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page=8', 
      'https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page=9', 
      'https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page=10', 
      'https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page=11', 
      'https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page=12', 
      'https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page=13', 
      'https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page=14', 
      'https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page=15', 
      'https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page=16', 
      'https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page=17', 
      'https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page=18', 
      'https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page=19', 
      'https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page=20', 
      'https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page=21']
for url in urls:
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'lxml')
    main_box = soup.find_all('div', class_ = '_2kHMtA')
    for box in main_box:
        laptop_name = box.find('div', class_ = '_4rR01T').text.strip()
        price = box.find('div', class_ = '_30jeq3 _1_WHN1').text.replace('₹', '').replace(',', '') 
        ratings_and_reviews = box.find('span', class_ = '_2_R_DZ')
        rating = box.find('div', class_ = '_3LWZlK')
        with open('laptop_data_new.csv', 'a') as f:
            f.write(laptop_name)
            f.write(',')
            f.write(price)
            f.write(',')
            if ratings_and_reviews == None:
                f.write('')
            else:    
                f.write(ratings_and_reviews.text.replace(',', ''))    
            f.write(',')
            if rating == None:
                f.write('')
            else:    
                f.write(rating.text)
            f.write('\n')     
print('File saved')    