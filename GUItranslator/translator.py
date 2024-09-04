from translate import Translator
import os
file_path = os.path.join(os.getcwd(), "OriginalLang.txt")

Translator = Translator(to_lang="fr")

try:
    with open(file_path, mode="r") as my_file:
        text = my_file.read()
        translation = Translator.translate(text)
        print(translation)
except FileNotFoundError as e:
    print("Please check your file path")
