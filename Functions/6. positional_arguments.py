def total_marks(maths, science, english, hindi, history):
    # Here we have taken 5 paramters,so once we call this function we need to add the arguments in order to put the correct marks for each subject that means position for the argument will matter whenever we will be calling the function.
    total = maths + science + english + hindi + history
    print(total)


total_marks(89, 74, 84, 11, 23)
# Here in this way we need to carefully see each subject marks and then need to add the marks in the argument.
total_marks(english=84, hindi=11, science=74, history=23, maths=89)
# To avoid the positional issue we have added the named argument for the function and sequence doesn't matter here.
