from autoscraper import AutoScraper

url = "https://commons.wikimedia.org/wiki/Main_Page"

wanted_list = ['Picture of the day', 'Nature', 'By location']


scraper = AutoScraper()
result = scraper.build(url, wanted_list)
print(result)