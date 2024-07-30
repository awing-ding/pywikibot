import lupa
from src import log


class Word:
    """
    A class to represent a word and its properties for generating wikicode.

    Attributes:
        _francais (str): The French term of the word.
        pierrick (str): A unique identifier for the word.
        _phonetique (str): The phonetic transcription of the word.
        _classe (str): The grammatical class of the word.
        _commentaire (str): Additional comments about the word.
        _definition (str): The definition of the word.
        _etymologie (str): The etymology of the word.
        _cyrilic (str): The Cyrillic script representation of the word.
        _hangeul (str): The Hangul script representation of the word.
        _wikicode (str): The generated wikicode for the word.

    Methods:
        __init__(self, entry): Initializes the Word object with data from a database entry.
        _deabreviate_class(self): Converts abbreviated class names to full names.
        _is_declinable(self): Checks if the word belongs to a declinable class.
        _generate_wikicode(self): Generates the wikicode based on the word's properties.
        get_wikicode(self): Returns the generated wikicode.
    """

    declinaisonFunction = "{{decl|%w}}"

    template = """
[[Category:Word]]
[[Category:%C]]
=== %C ===
%d
'''%P''' %p
# %D

== Étymologie ==
%E
== Traductions ==
%F

    """

    def __init__(self, entry) -> None:
        """
        Initializes the Word object with data from a database entry.

        Parameters:
            entry (tuple): A tuple containing the word data from the database.
        """
        self._francais = str(entry[0]).replace("None", "")
        self.pierrick = str(entry[1]).replace("None", "")
        self._phonetique = str(entry[2]).replace("None", "")
        self._classe = str(entry[3]).replace("None", "")
        self._commentaire = str(entry[4]).replace("None", "")
        self._definition = str(entry[5]).replace("None", "")
        self._etymologie = str(entry[6]).replace("None", "")
        self._cyrilic = str(entry[7]).replace("None", "")
        self._hangeul = str(entry[8]).replace("None", "")
        self.proceed = self.should_be_manually_added()
        if self.proceed :
            self._deabreviate_class()
            self._wikicode = ""
            self._generate_wikicode()
            if self.is_declinable():
                self.lua = lupa.LuaRuntime()
                with open("src/data/word/declinaison.lua") as f:
                    self.luaDeclinaison = f.read()
                self.declinaisons = self._declinaison()

    def _deabreviate_class(self) -> None:
        """
        Converts abbreviated class names to their full names.
        """
        matching = {
            "nom": "Nom",
            "nom p": "Nom propre",
            "prep": "Préposition",
            "préposition": "Préposition",
            "pron": "Pronom",
            "verbe": "Verbe",
            "conj": "Conjonction",
            "adj": "Adjectif",
            "adv": "Adverbe",
            "interjection": "Interjection",
            "pronom": "Pronom",
            "particule": "Particule",
            "det": "Déterminant",
            "prép": "Préposition",
            "conjug": "Conjugateur",
            "cardinal": "Cardinal"
        }
        self._classe = matching.get(self._classe, self._classe)

    def _declinaison(self) -> list[str]:
        """
        Generates the declinations for the word using a Lua script.

        Returns:
            list[str]: A list of declinations for the word.
        """
        words: str = self.lua.eval(self.luaDeclinaison)
        if words.find("Error") != -1:
            log("Error in lua script for word " + self.pierrick + " not proceeding further")
            self.proceed = False
            return []
        return words.split(' ')

    def is_declinable(self) -> bool:
        """
        Checks if the word belongs to a declinable class.

        Returns:
            bool: True if the word is declinable, False otherwise.
        """
        return self._classe in ["Nom", "Adjectif", "Déterminant", "Pronom"]

    def _generate_wikicode(self) -> None:
        """
        Generates the wikicode for the word based on its properties and the template.
        """
        self._wikicode = self.template.replace("%C", self._classe)
        if not self.is_declinable():
            self._wikicode = self._wikicode.replace("\n%d", "")
        else:
            self._wikicode = self._wikicode.replace("%d", self.declinaisonFunction.replace("%w", self.pierrick))
        self._wikicode = self._wikicode.replace("%P", self.pierrick)
        self._wikicode = self._wikicode.replace("%p", self._phonetique)
        self._wikicode = self._wikicode.replace("%E", self._etymologie)
        self._wikicode = self._wikicode.replace("%F", self._francais)
        self._wikicode = self._wikicode.replace("%D", self._definition)
        self._wikicode = self._wikicode.rstrip().lstrip()

    def get_wikicode(self) -> str:
        """
        Retrieves the generated wikicode for the word.

        This method returns the wikicode that has been generated by the _generate_wikicode method. The wikicode
        includes the word's properties formatted according to a predefined template, suitable for wiki entries.

        Returns:
            str: The generated wikicode for the word.
        """
        return self._wikicode

    def should_be_manually_added(self) -> bool:
        """
        Checks if the word should be manually added to the wiki.

        Returns:
            bool: True if the word should be manually added, False otherwise.
        """
        return (self._commentaire or self._classe is None or self._classe == "conjug" or
                self._classe == "cardinal" or self._classe == "moment" or self._classe == "particule"
                or self.pierrick is None or self._definition is None)
