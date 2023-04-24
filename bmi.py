from tkinter import *
FONT = ("Arial", 15, "normal")
FONT1 = ("Arial", 12, "normal")

window=Tk()
window.title
window.title("BMI Calculator")
window.geometry("1200x750")

def bmi_index():
    sonuc=(float(user_input1.get())) / ((float(user_input2.get())/100)**2)
    if sonuc>35:
        cikti="you are extremely obese"
    elif sonuc>30:
        cikti="you are obese"
    elif sonuc>25:
        cikti="you are owerweight"
    elif sonuc>18:
        cikti="you are normal"
    else:
        cikti="you are underweight"
    final_sonuc.config(text=cikti)
    
        

tabela1 = Label(text="Enter your weight (kg)",font=FONT)
tabela1.pack(padx=20, pady=20)

user_input1=Entry(window)
user_input1.pack(padx=10, pady=10)

tabela2 = Label(text="Enter your height (cm)",font=FONT)
tabela2.pack(padx=20, pady=20)

user_input2=Entry(window)
user_input2.pack(padx=10, pady=10)

button1=Button(window,text="Calculate",command=bmi_index)
button1.pack()

final_sonuc=Label(text="",font=FONT1)
final_sonuc.pack(padx=20, pady=20)

mainloop()