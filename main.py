class Recipe:
  def __init__(self, name, description, ingredients, steps):
    self.name = name
    self.description = description
    self.ingredients = ingredients
    self.steps = steps

r1 = Recipe("apple pie", "pie with apples", "apples, flour, cinnamon, sugar", ["cut the apples", "mix sugar and cinnamon", "roast them"]) #hard coded a new recipe

print("Welcome to MMY Recipe Book!")
print("Please select an option:\n Enter 1 to Create a Recipe\n Enter 2 to Search For a Recipe By Name\n Enter 3 to Browse All Recipes\n Enter -1 to Terminate the Program") #command line prompt
try: #error handling for any command besides an integer
  user_input = int(input())
  while user_input != -1: #runs until the user terminates the program
    if user_input == 1:
      print("Create a Recipe")
    elif user_input == 2:
      print("Search for a recipe")
    elif user_input == 3:
      print("Browse all recipes")
    else:
      print("Error: Command not found. Please try again.")
      print(
        "Please select an option:\n Enter 1 to Create a Recipe\n Enter 2 to Search For a Recipe By Name\n Enter 3 to Browse All Recipes\n Enter -1 to Terminate the Program")
    user_input = int(input())
except ValueError: #if command not an integer, send error message, and terminate the program
  print("Error: Command not found. Please try again.")

print("Thank you for participating in the recipe book!")
exit()