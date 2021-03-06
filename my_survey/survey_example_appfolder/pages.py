from otree.api import Currency as c, currency_range, safe_json
from ._builtin import Page, WaitPage
from .models import Constants, Player

#This is the pages.py file. Here we structure how our pages and pagesequence function.
#Each page has its own class where you always specify form_model = Player as we have players for each page
#and we have the form_fields in a list which indicate the variables we have on that page. There will be
#more functionality added here but this is a good start. 

class Welcome(Page):
    form_model = Player
    form_fields = ['device_type', 'operating_system', 'screen_height', 'screen_width', 'entry_question']
    
#with the function before_next_page you can can control what should happen. It is a nice feature for filtering
#or also setting variables
    def before_next_page(self):
        #here we are increasing the counter for each player that goes past the Welcome Page
        self.group.counter += 1


class SurveyPage(Page):
    form_model = Player
    form_fields = [ 'age_question', 'gender', 'party', 'favorite_pol', 'popout_question', 'popout_yes', 'popout_no']





class EndPage(Page):
    form_model = Player
    def vars_for_template(self):
        return {"group_assignment": safe_json(self.player.group_assignment)}
    

#Here we define in which ordering we want the pages to be shown. We always start with a Welcome page and end with an End page.
page_sequence = [Welcome,
                SurveyPage,
                EndPage]