from bs4 import BeautifulSoup
import requests

urls = ['https://www.trustpilot.com/categories/restaurants_bars?numberofreviews=0&status=all&timeperiod=0', 
'https://www.trustpilot.com/categories/restaurants_bars?numberofreviews=0&page=2&status=all&timeperiod=0',
'https://www.trustpilot.com/categories/restaurants_bars?numberofreviews=0&page=3&status=all&timeperiod=0',
'https://www.trustpilot.com/categories/restaurants_bars?numberofreviews=0&page=4&status=all&timeperiod=0',
'https://www.trustpilot.com/categories/restaurants_bars?numberofreviews=0&page=5&status=all&timeperiod=0',
'https://www.trustpilot.com/categories/restaurants_bars?numberofreviews=0&page=6&status=all&timeperiod=0',
'https://www.trustpilot.com/categories/restaurants_bars?numberofreviews=0&page=7&status=all&timeperiod=0',
'https://www.trustpilot.com/categories/restaurants_bars?numberofreviews=0&page=8&status=all&timeperiod=0']
for url in urls:
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    restaurants = soup.find_all('div', class_ = 'categoryBusinessListWrapper___14CgD')
    for index, restaurant in enumerate(restaurants):
        tags = restaurant.find_all('a', class_ = 'internal___1jK0Z wrapper___26yB4')
        for tag in tags:
            restaurant_name = tag.find('div', class_ = 'businessTitle___152-c').text.split(',')[0]
            ratings = tag.find('div', class_ = 'textRating___3F1NO')
            location = tag.find('span', class_ = 'locationZipcodeAndCity___33EfU')
            more_info = tag['href']
            with open(f'restaurant_review_data.csv', 'a') as f:
                f.write(restaurant_name)
                f.write(',')
                if ratings == None:
                    f.write('')
                else:
                    f.write(ratings.text)    
                f.write(',')
                if location == None:
                    f.write('')
                else:    
                    f.write(location.text.split(',')[0])
                f.write(',')
                f.write(more_info)    
                f.write('\n')
            print('File saved')    
            