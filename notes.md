# Full Stack React & Django - Traversy Media 

## Basic REST API 
- Install `pipenv install django djangorestframework django-rest-knox` in your pipenv shell 
- Next run `django-admin startproject leadmanager` in your pipenv shell 
- Then run in your pipenv shell `cd leadmanager/` then `python manage.py startapp leads`
- In our leadmanage/settings.py we add 'leads' and 'rest_framework' under INSTALLED_APPS and change our database to postgres under DATABASES
- Creating a model in models.py
  <code>
  class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    message = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
  </code>
- To make migrations run `python manage.py makemigrations leads` then `python manage.py migrate`
- With the rest_framework we run the serializer
- Create a `serializers.py` in your leads folder 
  - See page for part 1 branch for this one 
- Then create a `api.py` file in your leads folder 
  - Lead viewset, allows us to create a full CRUD API without having to specify the different methods 
  - We can use the defaultRouter and register an endpoint 
  - See in part 1 branch for this one 
- Then go into your urls.py in your leadmanager 
  - See update in part 1 branch 
- Then create a urls.py in your leads folder 
  - See in part 1 branch 
- Then you can run your server 
- Run in postman and you have full CRUDability 

## Implementing React 
- Now we want to start to implement React, we won't use create React app for this, we will create a frontend app and inside there, is where the entry point will be 
- Open up your terminal and navigate to your project folder and then run a pipenv shell 
- Then run `cd leadmanager`
- Then run `python manage.py startapp frontend`
- mkdir for React 
  - `mkdir -p ./frontend/src/components`
    - Everything we do lives here 
  - `mkdir -p ./frontend/{static, templates}/frontend`
    - Templates will be where our templates lives 
    - Static will be the compiled JS 
- `cd ../` -> `npm init -y` -> `npm i -D webpack webpack-cli` -> add git ignore from googling gitignore django -> `npm i -D @babel/core babel-loader @babel/preset-env @babel/preset-react babel-plugin-transform-class-properties` 
- React Steps: `npm i react react-dom prop-types`
- In order to use our presets, we need to create a file called .babelrc in our root
  - See file in implementing-react branch 
- Then create our webpack config files in the root called webpack.config.js
  - See file in implementing-react branch
- Then go into your package.json 
  - Replace test script with dev 
  - Add in a build script 
- Create an `index.js` in your `./leadmanager/frontend/src`
- Then create an `App.js` in `./leadmanager/frontend/src/components`
- Then create a `index.html` in `./leadmanager/frontend/templates/frontend`
- Go back into your leadmanager `settings.py` and add in the frontend to the app and add in 'frontend' to INSTALLED_APPS
- Go into your `views.py` in your frontend folder 
- Create a `urls.py` in your frontend folder and then update your urls.py in the leadmanagers urls.py to include your frontened urls, you want frontend to load before leads
- Then go into your terminal and run `npm run dev` 
- Then you will be able to see your React App on the localhost 
- Compoenents 
  - In the `./leadmanager/frontend/src/components/` and make a diretory called layout and a file called `Header.js` -> use rce to make a class based component -> add in compoenent to App.js
  - If you want to see changes, you have to run `npm run dev`, we can add a watch option to avoid doing this 
  - In your `./leadmanager/frontend/src/components/` folder make a directory called `leads` add these files `Dashbord.js - use rcf for this compoenent` `Form.js` `Leads.js`

## Redux & HTTP 
- Download Reducx Dev Tools on Chrome 
- Redux is completely separate from Redux
- To start run `npm i redux react-redux redux-thunk redux-devtools-extension` in your terminal
- The first thing you want to do is create your store file, this goes in your `./leadmanager/frontend/src/` folder, create a store.js
- Then to create your reducer you make a new directory called `reducers` in `./leadmanager/frontend/src/` and create an `index.js` in that folder
  - Then we want to bring in our store and reducers to our App.js in components
- Then we create a new reducer in `./leadmanager/frontend/src/reducers` called `leads.js`
  - Reducers - basically a function that takes in an action and evaluates and sends down certain state based on what that action does 
    - We define these with types 
- Create a folder in `./leadmanager/frontend/src/` called actions and then create a file called `types.js`
  - Types are basically constants that hold a string 
- Install axios in your terminal 
- In your `./leadmanager/frontend/src/` folder create a file called `leads.js`
  - Any actions we want to fire off go in here 
  - We'll be using something called dispatch to help with our server calls -> use whenever we dispatch an action to our reducer
  - In order to use redux, you need to us connect 
- Next, go into your `Leads.js` in your `./leadmanager/frontend/src/components/leads`
- Add Lead form
  - Go into your `Form.js` compoenent, we will need to add state `./leadmanager/frontend/src/components/leads`
  - Then go to `./leadmanager/frontend/src/actions` and edit your `leads.js` and `types.js` 
  - Then go to your `leads.js` in `./leadmanager/frontend/src/reducers`
  - Then go to your `Form.js` in  `./leadmanager/frontend/src/components/leads`

## Error Handling & Alerts 
- We are going to create an alerts component to show any errors when user submits a form, we will be using react-alerts 
  - Go into your terminal and install `npm i react-alert react-alert-template-basic react-transition-group`
  - Go into your `App.js` and add in the Provider
  - In `./leadmanager/frontend/src/components/layout/` create a new file called `Alerts.js` use rce 
  - Go back to your `App.js` and bring in the alerts 
- In `./leadmanager/frontend/src/reducers` create a new file called `errors.js` and we need to bring it into our `index.js`
  - We will also bring it into our `./leadmanager/frontend/src/actions` file in the `types.js`
  - Then go into your `leads.js` in `./leadmanager/frontend/src/actions` 
  - Then go into your `Alerts.js` and connect 
- Creating a messages reducer 
  - Go to `./leadmanager/frontend/src/reducers` and create a file called `messages.js` and you can basically copy what you have in your `errors.js`
  - Now we have to add this to our root reducer - `index.js` in the `./leadmanager/frontend/src/reducers`
  - In `./leadmanager/frontend/src/actions` create a new file called `messages.js`
  - Then go into your `leads.js` in `./leadmanager/frontend/src/actions`
  - Then go into your `Alerts.js`

## Django Token Authentication 
- This is where we get into authentication 
- We want to be able to authenticate, and see the leads if we don't have a token, we have to go back to the backend for this 
- Go to your `models.py` in`./leadmanager/leads` and we want to bring the user model that comes default with Django 
  - Bring this in `from django.contrib.auth.models import User`
    - Add this under messages `owner= models.ForeignKey(User, related_name='leads', on_delete=models.CASCADE, null=True)`
  - Stop your server and then cd into leadmanager/
  - Run `python manage.py makemigrations` in your terminal and then run `python manage.py migrate`
- Authentication 
  - Go into your `api.py` in your `./leadmanager/leads/` and change your permissions and your queryset 
  - To handle errors go to `leads.js` in `./leadmanager/frontend/src/actions` 
  - Then go into your `messages.js` in `./leadmanager/frontend/src/actions` 
- To authenticate we need to create a registration API to register a user and then once we register a user and create a login API and then when we login, we get a token 
  - We will be using Django Rest Knox, we have to add this to our settings and add in a REST_FRAMEWORK that knows we want to use knox - after this we need to run `python manage.py migrate`
  - We need to think about how to create our serializers before creating a user and logging in - we will need to create a brand new app for that 
    - Create a new app in Django for `accounts` using `python manage.py startapp accounts` in your terminal and then add your new app to your settings.py
    - Then create a file in your `./leadmanager/accounts/` directory called `serializers.py`
      - We're going to focus on registration first 
      - Django already does the auth for us, we're just using knox to create our tokens 
      - Now we need to create an `api.py` file in `./leadmanager/accounts/`
      - After this we need to create an endpoint, so we need to create another `urls.py` in `./leadmanager/accounts/`
      - We have to include our new urls in the `urls.py` in the leadmanager, `./leadmanager/leadmanager/`
      - Then try to register a user with postman 
- Now we want to be able to login 
  - Go back to your `serializers.py` in `./leadmanager/accounts/`
    - We won't use a model for this, we're just using the login to see if everything passes 
    - Then we go back into our `api.py` in `./leadmanager/accounts/`
    - Then we go back to our `urls.py` in `./leadmanager/accounts/`
    - Then do a post request to login on postman 
- Get User API 
  - Go to your `api.py` in `./leadmanager/accounts/`
  - Then go back to `urls.py` in `./leadmanager/accounts/` to give our API an endpoint
  - To access in postman we have to put a header with a key called `Authorization` and then the value as `Token userToken` <- will be a number 
- Creating a logout
  - There's a view we can bring into our urls, we just add the path 
  - Add this `path('/api/auth/logout', lnox_views.LogoutView.as_view(), name='knox_logout')` to your `urls.py` in `./leadmanager/accounts/` 
  - Once a user logs out, it invalidates that token 
  - When you just clear from local storage on the frontend, it's not truly logging out, you can still have that token in the backend 

## Auth State & Private Routes 
- First we're going to run `npm i react-router-dom` and then you can `npm run dev again`
- Then you're going to go into your `App.js` in `./leadmanager/frontend/src/components/`
  - Import this into your `App.js` `import { HashRouter as Router, Route, Switch, Redirect } from 'react-router-dom'`
  - We want to use HashRouter vs. BrowserRouter since our frontend is in our backend 
  - We also need to wrap our App in a <Router> before the <Fragement>
  - We want to surround all of our routes with Switch because we will run into issues when we create our private routes later 
- In your `./leadmanager/frontend/src/components/` folder create a folder called accounts 
  - Inside of accounts create a file called `Login.js` and `Register.js`
  - Start in `Register.js` and create an rce compoenent 
  - Then go to your `Login.js` 
  - Then import the files you created in the accounts folder to your `App.js`
  - Then add links to your `Header.js` in the `./leadmanager/frontend/src/components/layout` directory, so you can route to them  
- Next we need to add a login reducer 
  - Create a file called `auth.js` in `./leadmanager/frontend/src/reducers/`
  - Then go to your `index.js` in `./leadmanager/frontend/src/reducers/` 
  - Then go back to your `auth.js` in `./leadmanager/frontend/src/reducers/`
  - Next we want to create a private route, so we go to `./leadmanager/frontend/src/components/` and create a new folder called common (anything that doesn't fit into these categories) and create a file called `PrivateRoute.js`-> create a functional compoenent
  - Then bring this new compoenent into your `App.js`
- Now we need to constantly chck if this user is logged in, every time the `App.js` 
  - First we need to go into `types.js` in `./leadmanager/frontend/src/actions`
  - And then go back into `auth.js` in `./leadmanager/frontend/src/reducers/`
  - Now in our `./leadmanager/frontend/src/actions` folder create a file called `auth.js`
  - Go back into your `App.js` and bring in the action 

## Frontend Authentication 
- First we need to go into `types.js` in `./leadmanager/frontend/src/actions`
  - Then go back to your `auth.js` in `./leadmanager/frontend/src/actions`
  - Now go back into your `auth.js` in `./leadmanager/frontend/src/reducers/`
- Now we need a way to call our function, we need to connect it to the Login component 
  - Go to your `Login.js` in your `./leadmanager/frontend/src/components/accounts`
- Logout function 
  - Go to your `Header.js` in `./leadmanager/frontend/src/components/layout`
  - Adding functionality to our logout 
    - Go into `types.js` in `./leadmanager/frontend/src/actions`
    - Go to `auth.js` in `./leadmanager/frontend/src/actions`
    - Now go to `auth.js` in `./leadmanager/frontend/src/reducers/`
    - Now we need to bring that action in, so we need to go to `Header.js` in `./leadmanager/frontend/src/components/layout`
- Handling Login Errors 
  - Go into your `Alerts.js` in `./leadmanager/frontend/src/components/layout`
- Welcome message for user in navbar 
  - Go to your `Header.js` in `./leadmanager/frontend/src/components/layout`
- Cleaning up our code 
  - First we're going to clean up our `auth.js` in `./leadmanager/frontend/src/actions`
- Registration 
  - Go into `types.js` in `./leadmanager/frontend/src/actions`
  - Go to `auth.js` in `./leadmanager/frontend/src/actions`
  - Now go to `auth.js` in `./leadmanager/frontend/src/reducers/`
  - Now go into your `Register.js` in `./leadmanager/frontend/src/components/accounts/`
  - We also want to add in alerts, so go to your `Alerts.js` in `./leadmanager/frontend/src/components/layout`
- Send our token to the leads endpoints in order to load them and in order to add them 
  - Go to `leads.js` in `./leadmanager/frontend/src/actions`