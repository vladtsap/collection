# collection

> #### This project was forked from [infomate.club](https://github.com/vas3k/infomate.club)

_Collection_ is a small web service that shows multiple RSS sources on one page.

### Live URL: [collection.vladtsap.com](https://collection.vladtsap.com)

## Running it locally

The easy way. Install [docker](https://docs.docker.com/install/) on your machine. Then:

```
git clone git@github.com:vladtsap/collection.git
cd collection
docker-compose up --build
```

After that navigate to [localhost:8000](http://localhost:8000)

To terminate it:

```shell script
docker-compose down --remove-orphans
```


## Running for development

Make sure you have python3 and postresql installed locally.

#### Step 1: Install requirements

```
pip3 install -r requirements.txt --user
```

#### Step 2: Create a database structure

```
python3 manage.py migrate
```

#### Step 3: Take a look at [boards.yml](boards.yml)

This is the main source of truth for all RSS streams and collections in the service. All updates to the database are made through it. For the first time you can just use the existing one.

#### Step 4: Initialize your feeds

```
python3 scripts/initialize.py --config boards.yml
```

> Every time you make a change to boards.yml, just run this script again. He is smart enough to create the missing ones and remove the old ones.

#### Step 5: Fetch some articles

```
python3 scripts/update.py
```

> Don't run it too often, otherwise sites may ban your IP. There is a hardcoded cooldown interval for each feed, but you can use `--force` flag to ignore it.

#### Step 6: Run dev server

```
python3 manage.py runserver 8000
```

Then go to [localhost:8000](http://localhost:8000) again

## boards.yml format

```
boards:
- name: Tech            # board title
  slug: tech            # board url
  is_visible: true      # visibility on the main page
  is_private: false     # private boards require logging in
  curator:              # board author profile
    name: John Wick 
    title: Main news
    avatar: https://i.vas3k.ru/fhr.png 
    bio: Major technology media in English and Russian
    footer: >
      this is a general selection of popular technology media.
      The page is updated once per hour.
  blocks:               # list of logical feed blocks
  - name: English       # block title
    slug: en            # unique board id
    feeds:         
      - name: Hacker News
        url: https://news.ycombinator.com
        rss: https://news.ycombinator.com/rss
      - name: dev.to
        url: https://dev.to
        rss: https://dev.to/feed
      - name: TechCrunch
        rss: http://feeds.feedburner.com/TechCrunch/
        url: https://techcrunch.com
        is_parsable: false  # do not try to parse pages, show RSS content only
```

## License

[Apache 2.0](https://github.com/vas3k/infomate.club/blob/master/LICENSE) © Vasily Zubarev

> TL;DR: you can modify, distribute and use it commercially, 
but you MUST reference the original author or give a link to service