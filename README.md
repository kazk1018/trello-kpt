# trello-kpt

KPT tool CLI for Trello

## Requirements
* python 3.6
* libraries
    * Click
    * py-trello
    * PyYAML


```
pip install -f requirements.txt
```


## Configuration

```
python cli.py config new

# Set your API Key and Token

API Key: 
API Token:
```

## Commands

### Board
* new
* list
* get
* report (markdown output)

### Lists
* add
* get

### Organization (Team)
* list

## Set up KPT

```
python cli.py board new {board name} -o {your organization id}

python cli.py lists add {your new board id} Keep,Problem,Try

(Start KPT)
...

python cli.py board report {your board id} {mardown file path}
```

## TODO
* setup.py (install)
* other commands
