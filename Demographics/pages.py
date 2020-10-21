from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants



class Demographics(Page):
    form_model = "player"
    form_fields = ["age",
                   "gender",
                   "education",
                   "executiveSelf",
                   "executiveOther",
                   "contactPoliceBrutality",
                   "violentProtester",
                   "politicalOrientation"]
    # display only if consent is accpeted




page_sequence = [Demographics]
