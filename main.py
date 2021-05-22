from PySimpleGUI import PySimpleGUI as sg

medias = []
ch_total = 0

# Layouts
def create_media():
    sg.theme('DarkBlue12')
    layout = [
        [sg.Text('Nota', size=(12,1)), sg.Input(key='nota')],
        [sg.Text('Carga Horária', size=(12,1)), sg.Input(key='carga_horaria')],
        [sg.Button('Enviar'), sg.Button('Finalizar'), sg.Button('Fiquei de VS')]
    ]
    return sg.Window('Calculadora de CR UFF', layout=layout, finalize=True)

def calculate_vs():
    sg.theme('DarkBlue12')
    layout = [
        [sg.Text('Nota', size=(12,1)), sg.Input(key='nota')],
        [sg.Text('Nota da VS', size=(12,1)), sg.Input(key='nota_vs')],
        [sg.Text('Carga Horária', size=(12,1)), sg.Input(key='carga_horaria')],
        [sg.Button('Enviar')]
    ]
    return sg.Window('Calculadora de CR UFF com VS', layout=layout, finalize=True)

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

window1, window2, window3, window4 = create_media(), None, None, None

# Funcionalidade
while True:
    window, event, values = sg.read_all_windows()
    
    if (window == window1 or window == window2 or window == window3 or window == window4) and event == sg.WIN_CLOSED:
        break

    if window == window1 and event == 'Fiquei de VS':
        window4 = calculate_vs()
        window1.hide()

    if window == window4 and event == 'Enviar' and float(values['nota']) >= 0.0 and float(values['nota_vs']) >= 0.0 and int(values['carga_horaria']) > 0:
        window4.hide()
        if float(values['nota_vs']) >= 6.0:
            window2 = display_success(6.0, int(values['carga_horaria']))
            media = 6.0 * int(values['carga_horaria'])
        else:
            window2 = display_success((float(values['nota']) + float(values['nota_vs'])) / 2.0, int(values['carga_horaria']))
            media = ((float(values['nota']) + float(values['nota_vs'])) / 2.0) * int(values['carga_horaria'])
        medias.append(media)
        ch_total += int(values['carga_horaria'])

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