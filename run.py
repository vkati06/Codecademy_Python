"""
Create list of ingredients for a new main course and a 
dessert recipe, based on Gordon Ramsay recipes from the 
bbcgoodfood.com website.
http://www.bbcgoodfood.com/recipes/collection/gordon-ramsay
"""

from markov_python.cc_markov_2 import MarkovChain

mc_dessert = MarkovChain(num_key_words=3)

mc_dessert.add_file("dessert.txt")

with open("new_dessert.txt", "w") as textfile:
	for ing in mc_dessert.generate_text(max_length=7):
		textfile.write(str(ing) + "\n")
	textfile.close


mc_main = MarkovChain(num_key_words=3)

mc_main.add_file("main.txt")

with open("new_main_course.txt", "w") as textfile:
	for ing in mc_main.generate_text():
		textfile.write(str(ing) + "\n")
	textfile.close