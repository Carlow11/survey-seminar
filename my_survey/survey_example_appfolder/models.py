from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

import random

from survey_example_appfolder.HelperFunctions import random_number

author = 'Carlo Neuhaus'
doc = 'Homework_1'

class Constants(BaseConstants):
    name_in_url = 'homework_2'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
   def creating_session(self):
        for p in self.get_players():
                p.group_assignment = random.Random().randint(0, 1)
    
class Group(BaseGroup):
    counter = models.IntegerField(initial = 0)
    #this is how you can implement variables that can be used by every player
    #they are called group variables and useful for example when quota checking


class Player(BasePlayer):
    #this is the most important feature of this file. We can collect all the variables used on the html pages here
    
    #Welcome
    entry_question = models.StringField(blank = True)
    device_type = models.IntegerField()
    operating_system = models.IntegerField()
    screen_height = models.IntegerField(initial=-999)
    screen_width = models.IntegerField(initial=-999)
    entry_question = models.StringField(blank = True)
    # SurveyPage
    time_popout = models.StringField(initial='-999')
    age_question = models.IntegerField(max=110, min=1)  #we can also have max and min guidelines
    gender = models.IntegerField(initial=-999, label='Gender Question')  #we can add an initial value or a different label
    party = models.IntegerField(initial=-999, label = 'Party Question')
    favorite_pol = models.StringField(blank= True)
    popout_question = models.IntegerField(blank=True)
    popout_yes = models.StringField(blank=True)
    popout_no = models.StringField(blank=True)

 
    name_question = models.StringField(blank= True)
    
 
   
    #EndPage
    group_assignment = models.IntegerField() #the variable we declared on top


    #custom error message
        #has to: 
        #1) be in the class Player (important to indent the right way)
        #2) have a specific name "variablename"_error_message
    def age_question_error_message(player, value):
        if value > 50:
            return 'You are too old. Are you sure you are taking this course?'
                        