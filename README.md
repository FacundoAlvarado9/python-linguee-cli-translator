# Python Linguee CLI Translator
This is just a single-word translator, made using the Linguee API, more info about that in https://github.com/imankulov/linguee-api/

All credits for translations goes to Linguee. Amazing tool for language learning.

## Installation
Just download the script.

## Usage
Once the script is downloaded, go to its directory, and type in your command-line

```
python lingueecli.py word language_of_origin language_of_destination
```

For example:
```
python lingueecli.py sehenswürdigkeit german english
```

And you will hopefully get the following response:

```
Translating... *beep boop bap*
1 exact matches and translations found
Sehenswürdigkeit: sight attraction place of interest point of interest object of interest showplace 
Find more at https://www.linguee.com/de-en/search?source=auto&query=sehenswürdigkeit
```

You can get help by typing

```
python lingueecli.py --help
```

## How can I help?
I was thinking of maybe adding support for asking for word usage examples, one of the things Linguee is best at.