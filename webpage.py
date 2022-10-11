from flask import Flask, render_template, request
app = Flask(__name__)

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

@app.route("/")
def home():
    return render_template('home.html')



# @app.route('/browse', methods=['GET', 'POST'])
# def browse():
# 	if request.method == 'POST':
# 		return render_template('browse.html', shortcode=request.form['shortcode'])
# 	elif request.method == 'GET':
# 		return 'A GET request was made'
# 	else:
# 		return 'Not a valid request method for this route'


@app.route("/task", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
    	task = request.form.to_dict()["options"]
    	if task == "create":
    		return render_template('create.html')
    	elif task == "search":
    		return render_template('search.html')
    	elif task == "browse":
    		return render_template('browse.html', list_of_recipes=list_of_recipes)
    	else:
       		return "Error: Unable to Retrieve Your Requested Option"
    elif request.method == 'GET':
        return render_template('home.html', form=form)

@app.route("/create", methods=['POST'])
def create_a_recipe():
	print(request.form)
	return "Recipe Created" 

@app.route("/displayrecipe", methods=['POST'])
def display_the_recipe():
	print("display")
	print(request.form.to_dict())
	recipe_name = request.form.to_dict()["options"]
	print(recipe_name)
	for recipe in list_of_recipes:
		if recipe_name in recipe.name:
			return render_template('viewrecipe.html', name=recipe.name, description=recipe.description, ingredients=recipe.ingredients, steps=recipe.steps)
	return "Error: Recipe Not Found"

if __name__ == "__main__":
    app.run()

