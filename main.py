import turtle
import pandas

FONT_STYLE = ('Courier', 6, 'normal')

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
number_of_states = len(data)
number_of_correct = 0
correct_guesses = []

continueGame = True

while continueGame:
    answer_state = screen.textinput(title=f"{number_of_correct}/{number_of_states} States Correct", prompt="What's another state's name?").title()

    # end program on exit
    if answer_state == "Exit":
        break

    for state in data.state:
        if state == answer_state and answer_state not in correct_guesses:
            number_of_correct += 1
            correct_guesses.append(answer_state)
            correct_state_from_table = (data.loc[data['state'] == answer_state])

            correct_state_xcor = correct_state_from_table.at[correct_state_from_table.index[0], 'x']
            correct_state_ycor = correct_state_from_table.at[correct_state_from_table.index[0], 'y']

            correct_state = turtle.Turtle()
            correct_state.penup()
            correct_state.hideturtle()
            correct_state.goto(x=correct_state_xcor, y=correct_state_ycor)
            correct_state.color("black")
            correct_state.write(answer_state, align="CENTER", font=FONT_STYLE)

    # end program if the user guessed all states
    if len(correct_guesses) == len(data.state):
        break

# missed states to learn.csv
learn_to_states = []

for state in data.state:
    if state not in correct_guesses:
        learn_to_states.append(state)

table_learn_to_states = pandas.DataFrame(learn_to_states, columns=["states"])
table_learn_to_states.to_csv("learn.csv")
