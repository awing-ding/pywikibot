from src.log import log
from pywikibot import Site, Page
from pywikibot.pagegenerators import AllpagesPageGenerator
from pywikibot.bot import CreatingPageBot

from src import Data, Word


class Bot(CreatingPageBot):

    update_options = {
        "minor": False
    }

    def __init__(self, entry: tuple[str], namespace: str, db: Data) -> None:
        self.db = db
        self.site = Site()
        self.namespace = namespace
        self.pages_generator = AllpagesPageGenerator(site=self.site, namespace=namespace)
        self.data = entry
        super().__init__()

    def get_generator(self):
        while row := self.db.get_next_page():
            title = row[1]
            page = Page(self.site, title, ns=self.namespace)
            yield page

    def treat_pages(self) -> None:
        while page := self.db.get_next_page():
            word = Word(page)
            if word.proceed:
                if word.pierrick not in self.site.allpages():
                    main = Page(self.site, word.pierrick)
                    main.text = word.get_wikicode()
                    main.save(minor=False, botflag=True)

                    if word.is_declinable():
                        for decl in word.declinaisons:
                            if decl not in self.site.allpages():
                                decl = Page(self.site, decl)
                                decl.text = f"#REDIRECT [[{word.pierrick}]]"
                                decl.save(minor=False, botflag=True)
            else:
                log(f"Word {word.pierrick} should be manually added.")
