## Deployment: 

<u>PREREQUISITES</u> Before Deploying to Heroku please remember to run <b>python manage.py collectstatic</b> in Gitpod and commit to Gitub. As I discovered it is required to copy CSS and all static folder content images etc to Heroku.

<u>DEBUG=False</u> should always be set in produciton environment.

This project was developed using [GitPod](https://gitpod.io/), committed and pushed to [GitHub](https://github.com/) using a GitPod terminal and deployed using [Heroku](https://id.heroku.com/login).  



The following steps were taken:

### Step one: 
#### Setting up a new app in Heroku.
1. Select "New" and "Create new app".
1. Name the new app and click "Create new app".
1. Set region to Europe or US
1. In "Deploy" tab select Deployment to Github search and choose your Github repository you want to deploy
1. In "Setting" choose your buildpacks you require ie Python

***


### Step two: 
#### Add the Config Vars: 
1. click on the "Settings" tab at the top of the page
1. From your env.py copy the following settings
1. Open the "Reveal Config Vars" section and input the following information:
      * CLOUDINARY_URL: set to the url provided by [Cloudinary](https://cloudinary.com/)
      * DATABASE_URL: set to the DATABASE url ie postgres://....
      * SECRET_KEY: This is a key that you can make up but do not give to anyone
      I used [Djecrety Django secret key generator](https://djecrety.ir/) to create my secret key.
*The env.py file is used to protect keys that should only be accessed by the developer it should be added to .gitignore file to ensure that its never copied to Github.*  

***


### Step three:
#### Set up Cloudinary in settings.py:
1. After you have created the Config vars for Cloudinary (as above) and added it to the env.py you must now set it up in the settings.py 
1. In your settings.py file make your way down to INSTALLED_APPS, then add  'cloudinary_storage' and 'cloudinary'. Put these under the django apps and don't forget the comma at the end or you will get an error.
1. You now have to tell your app to use Cloudinary as the storage for your media and static files. This is done by writting the following code under the STATIC_URL   
`STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'`
`STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]`
`STATICROOT = os.path.join(BASE_DIR, 'staticfiles')`
`MEDIA_URL = '/media/'`
`DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'`

***

### Step four: 
#### Setting up templates:
1. In settings.py under the BASE_DIR key add a TEMPLATES_DIR variable and make it equal to `os.path.join(BASE_DIR, 'templates')`
1. Then scroll down to TEMPLATES and update 'DIRS' with the new TEMPLATE_DIR variable

***

### Step five:
#### Set up Allowed Hosts:
1. Search for the ALLOWED_HOSTS key. Inside the square brackets make it equal to your heroku app url and 'localhost'

***

### Step six:
#### Create a Procfile:
1. In the root of repository create a <b>Procfile</b> file this a Heroku specific file. (it has to be called exactly Procfile - casing matters)
1. Inside this file write **web: gunicorn *.wsgi** (the folder where your settings.py is located in my case it was in the main folder)
1. This tells Heroku how to run our project.

***


### Step seven:
#### Deploying: 
1. You can choose to either deploy your project using "Enable Automatic Deploys" or "Deploy Branch" in the manual deploy section.
      * Note, if you click on Automatic Deploys, you will still need to hit deploy branch to build the site
1. Heroku will now deploy the site.

***

Back to [Top of Page](#deployment)   
Back to [README.doc](/README.md)
