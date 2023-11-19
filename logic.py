import random
import PySimpleGUI as sg

def generate_random_number(start, end):
    return random.randint(start, end)

def create_layout(title, elements):
    layout = [[sg.Text(title)]]
    layout.extend(elements)
    return layout

def get_user_input(title, key):
    return sg.popup_get_text(title, key=key)

def display_popup(message):
    sg.popup(message)

def display_question_popup(day, month):
    return sg.popup_yes_no(f"Чи це {day} число та {month} місяць?", keep_on_top=True)

def restart_game_prompt():
    return sg.popup_yes_no("Бажаєте спробувати ще раз?", keep_on_top=True)

def guess_birthday_layout():
    return create_layout(
        "Оберіть межі для днів та місяців:",
        [
            [sg.Text("Початковий день (1-31):"), sg.InputText(key='start_day')],
            [sg.Text("Кінцевий день (1-31):"), sg.InputText(key='end_day')],
            [sg.Text("Початковий місяць (1-12):"), sg.InputText(key='start_month')],
            [sg.Text("Кінцевий місяць (1-12):"), sg.InputText(key='end_month')],
            [sg.Button('Почати гру'), sg.Button('Вийти')],
        ]
    )

def play_game(start_day, end_day, start_month, end_month):
    secret_day = generate_random_number(start_day, end_day)
    secret_month = generate_random_number(start_month, end_month)

    display_popup("Давайте спробуємо вгадати ваш день народження!")

    while True:
        guess_day = generate_random_number(start_day, end_day)
        guess_month = generate_random_number(start_month, end_month)

        if display_question_popup(guess_day, guess_month) == 'Yes':
            if guess_day == secret_day and guess_month == secret_month:
                display_popup("Ура! Я вгадав!")
            else:
                display_popup("Шкода, спробуймо ще раз.")

            if restart_game_prompt() == 'Yes':
                break
            else:
                return

def guess_birthday():
    layout = guess_birthday_layout()
    window = sg.Window('Вгадай день народження', layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Вийти':
            break

        if event == 'Почати гру':
            start_day = int(values['start_day'])
            end_day = int(values['end_day'])
            start_month = int(values['start_month'])
            end_month = int(values['end_month'])

            play_game(start_day, end_day, start_month, end_month)

    window.close()

guess_birthday()