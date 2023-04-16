# duolingOSINT

## Requirements

+ [Python](https://www.python.org/downloads/)
+ Packages :
  + `pip install -r requirements.txt`

## Usage

```
usage: duolingOSINT.py [-h] (-m MAIL | -u USERNAME)

options:
  -h, --help            show this help message and exit
  -m MAIL, --mail MAIL  Target mail address
  -u USERNAME, --username USERNAME Target Duolinguo username
```

## Exemple

```
> py duolingOSINT.py -m xxxxxxxxx@gmail.com

Found 1 user with the given information.
Informations about     : [USERNAME]
Profile picture        : https://simg-ssl.duolingo.com/avatars/xxxxxxxx/xxxxxxx/xxlarge
Name                   : xxxxxxxx
Account Creation Date  : xxxxxxxxxxxx
Country                : xxxxxxxx
Streak                 : xxx
Has recent activity    : True/False
Languages studied      : 
 + Language 1 (from Language)
   + xxx crowns (xx.xx %)
   + xxxxx xp
 + Language 2 (from Language)
   + xx crowns (xx.xx %)
   + xxxx xp
```

## Other

Inspired by [Palenath](https://github.com/megadose)'s work
