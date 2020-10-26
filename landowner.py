is_male = False
is_tall = True


if is_male and is_tall:
    print("you are a tall male")
elif is_male and not(is_tall):
    print("you are a shrot male")
elif not is_male and not(is_tall):
    print("you are a shrot girl")
elif not is_male and (is_tall):
    print("you are a tall girl")
