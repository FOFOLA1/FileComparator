from dotenv import load_dotenv

PySimpleGUI_License = load_dotenv("PSG_LICENCE")

import PySimpleGUI as psg

file_orig = ""
file_comp = ""
file_orig_cont = ""
file_comp_cont = ""
    
layout = [
    [
        psg.Text(
            "File Compare",
            font=('Arial Bold', 25),
            size=25,
            expand_x=True,
            justification='center')
    ],
    [
        psg.Frame(
            "",
            border_width=0,
            layout=[
                [
                    psg.Input(
                        file_orig,
                        expand_x=True,
                        font=('Arial', 15),
                        size=37,
                        expand_y=True,
                        key="--Inp_path1--"
                    ),
                    psg.Button(
                        "Browse",
                        font=('Arial', 15),
                        key="--BUTTON_browse1--"
                    )
                ],[
                    psg.Multiline(
                        file_orig_cont,
                        font=('Arial', 15),
                        s=(45,25),
                        horizontal_scroll=True,
                        key="--ML_file1--"
                    ),
                ]
            ]
        ),
        psg.VerticalLine(
            color="black"
        ),
        psg.Frame(
            "",
            border_width=0,
            layout=[
                [
                    psg.Input(
                        file_comp,
                        expand_x=True,
                        font=('Arial', 15),
                        size=37,
                        expand_y=True,
                        key="--Inp_path2--"
                    ),
                    psg.Button(
                        "Browse",
                        font=('Arial', 15),
                        key="--BUTTON_browse2--"
                    )
                ],[
                    psg.Multiline(
                        file_comp_cont,
                        font=('Arial', 15),
                        s=(45,25),
                        horizontal_scroll=True,
                        key="--ML_file2--"
                    ),
                ]
            ]
        )
    ],
    [
        psg.Button(
            "OK",
            font=('Arial Bold', 15),
            size=15,
            key="--BUTTON_OK--")
        
    ]
    
]

win = psg.Window(
    "File Compare", 
    layout=layout, 
    element_justification="center",
    resizable=True)


while True:
    event, values = win.read()
    print(event, values)
    
    if event in (None, 'Exit') or event == "--BUTTON_OK--":
        break
    
    elif event == "--BUTTON_browse1--":
        file_orig = psg.popup_get_file("", no_window=True)
        
        try:
            with open(file_orig, "r") as f:
                file_orig_cont = f.read()
        except:
            file_orig_cont = ""
        win["--ML_file1--"].update(file_orig_cont)
        win["--Inp_path1--"].update(file_orig)
        
    elif event == "--BUTTON_browse2--":
        file_comp = psg.popup_get_file("", no_window=True)
        
        try:   
            with open(file_comp, "r") as f:
                file_comp_cont = f.read()
        except:
            file_comp_cont = ""
            
        win["--ML_file2--"].update(file_comp_cont)
        win["--Inp_path2--"].update(file_comp)

win.close()