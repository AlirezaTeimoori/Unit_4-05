#Created by: Alireza Teimoori
#Created on: 7 Nov 2017
#Created for: ICS3UR-1
#Lesson: Unit 4-05
#This program calculates the volume with the parameters that user enters

PI = 3.14

import ui

def calculate_the_volume(radius,height):
    # calculates the volume 
    
    volume = (2 * PI * radius ** 2 * height)
    
    return volume

def calculate_button_touch_up_inside(sender):
    # runs when user touches calculate
    
    user_radius = int(view['radius_textfield'].text)
    user_height = int(view['height_textfiled'].text)
    
    answer = calculate_the_volume(user_radius , user_height)
    
    view['answer_label'].text = str(answer)
    
view = ui.load_view()
view.present('sheet')
