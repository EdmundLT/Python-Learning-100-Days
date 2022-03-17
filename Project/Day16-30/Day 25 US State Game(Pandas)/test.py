import pandas

data = pandas.read_csv("50_states.csv")

state_dict = data.state.to_dict()
del state_dict[]
print(state_dict)
