x = 0
score = x
# Question One
print("Signal Bandwidth is defined as the portion of _______ occupied by a signal.")   
answer_1 = input("a)Electromagnetic spectrum\nb)area\nc)waveform\nd)Channel\n:")
if answer_1.lower() == "a":
    print("Correct")
    x = x + 1   
else:
    print("Incorrect, The answer is Electromagnetic spectrum")



# Question Two
print("Frequency spectrum is the representation of a signal in _________")
answer_2 = input("a)Bandwidth\nb)Time domain\nc)Frequency domain\nd)space domain\n:")
if answer_2.lower() == "c" or answer_2.lower() == "Frequency domain":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, Frequency spectrum is the representation of a signal in frequency domain")

# Question Three
print("What is bandwidth?")
answer_3 = input("a)1/frequency\nb)difference of upper and lower frequency\nc)1/wavelength\nd)power*frequency\n:")
if answer_3.lower() == "b" or answer_3.lower() == "difference of upper and lower frequency":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, Bandwidth is the difference of upper and lower frequency")  

# Question Four
print("What is the wavelength for a frequency of 1 million hertz?")
answer_4 = input("a)30km\nb)3km\nc)30m\nd)300m\n:")
if answer_4.lower() == "d" or answer_4 == "300m":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, The answer is 300m")

# Question Five 
print("Power is always _______.")
answer_5 = input("a)A definite amount  of energy \nb)Expressed in watts\nc)The rate at which energy is used\nd)All of the above\n:")
if answer_5.lower() == "d" or answer_5.lower() == "All of the above":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, HAHA gotcha it is all of the above")


#Total Score
score = float(x / 5) * 100
print(x,"out of 5, that is",score, "%")
if x>2:
    print("THAT'S BRILLIANT! you're promoted to the next level...ALL THE BEST!")
    b=input("press y to continue")
    if b=="y":
        import os
        os.startfile('x2.py')
    else:
        b=input("press y or quit")
    
    
else:
    print("That's poor knowledge, try again!/n")
a=input("press y to continue")
if a=="y":
    import os
    os.startfile('x.py')
else:
    close()





