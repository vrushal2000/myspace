x = 0
score = x

print("COME ON! You can do it last level to go...ALL THE BEST!")
# Question One 
print("Carrier =80V USB= 10V LSB=9.5V m=0.25 Find the mistake in information above")
answer_1 = input("a)LSB should be 10\nb)USB should be 9.5\nc)USB and LSB should be 9\nd)All of the above\n:")
if answer_1.lower() == "a" or answer_1.lower()== "LSB should be 10":
    print("Correct")
    x = x + 1   
else:
    print("Incorrect, only the option LSB=10 satisfies the information")

# Question Two
print("Pc=133.33  m=o.4 Pt=150 What information is wrong")
answer_2 = input("a)Pc\nb)m\nc)Pt\nd)All of the above\n:")
if answer_2.lower() == "c" or answer_2.lower() == "Pt":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, Total power when calculated is different from given value")

# Question Three
print("A sinusoidal carrier has amplitude of 10V and frequency 30 kHz. It is amplitude modulated by a sinusoidal voltage of amplitude 3V and frequency 1kHz. Modulated voltage is developed across 50 Ohm resistance. Calculate total power")
answer_3 = input("a)1.045\nb)0.045\nc)2.105\nd)0.041\n:")
if answer_3.lower() == "a" or answer_3.lower() == "1.045":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, The answer is 1.045")  

# Question Four
print("To increase information transmission rate what should you do.")
answer_4 = input("a)increase frequency\nb)increase bandwidth\nc)decrease frequency \nd)decrease bandwidth\n:")
if answer_4.lower() == "b" or answer_4 == "increase bandwidth":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, Bandwidth is directly proportional to information transmission rate")

# Question Five 
print("How many time more bandwidth does the UHF band have than VHF band?")
answer_5 = input("a)1000 \nb) 10\nc)100\nd)1\n:")
if answer_5.lower() == "b" or answer_5.lower() == "10":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, The answer is 10")


#Total Score
score = float(x / 5) * 100
print(x,"out of 5, that is",score, "%")
if x>2:
    print("Bravo! you're good to go...!")
    b=input("press y to continue")
    if b=="y":
        close();
    else:
        close();
else:
    print("NEVERMIND , start again!")
a=input("press y to continue")
if a=="y":
    import os
    os.startfile('x.py')
else:
    close()
