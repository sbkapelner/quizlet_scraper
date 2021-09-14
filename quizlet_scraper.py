import requests
from bs4 import BeautifulSoup
import pandas as pd

my_headers = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15', 
'Accept-Encoding': 'gzip, deflate', 
'Accept': '*/*', 
'Connection': 'keep-alive'
}

html = requests.get('https://quizlet.com/1944473/linux-bash-commands-flash-cards/', headers=my_headers).text

soup = BeautifulSoup(html,'html.parser')

list_name = soup.title.text[0:-21]

span_tags = soup.find_all('span')

span_tags_clean = [item for item in span_tags if item.get('class') != None]

terms = [item.text for item in span_tags_clean if 'TermText' in item.get('class')]

terms_1 = [terms[i] for i in range(0,len(terms)) if i%2 == 0]
terms_2 = [terms[i] for i in range(0,len(terms)) if i%2 != 0]

pd.set_option("display.max_rows", None, "display.max_columns", None)
df_terms = pd.DataFrame(terms_2, terms_1, columns=[''])

print(f"\nList Name: {list_name}")
print(df_terms)

num_terms = soup.find_all('h4')[0].text.replace('(','').replace(')','')
print('\n'+num_terms[0:17]+':'+num_terms[17:])
