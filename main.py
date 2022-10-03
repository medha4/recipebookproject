class Recipe:
  def __init__(self, name, description, ingredients, steps):
    self.name = name
    self.description = description
    self.ingredients = ingredients
    self.steps = steps

r1 = Recipe("apple pie", "pie with apples", "apples, flour, cinnamon, sugar", ["cut the apples", "mix sugar and cinnamon", "roast them"])

