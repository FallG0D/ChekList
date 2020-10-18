#pady/x Отступ по Х или У сверху/ сбоку
#radiobutton- класс позволяющий выбрать только одно значение


#Импорт модулей
from tkinter import*
#Функция для текста
def open_text():
    text_frame.pack(side=TOP, anchor=0, pady=10)
    
    lbl_name.grid(row=0, column=1, sticky=E)
    ent_name.grid(row=0, column=1, sticky=W, padx=10)

    lbl_bdate.grid(row=1,column=0, sticky=E)
    ent_bdate.grid(row=1,column=1, sticky=W, padx=10)

def open_radio():
    radio_frame.pack(side=TOP, anchor=0, padx=10)



    lbl_sex.pack(side=Top, anchor=W)
    male.pack(side=Left, anchor=W)
    female.pack(side=Left, anchor=W)
    

#Окно для радиокнопок - выбор пола
radio_frame = Frame(master=root)

lbl_sex = Label(master=radio_frame, text="Выберите пол:")

var = Intvar()
var.set(0)
male = Radiobutton(master=radio_frame, text="Мужской", variable=var, value=0)
female = Radiobutton(master=radio_frame, text="Женский", variable=var, value=1)


#Установка основного окна
root = Tk()
root.title("Регистрация пользователя")

#Окно с текстом
text_frame= Frame(master=root)

lbl_name = Label(master=text_frame,text="Введите ФИО:")
ent_name = Entry(master=text_frame)

lbl_bdate = Label(master=text_frame,text="Введите дату рождения:")
ent_bdate = Entry(master=text_frame)

#Активируем функцию
open_text()
open_radio()
#Функции развертывания
root.mainloop()