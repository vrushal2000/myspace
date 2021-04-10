x = 0
score = x

print("THAT'S BRILLIANT! you're promoted to the next level...ALL THE BEST!")
# Question One 
print("How many watts are represented by 40dbW")
answer_1 = input("a)1000W\nb)10000W\nc)40000W\nd)40W\n:")
if answer_1.lower() == "b" or answer_1.lower()== "10000W":
    print("Correct")
    x = x + 1   
else:
    print("Incorrect, The answer is 10000W")

# Question Two
print("What is the seventh harmonic of 300kHz")
answer_2 = input("a)1260kHz\nb)2520kHz\nc)5040kHz\nd)7000kHz\n:")
if answer_2.lower() == "b" or answer_2.lower() == "2520kHz":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, the seventh harmonic of 300kHz is 2520kHz")

# Question Three
print("Vc=2, Vm=2 what change do you think will generate a under modulated waveform?")
answer_3 = input("a)decrease Vm such that Vm<Vc\nb)increase Vc such that Vc>Vm\nc)increase carrier voltage\nd)All of the above\n:")
if answer_3.lower() == "d" or answer_3.lower() == "All of the above":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, All of the options will generate under modulated waveform")  

# Question Four
print("In  a low-level modulation system, the type of amplifier that follows the modulated stage should be a _________")
answer_4 = input("a)Harmonic generator\nb)Linear Amplifier\nc)Class C Amplifier\nd)none of the above\n:")
if answer_4.lower() == "b" or answer_4 == "Linear Amplifier":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, The answer is Linear Amplifier")

# Question Five 
print("Vmax=20 Vmin=4 What is the reason for not perfect modulation?")
answer_5 = input("a)Over modulation \nb) under modulation\nc)Vmax not equal to Vmin\nd)None of the above\n:")
if answer_5.lower() == "b" or answer_5.lower() == "Under modulation":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, m<1 will generate a under modulated waveform")


#Total Score
score = float(x / 5) * 100
print(x,"out of 5, that is",score, "%")
if x>2:
    print("You're einsteinious! you're promoted to the next level...LAST LEVEL TO GO!")
    b=input("press y to continue")
    if b=="y":
        import os
        os.startfile('x3.py')
    else:
        b=input("press y or quit")
else:
    print("NEVERMIND , start again!")
a=input("press y to continue")
if a=="y":
    import os
    os.startfile('x.py')
else:
    close()
