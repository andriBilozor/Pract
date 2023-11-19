import random
import PySimpleGUI as sg

def generate_random_number(start, end):
    return random.randint(start, end)

def guess_birthday_layout():
    layout = [
        [sg.Text("Оберіть межі для днів та місяців:")],
        [sg.Text("Початковий день (1-31):"), sg.InputText(key='start_day')],
        [sg.Text("Кінцевий день (1-31):"), sg.InputText(key='end_day')],
        [sg.Text("Початковий місяць (1-12):"), sg.InputText(key='start_month')],
        [sg.Text("Кінцевий місяць (1-12):"), sg.InputText(key='end_month')],
        [sg.Button('Почати гру'), sg.Button('Вийти')],
    ]
    return layout

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

            secret_day = generate_random_number(start_day, end_day)
            secret_month = generate_random_number(start_month, end_month)

            sg.popup("Давайте спробуємо вгадати ваш день народження!")

            while True:
                guess_day = generate_random_number(start_day, end_day)
                guess_month = generate_random_number(start_month, end_month)

                layout = [
                    [sg.Text(f"Чи це {guess_day} число та {guess_month} місяць?")],
                    [sg.Button('Так'), sg.Button('Ні')],
                ]

                window_guess = sg.Window('Вгадай день народження', layout)

                event_guess, _ = window_guess.read()

                if event_guess == sg.WIN_CLOSED or event_guess == 'Так':
                    window_guess.close()
                    if guess_day == secret_day and guess_month == secret_month:
                        sg.popup("Ура! Я вгадав!")
                    else:
                        sg.popup("Шкода, спробуймо ще раз.")
                    
                    restart_layout = [
                        [sg.Text("Бажаєте спробувати ще раз?")],
                        [sg.Button('Так'), sg.Button('Вийти')],
                    ]
                    
                    restart_window = sg.Window('Продовжити?', restart_layout)
                    restart_event, _ = restart_window.read()
                    
                    if restart_event == 'Так':
                        restart_window.close()
                        break
                    else:
                        restart_window.close()
                        window.close()
                        return

                elif event_guess == 'Ні':
                    window_guess.close()

    window.close()

guess_birthday()