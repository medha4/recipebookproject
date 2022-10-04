class Recipe:
  def __init__(self, name, description, ingredients, steps):
    self.name = name
    self.description = description
    self.ingredients = ingredients
    self.steps = steps

r1 = Recipe("apple pie", "pie with apples", "apples, flour, cinnamon, sugar", ["cut the apples", "mix sugar and cinnamon", "roast them"]) #hard coded a new recipe
r2 = Recipe("pumpkin pie", "pie with pumpkins", "pumpkin, flour, cinnamon, sugar", ["cut the pumpkin", "mix sugar and cinnamon", "roast them"]) #hard coded a new recipe
r3 = Recipe("pecan pie", "pie with pecans", "pecans, flour, cinnamon, sugar", ["open the pecan box", "mix sugar and cinnamon", "roast them"]) #hard coded a new recipe


list_of_recipes = [r1, r2, r3] #hard coded list of recipes

def createRecipe():
	print("Please enter the name of your recipe: ")
	recipeName = input()
	print("Please enter the description for your recipe: ")
	recipeDescription = input()
	print("Please enter the ingredients for your recipe separated by commas: ")
	recipeIngredients = input()
	print("Please enter the steps for your recipe separated by commas")
	recipeSteps = input()
	list_of_recipes.append(Recipe(recipeName, recipeDescription, recipeIngredients, recipeSteps.split(",")))
	print("Recipe Created")

def displayRecipe(recipe_num):
  selected_recipe = list_of_recipes[recipe_num-1]
  print(selected_recipe.name)
  print("Description: ", selected_recipe.description)
  print("Ingredients: ", selected_recipe.ingredients)
  print("Steps:")
  step_counter = 0
  for step in selected_recipe.steps:
    step_counter+=1
    print(step_counter, step)
  response = input("Press enter to view this recipe step by step, or type SKIP.")
  if response.lower() != "skip":
    stepThroughRecipe(recipe_num)
  print("Enter any integer to return to the main menu :)")

def stepThroughRecipe(recipe_num):
  selected_recipe = list_of_recipes[recipe_num-1]
  steps = selected_recipe.steps
  step_counter = 0
  while(step_counter < len(steps)):
    print(str(step_counter+1) + " " + steps[step_counter])
    response = input("Press enter to view the next step, or enter EXIT to stop viewing this recipe.")
    if(response.lower() == "exit"):
      break
    else:
      step_counter += 1

print("Welcome to MMY Recipe Book!")
print("Please select an option:\n Enter 1 to Create a Recipe\n Enter 2 to Search For a Recipe By Name\n Enter 3 to Browse All Recipes\n Enter -1 to Terminate the Program") #command line prompt
try: #error handling for any command besides an integer
  user_input = int(input())
  while user_input != -1: #runs until the user terminates the program
    if user_input == 1:
      print("Create a Recipe Here")
      createRecipe()
    elif user_input == 2:
      print("Search for a recipe")
    elif user_input == 3:
      print("Browse All Recipes")
      recipe_counter = 0
      for recipe in list_of_recipes:
        recipe_counter+=1
        print(recipe_counter, recipe.name)
      print("Which number recipe would you like to view?") #need to add error handling
      recipe_to_view = int(input())
      while recipe_to_view > len(list_of_recipes) or recipe_to_view < 0:
        print("Invalid number, please try again")
        recipe_to_view = int(input())
      displayRecipe(recipe_to_view)
    else:
      print("Error: Command not found. Please try again.")
      print(
        "Please select an option:\n Enter 1 to Create a Recipe\n Enter 2 to Search For a Recipe By Name\n Enter 3 to Browse All Recipes\n Enter -1 to Terminate the Program")
    print(
      "Please select an option:\n Enter 1 to Create a Recipe\n Enter 2 to Search For a Recipe By Name\n Enter 3 to Browse All Recipes\n Enter -1 to Terminate the Program")
    user_input = int(input())
except ValueError: #if command not an integer, send error message, and terminate the program
  print("Error: Command not found. Please try again.")

print("Thank you for participating in the recipe book!")
exit()