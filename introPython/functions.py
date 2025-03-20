marks = int(input("Enter your marks: "))

def result(marks):
    if marks >= 90:
        print("Votre grade est A")
    elif marks >= 80:
        print("Votre grade est B")    
    elif marks >= 70:
        print("Votre grade est C")
    elif marks >= 60:
        print("Votre grade est D")
    else:
        print("You are fail")


result(marks)