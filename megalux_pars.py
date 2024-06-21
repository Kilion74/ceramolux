import requests  # pip install requests
from bs4 import BeautifulSoup  # pip install bs4
import csv

# pip install lxml

count = 1
while count <= 42:
    url = f'https://megaluxsamara.ru/product-category/keramogranit/page/{count}/?add_to_wishlist=17629&_wpnonce=64cce923c9'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    data = requests.get(url, headers=headers).text
    block = BeautifulSoup(data, 'lxml')
    heads = block.find('ul', class_='products columns-3').find_all('li')
    print(len(heads))
    for head in heads:
        w = head.find('div', class_='qodef-woo-product-inner').find_all('a')
        print(w[2].get('href'))
        get_url = (w[2].get('href'))
        loop = requests.get(get_url, headers=headers).text
        less = BeautifulSoup(loop, 'lxml')
        name = less.find('h1', class_='qodef-woo-product-title product_title entry-title')
        print(name.text)
        zagol = (name.text.strip())
        price = less.find('p', class_='price')
        print(price.text)
        cena = (price.text.strip())
        params = less.find('table', class_='woocommerce-product-attributes shop_attributes').find_all('tr')
        # print(len(params))
        param_1 = params[0].text.strip()
        print(' '.join(param_1.split()))
        charact_1 = (' '.join(param_1.split()))
        param_2 = params[1].text.strip()
        print(' '.join(param_2.split()))
        charact_2 = (' '.join(param_2.split()))
        param_3 = params[2].text.strip()
        print(' '.join(param_3.split()))
        charact_3 = (' '.join(param_3.split()))
        param_4 = params[3].text.strip()
        print(' '.join(param_4.split()))
        charact_4 = (' '.join(param_4.split()))
        try:
            param_5 = params[4].text.strip()
            print(' '.join(param_5.split()))
            charact_5 = (' '.join(param_5.split()))
        except:
            print('None')
            charact_5 = 'None'
        try:
            param_6 = params[5].text.strip()
            print(' '.join(param_6.split()))
            charact_6 = (' '.join(param_6.split()))
        except:
            print('None')
            charact_6 = 'None'
        pixx = less.find('figure', class_='woocommerce-product-gallery__wrapper').find('a').get('href')
        print(pixx)

        storage = {'name': zagol, 'price': cena, 'charact_1': charact_1, 'charact_2': charact_2, 'charact_3': charact_3,
                   'charact_4': charact_4, 'charact_5': charact_5, 'charact_6': charact_6, 'pixx': pixx, 'URL': get_url}
        fields = ['Name', 'Price', 'Param_1', 'Param_2', 'Param_3', 'Param_4', 'Param_5', 'Param_6',
                  'Photo_url', 'URL']
        with open('example.csv', 'a+', encoding='utf-16') as file:
            pisar = csv.writer(file, delimiter=';', lineterminator='\r')
            # Проверяем, находится ли файл в начале и пуст ли
            file.seek(0)
            if len(file.read()) == 0:
                pisar.writerow(fields)  # Записываем заголовки, только если файл пуст

            pisar.writerow(
                [storage['name'], storage['price'], storage['charact_1'], storage['charact_2'], storage['charact_3'],
                 storage['charact_4'], storage['charact_5'], storage['charact_6'], storage['pixx'], storage['URL']])

    count += 1
    print(count)
