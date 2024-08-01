from src.log import log, info
from pywikibot import Site, Page
from pywikibot.bot import CreatingPageBot

from src import Data, Word


class Bot(CreatingPageBot):
    """
    A bot class for creating and managing pages on a wiki site.
    Inherits from CreatingPageBot.
    """
    update_options = {
        "minor": False
    }

    def __init__(self, db: Data, namespace: str = None, namespace_id: int = 0) -> None:
        """
        Initializes the Bot class with database connection, namespace, and namespace ID.

        Args:
            db (Data): The database connection object.
            namespace (str, optional): The namespace for the pages. Defaults to None.
            namespace_id (int, optional): The ID of the namespace. Defaults to 0.
        """
        self.db = db
        self.site = Site()
        self.namespace = namespace
        self.namespace_id = namespace_id
        super().__init__()

    def treat_pages(self) -> None:
        """
        Processes pages from the database, creating or updating them on the wiki site.
        """
        while page := self.db.get_next_page():
            word = Word(page)
            if not word.proceed:
                log(f"Word {word.pierrick} should be manually added. : {word.why_not_proceed} ")
                continue
            else:
                main = Page(self.site, word.pierrick, ns=self.namespace_id)
                if main.exists():
                    info(f"{word.pierrick} already exists.")
                    continue
                else:
                    main.text = word.get_wikicode()
                    main.save(minor=False, bot=True)

                    if word.is_declinable():
                        for decl in word.declinaisons:
                            decl = Page(self.site, decl, ns=self.namespace_id)
                            if decl.exists():
                                info(f"{word.pierrick} already exists.")
                                continue
                            else:
                                if self.namespace is None:
                                    decl.text = f"#REDIRECT [[{word.pierrick}]]"
                                else:
                                    decl.text = f"#REDIRECT [[{self.namespace}:{word.pierrick}]]"
                                decl.save(minor=False, bot=True)
