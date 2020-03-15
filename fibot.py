from selenium import webdriver
import pandas as pd
import time

options = webdriver.FirefoxOptions()
options.headless = True 

with webdriver.Firefox(options=options) as driver:
  start = time.time()
  stanovi = []
  urls = ['https://www.beostan.co.rs/novi-beograd_izdavanje-stanova.html', 
  'https://www.beostan.co.rs/centar_izdavanje-stanova.html', 
  'https://www.beostan.co.rs/siri-beograd_izdavanje-stanova.html', 
  'https://www.beostan.co.rs/zemun_izdavanje-stanova.html',
  'https://www.beostan.co.rs/bezanijska-kosa_izdavanje-stanova.html'
  ]
  for url in urls:
    driver.get(url)
    elements = driver.find_element_by_class_name('items').find_elements_by_tag_name('li')

    for el in elements:
      # Print cisto da vidis da radi
      print(el.find_elements_by_class_name('title')[1].text)
      cena = el.text[el.text.find('Cena')+5 : el.text.find('Eura')]
      cena = cena.replace(' ', '')
      if(int(cena) <= 400 and el.get_attribute('data-cat')=='#namesten'):
        stanovi.append([el.find_elements_by_class_name('title')[1].text, el.find_element_by_tag_name('a').get_attribute('href'), cena])  

print(time.time() - start)

df = pd.DataFrame(stanovi, columns=['naziv', 'link','cena'])
df.to_csv('beostan.csv', sep=',', index=False)

