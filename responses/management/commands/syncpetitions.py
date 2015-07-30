from django.core.management.base import BaseCommand, CommandError

from whresponse.responses.models import Response, Petition

import requests
import bs4

def all_petitions():
    raw = ""
    x = 0
    final = []
    while True:
        response = requests.get("https://petitions.whitehouse.gov/responses/more/all/%s/2/0/" % x).json()['markup']
        if response == "":
            break
        raw += response
        x = x+1

    soup = bs4.BeautifulSoup(raw, "lxml")
    raw_titles = soup.find_all('div', { "class": "title" })
    for x in raw_titles:
        final += [[x.string,x.find('a')['href']]]

    return final

def grab_response(url):
    response = requests.get('https://petitions.whitehouse.gov%s' % url)
    soup = bs4.BeautifulSoup(response.content, "lxml")


    
    petition_response_list = soup.find('div',{'class':'petition-response'}).findAll('p')
    petition_response = "".join([str(x) for x in petition_response_list])


    petition_sections = soup.findAll('div',{'class': 'entry'})

    petitions = []
    totalsig = 0

    for x in petition_sections:
        link = x.find('a')
        rawnum = x.find('span',{'class': 'num'}).text
        num = int(rawnum.replace(',',''))
        petitions += [[num,link['href'],link.text]]
        totalsig += num

    return petition_response, petitions, totalsig

def master_grabber():
    allpetitions = all_petitions()

    final = []

    for x in allpetitions:
        response_text, petition_list, total_signatures = grab_response(x[1])
        final += [{
            'title': x[0],
            'url': x[1],
            'text': response_text,
            'petitions': petition_list,
            'total': total_signatures
        }]

    return final

class Command(BaseCommand):
    help = "Sync Whitehouse Content"

    def handle(self, *args, **options):
        responses = master_grabber()

        for x in responses:
            slug = x['url'].split('/')[2]
            defaults = {
                'title': x['title'],
                'total_signatures': x['total'],
                'response': x['text'],
                'url': x['url']
            }
            
            response, created = Response.objects.get_or_create(slug=slug,defaults=defaults)
            if created:
                for y in x['petitions']:
                    defaults = {
                        'response': response,
                        'title': y[2],
                        'signatures': y[0]
                    }
                    petition, pcreated = Petition.objects.get_or_create(url=y[1],defaults=defaults)
                    if pcreated:
                        print "Created Petition %s (%s)" % (petition.title, petition.pk)
                print "Created Response %s (%s)" % (response.title, response.pk)
