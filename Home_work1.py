import datetime
print("Здравствуй")
name = input("Стой куда ты? Ну ты и соня, как тебя зовут?: ")
name = name.strip()
print("Что это за имя такое? " + name.title() + " Ну хорошо")
age = int(input("А скажи " +  name.title() + ", сколько тебе лет?: "))
todayYear = datetime.datetime.now().year
print("Ого так ты", + (todayYear - age), "года")
