# Made to Share Recipe Online Recipe Shearing Site 

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

!Register](https://res.cloudinary.com/dbwtdwgnt/image/upload/v1621762980/3rd%20project/IMG_0272_ihyfkl.jpg)

![Upload Recipe](https://res.cloudinary.com/dbwtdwgnt/image/upload/v1621762979/3rd%20project/IMG_0270_xj3ljg.jpg)

**Media used in the project**

All recipes uploaded are my own photos and recipes and the images can be found on [Cookpad](https://cookpad.com)
Imager for the base.html was downloaded from [Unsplash](https://unsplash.com/photos/jUPOXXRNdcA)

**Following websites were used for searching for answers**

[Stckoverflow](https://stackoverflow.com/) , mainly rely on this website searching for solution, although never copied code 
With the documentation on Flask I was using the following website: [Flask](https://flask.palletsprojects.com/en/2.0.x/)
Many search would come with flask and python questions on the following website: [GeekforGeeks](https://www.geeksforgeeks.org/)
How to use SelectMultipleField, although i didn’t end up using it: [SelectMultiple](https://stackoverflow.com/questions/13558345/flask-app-using-wtforms-with-selectmultiplefield)
