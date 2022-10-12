from pymongo import MongoClient
import pymongo

def get_database():
	username = "recipebook"
	password = "mmyrecipebook123"
	CONNECTION_STRING = f"mongodb+srv://{username}:{password}@cluster0.hq13anp.mongodb.net/?retryWrites=true&w=majority"
	client = MongoClient(CONNECTION_STRING)
	database = client.get_database('recipe-book')
	return database

def sendRecipeToDatabase(recipe):
    recipeBook = get_database()
    recipes = recipeBook['recipes']
    recipeData = recipe.__dict__
    recipes.insert_one(recipeData)

def getRecipeFromDatabase(recipeName):
    recipeBook = get_database()
    recipes = recipeBook['recipes']
    if recipes.count_documents({'name': recipeName}) == 0:
        return False
    else:
        return recipes.find_one({'name': recipeName})

def getRecipeSubstringFromDatabase(recipeName):
    recipeBook = get_database()
    recipes = recipeBook['recipes']
    if recipes.count_documents({"name" : {'$regex' : recipeName}}) == 0:
        return False
    else:
        return db.users.findOne({"name" : {'$regex' : recipeName}})

def getRecipesFromDatabase(delimiter):
    recipeBook = get_database()
    recipes = recipeBook['recipes']
    recipeList = [val for val in recipes.find()]
    print(recipeList)
    if len(recipeList) >= delimiter:
        return recipeList[:delimiter]
    else:
        return recipeList