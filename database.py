from pymongo import MongoClient
import pymongo

def get_database():
	username = "recipebook"
	password = "ItjW9fWDnItWKufO"
	CONNECTION_STRING = f"mongodb+srv://{username}:{password}@cluster0.hq13anp.mongodb.net/?retryWrites=true&w=majority"
	client = MongoClient(CONNECTION_STRING)
	database = client.get_database('recipe-book')
	return database

def sendRecipeToDatabase(recipe):
    recipeBook = get_database()
    recipes = recipeBook['recipes']
    recipe = recipes.__dict__
    recipes.insert_one(recipe)

def getRecipeFromDatabase(recipeName):
    recipeBook = get_database()
    recipes = recipeBook['recipes']
    if recipes.count_documents({'name': recipeName}) == 0:
        print(f"Sorry, but recipe {recipeName} does not exist...")
    else:
        return recipes.find_one({'name': recipeName})

def getRecipeSubstringFromDatabase(recipeName):
    recipeBook = get_database()
    recipes = recipeBook['recipes']
    if recipes.count_documents({"name" : {'$regex' : recipeName}}) == 0:
        print(f"Sorry, but giveaway #{giveawayID} does not exist...")
    else:
        db.users.findOne({"name" : {'$regex' : recipeName}})