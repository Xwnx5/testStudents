import tkinter as tk
from tkinter import messagebox
import json
from spravki import sprawka_tkinter, sprawka_django, sprawka_numpy

root = tk.Tk()
root.configure(bg="#5FA8F3")
root.title("Wictorio")
root.geometry("1280x720")
root.resizable(False,False)

icon = tk.PhotoImage(file='icon.png')
# Установить иконку
root.wm_iconphoto(True, icon)

zlabel = None
button1 = None
button2 = None
button3 = None
text_label = None

photo = tk.PhotoImage(file='wictorio.png')
global image
image =photo

global canvas
global username_entry
global password_entry
global new_username_entry
global new_password_entry
global username_label
global password_label
global username_button
global password_button
global username

def nikita_module():

    global canvas
    global username_entry
    global password_entry
    global new_username_entry
    global new_password_entry
    global username_label
    global password_label
    global new_username_label
    global new_password_label
    global login_button
    global register_button
    global username


    canvas = tk.Canvas(root, width=295, height=150, bg='#5fa8f3')
    canvas.place(relx=0.5, y = 50, anchor='center')

    global image
    image = canvas.create_image(150, 90, image=photo)

    # Функция для обработки нажатия кнопки "Войти"
    def login():
        
        with open('registr_auth.json', 'r') as f:
            users = json.load(f)
        
        global username

        username = username_entry.get()
        password = password_entry.get()
        #username = 'user1'
        #password = 'password1'


        if username in users and users[username] == password:
            messagebox.showinfo("Результат авторизации", "Авторизация прошла успешно")
            glaw()
            return True
        
        messagebox.showinfo("Результат авторизации", "Неверное имя пользователя или пароль")
        return False

        
        
    # Функция для обработки нажатия кнопки "Зарегистрироваться"
    def register():
        username = new_username_entry.get()
        password = new_password_entry.get()

        # открываем файл с данными пользователей
        with open('registr_auth.json', 'r') as f:
            users = json.load(f)

        # проверяем, что такого пользователя еще нет в базе
        if username in users:
            messagebox.showinfo("Результат регистрации", "Пользователь не зарегистрирован, логин уже занят")
            return False

        # добавляем нового пользователя в базу
        users[username] = password

        # сохраняем изменения в файле
        with open('registr_auth.json', 'w') as f:
            json.dump(users, f)

        messagebox.showinfo("Результат регистрации", "Регистрация прошла успешно")
        return True

        

    # Поля для ввода имени пользователя и пароля при входе
    username_label = tk.Label(root, text="Имя пользователя:", bg='#5fa8f3', fg='white', font=('Montserrat', 15))
    username_label.place(relx = 0.5, y = 125, anchor='center')
    username_entry = tk.Entry(root, bg='#c9e3ff')
    username_entry.place(relx = 0.5, y = 150, anchor='center')

    password_label = tk.Label(root, text="Пароль:",bg='#5fa8f3', fg='white', font=('Montserrat', 15))
    password_label.place(relx = 0.5, y = 205, anchor='center')
    password_entry = tk.Entry(root, show="*", bg='#c9e3ff')
    password_entry.place(relx = 0.5, y = 230, anchor='center')

    login_button = tk.Button(root, text="Войти", command=(login), bg='#5fa8f3', fg='white', font=('Montserrat', 15))
    login_button.place(relx = 0.5, y = 280, anchor='center')

    def change_color_on_hover(event):
        login_button.config(bg='#0289D4')  

    def change_color_on_hover2(event):
        login_button.config(bg='#5fa8f3')  

    login_button.bind('<Enter>', change_color_on_hover)
    login_button.bind('<Leave>', change_color_on_hover2)

    # Поля для ввода имени пользователя и пароля при регистрации
    new_username_label = tk.Label(root, text="Логин:", bg='#5fa8f3', fg='white', font=('Montserrat', 15))
    new_username_label.place(relx = 0.5, y = 345, anchor='center')
    new_username_entry = tk.Entry(root, bg='#c9e3ff')
    new_username_entry.place(relx = 0.5, y = 370, anchor='center')

    new_password_label = tk.Label(root, text="Пароль:", bg='#5fa8f3', fg='white', font=('Montserrat', 15))
    new_password_label.place(relx = 0.5, y = 425, anchor='center')
    new_password_entry = tk.Entry(root, show="*", bg='#c9e3ff')
    new_password_entry.place(relx = 0.5, y = 450, anchor='center')

    register_button = tk.Button(root, text="Зарегистрироваться", command=register, bg='#5fa8f3', fg='white', font=('Montserrat', 15))
    register_button.place(relx = 0.5, y = 500, anchor='center')

    def change_color_on_register_button(event):
        register_button.config(bg='#0289D4')  

    def change_color_on_register_button2(event):
        register_button.config(bg='#5fa8f3')  

    register_button.bind('<Enter>', change_color_on_register_button)
    register_button.bind('<Leave>', change_color_on_register_button2)

def glaw():
    global zlabel, button1, button2, button3 ,text_label

    global canvas
    global username_entry
    global password_entry
    global new_username_entry
    global new_password_entry
    global username_label
    global password_label
    global login_button
    global register_button
    global new_username_label
    global new_password_label
    
    canvas.place_forget()
    username_entry.place_forget()
    password_entry.place_forget()
    new_username_entry.place_forget()
    new_password_entry.place_forget()
    username_label.place_forget()
    password_label.place_forget()
    login_button.place_forget()
    register_button.place_forget()
    new_username_label.place_forget()
    new_password_label.place_forget()

    zlabel = tk.Label(root, text="Главное меню", font=("Montserrat", 34), fg="white", bg="#5FA8F3")
    zlabel.place(relx=0.5, rely=0.2, anchor='center')

    button1 = tk.Button(root, text="Тесты", bg="#5FA8F3", font=("Montserrat", 20), fg="white", command=wtest)
    button1.place(relx=0.5, rely=0.4, anchor='center')
    def change_color_on_hover1(event):
        button1.config(bg="#0289d4")
    def change_color_on_leave1(event):
        button1.config(bg="#5FA8F3")
    button1.bind("<Enter>" ,change_color_on_hover1)
    button1.bind("<Leave>" ,change_color_on_leave1)

    button2 = tk.Button(root, text="Лидеры", bg="#5FA8F3", font=("Montserrat", 20), fg="white")
    button2.place(relx=0.5, rely=0.5, anchor='center')
    def change_color_on_hover2(event):
        button2.config(bg="#0289d4")
    def change_color_on_leave2(event):
        button2.config(bg="#5FA8F3")
    button2.bind("<Enter>" ,change_color_on_hover2)
    button2.bind("<Leave>" ,change_color_on_leave2)

    button3 = tk.Button(root, text="Справочник", bg="#5FA8F3", font=("Montserrat", 20), fg="white", command=spraw)
    button3.place(relx=0.5, rely=0.6, anchor='center')
    def change_color_on_hover3(event):
        button3.config(bg="#0289d4")
    def change_color_on_leave3(event):
        button3.config(bg="#5FA8F3")
    button3.bind("<Enter>" ,change_color_on_hover3)
    button3.bind("<Leave>" ,change_color_on_leave3)


def spraw():
    global zlabel, button1, button2, button3 ,text_label
    # скрыть кнопки выбора тестов
    zlabel.place_forget()
    button1.place_forget()
    button2.place_forget()
    button3.place_forget()
    # Создаем заголовок по центру сверху
    zlabel = tk.Label(root,
                      text="Справочник по:",
                      font=("Montserrat", 34),
                      fg="white",
                      bg="#5FA8F3")
    zlabel.place(relx=0.5, rely=0.2, anchor='center')
    def sprawtkinter1():
        main_button.place_forget()
        sprawtkinter()
        pass
    # Создаем три кнопки по центру друг под за другом слева на право
    button1 = tk.Button(root,
                        text="tkinter",
                        bg="#5FA8F3",
                        font=("Montserrat", 20),
                        fg="white",
                        width=18, command=sprawtkinter1)
    button1.place(relx=0.25, rely=0.5, anchor='center')
    def sprawDJ1():
        main_button.place_forget()
        sprawDJ()
        pass
    button2 = tk.Button(root,
                        text="Django",
                        bg="#5FA8F3",
                        font=("Montserrat", 20),
                        fg="white",
                        width=18, command = sprawDJ1)
    button2.place(relx=0.5, rely=0.5, anchor='center')
    def sprawNp1():
        main_button.place_forget()
        sprawNp()
        pass
    button3 = tk.Button(root,
                        text="NumPy",
                        bg="#5FA8F3",
                        font=("Montserrat", 20),
                        fg="white",
                        width=18, command=sprawNp1)
    button3.place(relx=0.75, rely=0.5, anchor='center')
    def glaw2():
        main_button.place_forget()
        button1.place_forget()
        button2.place_forget()
        button3.place_forget()
        zlabel.place_forget()
        glaw()
        pass

    # Создание кнопки "Главная"
    main_button = tk.Button(root, text="меню", font=("Montserrat", 20), fg="white", bg="#5FA8F3", command=glaw2)
    main_button.place(relx=0.5, rely=0.90, anchor='center')
    def change_color_on_hover5(event):
        main_button.config(bg="#0289d4")
    def change_color_on_hover6(event):
        main_button.config(bg="#5FA8F3")
    main_button.bind("<Enter>" ,change_color_on_hover5)
    main_button.bind("<Leave>" ,change_color_on_hover6)

    # Добавляем эффект при наведении курсора на кнопку 2
    def change_color_on_hover1(event):
        button1.config(bg="#0289d4")

    def change_color_on_hover1_2(event):
        button1.config(bg="#5FA8F3")
    
    def change_color_on_hover2(event):
        button2.config(bg="#0289d4")

    def change_color_on_hover2_2(event):
        button2.config(bg="#5FA8F3")

    def change_color_on_hover3(event):
        button3.config(bg="#0289d4")

    def change_color_on_hover3_2(event):
        button3.config(bg="#5FA8F3")

    button1.bind("<Enter>" ,change_color_on_hover1)
    button1.bind("<Leave>" ,change_color_on_hover1_2)

    button3.bind("<Enter>" ,change_color_on_hover3)
    button3.bind("<Leave>" ,change_color_on_hover3_2)

    button2.bind("<Enter>" ,change_color_on_hover2)
    button2.bind("<Leave>" ,change_color_on_hover2_2)

def testDjango():
    global zlabel, button1, button2, button3, text_label
    # скрыть кнопки выбора тестов
    zlabel.place_forget()
    button1.place_forget()
    button2.place_forget()
    button3.place_forget()

    # список вопросов и правильных ответов
    questions = [
        {
            "question": "Вопрос 1:Что такое Django? ",
            "answers": ["Фреймворк для разработки на языке Java ", "Фреймворк для разработки веб-приложений на языке Python", "Редактор кода для работы с HTML и CSS",
                        "Веб-сервер для хранения статических файлов"],
            "right_answer": "Фреймворк для разработки веб-приложений на языке Python"
        },
        {
            "question": "Вопрос 2:Какая модель базы данных используется в Django по умолчанию?",
            "answers": ["NoSQL", "MySQL", "SQLite", "PostgreSQL"],
            "right_answer": "SQLite"
        },
        {
            "question": "Вопрос 3:Какой файл содержит основные настройки проекта Django?",
            "answers": ["views.py", "models.py", "settings.py", "urls.py"],
            "right_answer": "settings.py"
        },
        {
            "question": "Вопрос 4:Как создать новое Django приложение?",
            "answers": [
                "Создать новый Python-скрипт в папке проекта",
                "Использовать команду python manage.py startapp < app_name > ",
                "Использовать команду python manage.py createapp < app_name > ",
                "Создать новую папку внутри проекта и добавить туда необходимые файлы"
            ],
            "right_answer": "Использовать команду python manage.py startapp < app_name > "
        },
        {
            "question": "Вопрос 5:Какие две основные части веб-приложения можно реализовать с \nпомощью Django?",
            "answers": [
                "Клиентскую и серверную",
                "Мобильную и десктопную",
                "Бэкенд и фронтенд",
                "Административную панель и пользовательский интерфейс"
            ],
            "right_answer": "Бэкенд и фронтенд"
        },
        {
            "question": "Вопрос 6:Какой шаблонный язык используется в Django?",
            "answers": [
                "HTML",
                "CSS",
                "JavaScript",
                "Django Template Language"
            ],
            "right_answer": "Django Template Language"
        },
        {
            "question": "Вопрос 7:Что такое ORM в Django?",
            "answers": [
                "Объектно-реляционное отображение, позволяющее \nработать с базой данных через объекты Python",
                "Открытый стандарт обмена данными в Интернете",
                "Механизм для создания автоматически генерируемой документации кода",
                "Функционал для проверки корректности написания кода"
            ],
            "right_answer": "Объектно-реляционное отображение, позволяющее работать с базой данных через объекты Python"
        },
        {
            "question": "Вопрос 8:Какая команда используется для запуска локального \nсервера Django?",
            "answers": [
                "python runserver",
                "django start",
                "run server",
                "start django"
            ],
            "right_answer": "python runserver"
        },
        {
            "question": "Вопрос 9:Какие части проекта могут быть созданы с помощью \n\tDjango Rest Framework?",
            "answers": [
                "Только клиентская часть",
                "Все части веб-приложения",
                "Только серверная часть",
                "Десктопные приложения"
            ],
            "right_answer": "Только серверная часть"
        },
        {
            "question": "Вопрос 10:Какое расширение файлов используется для шаблонов Django?",
            "answers": [
                ".html",
                ".py",
                ".css",
                ".js"
            ],
            "right_answer": ".html"
        }
    ]

    ball = 0  # переменная для хранения количества правильных ответов
    question_no = 0  # номер текущего вопроса

    # создаем элементы интерфейса
    question_label = tk.Label(root, text=questions[question_no]["question"], font=("Montserrat", 20), fg="white",
                              bg="#5FA8F3")
    question_label.place(relx=0.1, rely=0.2)

    answer_buttons = []
    for i, answer in enumerate(questions[question_no]["answers"]):
        button = tk.Button(root, text=answer, font=("Montserrat", 16), fg="white", bg="#1D6FB7", height=2)
        button.place(relx=0.1, rely=0.3 + i * 0.15)
        answer_buttons.append(button)

    next_button = tk.Button(root, text="Далее", font=("Montserrat", 16), fg="white", bg="#1D6FB7", width=10,
                            command=lambda: next_question())
    next_button.place(relx=0.8, rely=0.9)

    def next_question():
        nonlocal question_no, ball
        # проверяем ответ на текущий вопрос

        for button in answer_buttons:
            button.configure(bg='#1D6FB7')

        selected_answer = None
        for i, button in enumerate(answer_buttons):
            if button["relief"] == "sunken":
                selected_answer = questions[question_no]["answers"][i]
                break

        if selected_answer == questions[question_no]["right_answer"]:
            ball += 1

        # переходим к следующему вопросу или завершаем тест
        question_no += 1
        if question_no < len(questions):
            question_label.configure(text=questions[question_no]["question"])
            for i, answer in enumerate(questions[question_no]["answers"]):
                answer_buttons[i].configure(text=answer, relief="raised")
        else:
            # скрываем элементы интерфейса и выводим результаты теста
            question_label.place_forget()
            for button in answer_buttons:
                button.place_forget()
            next_button.place_forget()
            #tk.Label(root, text=f"Your score: {ball}/{len(questions)}", font=("Montserrat", 34), fg="white",bg="#5FA8F3").place(relx=0.5, rely=0.4, anchor='center')
            
            #name = user_data["name"]
            name = username
            #score = user_data["score"]
            score = ball*10
           
            # загружаем текущие результаты из JSON-файла
            with open("bd_django.json", 'r', encoding='utf-8') as file:
                data = json.load(file)
            results = {
                        "name": f"{username}",
                        "score": score
                      }
            data[f"user{len(data)+1}"] = results
            # сохраняем отсортированные результаты в JSON-файл
            with open("bd_django.json", 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
            
            # Загрузка данных из JSON файла
            with open("bd_django.json", 'r', encoding='utf-8') as f:
                results = json.load(f)

            # Получение имени пользователя и его результатов
            user_data = results["user"]

            label1 = tk.Label(root, text="Поздравляем с окончанием теста!!!", bg="#5FA8F3", font=("Montserrat", 34), fg="white")
            label1.place(relx=0.5, rely=0.12, anchor='center')

            label2 = tk.Label(root, text=f"{name}, ваш результат:", bg="#5FA8F3", font=("Montserrat", 34), fg="white")
            label2.place(relx=0.5, rely=0.2, anchor='center')

            label3 = tk.Label(root, text=f"{score} баллов из 100", bg="#5FA8F3", font=("Montserrat", 34), fg="white")
            label3.place(relx=0.5, rely=0.3, anchor='center')
            
            label4 = tk.Label(root, bg="white", font=("Montserrat", 15), fg="black")
            label4.place(relx=0.5, rely=0.62, anchor='center', width=450, height=300)

            headers = ["ИМЯ ИГРОКА", "ОЧКИ"]

            data = []

            for key in results:
                if key.startswith("user"):
                    user = results[key]
                    data.append([user["name"], user["score"]])

            # Сортировка данных по убыванию баллов
            data.sort(key=lambda x: x[1], reverse=True)

            # Заполнение таблицы
            for i in range(len(headers)):
                header_label = tk.Label(root, text=headers[i], font=("Montserrat", 15), bg="white")
                header_label.place(relx=0.41 + 0.2 * i, rely=0.47, anchor='center')

            for j in range(len(data[:5])):
                for k in range(len(data[j])):
                    data_label = tk.Label(root, text=data[j][k], font=("Montserrat", 15), bg="white")
                    data_label.place(relx=0.41 + 0.2 * k, rely=0.53 + j * 0.06, anchor='center')

            button = tk.Button(root, text="Закончить", bg="#5FA8F3", font=("Montserrat", 20), fg="white")
            button.place(relx=0.5, rely=0.92, anchor='center')

            def change_color_on_hover1(event):
                button.config(bg="#0289d4")

            def change_color_on_hover2(event):
                button.config(bg="#5fa8f3")

            button.bind("<Enter>", change_color_on_hover1)
            button.bind("<Leave>", change_color_on_hover2)

    def select_answer(i):
        # меняем стиль кнопки при выборе ответа
        for j, button in enumerate(answer_buttons):
            if i == j:
                button.configure(relief="sunken")
                button.config(bg='#18a058')

            else:
                button.configure(relief="raised")
                button.config(bg='#1D6FB7')

    # привязываем функцию обработки выбора ответа к каждой кнопке
    for i, button in enumerate(answer_buttons):
        button.configure(command=lambda i=i: select_answer(i))

def testNumPy():
    global zlabel, button1, button2, button3, text_label
    # скрыть кнопки выбора тестов
    zlabel.place_forget()
    button1.place_forget()
    button2.place_forget()
    button3.place_forget()

    # список вопросов и правильных ответов
    questions = [
        {
            "question": "Вопрос 1:Какой модуль необходимо импортировать\n для работы с NumPy в Python? ",
            "answers": ["pandas ", "numpy", "sklearn",
                        "matplotlib"],
            "right_answer": "numpy"
        },
        {
            "question": "Вопрос 2:Как создать массив из нулей размером 3x3 в NumPy?",
            "answers": ["np.zeros((3))", "np.zeros(3)", "np.zeros((3,3))", "np.zeroes((3x3))"],
            "right_answer": "np.zeros((3,3))"
        },
        {
            "question": "Вопрос 3:Какие математические операции можно применять к \nмассивам NumPy?",
            "answers": ["Умножение на число", "Сложение", "Вычитание", "Все перечисленные"],
            "right_answer": "Все перечисленные"
        },
        {
            "question": "Вопрос 4:Как получить максимальное значение в массиве NumPy?",
            "answers": [
                "np.maximum(array)",
                "np.max(array)",
                "array.max()",
                "max(array)"
            ],
            "right_answer": "np.max(array)"
        },
        {
            "question": "Вопрос 5:Как узнать форму массива NumPy?",
            "answers": [
                "array.shape()",
                "np.shape(array)",
                "shape.array()",
                "array.ndim()"
            ],
            "right_answer": "np.shape(array)"
        },
        {
            "question": "Вопрос 6:Как создать массив со значениями от 0 до 9 включительно\n в NumPy?",
            "answers": [
                "np.array([0:9])",
                "np.array(range(0, 9))",
                "np.arange(10)",
                "np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])"
            ],
            "right_answer": "np.arange(10)"
        },
        {
            "question": "Вопрос 7:Как изменить форму массива NumPy?",
            "answers": [
                "array.reshape((new_shape))",
                "np.reshape(array, new_shape)",
                "array.resize(new_shape)",
                "Все перечисленные"
            ],
            "right_answer": "array.reshape((new_shape))"
        },
        {
            "question": "Вопрос 8:Как получить среднее значение элементов массива NumPy?",
            "answers": [
                "np.mean(array)",
                "array.mean()",
                "mean(array)",
                "np.average(array)"
            ],
            "right_answer": "np.mean(array)"
        },
        {
            "question": "Вопрос 9:Как умножить два массива в NumPy поэлементно?",
            "answers": [
                "array1 @ array2",
                "np.multiply(array1, array2)",
                "np.dot(array1, array2)",
                "array1 * array2"
            ],
            "right_answer": "np.multiply(array1, array2)"
        },
        {
            "question": "Вопрос 10:Какой тип данных может храниться в массивах NumPy?",
            "answers": [
                "Целые числа и строки",
                "Только целые числа",
                "Любой тип данных, поддерживаемый Python",
                "Строки и вещественные числа"
            ],
            "right_answer": "Любой тип данных, поддерживаемый Python"
        }
    ]

    ball = 0  # переменная для хранения количества правильных ответов
    question_no = 0  # номер текущего вопроса

    # создаем элементы интерфейса
    question_label = tk.Label(root, text=questions[question_no]["question"], font=("Montserrat", 20), fg="white",
                              bg="#5FA8F3")
    question_label.place(relx=0.1, rely=0.2)

    answer_buttons = []
    for i, answer in enumerate(questions[question_no]["answers"]):
        button = tk.Button(root, text=answer, font=("Montserrat", 16), fg="white", bg="#1D6FB7", height=2)
        button.place(relx=0.1, rely=0.3 + i * 0.15)
        answer_buttons.append(button)

    next_button = tk.Button(root, text="Далее", font=("Montserrat", 16), fg="white", bg="#1D6FB7", width=10,
                            command=lambda: next_question())
    next_button.place(relx=0.8, rely=0.9)

    def next_question():
        nonlocal question_no, ball
        # проверяем ответ на текущий вопрос

        for button in answer_buttons:
            button.configure(bg='#1D6FB7')

        selected_answer = None
        for i, button in enumerate(answer_buttons):
            if button["relief"] == "sunken":
                selected_answer = questions[question_no]["answers"][i]
                break

        if selected_answer == questions[question_no]["right_answer"]:
            ball += 1

        # переходим к следующему вопросу или завершаем тест
        question_no += 1
        if question_no < len(questions):
            question_label.configure(text=questions[question_no]["question"])
            for i, answer in enumerate(questions[question_no]["answers"]):
                answer_buttons[i].configure(text=answer, relief="raised")
        else:
            # скрываем элементы интерфейса и выводим результаты теста
            question_label.place_forget()
            for button in answer_buttons:
                button.place_forget()
            next_button.place_forget()
            #tk.Label(root, text=f"Your score: {ball}/{len(questions)}", font=("Montserrat", 34), fg="white",bg="#5FA8F3").place(relx=0.5, rely=0.4, anchor='center')
            #name = user_data["name"]
            name = username
            #score = user_data["score"]
            score = ball*10
           
            # загружаем текущие результаты из JSON-файла
            with open("bd_numpy.json", 'r', encoding='utf-8') as file:
                data = json.load(file)
            results = {
                        "name": f"{username}",
                        "score": score
                      }
            data[f"user{len(data)+1}"] = results
            # сохраняем отсортированные результаты в JSON-файл
            with open("bd_numpy.json", 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
            
            # Загрузка данных из JSON файла
            with open("bd_numpy.json", 'r', encoding='utf-8') as f:
                results = json.load(f)

            # Получение имени пользователя и его результатов
            user_data = results["user"]

            label1 = tk.Label(root, text="Поздравляем с окончанием теста!!!", bg="#5FA8F3", font=("Montserrat", 34), fg="white")
            label1.place(relx=0.5, rely=0.12, anchor='center')

            label2 = tk.Label(root, text=f"{name}, ваш результат:", bg="#5FA8F3", font=("Montserrat", 34), fg="white")
            label2.place(relx=0.5, rely=0.2, anchor='center')

            label3 = tk.Label(root, text=f"{score} баллов из 100", bg="#5FA8F3", font=("Montserrat", 34), fg="white")
            label3.place(relx=0.5, rely=0.3, anchor='center')
            
            label4 = tk.Label(root, bg="white", font=("Montserrat", 15), fg="black")
            label4.place(relx=0.5, rely=0.62, anchor='center', width=450, height=300)

            headers = ["ИМЯ ИГРОКА", "ОЧКИ"]

            data = []

            for key in results:
                if key.startswith("user"):
                    user = results[key]
                    data.append([user["name"], user["score"]])

            # Сортировка данных по убыванию баллов
            data.sort(key=lambda x: x[1], reverse=True)

            # Заполнение таблицы
            for i in range(len(headers)):
                header_label = tk.Label(root, text=headers[i], font=("Montserrat", 15), bg="white")
                header_label.place(relx=0.41 + 0.2 * i, rely=0.47, anchor='center')

            for j in range(len(data[:5])):
                for k in range(len(data[j])):
                    data_label = tk.Label(root, text=data[j][k], font=("Montserrat", 15), bg="white")
                    data_label.place(relx=0.41 + 0.2 * k, rely=0.53 + j * 0.06, anchor='center')

            button = tk.Button(root, text="Закончить", bg="#5FA8F3", font=("Montserrat", 20), fg="white")
            button.place(relx=0.5, rely=0.92, anchor='center')

            def change_color_on_hover1(event):
                button.config(bg="#0289d4")

            def change_color_on_hover2(event):
                button.config(bg="#5fa8f3")

            button.bind("<Enter>", change_color_on_hover1)
            button.bind("<Leave>", change_color_on_hover2)

    def select_answer(i):
        # меняем стиль кнопки при выборе ответа
        for j, button in enumerate(answer_buttons):
            if i == j:
                button.configure(relief="sunken")
                button.config(bg='#18a058')

            else:
                button.configure(relief="raised")
                button.config(bg='#1D6FB7')

    # привязываем функцию обработки выбора ответа к каждой кнопке
    for i, button in enumerate(answer_buttons):
        button.configure(command=lambda i=i: select_answer(i))


def testTkinter():
    global zlabel, button1, button2, button3, text_label
    # скрыть кнопки выбора тестов
    zlabel.place_forget()
    button1.place_forget()
    button2.place_forget()
    button3.place_forget()

    # список вопросов и правильных ответов
    questions = [
        {
            "question": "Вопрос 1:Что такое библиотека Tkinter? ",
            "answers": ["Библиотека для работы с базами данных ", "Библиотека для создания графического пользовательского интерфейса ", "Библиотека для создания анимации",
                        "Библиотека для парсинга веб-страниц"],
            "right_answer": "Библиотека для создания графического пользовательского интерфейса "
        },
        {
            "question": "Вопрос 2:Какой метод используется для создания нового окна в Tkinter?",
            "answers": ["create_window()", "new_window()", "Tk()", "window.create()"],
            "right_answer": "Tk()"
        },
        {
            "question": "Вопрос 3:Как добавить текст в виджет Label в Tkinter?",
            "answers": ["label.add_text()", "label.config(text=текст) ", "label.append(текст)", "label.set(текст)"],
            "right_answer": "label.config(text=текст) "
        },
        {
            "question": "Вопрос 4:Какие из перечисленных выражений будут использоваться для\n создания кнопки в Tkinter?",
            "answers": [
                "Button",
                "Text",
                "LabelFrame",
                "Canvas"
            ],
            "right_answer": "Button"
        },
        {
            "question": "Вопрос 5:Как зарегистрировать обработчик события на кнопке в Tkinter?",
            "answers": [
                "button.register_handler()",
                "button.attach_event_handler()",
                "button.bind(event_name, handler)",
                "button.add_event_listener()"
            ],
            "right_answer": "button.bind(event_name, handler)"
        },
        {
            "question": "Вопрос 6:Как добавить изображение в Tkinter?",
            "answers": [
                "image.load()",
                "image.set()",
                "PhotoImage(file=путь_к_изображению) ",
                "photo.add()"
            ],
            "right_answer": "PhotoImage(file=путь_к_изображению) "
        },
        {
            "question": "Вопрос 7:Как закрыть окно в Tkinter?",
            "answers": [
                "win.exit()",
                "win.destroy()",
                "win.close()",
                "win.quit()"
            ],
            "right_answer": "win.destroy()"
        },
        {
            "question": "Вопрос 8:Как добавить поля для текста в Tkinter?",
            "answers": [
                "Text",
                "Entry",
                "Label",
                "Message"
            ],
            "right_answer": "Entry"
        },
        {
            "question": "Вопрос 9:Что такое меню в Tkinter?",
            "answers": [
                "Список доступных опций для выбора пользователем ",
                "Интерфейс приложения, который отображается при запуске",
                "Область виджетов, которые могут быть перемещены по экрану",
                "Виджет для отображения диалоговых окон"
            ],
            "right_answer": "Список доступных опций для выбора пользователем"
        },
        {
            "question": "Вопрос 10:Как разместить элементы на форме в Tkinter?",
            "answers": [
                "grid()",
                "place()",
                "pack()",
                "Все выше перечисленные"
            ],
            "right_answer": "Все выше перечисленные"
        },
    ]

    ball = 0  # переменная для хранения количества правильных ответов
    question_no = 0  # номер текущего вопроса

    # создаем элементы интерфейса
    question_label = tk.Label(root, text=questions[question_no]["question"], font=("Montserrat", 20), fg="white",
                              bg="#5FA8F3")
    question_label.place(relx=0.1, rely=0.2)

    answer_buttons = []
    for i, answer in enumerate(questions[question_no]["answers"]):
        button = tk.Button(root, text=answer, font=("Montserrat", 16), fg="white", bg="#1D6FB7", height=2)
        button.place(relx=0.1, rely=0.3 + i * 0.15)
        answer_buttons.append(button)

    next_button = tk.Button(root, text="Далее", font=("Montserrat", 16), fg="white", bg="#1D6FB7", width=10,
                            command=lambda: next_question())
    next_button.place(relx=0.8, rely=0.9)

    def next_question():
        nonlocal question_no, ball
        global username
        # проверяем ответ на текущий вопрос

        for button in answer_buttons:
            button.configure(bg='#1D6FB7')

        selected_answer = None
        for i, button in enumerate(answer_buttons):
            if button["relief"] == "sunken":
                selected_answer = questions[question_no]["answers"][i]
                break

        if selected_answer == questions[question_no]["right_answer"]:
            ball += 1

        # переходим к следующему вопросу или завершаем тест
        question_no += 1
        if question_no < len(questions):
            question_label.configure(text=questions[question_no]["question"])
            for i, answer in enumerate(questions[question_no]["answers"]):
                answer_buttons[i].configure(text=answer, relief="raised")
        else:
            # скрываем элементы интерфейса и выводим результаты теста
            question_label.place_forget()
            for button in answer_buttons:
                button.place_forget()
            next_button.place_forget()
            #tk.Label(root, text=f"Your score: {ball}/{len(questions)}", font=("Montserrat", 34), fg="white",bg="#5FA8F3").place(relx=0.5, rely=0.4, anchor='center')
            #name = user_data["name"]
            name = username
            #score = user_data["score"]
            score = ball*10
           
            # загружаем текущие результаты из JSON-файла
            with open("bd_tkinter.json", 'r', encoding='utf-8') as file:
                data = json.load(file)
            results = {
                        "name": f"{username}",
                        "score": score
                      }
            data[f"user{len(data)+1}"] = results
            # сохраняем отсортированные результаты в JSON-файл
            with open("bd_tkinter.json", 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
            
            # Загрузка данных из JSON файла
            with open("bd_tkinter.json", 'r', encoding='utf-8') as f:
                results = json.load(f)

            # Получение имени пользователя и его результатов
            user_data = results["user"]

            label1 = tk.Label(root, text="Поздравляем с окончанием теста!!!", bg="#5FA8F3", font=("Montserrat", 34), fg="white")
            label1.place(relx=0.5, rely=0.12, anchor='center')

            label2 = tk.Label(root, text=f"{name}, ваш результат:", bg="#5FA8F3", font=("Montserrat", 34), fg="white")
            label2.place(relx=0.5, rely=0.2, anchor='center')

            label3 = tk.Label(root, text=f"{score} баллов из 100", bg="#5FA8F3", font=("Montserrat", 34), fg="white")
            label3.place(relx=0.5, rely=0.3, anchor='center')
            
            label4 = tk.Label(root, bg="white", font=("Montserrat", 15), fg="black")
            label4.place(relx=0.5, rely=0.62, anchor='center', width=450, height=300)

            headers = ["ИМЯ ИГРОКА", "ОЧКИ"]

            data = []

            for key in results:
                if key.startswith("user"):
                    user = results[key]
                    data.append([user["name"], user["score"]])

            # Сортировка данных по убыванию баллов
            data.sort(key=lambda x: x[1], reverse=True)

            # Заполнение таблицы
            for i in range(len(headers)):
                header_label = tk.Label(root, text=headers[i], font=("Montserrat", 15), bg="white")
                header_label.place(relx=0.41 + 0.2 * i, rely=0.47, anchor='center')

            for j in range(len(data[:5])):
                for k in range(len(data[j])):
                    data_label = tk.Label(root, text=data[j][k], font=("Montserrat", 15), bg="white")
                    data_label.place(relx=0.41 + 0.2 * k, rely=0.53 + j * 0.06, anchor='center')

            button = tk.Button(root, text="Закончить", bg="#5FA8F3", font=("Montserrat", 20), fg="white")
            button.place(relx=0.5, rely=0.92, anchor='center')

            def change_color_on_hover1(event):
                button.config(bg="#0289d4")

            def change_color_on_hover2(event):
                button.config(bg="#5fa8f3")

            button.bind("<Enter>", change_color_on_hover1)
            button.bind("<Leave>", change_color_on_hover2)

    def select_answer(i):
        # меняем стиль кнопки при выборе ответа
        for j, button in enumerate(answer_buttons):
            if i == j:
                button.configure(relief="sunken")
                button.config(bg='#18a058')

            else:
                button.configure(relief="raised")
                button.config(bg='#1D6FB7')

    # привязываем функцию обработки выбора ответа к каждой кнопке
    for i, button in enumerate(answer_buttons):
        button.configure(command=lambda i=i: select_answer(i))

def wtest():
    global zlabel, button1, button2, button3 ,text_label
    # скрыть кнопки выбора тестов
    zlabel.place_forget()
    button1.place_forget()
    button2.place_forget()
    button3.place_forget()
    zlabel = tk.Label(root, text="Выберите тест", font=("Montserrat", 34), fg="white", bg="#5FA8F3")
    zlabel.place(relx=0.5, rely=0.2, anchor='center')
    def testDjango1():
        main_button.place_forget()
        testDjango()
        pass
    button1 = tk.Button(root, text="Тест Django", bg="#5FA8F3", font=("Montserrat", 20), fg="white", width=20,command=testDjango1)
    button1.place(relx=0.5, rely=0.4, anchor='center')
    def change_color_on_hover1(event):
        button1.config(bg="#0289d4")
    def change_color_on_hover2(event):
        button1.config(bg="#5FA8F3")
    button1.bind("<Enter>" ,change_color_on_hover1)
    button1.bind("<Leave>" ,change_color_on_hover2)
    def testNumPy1():
        main_button.place_forget()
        testNumPy()
        pass
    button2 = tk.Button(root, text="NumPy", bg="#5FA8F3", font=("Montserrat", 20), fg="white", width=20, command=testNumPy1)
    button2.place(relx=0.5, rely=0.5, anchor='center')
    def change_color_on_hover3(event):
        button2.config(bg="#0289d4")
    def change_color_on_hover4(event):
        button2.config(bg="#5FA8F3")
    button2.bind("<Enter>" ,change_color_on_hover3)
    button2.bind("<Leave>" ,change_color_on_hover4)
    def testTkinter1():
        main_button.place_forget()
        testTkinter()
        pass
    button3 = tk.Button(root, text="tkinter", bg="#5FA8F3", font=("Montserrat", 20), fg="white", width=20, command=testTkinter1)
    button3.place(relx=0.5, rely=0.6, anchor='center')
    def change_color_on_hover5(event):
        button3.config(bg="#0289d4")
    def change_color_on_hover6(event):
        button3.config(bg="#5FA8F3")
    button3.bind("<Enter>" ,change_color_on_hover5)
    button3.bind("<Leave>" ,change_color_on_hover6)

    def glaw2():
        main_button.place_forget()
        button1.place_forget()
        button2.place_forget()
        button3.place_forget()
        zlabel.place_forget()
        glaw()
        pass

    # Создание кнопки "Главная"
    main_button = tk.Button(root, text="меню", font=("Montserrat", 20), fg="white", bg="#5FA8F3", command=glaw2)
    main_button.place(relx=0.5, rely=0.90, anchor='center')
    def change_color_on_hover5(event):
        main_button.config(bg="#0289d4")
    def change_color_on_hover6(event):
        main_button.config(bg="#5FA8F3")
    main_button.bind("<Enter>" ,change_color_on_hover5)
    main_button.bind("<Leave>" ,change_color_on_hover6)

def sprawDJ():
    global zlabel, button1, button2, button3 ,text_label
    # скрыть кнопки выбора тестов
    zlabel.place_forget()
    button1.place_forget()
    button2.place_forget()
    button3.place_forget()
    zlabel = tk.Label(root, text="Справочник по Django Framework", font=("Montserrat", 34), fg="white", bg="#5FA8F3")
    zlabel.place(relx=0.5, rely=0.1, anchor='center')

    # Отображение текста о Django
    text = sprawka_django

    label_frame = tk.LabelFrame(root, text="Django Framework")
    label_frame.pack(padx=10, pady=120)

    # Создаем листающуюся метку с использованием Scrollbar и Text
    scrollbar = tk.Scrollbar(label_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    text_widget = tk.Text(label_frame, wrap='word', yscrollcommand=scrollbar.set)
    text_widget.pack(expand=True, fill=tk.BOTH)

    scrollbar.config(command=text_widget.yview)

    def glaw2():
        main_button.place_forget()
        zlabel.place_forget()
        label_frame.pack_forget()
        text_widget.pack_forget()
        glaw()
        pass

    # Добавляем текст в метку
    text_widget.insert(tk.END, text)
    # Создание кнопки "Главная"
    main_button = tk.Button(root, text="меню", font=("Montserrat", 20), fg="white", bg="#5FA8F3", command=glaw2)
    main_button.place(relx=0.5, rely=0.90, anchor='center')
    def change_color_on_hover5(event):
        main_button.config(bg="#0289d4")
    def change_color_on_hover6(event):
        main_button.config(bg="#5FA8F3")
    main_button.bind("<Enter>" ,change_color_on_hover5)
    main_button.bind("<Leave>" ,change_color_on_hover6)

def sprawNp():
    global zlabel, button1, button2, button3 ,text_label
    # скрыть кнопки выбора тестов
    zlabel.place_forget()
    button1.place_forget()
    button2.place_forget()
    button3.place_forget()
    zlabel = tk.Label(root, text="Справочник по NumPy", font=("Montserrat", 34), fg="white", bg="#5FA8F3")
    zlabel.place(relx=0.5, rely=0.1, anchor='center')

    # Отображение текста о numpy
    text = sprawka_numpy

    label_frame = tk.LabelFrame(root, text="NumPy")
    label_frame.pack(padx=10, pady=120)

    # Создаем листающуюся метку с использованием Scrollbar и Text
    scrollbar = tk.Scrollbar(label_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    text_widget = tk.Text(label_frame, wrap='word', yscrollcommand=scrollbar.set)
    text_widget.pack(expand=True, fill=tk.BOTH)

    scrollbar.config(command=text_widget.yview)

    # Добавляем текст в метку
    text_widget.insert(tk.END, text)
    def glaw2():
        main_button.place_forget()
        zlabel.place_forget()
        label_frame.pack_forget()
        text_widget.pack_forget()
        glaw()
        pass

    # Добавляем текст в метку
    text_widget.insert(tk.END, text)
    # Создание кнопки "Главная"
    main_button = tk.Button(root, text="меню", font=("Montserrat", 20), fg="white", bg="#5FA8F3", command=glaw2)
    main_button.place(relx=0.5, rely=0.90, anchor='center')
    def change_color_on_hover5(event):
        main_button.config(bg="#0289d4")
    def change_color_on_hover6(event):
        main_button.config(bg="#5FA8F3")
    main_button.bind("<Enter>" ,change_color_on_hover5)
    main_button.bind("<Leave>" ,change_color_on_hover6)
def sprawtkinter():
    global zlabel, button1, button2, button3 ,text_label
    # скрыть кнопки выбора тестов
    zlabel.place_forget()
    button1.place_forget()
    button2.place_forget()
    button3.place_forget()
    zlabel = tk.Label(root, text="Справочник по Tkinter", font=("Montserrat", 34), fg="white", bg="#5FA8F3")
    zlabel.place(relx=0.5, rely=0.1, anchor='center')

    # Отображение текста о tkinter
    text = sprawka_tkinter

    label_frame = tk.LabelFrame(root, text="tkinter")
    label_frame.pack(padx=10, pady=120)

    # Создаем листающуюся метку с использованием Scrollbar и Text
    scrollbar = tk.Scrollbar(label_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    text_widget = tk.Text(label_frame, wrap='word', yscrollcommand=scrollbar.set)
    text_widget.pack(expand=True, fill=tk.BOTH)

    scrollbar.config(command=text_widget.yview)

    # Добавляем текст в метку
    text_widget.insert(tk.END, text)
    def glaw2():
        main_button.place_forget()
        zlabel.place_forget()
        label_frame.pack_forget()
        text_widget.pack_forget()
        glaw()
        pass

    # Добавляем текст в метку
    text_widget.insert(tk.END, text)
    # Создание кнопки "Главная"
    main_button = tk.Button(root, text="меню", font=("Montserrat", 20), fg="white", bg="#5FA8F3", command=glaw2)
    main_button.place(relx=0.5, rely=0.90, anchor='center')
    def change_color_on_hover5(event):
        main_button.config(bg="#0289d4")
    def change_color_on_hover6(event):
        main_button.config(bg="#5FA8F3")
    main_button.bind("<Enter>" ,change_color_on_hover5)
    main_button.bind("<Leave>" ,change_color_on_hover6)

if __name__ == "__main__":
    nikita_module()
    
    root.mainloop()