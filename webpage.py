from flask import Flask, render_template, request
app = Flask(__name__)

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
    		return render_template('browse.html')
    	else:
       		return "Error: Unable to Retrieve Your Requested Option"
    elif request.method == 'GET':
        return render_template('home.html', form=form)

@app.route("/create", methods=['POST'])
def create_a_recipe():
	print(request.form)
	return "Recipe Created" 

if __name__ == "__main__":
    app.run()

