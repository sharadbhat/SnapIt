# SnapIt

A clone of [Unsplash](https://unsplash.com).

### Requirements

To install the requirements,

```bash
pip install -r requirements.txt
```

### Creating database

```mysql
create database unsplash;
```

```bash
mysql –u [username] -p -h[hostname] unsplash < dump.sql
```

### Creating configuration file

- Create a file name ```db_congig.json``` in the root directory.
- Add the following data,

```json
{
  "host": "[hostname]",
  "user": "[username]",
  "passwd": "[password]",
  "db": "unsplash"
}
```

### Starting server

```bash
python app.py
```

## You're done!

Visit your [localhost:8080](https://localhost:8080) to see it in action.

##### Disclaimer
All photos were taken from [Unsplash](https://unsplash.com).

## Screenshots

#### Landing Page

![Landing Page](https://github.com/sharadbhat/InstaClone/blob/master/Screenshots/landing.jpg "Landing Page")

#### Login Page

![Login Page](https://github.com/sharadbhat/InstaClone/blob/master/Screenshots/login.jpg "Login Page")

#### Homepage

![Homepage](https://github.com/sharadbhat/InstaClone/blob/master/Screenshots/homepage.jpg "Homepage")

#### Search

![Search](https://github.com/sharadbhat/InstaClone/blob/master/Screenshots/search.jpg "Search")

#### Profile

![Profile](https://github.com/sharadbhat/InstaClone/blob/master/Screenshots/profile.jpg "Profile")

#### User's photo

![User Photo](https://github.com/sharadbhat/InstaClone/blob/master/Screenshots/own_upload.png "User Photo")

#### Other User's Photo

![Other Photo](https://github.com/sharadbhat/InstaClone/blob/master/Screenshots/other_photo.png "Other user")
