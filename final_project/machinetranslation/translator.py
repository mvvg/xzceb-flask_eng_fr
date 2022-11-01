'''French-english, english-french translator service'''
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = 'Q7A8uyo2vbs3qUXzthPfGTNgQGTvvyOxwQ2vNKmKMRKO'
url = 'https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/748ed225-d86e-42af-996c-cc71f0c9806c'

authenticator=IAMAuthenticator(apikey)
language_translator =LanguageTranslatorV3(
    version='2018-05-01',
    authenticator= authenticator
)
language_translator.set_service_url(url)

def english_to_french(english_text):
    ''' Translate English to French'''
    translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    ''' Translate French to English '''
    translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text

print(english_to_french('Thanks'))