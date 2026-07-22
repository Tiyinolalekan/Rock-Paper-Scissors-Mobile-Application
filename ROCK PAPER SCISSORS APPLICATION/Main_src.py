##CONVERTING THE ROCK PAPER SCISSORS APPLICATION TO INCLUDE A GUI
##TIYIN O 22/02/2025

import random
import customtkinter as ctk
from PIL import Image  # Required for image handling





ctk.set_appearance_mode("light")

root = ctk.CTk()
root.configure(fg_color="#00C3FF")  # Light blue background (HEX for light blue)
root.geometry("1000x700")
root.title("Tiyin's Amazing Wonderful Exdupilous RPS App!!!")

MAX_PLAYS= 10
player_wins = 0
bot_wins = 0
draws = 0

player_wins_msg = "YOUR SCORE (๑˃ᴗ˂): " 
bot_wins_msg = "BOTTY (♡˙︶˙♡): " 
draws_msg = "TIES (≖_≖) : " 




outcomes = {1: "ROCK (≧◡≦) ♡",
            2 : "PAPER(´∀｀)♡",
            3 : "SCISSORS(ʃƪ˘ﻬ˘)"}

players = {1 : "You",
           2 : "Robot"}

user_id = 1
bot_id = 2



def bot_choice() :
    bot  = random.randint(1, 3)
    return bot

def rock_on_click() :
    user = 1
    choice_comparison(user, bot_choice(), outcome_msg, robot_image_label, robot_choice_label, user_result, bot_result, draw_result) 
    return user

def paper_on_click() :
    user = 2
    choice_comparison(user, bot_choice(), outcome_msg, robot_image_label, robot_choice_label, user_result, bot_result, draw_result) 
    return user

def scissors_on_click() :
    user = 3
    choice_comparison(user, bot_choice(), outcome_msg, robot_image_label, robot_choice_label, user_result, bot_result, draw_result) 
    return user


def choice_comparison(user, bot, label, bot_icon, bot_label, user_result_label, bot_result_label, draw_label) :
    global player_wins, bot_wins, draws  # Declare global variables
    if user == bot :
        label.configure(text = "A TIE (✿◕‿◕)")
        draws += 1
        draw_label.configure(text = draws_msg + str(draws))
        bot_label.configure(text = outcomes[bot])

    ##HUMAN WINNIJNG SCENARIO
    elif user == 1 and bot == 3 :
        label.configure(text = "YOU WIN (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧")
        player_wins += 1
        user_result_label.configure(text = player_wins_msg + str(player_wins))
        bot_icon.configure(image = ROBOT_IMAGE_LOSS)
        bot_label.configure(text = outcomes[bot])
        return user_id
    
    elif user == 2 and bot == 1 :
        label.configure(text = "YOU WIN (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧")
        player_wins += 1
        user_result_label.configure(text = player_wins_msg + str(player_wins))
        bot_icon.configure(image = ROBOT_IMAGE_LOSS)
        bot_label.configure(text = outcomes[bot])
        
        return user_id
    
    elif user == 3 and bot == 2:
        label.configure(text = "YOU WIN (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧")
        player_wins += 1
        user_result_label.configure(text = player_wins_msg + str(player_wins))
        bot_icon.configure(image = ROBOT_IMAGE_LOSS)
        bot_label.configure(text = outcomes[bot])

        return user_id
    
    ##ROBOT WINNIJNG SCENARIO

    elif bot == 1 and user == 3 :
        label.configure(text = "YOU LOSE! (¬‿¬ )")
        bot_wins += 1
        bot_result_label.configure(text = bot_wins_msg + str(bot_wins))
        bot_icon.configure(image = ROBOT_IMAGE_WIN)
        bot_label.configure(text = outcomes[bot])
        return bot_id
    
    elif bot == 2 and user == 1 :
        label.configure(text = "YOU LOSE! (¬‿¬ )")
        bot_wins += 1
        bot_result_label.configure(text = bot_wins_msg + str(bot_wins))
        bot_icon.configure(image = ROBOT_IMAGE_WIN)
        bot_label.configure(text = outcomes[bot])
        return bot_id
    
    elif bot == 3 and user == 2:
        label.configure(text = "YOU LOSE! (¬‿¬ )")
        bot_wins += 1
        bot_result_label.configure(text = bot_wins_msg + str(bot_wins))
        bot_icon.configure(image = ROBOT_IMAGE_WIN)
        bot_label.configure(text = outcomes[bot])
        return bot_id

    else :
        label.configure(text = "A TIE (✿◕‿◕)")
        draws += 1
        draw_label.configure(text = draws_msg + str(draws))
        bot_label.configure(text = outcomes[bot])



frame = ctk.CTkFrame(master=root, fg_color= "#F7C1E2")
frame.pack(pady=20, padx=60, fill="both", expand=True)

custom_font_sub_heading = ctk.CTkFont(family="Arial", size=16, weight="bold")
custom_font_sub_heading2 = ctk.CTkFont(family="Arial", size=18, weight="bold")

custom_font_title = ctk.CTkFont(family="Arial", size=28, weight="bold")

# Load images for the corners
corner_icon = ctk.CTkImage(light_image=Image.open("Rock_Paper_Scissors_App/cloud_rainbow.png"), size=(50, 50))
corner_icon_2 = ctk.CTkImage(light_image=Image.open("Rock_Paper_Scissors_App/heart.png"), size=(50, 50))


# Place images in the corners using .place()
top_left_icon = ctk.CTkLabel(root, image=corner_icon, text="")
top_left_icon.place(x=10, y=10)  # Top-left corner

top_right_icon = ctk.CTkLabel(root, image=corner_icon_2, text="")
top_right_icon.place(x=940, y=10)  # Top-right corner (1000 - icon width - margin)

bottom_left_icon = ctk.CTkLabel(root, image=corner_icon_2, text="")
bottom_left_icon.place(x=10, y=640)  # Bottom-left corner

bottom_right_icon = ctk.CTkLabel(root, image=corner_icon, text="")
bottom_right_icon.place(x=940, y=640)  # Bottom-right corner


main_label = ctk.CTkLabel(frame, text="ROCK PAPER SCISSORS!!!!", text_color="#00C3FF", font=custom_font_title)
main_label.pack(pady=12)

## #00C3FF CYAN BLUE
## #44FF00 LEMON GREEN
## #da8cc2  LIGHT PINK
##rgb(133, 102, 179)  VIOLET


ROBOT_IMAGE = ctk.CTkImage(light_image=Image.open("Rock_Paper_Scissors_App\cloud_idle.png"), size=(200, 200))  
ROBOT_IMAGE_LOSS = ctk.CTkImage(light_image=Image.open("Rock_Paper_Scissors_App\cloud_loss.png"), size=(200, 200))  
ROBOT_IMAGE_WIN = ctk.CTkImage(light_image=Image.open("Rock_Paper_Scissors_App\cloud_win.png"), size=(200, 200))  
ROCK_IMAGE = ctk.CTkImage(light_image=Image.open("Rock_Paper_Scissors_App\p_rock.png"), size=(70, 70))  
PAPER_IMAGE = ctk.CTkImage(light_image=Image.open("Rock_Paper_Scissors_App\paper.png"), size=(70, 70))  
SCISSORS_IMAGE = ctk.CTkImage(light_image=Image.open("Rock_Paper_Scissors_App\scissors.png"), size=(70, 70))  





robot_image_label = ctk.CTkLabel(frame, image=ROBOT_IMAGE, text="")  # Empty text to show only image
robot_image_label.pack(pady=12)

robot_choice_label = ctk.CTkLabel(frame, text = "", text_color= "#c50505", font =custom_font_sub_heading2)
robot_choice_label.pack(pady = 12)

outcome_msg = ctk.CTkLabel(frame, text = "LET'S PLAY (づ｡◕‿‿◕｡)づ", font =custom_font_sub_heading, text_color="#00C3FF" )
outcome_msg.pack(pady = 12)


icons_frame = ctk.CTkFrame(frame, fg_color="transparent")  
icons_frame.pack(pady=12)  # Center inside main frame

rock_button = ctk.CTkButton(icons_frame, image = ROCK_IMAGE,
                             text = "", text_color= "black",
                             fg_color= "transparent", hover_color= "#a30867",
                             command= rock_on_click)
rock_button.pack(side="left", padx=10)

paper_button = ctk.CTkButton(icons_frame, image = PAPER_IMAGE,
                             text = "", text_color= "black",
                             fg_color= "transparent", hover_color= "#a30867",
                             command= paper_on_click)
paper_button.pack(side="left", padx=10)

scissors_button = ctk.CTkButton(icons_frame, image = SCISSORS_IMAGE,
                             text = "", text_color= "black",
                             fg_color= "transparent", hover_color= "#a30867",
                             command= scissors_on_click)
scissors_button.pack(side="left", padx=10)

result_frame = ctk.CTkFrame(frame, fg_color="transparent")  
result_frame.pack(pady=72)  # Center inside main frame

user_result = ctk.CTkLabel(result_frame, text = player_wins_msg, text_color = "black",  font = custom_font_sub_heading)
user_result.pack(side = "left", padx = 20)

draw_result = ctk.CTkLabel(result_frame, text = draws_msg, text_color = "black",  font = custom_font_sub_heading )
draw_result.pack(side = "left", padx = 20)

bot_result = ctk.CTkLabel(result_frame, text = bot_wins_msg, text_color = "black",  font = custom_font_sub_heading )
bot_result.pack(side = "left", padx = 20)



# Start the event loop
root.mainloop()
