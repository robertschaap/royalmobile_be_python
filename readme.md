# RoyalMobile | Webstore

##### Technologies
Python | Flask | SQL Alchemy | PyTest | Invoke

### Scope
##### What it was designed to do
+ Be a simple backend to the webstore
+ Have a few routes
+ Be a test of some manual data manipulation (hence no DB for now)

##### What it wasn't designed to do
- Manage session or users
- Be a full commercial back-end (i.e. some things like the manual DB are impractical though interesting to implement and past accepting an order there is no functionality)

##### What it wasn't designed to do

##### Installation Notes
Please feel free to download or clone the repository. This is just the back-end, front-end repositories are named `royalmobile_fe_*`. By default the back-end will run on port `4000`, which the front-end repositories are configured to listen to. Please make sure you have at least Python 3.7.

To run:
- From project root
- Run `pipenv shell`
- Run `invoke start`
