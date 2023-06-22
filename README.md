# St Benedict's Garden of life
This is a promise website to be for my uncle Fr. Vicente 'Inting' Mandaya who devevelop and founded St Benedict's Garden of life.
Most of the features in this site are already in place except that the services being offered is still an imagination awaiting for a final decision on how to market
St Benedict's to customers.

St Bendict's has been open to the public for a quite sometime now servicing variety of religious activities that you can see in the gallery, like Station of the Cross, Retreats, Recollection, Sto. Nino celebration and many more..

St Benedict's Garden of Life is a fully responsive website that allow users to book, update and delete a reservation. Only sign-up users are allowed to create a booking,
otherwise the user can have a looked only at the St Benedict's Garden of life website.

![responsive image](./static/images/responsive.png)


# Navigation
 * The navigation bar is featured in  seven pages.
 * When the user is not logged in, the Sign Up and Log in button displays but when a user is logged in this disappears and replaced with Reservations and Log Out buttons including the username of the user and a welcome to St Benedict! message. A successfully signed message also displays in the reservations page.
 * The Contact and Services uses dropdown to access the page.
 * The buttons are using a color combination of brown #FFFFFF with a hover effect.
 * It uses linear-gradient(to right, rgb(160, 48, 26), #FFFFFF) background color.
 * The hand praying icon is taken from font awesome.

 ![navigation screeenshot](./static/images/nav_not_login.png)

 ![navigation screenshot when user is logged in](./static/images/nav_when_loggedin.png)

 ![signed in success](./static/images/signed_in_success.png)


 # Landing Page
  * The landing page image is the side view structure of the St Benedict's Garden main attraction in the hills of Sitio Migsale.
  * It has a welcome message overlay and book now link to bring the user to the Log in page. The user will be ask to sign up first if the users have not created an account yet.
    Once the user is signed in, the user will be redirected back to the home page. The user can then click the book now button and brings the user to the booking form page. The user can also access the booking form page through the Reservations button and then click the make a booking here button.

 ![home page](./static/images/hom_page.png) 
 
 ![home page when user signed in](./static/images/home_page_signed_in.png)

 * This is how the homepage looks in a mobile device.

 ![home page in mobile device](./static/images/home_page_smaller_screen.png)

# Gallery
 * In this page the user can take a look of the images taken from St Benedict'Garden of Life.
 * It has a column count of 3 in most devices and column count of 1 when it has a max-width of 414px. 

 ![gallery page](./static/images/gallery.png)

 ![gallery page mobile device](./static/images/gallery_page_smaller_screen.png)


# Our Story Page
 * Here the user can read a little bit of story on how St Benedict's Garden of Life had all started.
 * The image of a Priest is Fr Inting himself and the content of the story was provided by him.
 * The second image was the very first structure built in the St. Benedict's garden of Life. 

 ![our story page](./static/images/our_story.png)

 ![our story page in a mobile device](./static/images/our_story_sm.png)
 ![our story page in a mobile device](./static/images/our_story_sm1.png)


# Contact Page
 * In this page the location and Contact us are displayed alongside in a desktop view using an inline display.
 * In a mobile device, the view is a block display

 ![contact](./static/images/contact.png)

 ![contact mobile device](./static/images/contact_sm.png)


# Services 
 * The services being offered on this site is an imagination but can be use in the near future..
 * A book now button below the images will bring the user to the booking form page.
 * Images are all taken on site during previous activities in St Benedict's Garden of Life.

 ![services screenshot](./static/images/services.png)

 ![services1 screenshot](./static/images/services1.png)

# Deployment
## Setting up basic Django Project and Deploying to Heroku
 * You can find the instructions [here](https://docs.google.com/document/d/1P5CWvS5cYalkQOLeQiijpSViDPogtKM7ZGyqK-yehhQ/edit), a cheat sheet created by [Code Institute](https://codeinstitute.net/ie/)

## Heroku Deployment 
 * After following the instructions above
   * Add another Config Var in Heroku's Settings, The key is PORT and the value is 8000
   * Click Deploy tab in Heroku
   * In the 'Deployment method' section select 'Github' and click the 'connect to Github' button to confirm.
   * In the 'search' box enter the Github repository name for the project
   * Click search and then click connect to link the heroku app with the Github repository. The box will confirm that heroku is connected to the repository.

## Final Deployment
 * In the (IDE) Integrated Development Environment:
  * When development is complete change the debug setting to: DEBUG = False in settings.py   
  * In Heroku settings config vars delete the DISABLE_COLLECTSTATIC
  * In Heroku click the 'Deploy Branch' branch button. When deployment is successful, a message 'Your app is deployed to heroku. Click open app button and the The install worked successfully! Congratulations! messages will be displayed.

