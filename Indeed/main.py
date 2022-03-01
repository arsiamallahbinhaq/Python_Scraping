import os
import json
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://id.indeed.com/jobs?"
site = "https://id.indeed.com/"
params = {
    'q': 'python developer',
    'l': 'Jakarta'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}
res = requests.get(url, params=params, headers=headers)


def get_total_pages(query, location):
    params = {
        'q': query,
        'l': location
    }
    res = requests.get(url, params=params, headers=headers)

    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    with open('temp/res.html', 'w+') as outfile:
        outfile.write(res.text)
        outfile.close()

    total_pages = []
    #Scraping steps
    soup = BeautifulSoup(res.text, 'html.parser')
    pagination = soup.find('ul', 'pagination-list')
    pages = pagination.find_all('li')
    for page in pages:
        total_pages.append(page.text)

    total = int(max(total_pages))
    #print(total)
    return total

def get_all_items(query, location, start, page):
    params = {
        'q': query,
        'l': location,
        'start': start
    }
    res = requests.get(url, params=params, headers=headers)

    with open('temp/res.html', 'w+') as outfile:
        outfile.write(res.text)
        outfile.close()

    soup = BeautifulSoup(res.text, 'html.parser')

    # Scraping process
    contents = soup.find_all('table', 'jobCard_mainContent')
    print(contents)

    # pick items
    # title, company name, company link, company address
    job_list = []
    for item in contents:
        title = item.find('h2', 'jobTitle').text
        title_rev = title.replace('Baru', '')
        company = item.find('span', 'companyName')
        comp_name = company.text
        try:
            comp_link = site + company.find('a')['href']
        except:
            comp_link = 'Link is not available'
        #sorting data
        data_dict = {
            'title': title_rev,
            'company_name': comp_name,
            'company_link': comp_link
        }
        #print(data_dict)
        job_list.append(data_dict)

    #print('Jumlah data ada:', len(job_list))
    #print(f'Jumlah data: {len(job_list)}')

    #writing json file
    try:
        os.mkdir('json_result')
    except FileExistsError:
        pass
    with open(f'json_result/{query}_in_{location}_page_{page}.json', 'w+') as json_data:
        json.dump(job_list, json_data)
    print('json created')

    return job_list

def create_document(dataFrame, filename):

    try:
        os.mkdir('data_result')
    except FileExistsError:
        pass

    df = pd.DataFrame(dataFrame)
    df.to_csv(f'data_result/{filename}.csv', index=False)
    df.to_excel(f'data_result/{filename}.xlsx', index=False)

    print(f'{filename}.csv and {filename}.xlsx successfully created')

def run():
    query = input('Enter your query: ')
    location = input('Enter your location: ')

    total = get_total_pages(query, location)
    counter = 0
    final_result = []

    #looping
    for page in range(total):
        page += 1
        counter += 10
        final_result += get_all_items(query, location, counter, page)

        # formatting data
        try:
            os.mkdir('reports')
        except FileExistsError:
            pass

        with open('reports/{}.json'.format(query), 'w+') as final_data:
            json.dump(final_result, final_data)

        print('Data JSON Created')
        create_document(final_result, query)



if __name__ == '__main__':
    run()