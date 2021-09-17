from splinter import Browser
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
executable_path = {'executable_path': ChromeDriverManager().install()}

def scrape():
    browser = Browser('chrome', **executable_path, headless=False)
    title, paragraph = news(browser)
    data = {}
    data['title'] = title
    data['paragraph'] = paragraph
    data['image'] = image(browser)
    data['facts'] = facts() 
    data['hemis'] = hemis(browser)
    return data 

def news(browser):
    browser.visit('https://redplanetscience.com/')
    title = browser.find_by_css('div.content_title').text
    paragraph = browser.find_by_css('div.article_teaser_body').text
    return title, paragraph

def image(browser):
    browser.visit('https://spaceimages-mars.com/')
    return browser.find_by_css('img.headerimage')['src']

def facts():
    return pd.read_html('https://galaxyfacts-mars.com/',
            header=None, index_col=None,)[0].rename(columns = {0: 'Index', 1:'Mars', 2:'Earth'}).to_html(index=False,
            classes='table table-stripped')

def hemis(browser): 
    browser.visit('https://marshemispheres.com/')

    hemispheres = []
    for i in range(4):
        hemisphere = {}
        hemisphere['title'] = browser.find_by_css("a.itemLink h3")[i].text
        browser.find_by_css("a.itemLink h3")[i].click()
        hemisphere['url'] = browser.find_by_text("Sample")["href"]
        hemispheres.append(hemisphere)
        browser.back()
    browser.quit()
    return hemispheres