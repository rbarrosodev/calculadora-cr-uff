from PySimpleGUI import PySimpleGUI as sg

medias = []
ch_total = 0

# Layouts
def create_media():
    sg.theme('DarkBlue12')
    layout = [
        [sg.Text('Nota', size=(12,1)), sg.Input(key='nota')],
        [sg.Text('Carga Horária', size=(12,1)), sg.Input(key='carga_horaria')],
        [sg.Button('Enviar'), sg.Button('Finalizar')]
    ]
    return sg.Window('Calculadora de CR UFF', layout=layout, finalize=True)

def display_success(x, y):
    sg.theme('DarkBlue12')
    layout = [
        [sg.Text('Sua média foi criada com sucesso!')],
        [sg.Text(f'Nota: {x}')],
        [sg.Text(f'Carga Horária: {y}')],
        [sg.Button('Voltar')]
    ]
    return sg.Window('Media criada', layout=layout, finalize=True)

def display_cr(x):
    sg.theme('DarkBlue12')
    layout = [
        [sg.Text(f'Seu CR atual é: {x}')],
        [sg.Button('Finalizar')]
    ]
    return sg.Window('CR calculado', layout=layout, finalize=True)

window1, window2, window3 = create_media(), None, None

# Funcionalidade
while True:
    window, event, values = sg.read_all_windows()
    
    if window == window1 and event == sg.WIN_CLOSED:
        break

    if window == window1 and event == 'Enviar' and float(values['nota']) >= 0.0 and int(values['carga_horaria']) > 0:
        window2 = display_success(float(values['nota']), int(values['carga_horaria']))
        window1.hide()
        media = float(values['nota']) * int(values['carga_horaria'])
        medias.append(media)
        ch_total += int(values['carga_horaria'])
    
    if window == window1 and event == 'Finalizar' and sum(medias) > 0.0:
        cr = round((sum(medias) / ch_total), 2)
        window3 = display_cr(cr)
        window1.hide()
    
    if window == window2 and event == 'Voltar':
        window1.find_element('nota').update('')
        window1.find_element('carga_horaria').update('')
        window2.hide()
        window1.un_hide()

    if window == window3 and event == 'Finalizar':
        break