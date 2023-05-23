import requests
from bs4 import BeautifulSoup
import re



def get_citations_needed_count(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    citations = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')
    return len(citations)

def get_citations_needed_report(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    citations = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')
    report = ""
    sentences_set = set()
    for citation in citations:
        parent_element = citation.find_previous('p')
        passage = parent_element.get_text()
        sentences = re.findall(r'[^.!?]+?\.\[citation needed\]', passage)
        for sentence in sentences:
            sentence = sentence.strip()
            sentences_set.add(sentence)

    for sentence in sentences_set:
        report+=f"Citation needed for \"{sentence}\"\n\n"  
             
    return report




url = 'https://en.wikipedia.org/wiki/History_of_Mexico'
count = get_citations_needed_count(url)
print(f"Number of citations needed: {count}")
print()
report = get_citations_needed_report(url)
print(report)