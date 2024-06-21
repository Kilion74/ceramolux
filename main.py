import requests  # pip install requests
from bs4 import BeautifulSoup  # pip install bs4

# pip install lxml


url = 'https://megaluxsamara.ru/product-category/keramogranit/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
data = requests.get(url, headers=headers).text
block = BeautifulSoup(data, 'lxml')
heads = block.find('ul', class_='products columns-3').find_all('li')
print(len(heads))
for head in heads:
    w = head.find('div', class_='qodef-woo-product-inner').find_all('a')
    # print(w[2].get('href'))
    get_url = (w[2].get('href'))
    loop = requests.get(get_url, headers=headers).text
    less = BeautifulSoup(loop, 'lxml')
    name = less.find('h1', class_='qodef-woo-product-title product_title entry-title')
    print(name.text)
    price = less.find('p', class_='price')
    print(price.text)
    params = less.find('table', class_='woocommerce-product-attributes shop_attributes').find_all('tr')
    # print(len(params))
    param_1 = params[0].text
    print(' '.join(param_1.split()))
    param_2 = params[1].text
    print(' '.join(param_2.split()))
    param_3 = params[2].text
    print(' '.join(param_3.split()))
    param_4 = params[3].text
    print(' '.join(param_4.split()))
    param_5 = params[4].text
    print(' '.join(param_5.split()))
    param_6 = params[5].text
    print(' '.join(param_6.split()))
    pixx = less.find('figure', class_='woocommerce-product-gallery__wrapper').find('a').get('href')
    print(pixx)
