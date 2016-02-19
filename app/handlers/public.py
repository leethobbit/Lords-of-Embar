from .base import BaseRequestHandler
from app.data import race


class PublicRequestHandler(BaseRequestHandler):
    """ Onboarding Web Pages
        - / index page
    """
    def get_index(self):
        return self.html_view('public/index.html',
            races=race.RACES
        )
