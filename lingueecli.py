import argparse
import json
import requests

API_BASE_URL = 'https://linguee-api.herokuapp.com/api?'
FIND_MORE_BASE_URL = 'https://www.linguee.com/'

headers = {'Content-Type': 'application/json'}

codes_of_supported_langs = {
"english": "en",
"spanish": "es",
"portuguese": "pt",
"german": "de",
"french": "fr",
"italian": "it",
"russian": "ru",
"dutch": "nl",
"polish": "pl",
"chinese": "zh",
"bulgarian": "bg",
"czech": "cs",
"danish": "da",
"greek": "el",
"estonian": "et",
"finnish": "fi",
"hungarian": "hu",
"japanese": "ja",
"lithuanian": "lt",
"latvian": "lv",
"maltese": "mt",
"romanian": "ro",
"slovak": "sk",
"slovene": "sl",
"swedish": "sv",}

def get_language_two_letter_code(full_name_of_language):
    #We standardize the incoming full name, make it all lowercase
    full_name_of_language = str(full_name_of_language).lower()
    #We get the two letter code from the dictionary
    two_letter_code = codes_of_supported_langs.get(full_name_of_language)
    #And of course, return it
    return two_letter_code

def translate(word, origin, dest):
    api_url = '{0}q={1}&src={2}&dst={3}'.format(API_BASE_URL, word, origin, dest)

    results = [] #Saves the strings that show exact match and translation, of format: "Match: translation1, translation2..."
    number_of_exact_matches_found = 0

    print("Translating... *beep boop bap*")

    response = requests.get(api_url, headers=headers)

    if(response.status_code == 200): #If linguee found something
        result_dict = json.loads(response.content.decode('utf-8'))

        for exact_match in result_dict["exact_matches"]: #For each match 
            if(exact_match["lemma_id"].startswith(origin.upper())): #In the origin language (linguee also shows matches for the inverse dest->origin)

                number_of_exact_matches_found += 1
                current_match_and_translation_str = exact_match["text"] + ": "

                for translation in exact_match["translations"]:
                    current_match_and_translation_str += translation["text"] + " " #We append the translation to its result string

                results.append(current_match_and_translation_str) #We add the result string to the list of result strings

        #Having done the dirty work
        print(str(number_of_exact_matches_found) + " exact matches and translations found")

        for match_and_translation in results: #We print the results we found
            print(match_and_translation)

        if(number_of_exact_matches_found > 0): #And offer a link for more info
            find_more_url = FIND_MORE_BASE_URL + origin + "-" + dest + "/search?source=auto&query=" + word
            print("Find more at " + find_more_url)

    else: #If linguee returns an error
        print("Oops! Something went wrong")
        print("0 results found")

        if(response.status_code == 404):
            print("Linguee says: Term not found") #Most often it couldn't find a matching term in the origin language
        else:
            print("Linguee says: " + str(response.status_code)) #Otherwise, we print the error code (TODO: print error message)

    return results


#Main program

supported_langs_list = ""
for supported_lang in codes_of_supported_langs.keys():
    supported_langs_list += supported_lang.capitalize() + ", "

parser = argparse.ArgumentParser(
        description="Translate a word from one language to another using the Linguee API",
        epilog="Supported languages: " + supported_langs_list) #We create an argument parser in order to work with arguments from terminal

#Help for the user
parser.add_argument("word", type=str, help="Word you want to translate")
parser.add_argument("orig", type=str, help="Language of origin")
parser.add_argument("dest", type=str, help="Language of destination")

#We take the user's arguments
args = parser.parse_args()

#We get the two letter codes of the languages inserted by the user as args
origin_lang_code = get_language_two_letter_code(args.orig)
dest_lang_code = get_language_two_letter_code(args.dest)

if((origin_lang_code != None) & (dest_lang_code != None)): #If we found the 2-letter code for both langs
    #We call the Translate method with the arguments
    translate(args.word, origin_lang_code, dest_lang_code)
