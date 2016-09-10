import urllib2
from bs4 import BeautifulSoup
import re

"""
Collect the ingredients of some Gordon Ramsay's recipes
from http://www.bbcgoodfood.com/recipes/collection/gordon-ramsay, 
then write them into two text files (main course and dessert).
"""

main_course_urls = ['http://www.bbcgoodfood.com/recipes/711659/rack-of-lamb-with-warm-salad-of-mixed-beans-and-sl', \
'http://www.bbcgoodfood.com/recipes/5032/beef-bourguignon', \
'http://www.bbcgoodfood.com/recipes/2538/beef-wellington', \
'http://www.bbcgoodfood.com/recipes/2197/rocket-mushroom-and-bacon-quiche', \
'http://www.bbcgoodfood.com/recipes/2476/gordons-mix-and-match-steak', \
'http://www.bbcgoodfood.com/recipes/4916/pork-and-ham-pie', \
'http://www.bbcgoodfood.com/recipes/644646/panfried-sea-trout-peas-and-chorizo-fricasse', \
'http://www.bbcgoodfood.com/recipes/473631/spaghetti-with-seafood-velout', \
'http://www.bbcgoodfood.com/recipes/5934/mediterranean-salmon-fillet']

dessert_urls = ['http://www.bbcgoodfood.com/recipes/359609/frozen-banana-and-praline-parfait', \
'http://www.bbcgoodfood.com/recipes/4806/chocolate-marquise', \
'http://www.bbcgoodfood.com/recipes/6591/lemon-tart-with-summer-berries', \
'http://www.bbcgoodfood.com/recipes/558628/strawberry-and-white-chocolate-millefeuille',
'http://www.bbcgoodfood.com/recipes/4443/strawberry-sable-tart', \
'http://www.bbcgoodfood.com/recipes/4630/summer-berry-meringues', \
'http://www.bbcgoodfood.com/recipes/4778/pear-tarte-tatin']

def create_ing_list(dish_type, file_name):

      if dish_type == "main":
            my_links = main_course_urls
      elif dish_type == "dessert":
            my_links = dessert_urls
      else:
            return

      for links in my_links:

            req = urllib2.Request(links, headers={'User-Agent' : "Something"})
            html = urllib2.urlopen(req)

            soup = BeautifulSoup(html, 'lxml')

            with open(file_name, "a") as textfile:

               for tag in soup.find_all("li", "ingredients-list__item"):
                  	if len(tag.contents) > 1:
                  		for tags in tag.contents:
                  			try:
                  				textfile.write(tag.contents[0] + tags.text + "\n")
                  			except:
                  				pass
                  	else:
                  		try:
                  			textfile.write(tag.text + "\n")
                  		except:
                  			pass
            textfile.close

"""
Probably this is not the best way to ged rid of references / links
and encoding problems :(
"""

create_ing_list("main", "main.txt")
create_ing_list("dessert", "dessert.txt")