import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_turtle = turtle.Turtle()
answer_turtle.pu()
answer_turtle.hideturtle()
state_guessed = []


# def find_x(row, number):
#     x1 = (row["x"])
#     ans_x = x1[number]
#     return ans_x


# def find_y(row, number):
#     x2 = (row["y"])
#     ans_y = x2[number]
#     return ans_y
data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
state_dict = data.state.to_dict()
score = 0
while len(state_guessed) < 50:
    total_state = 50
    answer_state = screen.textinput(
        title=f"{score}/{total_state}Guess the State", prompt="What's another State's name?")
    ans = answer_state.title()

    if ans == "Exit":
        missing_states = []
        for state in state_list:
            if state not in state_guessed:
                missing_states.append(state)
        end_data = pandas.DataFrame(missing_states)
        end_data.to_csv("end_data.csv")
        break
    if ans in state_list:
        state_guessed.append(ans)
        score += 1
        # ans_row = data[data.state == ans].to_dict()
        # state_x = find_x(ans_row, row_num)
        # state_y = find_y(ans_row, row_num)
        state_data = data[data.state == ans]
        answer_turtle.setposition(int(state_data.x), int(state_data.y))
        answer_turtle.write(arg=ans)
        row_num = data[data['state'] == ans].index[0]
        del state_dict[row_num]
