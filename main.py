from flask import Flask, render_template, request

app = Flask(__name__)

# Temporary storage for recipes
recipes = []

@app.route('/')
def index():
    return render_template('index.html', recipes=recipes)

@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        title = request.form['title']
        ingredients = request.form['ingredients'].split('\n')  # Split by new line to create a list
        instructions = request.form['instructions'].split('\n')  # Split by new line to create a list
        recipe = {'title': title, 'ingredients': ingredients, 'instructions': instructions}
        recipes.append(recipe)
        return render_template('index.html', recipes=recipes)
    return render_template('add_recipe.html')









