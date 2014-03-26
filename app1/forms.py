#-*- coding: utf-8 -*-

############################################
#
# File Name : forms.py
#
# Purpose :
#
# Creation Date : 26-03-2014
#
# Last Modified : Wed 26 Mar 2014 09:16:42 PM MSK
#
# Created By : plushka
#
############################################


from django import forms

GENDER_CHOICES = (
    ('Male', 'I\'m Man'),
    ('Female', 'I\'m Woman'),
    ('uname', 'Arch Info'),
    ('listdir', 'Listing directory'),
)


class MyForm(forms.Form):
    my_choice_field = forms.ChoiceField(choices=GENDER_CHOICES)
