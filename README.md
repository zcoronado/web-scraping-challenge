# Web Scraping Homework - Mission to Mars

![mission_to_mars](Images/mission_to_mars.png)

In this project, I build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. 


## Step 1 - Scraping

Completed my initial scraping using Jupyter Notebook, Pandas, and Requests/Splinter.

* Scraped the [Mars News Site](https://redplanetscience.com/) and collect the latest News Title and Paragraph Text. A

### JPL Mars Space Images - Featured Image

* Visited the url for the Featured Space Image site [here](https://spaceimages-mars.com).

### Mars Facts

* Visited the Mars Facts webpage [here](https://galaxyfacts-mars.com) and scraped the table containing facts about the planet including Diameter, Mass, etc.


### Mars Hemispheres

* Visited the astrogeology site [here](https://marshemispheres.com/) to obtain high resolution images for each of Mar's hemispheres.

## Step 2 - MongoDB and Flask Application

Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.


![final_app_part1.png](Images/final_app.png)

- - -