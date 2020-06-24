import pywikibot
import csv

site = pywikibot.Site()

with open('bitcoinwiki-backup.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)

    for p in site.allpages():
        try:
            txt = p.get()
            csvwriter.writerow([p.title(), txt])
        except pywikibot.exceptions.IsRedirectPage:
            print ('ignore redirects for now')
        

