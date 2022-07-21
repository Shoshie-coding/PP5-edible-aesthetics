# **Cogito, ergo sum**


# Photo Aesthetics

## **Table of Contents**

1. [About this project](#About-project)
2. [SEO and Marketing](#SEO-marketing)

3. [UX](#UX)

4. [User Stories](#user-stories)
5. [Main Features](#features)
6. [Wire Frames](#wire-frames)
7. [Agile Methodology](#agile)
8. [Testing](#testing)
9. [Technologies used](#technologies)
6. [Deployment](#deployment)
9. [Credits](#credits)

## **About this project**
This is a fully-responsive e-commerce website that was built using Django framework with Python and Booostrap as main technologies. 
This website represents an online shop that sells high quality photo prints and fine art prints. It sells also has prints of period or vintage art pieces. 
Users can login for an account and they can sign up to the newsletter. They can add their favorite prints to the wishlist and view these items from their profile. 
The targeted demographis is anyone who enjoys art and photography and want to buy good quality prints.  

## **SEO and Marketing**

## **User Stories**
User Stories have been achieved to built this website as follows:

### Viewing product and navigation

As a Shopper I can view a list of products so that I can see what the shop can offer 

As a Shopper I can view specific product details so that I can see the price, description and product image

As a Shopper I can register for an account so that I can set up a profile for the website and view it

As a Shopper I can see all my purchases so that I can see how much I spent on each item

As a Shopper I can see what is in my shopping bag so I can can check all the items are correct

As a Shopper I can identify the categories of products on the website so I can see all my options before making a purchase



### Registration and User accounts


- As a Shopper I can login and logout so that I can access my personal account information

- As a Shopper I can easily recover my password if I forget it so that I can access my account info and purchase history

- As a Shopper I can receive a registration confirmation email so that I can verify my registration to the site was successful

- As a Shopper I can set up a personalised user profile so that I can view my order history and personal details


### Searching and Sorting products


- As a Shopper I can sort the list of available products so that I can easily identify best priced and categorically sorted products

- As a Shopper I can sort a specific category of product so that I can find the best priced in a specific category or sort the products by name

- As a Shopper I can sort multiple categories of products at the same time so that I can find the best priced products across categories such as ‘photography’ or ‘period art prints’.

- As a Shopper I can search for a product by name or description so that I can find specific product I’d like to purchase

- As a Shopper I can see the number of results for my search so I can see if the product I want is available


### Purchasing and Checkout

- As a Shopper I can select the size and quantity of products when purchasing them so that I can be sure I make no mistakes about the quantity and print size

- As a Shopper I can see messages from the shop so that I know if my item was added to the bag or removed


- As a Shopper I can view items in my bag to be purchased so that I can identify the total cost of my purchase and all items I will receive

- As a Shopper I can adjust the quantity of items in my bag so that I can make changes to my purchase before checkout

- As a Shopper I can easily enter my payment information so that I can add to checkout my desired products

- As a Shopper I know that my personal and payment information is safe and secure so that I can confidently provide the necessary card details to make a purchase


### Wishlist

- As a Shopper I can navigate to a product and click on the add to Wishlist button so that I can add the products I want to purchase in the future

- As a Shopper I can navigate to My Profile and remove items from My Wishlist so that I can remove a product I’m not interested in buying anymore


### Admin & Management (CRUD)

- As an Admin User I can add new products to the website so that I can provide clients with new incoming products.

- As an Admin User I can modify product details so that I can update product details

- As an Admin User I can delete products so that I can update the site when a product isn’t being sold anymore



### Newsletter subscriber

- As a **Shopper / Admin** I want to **register to the site's newsletter** so that **I can be kept up to date with marketing updates and news**


- As a Shopper / Admin I can see a pop up message when signing up for newsletter

### Pop up messages / Toasts

- As a site user I want to see pop-up messages when I make an action to confirm transactions and changes** so that I can rest assured my transactions and activities have been successful**


### Deploy project

- As a Shopper I can access the website in a publicly accessible domain so that I can view the website and use its functionalities


### User Stories to implement

- As a Shopper I want to be able to see price changing depending on which print size I chose so that I can see if the price is different or not.


## **SEO and Marketing**
I've created a custom Newsletter model to send marketing emails and updates on new products and releases. 

I've also create a Facebook business page in order to keep in touch with clients and users on social media as well.
The page can be accessed here [Facebook page](https://www.facebook.com/profile.php?id=100083382653686&is_tour_dismissed=true)

### SEO
In order to improve SEO for this website I've used several main keywords such as fine art prints, period art prints, nature photography. I've also used descriptive meta tags such as landscape photography and calm landscape prints. 




## **Deployment**

### GitHub Pages
The project was deployed to GitHub Pages using the following steps:
1. Go to GitHub and locate the repository to be deployed [GitHub Repository](https://github.com/Shoshie-coding/project-1)
2. On the top right-hand side - click Settings
3. Scroll down until you locate the Pages tab on the left-hand side navigation menu. 
4. Under Source - click on the drop-down called None and select Main and leave the /(root) option as it is. 
5. Click Save 
6.  The Page refreshes itself - message " Your site is ready to be published at https://shoshie-coding.github.io/project-1/. 
7. Refresh page - notice message -  Your site is published at https://shoshie-coding.github.io/project-1/. 

### Deployment on Heroku

This project was deployed on Heroku using these steps:

2. Log in to Heroku and create a new app.
3. Add the Heroku Postgres add-on
4. Go to gitpod workspace and install dj_database_url and psycopg2 and freeze requierements in requirements.txt
5. Make migrations, load categories and respective products
6. Create Heroku Super User and follow onscreen prompts
8. Create an if statement so debug is set be true only if there's a variable called development in os.environ otherwise it will use the default configuration.
9. Create a Procfile to tell Heroku to create a web dyno;
10. Disable COLLECTSTATIC with command 'heroku config:set DISABLE_COLLECTSTATIC=1 --app photo-aesthetics'
11. Add the Heroku app under ALLOWED_HOSTS in Settings.py
12. Deploy to Heroku
13. In Heroku, inside the app go to Deploy tab and set deploy to Github, search for the project repo and click connect. Set deployment to automatic preferably so 
12. Generate secret key for the Heroku app and add it to env.py which is included in the .gitignore file for safety purposes. 
13. In settings.py set up debug to true only if there is a variable called development in the environment;



4. Complete the config vars section
5. Link Heroku and GitHub accounts together
6. Select the Github repo that you use for the app and give it a name
7. Click on deploy.



### Clone a repository using these steps:
1. On GitHub, navigate to the main page of the repository.

2. Above the list of files, click the Code button.
3. To clone the repository using HTTPS, under "Clone with HTTPS", click the clone symbol. To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click Use SSH, then click the clone symbol next to it. To clone a repository using GitHub CLI, click Use GitHub CLI, then click the same clone symbol .
4. Open Git Bash and change the current working directory to the location where you want the cloned directory.

5. Type git clone, and then paste the URL you copied earlier.

6. You will see a message confirmation that the command was successul.


[Back to top ⇧](#)













![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome Cristina Onea,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **September 1, 2021**

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.


[Back to top ⇧](#)


**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
