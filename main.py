#Module import
import sys  # imports sys for the sys.exit() function that allows the program to be stopped
import turtle

#reset button setup
turtle.addshape("resetbtn.gif")
resetbtn = turtle.Turtle()

#HCP program

#GUI
screen = turtle.Screen()  # creates the screen for the GUI
turtle.setup(700, 600)  # setup screen with H x W dimentions
screen.bgpic('background.gif')  # set background of turtle graphics

#Split up cards list
open_cardlist = open("cardlist.txt", "r")  #list that goes from 0 - 52
cardlist_raw = open_cardlist.read()
cardlist = []  #new list to store value
for i in range(0, len(cardlist_raw),
               2):  #looping through string variable in steps of 2
    merge = cardlist_raw[i] + cardlist_raw[
        i + 1]  #temp variable to store the 2 digit value of the string
    cardlist.append(merge)  #here the merged value is added to the list

#Split up bri list
bricards = open("NZBcards.bri", "r")
firstboard_raw = bricards.read(78)

firstboard = []
for i in range(0, len(firstboard_raw), 2): #splits up the bri list in two's
    merge = firstboard_raw[i] + firstboard_raw[i + 1]
    firstboard.append(merge)

#creating hands
#extracting hands from bri
northhand_x = firstboard[:13]  #first 13 card
easthand_x = firstboard[13:26]  # 13 to 26 cards
southhand_x = firstboard[26:39]  #and 26 to 39 cards
#entering extracted hands into new lists
northhand = list(northhand_x)
southhand = list(southhand_x)
easthand = list(easthand_x)

#calculate west hand by using sets to subtract from each other
full_deck = set(cardlist)
northhand_set = set(northhand_x)
easthand_set = set(easthand_x)
southhand_set = set(southhand_x)

westhand_set = full_deck - northhand_set - easthand_set - southhand_set
westhand = list(westhand_set)

#Import dictionary from CSV containing all data entry
import csv

with open('card_database.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('card_database_new.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        card_database = {
            rows[0]: rows[1]
            for rows in reader
        }  #creates database dictionay that stores rows 1 and 2 (bri encoded value and card indentifiers )

with open('card_database.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('card_databasepoints_new.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        card_databasepoints = {
            rows[0]: rows[2]
            for rows in reader
        }  #creates database disctionary that stores rows 1 and 3 (bri encoded value and associated point value)


#generate points list along with the points list added up to find the HCP
def card_manipulation():
    global northhand_hcp, easthand_hcp, southhand_hcp, westhand_hcp
    northhand_pointlist = [
        str(sum(int(card_databasepoints[k]) for k in y.split()))
        for y in northhand
    ]

    northhand_hcp = sum(
        sum(int(card_databasepoints[k]) for k in y.split()) for y in northhand)

    easthand_pointlist = [
        str(sum(int(card_databasepoints[k]) for k in y.split()))
        for y in easthand
    ]

    easthand_hcp = sum(
        sum(int(card_databasepoints[k]) for k in y.split()) for y in easthand)

    southhand_pointlist = [
        str(sum(int(card_databasepoints[k]) for k in y.split()))
        for y in southhand
    ]

    southhand_hcp = sum(
        sum(int(card_databasepoints[k]) for k in y.split()) for y in southhand)

    westhand_pointlist = [
        str(sum(int(card_databasepoints[k]) for k in y.split()))
        for y in westhand
    ]

    westhand_hcp = sum(
        sum(int(card_databasepoints[k]) for k in y.split()) for y in westhand)


#this function initialises the cards by asking the user on which hand they want to calculate the HCP of
def init_cards():
    turtle.penup()
    turtle.setpos(0, -20)
    turtle.write(
        "Please enter either north, east, south or west as your input.",
        align="center",
        font=("Courier", 12, "italic")
    )  #writing with turtle to make sure the user understands which inputs are accepted
    hand_input = screen.textinput(
        "handinput", "What hand do you want to calculate the HCP of?:"
    )  #asking the user which hand they want
    turtle.clear()
    position_cards(
    )  #run the positioncards function that sets up the card deck
    if hand_input in [
            'north', 'n', 'northhand', '1', 'norhhand', 'northand', 'nrthhand',
            'nrth'
    ]:  #robust input checker makes sure that multiple inputs that are similar would be accepted, helps make the program feel more robust as it "predicts" what the user wants and overall helps the quality of life of the program
        northhand_cardgen()
    elif hand_input in [
            'east', 'e', 'easthand', '2', 'eashand', 'easthnd', 'eashand',
            'est'
    ]:
        easthand_cardgen()
    elif hand_input in [
            'south', 's', 'southhand', '3', 'souhand', 'southand', 'sohand',
            'sth'
    ]:
        southhand_cardgen()
    elif hand_input in [
            'west', 'w', 'westhand', '4', 'weshand', 'wshand', 'wehand', 'wst'
    ]:
        westhand_cardgen()
    else:  #this essentially repeats what was asked earlier but mentions the wrong input error to the user to make sure that they don't do it again.
        turtle.penup()
        turtle.setpos(0, -20)
        turtle.write(
            "Please enter either north, east, south or west as your input.",
            align="center",
            font=(
                "Courier", 12,
                "italic"))  #tells the user which inputs are accepted once more
        hand_input2 = screen.textinput(
            "handinput", "You entered an invalid input, please try again:")
        turtle.clear()
        if hand_input2 in [
                'north', 'n', 'northhand', '1', 'norhhand', 'northand',
                'nrthhand', 'nrth'
        ]:
            northhand_cardgen()
        elif hand_input2 in [
                'east', 'e', 'easthand', '2', 'eashand', 'easthnd', 'eashand',
                'est'
        ]:
            easthand_cardgen()
        elif hand_input2 in [
                'south', 's', 'southhand', '3', 'souhand', 'southand',
                'sohand', 'sth'
        ]:
            southhand_cardgen()
        elif hand_input2 in [
                'west', 'w', 'westhand', '4', 'weshand', 'wshand', 'wehand',
                'wst'
        ]:
            westhand_cardgen()
        else:
            main(
            )  #if they enter an invalid input again the program returns to the start and resets.


def northhand_cardgen(
):  #this function generates the cards by pulling out values out of a list that is created by comparing against a database
    global cardpics_raw  #making the variable accessible outside the function
    cardpics_raw = [
        card_database[k] for k in northhand
    ]  #generates list for the hand showing all the card indentifier names in the hand.

    #adds ".gif" to the end of every item in the list to select the images that are being displayed
    card_1.shape(cardpics_raw[0] + ".gif")
    card_2.shape(cardpics_raw[1] + ".gif")
    card_3.shape(cardpics_raw[2] + ".gif")
    card_4.shape(cardpics_raw[3] + ".gif")
    card_5.shape(cardpics_raw[4] + ".gif")
    card_6.shape(cardpics_raw[5] + ".gif")
    card_7.shape(cardpics_raw[6] + ".gif")
    card_8.shape(cardpics_raw[7] + ".gif")
    card_9.shape(cardpics_raw[8] + ".gif")
    card_10.shape(cardpics_raw[9] + ".gif")
    card_11.shape(cardpics_raw[10] + ".gif")
    card_12.shape(cardpics_raw[11] + ".gif")
    card_13.shape(cardpics_raw[12] + ".gif")
    north_HCPGUI()  #runs th4e north gui function


#east hand version of the former funtion
def easthand_cardgen():
    global cardpics_raw
    cardpics_raw = [card_database[k] for k in easthand]

    card_1.shape(cardpics_raw[0] + ".gif")
    card_2.shape(cardpics_raw[1] + ".gif")
    card_3.shape(cardpics_raw[2] + ".gif")
    card_4.shape(cardpics_raw[3] + ".gif")
    card_5.shape(cardpics_raw[4] + ".gif")
    card_6.shape(cardpics_raw[5] + ".gif")
    card_7.shape(cardpics_raw[6] + ".gif")
    card_8.shape(cardpics_raw[7] + ".gif")
    card_9.shape(cardpics_raw[8] + ".gif")
    card_10.shape(cardpics_raw[9] + ".gif")
    card_11.shape(cardpics_raw[10] + ".gif")
    card_12.shape(cardpics_raw[11] + ".gif")
    card_13.shape(cardpics_raw[12] + ".gif")
    east_HCPGUI()


#south hand version of the former funtion
def southhand_cardgen():
    global cardpics_raw
    cardpics_raw = [card_database[k] for k in southhand]

    card_1.shape(cardpics_raw[0] + ".gif")
    card_2.shape(cardpics_raw[1] + ".gif")
    card_3.shape(cardpics_raw[2] + ".gif")
    card_4.shape(cardpics_raw[3] + ".gif")
    card_5.shape(cardpics_raw[4] + ".gif")
    card_6.shape(cardpics_raw[5] + ".gif")
    card_7.shape(cardpics_raw[6] + ".gif")
    card_8.shape(cardpics_raw[7] + ".gif")
    card_9.shape(cardpics_raw[8] + ".gif")
    card_10.shape(cardpics_raw[9] + ".gif")
    card_11.shape(cardpics_raw[10] + ".gif")
    card_12.shape(cardpics_raw[11] + ".gif")
    card_13.shape(cardpics_raw[12] + ".gif")
    south_HCPGUI()


#west hand version of the former funtion
def westhand_cardgen():
    global cardpics_raw
    cardpics_raw = [card_database[k] for k in westhand]

    card_1.shape(cardpics_raw[0] + ".gif")
    card_2.shape(cardpics_raw[1] + ".gif")
    card_3.shape(cardpics_raw[2] + ".gif")
    card_4.shape(cardpics_raw[3] + ".gif")
    card_5.shape(cardpics_raw[4] + ".gif")
    card_6.shape(cardpics_raw[5] + ".gif")
    card_7.shape(cardpics_raw[6] + ".gif")
    card_8.shape(cardpics_raw[7] + ".gif")
    card_9.shape(cardpics_raw[8] + ".gif")
    card_10.shape(cardpics_raw[9] + ".gif")
    card_11.shape(cardpics_raw[10] + ".gif")
    card_12.shape(cardpics_raw[11] + ".gif")
    card_13.shape(cardpics_raw[12] + ".gif")
    west_HCPGUI()


def north_HCPGUI(
):  #this finction essentially asks questions in a gui format along with writing instructions and other relevant information
    global resetbtn
    HCP_input = screen.numinput(
        "HCP input",
        "What is the HCP of the displayed north hand?:")  #asks what the HCP is
    if HCP_input > 37:
      errorinput_ = screen.textinput("Input error", "The HCP can't be smaller than 0 or greater than 37! Type yes to try again or no to return to the main menu:")
      if errorinput_ in ['yes', 'y', 'yea', 'sure', 'ok', 'yep', 'yup', 'ye']: 
        north_HCPGUI()
      else:
        main()
    elif HCP_input < 0:
      errorinput_ = screen.textinput("Input error", "The HCP can't be smaller than 0 or greater than 37! Type yes to try again or no to return to the main menu:")
      if errorinput_ in ['yes', 'y', 'yea', 'sure', 'ok', 'yep', 'yup', 'ye']: 
        north_HCPGUI()
      else:
        main()
    elif HCP_input == northhand_hcp:  #matches the input with the actual HCP and if correct continues
        turtle.penup()
        turtle.setpos(0, 50)
        turtle.write(
            "Congratulations the HCP entered is correct!",
            align="center",
            font=("Courier", 12, "italic"
                  ))  #congradulates the user on getting the answer correct.
        turtle.hideturtle()
        return_ = screen.textinput(
            "Exit to main menu",
            "Would you like to return to the start of the program?:"
        )  #asks the user if they want to return to the main menu
        if return_ in [
                'yes', 'y', 'yea', 'sure', 'ok', 'yep', 'yup', 'ye'
        ]:  #robust input method which allows many different synonyms for "yes" to be used.
            turtle.clear(
            )  #clears the turtle to ensure the text doesn't stay later.
            main(
            )  #if the input was a form of "yes" then this takes them back to the main function (start of program)
        else:
            exit(
            )  #if they enter anything else (such as no) then the program will run the exit function.
    else:
        answer_help = screen.textinput(
            "HCP helper",
            "The answer you entered for HCP was incorrect, would you like some help?, Type (No) to exit program:"
        )  #help menu makes sure the user knows how to calculate the HCP if they need a reminder and also displays the correct HCP
        if answer_help in [
                'yes', 'y', 'yea', 'sure', 'ok', 'yep', 'yup', 'ye'
        ]:
            turtle.penup()
            turtle.setpos(238, 150)
            turtle.write(
                "HCP Bridge Point Values: \n Ace = 4 points \n King = 3 points \n Queen = 2 points \n Jack = 1 point",
                align="center",
                font=("Courier", 11,
                      "italic"))  #writes the point values for each card type
            turtle.penup()
            turtle.setpos(-230, 120)
            turtle.write(
                "HCP Definition: \n High card points (HCP) \n are the cornerstone of \n hand evaluation. They \n represent numeric values \n for each honor card:\n A, K, Q and J",
                align="center",
                font=("Courier", 10, "italic")
            )  #writes the definition of HCP to potentially help the user understand
            turtle.penup()
            turtle.setpos(0, 50)
            turtle.write(
                "The correct HCP was: " + str(northhand_hcp),
                align="center",
                font=("Courier", 12,
                      "italic"))  #writes what the correct HCP is.
            resetbtn.shape("resetbtn.gif")  #diplays "reset" image
            resetbtn.penup()
            resetbtn.showturtle()
            resetbtn.goto(0, -270)
            resetbtn.onclick(
                reset
            )  #when the reset image is clicked the program resets and is taken back to the start with the funtion "main()" being run
            turtle.done(
            )  #closes the turtle to ensure if the program is running on a system such as windows or unix based systems then the program won't close and will stay open for further user inputs (this allows the user to read the information displayed aslong with allowing the user to click the reset button if needed)
        else:
            main(
            )  #if the user doesn't want help they are redirected towards the main menu


def east_HCPGUI():
    HCP_input = screen.numinput(
        "HCP input", "What is the HCP of the displayed east hand?:")
    if HCP_input > 37:
      errorinput_ = screen.textinput("Input error", "The HCP can't be smaller than 0 or greater than 37! Type yes to try again or no to return to the main menu:")
      if errorinput_ in ['yes', 'y', 'yea', 'sure', 'ok', 'yep', 'yup', 'ye']: 
        east_HCPGUI()
      else:
        main()
    elif HCP_input < 0:
      errorinput_ = screen.textinput("Input error", "The HCP can't be smaller than 0 or greater than 37! Type yes to try again or no to return to the main menu:")
      if errorinput_ in ['yes', 'y', 'yea', 'sure', 'ok', 'yep', 'yup', 'ye']: 
        east_HCPGUI()
      else:
        main()
    elif HCP_input == easthand_hcp:
        turtle.penup()
        turtle.setpos(0, 50)
        turtle.write(
            "Congratulations the HCP entered is correct!",
            align="center",
            font=("Courier", 12, "italic"))
        turtle.hideturtle()
        return_ = screen.textinput(
            "Exit to main menu",
            "Would you like to return to the start of the program?:")
        if return_ in ['yes', 'y', 'yea', 'sure', 'ok', 'yep', 'yup', 'ye']:
            turtle.clear()
            main()
        else:
            exit()
    else:
        answer_help = screen.textinput(
            "HCP helper",
            "The answer you entered for HCP was incorrect, would you like some help?, Type (No) to exit program::"
        )
        if answer_help in [
                'yes', 'y', 'yea', 'sure', 'ok', 'yep', 'yup', 'ye'
        ]:
            turtle.penup()
            turtle.setpos(238, 150)
            turtle.write(
                "HCP Bridge Point Values: \n Ace = 4 points \n King = 3 points \n Queen = 2 points \n Jack = 1 point",
                align="center",
                font=("Courier", 11, "italic"))
            turtle.penup()
            turtle.setpos(-230, 120)
            turtle.write(
                "HCP Definition: \n High card points (HCP) \n are the cornerstone of \n hand evaluation. They \n represent numeric values \n for each honor card:\n A, K, Q and J",
                align="center",
                font=("Courier", 10, "italic"))
            turtle.penup()
            turtle.setpos(0, 50)
            turtle.write(
                "The correct HCP was: " + str(easthand_hcp),
                align="center",
                font=("Courier", 12, "italic"))
            resetbtn.shape("resetbtn.gif")
            resetbtn.penup()
            resetbtn.showturtle()
            resetbtn.goto(0, -270)
            resetbtn.onclick(reset)
            turtle.done()
        else:
            main()


def south_HCPGUI():
    HCP_input = screen.numinput(
        "HCP input", "What is the HCP of the displayed south hand?:")
    if HCP_input > 37:
      errorinput_ = screen.textinput("Input error", "The HCP can't be smaller than 0 or greater than 37! Type yes to try again or no to return to the main menu:")
      if errorinput_ in ['yes', 'y', 'yea', 'sure', 'ok', 'yep', 'yup', 'ye']: 
        south_HCPGUI()
      else:
        main()
    elif HCP_input < 0:
      errorinput_ = screen.textinput("Input error", "The HCP can't be smaller than 0 or greater than 37! Type yes to try again or no to return to the main menu:")
      if errorinput_ in ['yes', 'y', 'yea', 'sure', 'ok', 'yep', 'yup', 'ye']: 
        south_HCPGUI()
      else:
        main()
    elif HCP_input == southhand_hcp:
        turtle.penup()
        turtle.setpos(0, 50)
        turtle.write(
            "Congratulations the HCP entered is correct!",
            align="center",
            font=("Courier", 12, "italic"))
        turtle.hideturtle()
        return_ = screen.textinput(
            "Exit to main menu",
            "Would you like to return to the start of the program?:")
        if return_ in ['yes', 'y', 'yea', 'sure', 'ok', 'yep', 'yup', 'ye']:
            turtle.clear()
            main()
        else:
            exit()
    else:
        answer_help = screen.textinput(
            "HCP helper",
            "The answer you entered for HCP was incorrect, would you like some help?, Type (No) to exit program:"
        )
        if answer_help in [
                'yes', 'y', 'yea', 'sure', 'ok', 'yep', 'yup', 'ye'
        ]:
            turtle.penup()
            turtle.setpos(238, 150)
            turtle.write(
                "HCP Bridge Point Values: \n Ace = 4 points \n King = 3 points \n Queen = 2 points \n Jack = 1 point",
                align="center",
                font=("Courier", 11, "italic"))
            turtle.penup()
            turtle.setpos(-230, 120)
            turtle.write(
                "HCP Definition: \n High card points (HCP) \n are the cornerstone of \n hand evaluation. They \n represent numeric values \n for each honor card:\n A, K, Q and J",
                align="center",
                font=("Courier", 10, "italic"))
            turtle.penup()
            turtle.setpos(0, 50)
            turtle.write(
                "The correct HCP was: " + str(southhand_hcp),
                align="center",
                font=("Courier", 12, "italic"))
            resetbtn.shape("resetbtn.gif")
            resetbtn.penup()
            resetbtn.showturtle()
            resetbtn.goto(0, -270)
            resetbtn.onclick(reset)
            turtle.done()
        else:
            main()


def west_HCPGUI():
    HCP_input = screen.numinput(
        "HCP input", "What is the HCP of the displayed west hand?:")
    if HCP_input > 37:
      errorinput_ = screen.textinput("Input error", "The HCP can't be smaller than 0 or greater than 37! Type yes to try again or no to return to the main menu:")
      if errorinput_ in ['yes', 'y', 'yea', 'sure', 'ok', 'yep', 'yup', 'ye']: 
        west_HCPGUI()
      else:
        main()
    elif HCP_input < 0:
      errorinput_ = screen.textinput("Input error", "The HCP can't be smaller than 0 or greater than 37! Type yes to try again or no to return to the main menu:")
      if errorinput_ in ['yes', 'y', 'yea', 'sure', 'ok', 'yep', 'yup', 'ye']: 
        west_HCPGUI()
      else:
        main()
    elif HCP_input == westhand_hcp:
        turtle.penup()
        turtle.setpos(0, 50)
        turtle.write(
            "Congratulations the HCP entered is correct!",
            align="center",
            font=("Courier", 12, "italic"))
        turtle.hideturtle()
        return_ = screen.textinput(
            "Exit to main menu",
            "Would you like to return to the start of the program?:")
        if return_ in ['yes', 'y', 'yea', 'sure', 'ok', 'yep', 'yup', 'ye']:
            turtle.clear()
            main()
        else:
            exit()
    else:
        answer_help = screen.textinput(
            "HCP helper",
            "The answer you entered for HCP was incorrect, would you like some help?, Type (No) to exit program:"
        )
        if answer_help in [
                'yes', 'y', 'yea', 'sure', 'ok', 'yep', 'yup', 'ye'
        ]:
            turtle.penup()
            turtle.setpos(238, 150)
            turtle.write(
                "HCP Bridge Point Values: \n Ace = 4 points \n King = 3 points \n Queen = 2 points \n Jack = 1 point",
                align="center",
                font=("Courier", 11, "italic"))
            turtle.penup()
            turtle.setpos(-230, 120)
            turtle.write(
                "HCP Definition: \n High card points (HCP) \n are the cornerstone of \n hand evaluation. They \n represent numeric values \n for each honor card:\n A, K, Q and J",
                align="center",
                font=("Courier", 10, "italic"))
            turtle.penup()
            turtle.setpos(0, 50)
            turtle.write(
                "The correct HCP was: " + str(westhand_hcp),
                align="center",
                font=("Courier", 12, "italic"))
            resetbtn.shape("resetbtn.gif")
            resetbtn.penup()
            resetbtn.showturtle()
            resetbtn.goto(0, -270)
            resetbtn.onclick(reset)
            turtle.done()
        else:
            main()


def position_cards(
):  #this function creates the card turtles and globalises them.
    global loading_animation, card_1, card_2, card_3, card_4, card_5, card_6, card_7, card_8, card_9, card_10, card_11, card_12, card_13
    card_1 = turtle.Turtle()
    card_2 = turtle.Turtle()
    card_3 = turtle.Turtle()
    card_4 = turtle.Turtle()
    card_5 = turtle.Turtle()
    card_6 = turtle.Turtle()
    card_7 = turtle.Turtle()
    card_8 = turtle.Turtle()
    card_9 = turtle.Turtle()
    card_10 = turtle.Turtle()
    card_11 = turtle.Turtle()
    card_12 = turtle.Turtle()
    card_13 = turtle.Turtle()

    #this area of the code sets the position of all the cards to form an aesthetically pleasing deck of cards.
    card_1.penup()
    card_1.goto(-267.5, -175)

    card_2.penup()
    card_2.goto(-177.5, -175)

    card_3.penup()
    card_3.goto(-87.5, -175)

    card_4.penup()
    card_4.goto(2.5, -175)

    card_5.penup()
    card_5.goto(92.5, -175)

    card_6.penup()
    card_6.goto(182.5, -175)

    card_7.penup()
    card_7.goto(272.5, -175)

    card_8.penup()
    card_8.goto(-222.5, -35)

    card_9.penup()
    card_9.goto(-132.5, -35)

    card_10.penup()
    card_10.goto(-42.5, -35)

    card_11.penup()
    card_11.goto(47.5, -35)

    card_12.penup()
    card_12.goto(137.5, -35)

    card_13.penup()
    card_13.goto(227.5, -35)


#creates turtles
#add all shapes to screen
def init_gui(
):  #this initialises the gui by importing some lists along with adding the logo
    cardlist_cardname = open('cardlist_cardname.txt')
    screen.addshape('PCBRIDGELOGO.gif')
    logo = turtle.Turtle()
    logo.shape('PCBRIDGELOGO.gif')
    logo.penup()
    logo.goto(0, 200)
    for i in range(52):  #this adds all the shapes to the screen
        screen.addshape(cardlist_cardname.read(2) + '.gif')


def exit():  #this function runs the sys exit that closes the program
    sys.exit()


#reset the reset turtle image (clear) and run the main function
def reset(x, y):
    main()


# initialise()
def main():
    turtle.resetscreen(
    )  #resets all the cards on screen ( this is useful when the player wants to re do the program or try another hand)
    turtle.hideturtle()  #hides the turtle pointer
    resetbtn.hideturtle()  #hides the reset button
    init_gui()  #runs the init gui function
    card_manipulation()  #runs the card manipulation function
    init_cards()  #runs the function that initialises the cards


main()  #starts the whole program
