from bs4 import BeautifulSoup

html_doc = """
<html>
    <head>
    <title>Titre de votre site</title>
    </head>
    <body>
        <p class="c1 c2">texte a lire1</p>
        <p class="c3">texte a lire2</p>
    </body>
</html>
"""

soup = BeautifulSoup(html_doc)

print soup.extract()

for p in soup.find_all('p'):
    print p.get("class")
    
print "---------------"

for p in soup.find_all('p'):
    print p
    p.string = "NV T"
    print p
    
print soup

print "-----------------------"

for p in soup.find_all('p'):
    n = BeautifulSoup('<pre>%s</pre>' % p.string)
    p.replace_with(n.body.contents[0])
    
print soup.prettify()  
