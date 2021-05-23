# Made to Share Recipe Online Recipe Shearing Site 

**PLease click [here](https://cookbook-milestone-project.herokuapp.com/) to check out the deplyed site**

## User Experience:

### Project Goals:

The goal of this project is to create a nice, healthy recipe sharing website that is also suitable for people on Keto diet.
The target audience are homecooks, new cooks, those who love to share their creations and those who just started cooking or dieting, so basically everyone can benefit from the site. My passion is cooking and healthy cooking. That's why I created this site and I am also a qualified chef so recipes and pictures which I uploaded were already in my repertoar. 

#### User Goals:
**Generic**

* Easy to navigate website with amazing home cooked recipes
* Find food, that cooked by other “ordinary” people, that means everyone can recreate these recipes at home 
* Upload and take pride for those dishes that the user created 
* Search Breakfast, Main Meal, Snack, and Keto recipes (which also included in the other categories as well, because even diet food can be easy to make and very taste at the same time)

**Non registered or non logged in Users**:

* User starts on the Home page where they can find on the navigation bar a Home, Sign In/ Register and All Recipes tab
* Also in the main image a search bar is presented 
* And on the Home page body there are 4 links that take the user for the Breakfast, Main Meal, Snacks and Keto categories
*  Search via the search bar: With this tool the entered word searched through the recipe title, story, ingredients and category lists. The search is searches by words, so if the recipe contains that word it will come up in the results, If no match is found in the recipes, user will be ask to make another search
* Users without registration or login can also see All Recipes that have been uploaded to the site, by clicking the All Recipes tab in the navbar. RThis will display all recipes have been uploaded and will return on the page in a card format, showing the image, title, author name and the short story of the recipe
* By clicking View Recipe the user is navigated to the full recipe page, where can read the full description, ingredients and step of the dish
* If the user wishes to register then they can do it by clicking in the navigation bar to the Sign in/ Register tab and select register from the 2 tabs there. To able to successfully register, user needs to provide password for confirmation again and must choose a username that is not taken yet



**Logged In users**:

*If user creates or already have an account and entered valid details, navigation bar expends and displayed the following options: Home, Upload Recipes, My Recipes, Sign Out, All Recipes
* Search and select categories options are also available for these user in the same way mentioned above 
* User is able to upload recipe by select so from the navbar: providing url for the image, adding title, a short story, ingredients separated by comma, steps and selecting from the drop down options if the recipe is keto and which categories they wish to call their creation
* On My Recipe tab they able to see all their uploaded recipes, and by clicking to view them they will be presented with 2 buttons, giving the options of Edit or Delete their recipe
* The Delete recipe button is displayed by a red button and by calling it will take the user to the Delete pager where a warning sign reassuring that this is definitely what is the user wish to do. If the user doesn't want to delete the recipe, a cancel button is provided which takes the user back to the original recipe. If user wished to go ahead with the delation, then by clicking again a red delete button, their recipe is deleted from the page and database and the user is take back to their recipe My Recipe page, where a flash message inform them about the successful recipe removal
* Similarly, if the user wishes to edit their recipe they can do so by clicking on the edit button and they will be taken to the edit page which is the same looking as the upload recipe page, but with the already filled in data, ready to edit. They are able to change all the fillers that they entered through the upload recipe process. If the user changed their mind about editing the recipe, a cancel button is provided next to the save button and they are taken back to the original recipe page

**Sign Out**:

User is able to sign out of their profile by clicking Sign Out tab on the navbar

**All Recipes**

Users are also able to browse through all the recipes other people have uploaded without searching for selecting special categories. In this case they can get some inspiration and might return to later to cook that recipe, or it is great for those who can’t decide what they fancy to eat or cook

#### Project and wireframes:
**Generic**

* The project was created by using:
	*Python
	*HTML5
	*CSS/Bootstrap
	*Mongo
	*Flask
	*JS/JQuery
The bases of the website was downloaded from [Start Bootstrap/theme/agency](https://startbootstrap.com/theme/agency)

**Following CRUD**:

* User is able to create a recipe (Upload Recipe)
* User is able to read data by searching for the recipes or navigate to them by url 
* User is able to edit or update their data entered by using Edit Recipe 
* User is able to delete data from the database by clicking Delete Recipe

**Wireframes**:

![Home page](https://res.cloudinary.com/dbwtdwgnt/image/upload/v1621762978/3rd%20project/IMG_0265_hzyr9g.jpg)

![Category Page](https://res.cloudinary.com/dbwtdwgnt/image/upload/v1621762978/3rd%20project/IMG_0267_fms1li.jpg)

![Profile Page](https://res.cloudinary.com/dbwtdwgnt/image/upload/v1621762979/3rd%20project/IMG_0269_sqmanx.jpg)

![Sign In](https://res.cloudinary.com/dbwtdwgnt/image/upload/v1621762980/3rd%20project/IMG_0271_ctf54w.jpg)

![Register](https://res.cloudinary.com/dbwtdwgnt/image/upload/v1621762980/3rd%20project/IMG_0272_ihyfkl.jpg)

![Upload Recipe](https://res.cloudinary.com/dbwtdwgnt/image/upload/v1621762979/3rd%20project/IMG_0270_xj3ljg.jpg)

**Media used in the project**

All recipes uploaded are my own photos and recipes and the images can be found on [Cookpad](https://cookpad.com)
Imager for the base.html was downloaded from [Unsplash](https://unsplash.com/photos/jUPOXXRNdcA)

**Following websites were used for searching for answers**

[Stckoverflow](https://stackoverflow.com/) , mainly rely on this website searching for solution, although never copied code 
With the documentation on Flask I was using the following website: [Flask](https://flask.palletsprojects.com/en/2.0.x/)
Many search would come with flask and python questions on the following website: [GeekforGeeks](https://www.geeksforgeeks.org/)
How to use SelectMultipleField, although i didn’t end up using it: [SelectMultiple](https://stackoverflow.com/questions/13558345/flask-app-using-wtforms-with-selectmultiplefield)

#### Testing and usertesting :
**Validators**
* [HTML](https://validator.w3.org/)
*[Python](https://extendsclass.com/python-tester.html)

**Bugs**:
*The site was testing regularly, after each class ot app was created and debugger was run constantly on the site. I have had a bug during building the @ all_recipes function as it was not returning all the data from the recipes when it was submitted, it either returned all the recipes or it returned only one category. After reading the documentation and looking at the code on stack overflow I figured the right way to structure the app.
* During login page build the return was either successfully registered and returned to the signed in page or got an error message, figured to swap the code other way around and first declare if the user is not existing then declare that later in the @app route.
* Also used Breakpoint to debug the code most of the time, which helped to know the when is the point my code is executed so it most of the time lead to an answer, instead of searching through massive amount of answers and codes from the web
* Installed and deleted many elements of FlaskForms and wtforms, as found an easier way to deal with the issues. Eg: stacked with the way to upload the image in the recipe and use path. In the end my mentor pointed me in the right direction and gave me a hint to use url to upload images. In this case I can avoid people uploading large data into my database and can reduce viruses being uploaded to the base. 
* Issue with the bolean keto button on upload recipe page which in the lack of time led me to the conclusion to just use a string instead a thick box true or false boolean. In the end i changed the keto recipe to a yes or no drop down select field and string
* On the final deployment of the project, Heroku was not deploying my project, so got in touch with the student support where they advise me to update again my requirements.txt with the full list, which work, but in the same time totally destroyed my code, to the extend it was broken in every way it could be. 
Fixed and changed all session.get(‘existing_user’) in Edit Upload and Login classes and tested the site if it works. When I tried to deploy again in Heroku There was another exact same error message which was fixed before. So got in touch with Student Tutors again. 
Installed and reinstalled wireframes and forms, disconnected GitHub and Connected again with Heroku. In the end those files were causing the problems which were extras from installations. It affected my werkzeug hashing code but doesn't affected in the  database. 
Most importantly could deployed my project ASAP


**Usertesting**
* The site works in every different and media been added to the styling, it has been tested 
* User feedback is positive and easy to navigate on site
* During user testing the biggest issue i found was the keto recipe button which later was changed to string and selectfiels 

## Deployments
- My project was built and it is stored on Github I created a master branch for the project in the following way: Go to your GitHub account and select “New Repository” from the drop down menu Next to the owner after the / add a short name to repository Select add README file and add .gitignore file Create repository
- If you wish to clone: On GitHub navigate to the main page of the repository Click clone or download green button Click on the copy icon at the end of the https:// link Open the terminal Navigate to the location where the repository is going to be stored With the repository URL enter the following $ git clone https://github.com/ZitaBalint/Third-Milestone-Project-Cookbook.git Press enter and the local repository was created
- Please follow this link to [Get started with Heroku](https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true)
- My Recipe sharing website [Made To Share](https://cookbook-milestone-project.herokuapp.com/) was deployed in Heroku and can be reached by clickinh on the link 