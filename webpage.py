from flask import Flask, render_template, request
from fuzzywuzzy import fuzz
from database import get_database, sendRecipeToDatabase, getRecipeFromDatabase, getRecipeSubstringFromDatabase, getRecipesFromDatabase

app = Flask(__name__,template_folder='./templates',static_folder='./assets')

class Recipe: #created the recipe class
	def __init__(self, name, description, ingredients, steps):
		self.name = name
		self.description = description
		self.ingredients = ingredients
		self.steps = steps

r1 = Recipe("apple pie", "pie with apples", "apples, flour, cinnamon, sugar", ["cut the apples", "mix sugar and cinnamon", "roast them"]) #hard coded a new recipe
r2 = Recipe("pumpkin pie", "pie with pumpkins", "pumpkin, flour, cinnamon, sugar", ["cut the pumpkin", "mix sugar and cinnamon", "roast them"]) #hard coded a new recipe
r3 = Recipe("pecan pie", "pie with pecans", "pecans, flour, cinnamon, sugar", ["open the pecan box", "mix sugar and cinnamon", "roast them"]) #hard coded a new recipe


list_of_recipes = [r1, r2, r3] #hard coded list of recipes


def searchBySubstring(recipe_name): #if the recipe the user is searching for matches a substring within another recipe then it selects the first recipe that matches
	recipe_num = 0
	list_of_recipes = getRecipesFromDatabase(10)
	for recipe in list_of_recipes:
		recipe_num+=1
		if(recipe_name.lower() in recipe['name'].lower()):
			return True, recipe, recipe_num
	return False, -1, -1

def searchByFuzzy(recipe_name): #selects and returns the recipe that is slightly off from other recipes
	recipe_num = 0
	list_of_recipes = getRecipesFromDatabase(10)
	for recipe in list_of_recipes:
		recipe_num+=1
		if(fuzz.ratio(recipe_name.lower(), recipe['name'].lower()) >= 70): #if the fuzzy ratio is 70% or higher, then it will return the recipe
			return True, recipe, recipe_num
	return False, -1



@app.route("/")
def home():
		return render_template('home.html')

@app.route("/homepage")
def homepage():
		return render_template('home.html')

@app.route("/createpage")
def createpage():
		return render_template('create.html')

@app.route("/searchpage")
def searchpage():
		return render_template('search.html')

@app.route("/browsepage")
def browsepage():
	return render_template('browse.html', list_of_recipes=getRecipesFromDatabase(10))


@app.route("/errorpage")
def errorpage():
		return render_template('error.html')



# @app.route('/browse', methods=['GET', 'POST'])
# def browse():
# 	if request.method == 'POST':
# 		return render_template('browse.html', shortcode=request.form['shortcode'])
# 	elif request.method == 'GET':
# 		return 'A GET request was made'
# 	else:
# 		return 'Not a valid request method for this route'


# @app.route("/task", methods=['GET', 'POST'])
# def index():
# 		if request.method == 'POST':
# 			task = request.form.to_dict()["options"]
# 			if task == "create":
# 				return render_template('create.html')
# 			elif task == "search":
# 				return render_template('search.html')
# 			elif task == "browse":
# 				return render_template('browse.html', list_of_recipes=getRecipesFromDatabase(10))
# 			else:
# 					return "Error: Unable to Retrieve Your Requested Option"
# 		elif request.method == 'GET':
# 				return render_template('home.html', form=form)

@app.route("/create", methods=['POST'])
def create_a_recipe():
	recipe_dict = request.form.to_dict()
	# list_of_recipes.append(Recipe(recipe_dict['recipename'], recipe_dict['recipedescription'], recipe_dict['recipeingredients'], recipe_dict['recipesteps'].split(","))) #adds the recipe object to the internal list of recipes
	sendRecipeToDatabase(Recipe(recipe_dict['recipename'], recipe_dict['recipedescription'], recipe_dict['recipeingredients'], recipe_dict['recipesteps'].split(","))) #adds the recipe object to the internal list of recipes
	return render_template('viewrecipe.html', name=recipe_dict['recipename'], description=recipe_dict['recipedescription'], ingredients=recipe_dict['recipeingredients'], steps=recipe_dict['recipesteps'].split(","))

@app.route("/displayrecipe", methods=['POST'])
def display_the_recipe():
	print("display")
	print(request.form.to_dict())
	recipe_name = request.form.to_dict()["options"]
	# print(recipe_name)
	# for recipe in list_of_recipes:
	# 	if recipe_name in recipe.name:
	x, selected_recipe, recipe_num = searchBySubstring(recipe_name) #search by substring matching
	if selected_recipe != False:
		return render_template('viewrecipe.html', name=selected_recipe['name'], description=selected_recipe['description'], ingredients=selected_recipe['ingredients'], steps=selected_recipe['steps'])
	return render_template('error.html')

@app.route("/search", methods=['POST'])
def search_for_recipe():
	recipe_name = request.form.to_dict()['search']
	x = False
	recipe_num = 0
	list_of_recipes = getRecipesFromDatabase(10)
	for recipe in list_of_recipes:
		recipe_num+=1
		print(recipe)
		if(recipe['name'].lower() == recipe_name.lower()): #search for a recipe exactly by name
			x = True
			selected_recipe = recipe
			return render_template('viewrecipe.html', name=selected_recipe['name'], description=selected_recipe['description'], ingredients=selected_recipe['ingredients'], steps=selected_recipe['steps'])
	if x == False:
		x, selected_recipe, recipe_num = searchBySubstring(recipe_name) #search by substring matching
		if not x:
			x, selected_recipe, recipe_num = searchByFuzzy(recipe_name) #search by fuzzy searching
			if not x:
				return render_template('error.html')
			else:
				return render_template('viewrecipe.html', name=selected_recipe['name'], description=selected_recipe['description'], ingredients=selected_recipe['ingredients'], steps=selected_recipe['steps'])
		else:
			return render_template('viewrecipe.html', name=selected_recipe['name'], description=selected_recipe['description'], ingredients=selected_recipe['ingredients'], steps=selected_recipe['steps'])

if __name__ == "__main__":
		app.run()

