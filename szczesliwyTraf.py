''' Projekt - wyszukiwanie typu 'szczęśliwy traf' w Google.
Program otwiera przeglądarkę wraz z pierwszymi pięcioma wynikami
w nowych kartach.'''

import requests, webbrowser, bs4

print('Wyszukiwanie...')
res = requests.get('http://google.pl/search?q=' + 'pelargonia bluszczolistna')
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
linkElems = soup.select('.r a')

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.pl'+ linkElems[i].get('href'))
    

                                                           

       



                                                           


                                                           

       

