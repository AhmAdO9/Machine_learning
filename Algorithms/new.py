# from bs4 import BeautifulSoup
# import requests

# # payload = {'api_key':'fad18a2d9c10564534e0108b6df31366',
           
# #            'url':'https://www.nytimes.com/2023/07/18/magazine/wikipedia-ai-chatgpt.html'}

# response = requests.get("https://www.mage.ai/blog/definitive-guide-to-accuracy-precision-recall-for-product-developers")

# soup = BeautifulSoup(response.text, "html.parser")
# data = soup.find('a', class_='Link__LinkStyle-sc-15mjx5r-0 cZPHya').get('href')

# response = requests.get(data)
# soup = BeautifulSoup(response.text, "html.parser")
# data =soup.find('span', string = "https://m.mage.ai/how-to-get-started-with-ai-ml-8630fecfd776").parent.get('href')
# response = requests.get(data)
# soup = BeautifulSoup(response.text, "html.parser")
# data = soup.find('h1', id='30ed').text
# print(data)






