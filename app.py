from scrape import scrape
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

#create an instance of flask 
app = Flask(__name__)

#connect to Mongo
mongo = PyMongo(app, uri='mongodb://localhost:27017/mars_db')

#route to index.html 
@app.route("/")
def web():
    # mars = mongo.db.mars.find_one()
    # return render_template('index.html', mars=mars)
    
    # Find one record of data from mongo db
    mars = mongo.db.mars.find_one()

    print(mars)

    # Return template and data
    return render_template("index.html", mars=mars)

# Route that will trigger the scrape function
@app.route("/scrape")
def mars_scrape():

    # Run the scrape function
    mars_dict = scrape()

    # Update the Mongo database using update and upsert=True
    mongo.db.mars.update({}, mars_dict, upsert=True)

    # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)



# if '__main__'==__name__:
#     app.run(debug=True)