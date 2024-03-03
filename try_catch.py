hrs = input("Enter Hours:")
rate_p_hr = input("Enter Rate per hour:")
try:
    h = float(hrs)
    rph = float(rate_p_hr)
except:
    print("Error: Please enter numeric input")
    quit()
if h<=40.0:
    print(float(h*rph))
else:
    temp = (h-40.0)*(1.5 * rph)
    print((40* rph)+temp)

score = input("Enter Score: ")
s = float(score)
if s>=0.9:
    print('A')
elif s>=0.8 and s<0.9:
    print('B')