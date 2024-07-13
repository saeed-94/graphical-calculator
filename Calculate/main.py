import flet as ft
import math

def main(page: ft.Page):
    page.title = "Calculator"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.window_width = 400
    page.window_height = 480 
    page.window.resizable = False
    page.bgcolor = "#071952"
    page.update()
    
    def click(e):

        if e.control.data in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "+", "-", "*", "/", "(", ")"]:
      
          if e.control.data == ".":
                if "." not in Txt.value:
                    Txt.value += "."
          else:
                Txt.value = str(Txt.value) + str(e.control.data)
    
                page.update()

        elif e.control.data == "=":
                try:
                    result = eval(Txt.value)
                    if isinstance(result, float) and result.is_integer():
                        Txt.value = str(int(result))
                    else:
                        Txt.value = str(result)
                except ZeroDivisionError:
                    Txt.value = "NAN"
                
                page.update()
        
        elif e.control.data == "C":
            Txt.value = ""
            page.update()

        elif e.control.data == "<":
            lst = list(Txt.value)
            lst.pop()
            Txt.value = "".join(map(str, lst))
            page.update()
        
        elif e.control.data == "π":
            Txt.value = math.pi
            print(math.pi)
            page.update()
        
        elif e.control.data == "x²":
            Txt.value = math.pow(float(Txt.value), 2)
            page.update()
        
        elif e.control.data == "abs":
            Txt.value = abs(float(Txt.value))
            page.update()

        elif e.control.data == "√x":
            Txt.value = math.sqrt(float(Txt.value))
            page.update()

        elif e.control.data == "Sin()":
            if (float(Txt.value)) % 180 == 0:
                Txt.value = math.sin(math.radians(float(Txt.value)))    
                Txt.value = round(Txt.value)
                page.update()
        
            else:     
                Txt.value = math.sin(math.radians(float(Txt.value)))
                page.update()

        elif e.control.data == "Cos()":
            if (float(Txt.value)) % 180 == 90:
                Txt.value = math.cos(math.radians(float(Txt.value)))    
                Txt.value = round(Txt.value)
                page.update()
            else:
                Txt.value = math.cos(math.radians(float(Txt.value)))
                page.update()
        
        elif e.control.data == "Tan()":
            if (float(Txt.value)) % 180 == 90:
                Txt.value = "NAN"
                page.update()
            else:

                Txt.value = math.tan(math.radians(float(Txt.value)))
                page.update()

        elif e.control.data == "Cot()":
            if (float(Txt.value)) % 180 == 0:
                Txt.value = "NAN"
                page.update()

            if (float(Txt.value)) % 180 == 90:
                Txt.value = str(0)
                
                page.update()
            else:

                Txt.value = 1 / (math.tan(math.radians(float(Txt.value))))
                page.update()





    Txt = ft.TextField(border_color="#ffffff", read_only=True, text_size= 30)
 
    btn_sin = ft.ElevatedButton(text= "Sin()", data = "Sin()",on_click = click,width=85, height=40, bgcolor= "#37B7C3", color="#232323" ,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)))
    btn_cos = ft.ElevatedButton(text= "Cos()", data = "Cos()",on_click = click,width=85, height=40, bgcolor= "#37B7C3", color="#232323" ,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)))
    btn_tan = ft.ElevatedButton(text= "Tan()", data = "Tan()",on_click = click,width=85, height=40, bgcolor= "#37B7C3", color="#232323" ,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)))
    btn_cot = ft.ElevatedButton(text= "Cot()", data="Cot()",on_click = click,width=85, height=40, bgcolor= "#37B7C3", color="#232323" ,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)))

    btn_square = ft.ElevatedButton(text= "x²",data = "x²",on_click = click,width=85, height=40, bgcolor= "#37B7C3", color="#232323" ,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)))
    btn_abs = ft.ElevatedButton(text= "abs",data= "abs",on_click = click,width=85, height=40, bgcolor= "#37B7C3", color="#232323" ,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)))
    btn_pi = ft.ElevatedButton(text= "π",data="π",on_click = click,width=85, height=40, bgcolor= "#37B7C3", color="#232323" ,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)))
    btn_squareـroot = ft.ElevatedButton(text= "√x",data = "√x", on_click = click,width=85, height=40, bgcolor= "#37B7C3", color="#232323" ,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)))

    btn_delete_char = ft.ElevatedButton(text= "<",data="<",on_click= click,width=85, height=40, bgcolor= "#80AF81", color="#232323" ,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)))
    btn_parentheses_open = ft.ElevatedButton(text= "(", data = "(",on_click = click,width=85, height=40, bgcolor= "#80AF81", color="#232323" ,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)))
    btn_parentheses_close = ft.ElevatedButton(text= ")", data = ")",on_click = click,width=85, height=40, bgcolor= "#80AF81", color="#232323" ,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)))
    btn_division = ft.ElevatedButton(text= "÷", data = "/",on_click = click,width=85, height=40, bgcolor= "#80AF81", color="#232323" ,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)))
 
    btn_7 = ft.ElevatedButton(text= "7", data = "7",on_click = click,width=85, height=40, bgcolor= "#FFFFFF", color="#232323" ,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)))
    btn_8 = ft.ElevatedButton(text= "8", data = "8",on_click = click,width=85, height=40, bgcolor= "#FFFFFF", color="#232323" ,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)))
    btn_9 = ft.ElevatedButton(text= "9", data = "9",on_click = click,width=85, height=40, bgcolor= "#FFFFFF", color="#232323" ,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)))
    btn_multiplication = ft.ElevatedButton(text= "X", data = "*", on_click=click,width=85, height=40, bgcolor= "#80AF81", color="#232323" ,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)))

    btn_4 = ft.ElevatedButton(text= "4", data = "4",on_click = click,width=85, height=40, bgcolor= "#FFFFFF", color="#232323" ,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)))
    btn_5 = ft.ElevatedButton(text= "5", data = "5",on_click = click,width=85, height=40, bgcolor= "#FFFFFF", color="#232323" ,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)))
    btn_6 = ft.ElevatedButton(text= "6", data = "6",on_click = click,width=85, height=40, bgcolor= "#FFFFFF", color="#232323" ,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)))
    btn_subtraction = ft.ElevatedButton(text= "-", data = "-",on_click = click,width=85, height=40, bgcolor= "#80AF81", color="#232323" ,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)))

    btn_1 = ft.ElevatedButton(text= "1", data = "1",on_click = click,width=85, height=40, bgcolor= "#FFFFFF", color="#232323" ,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)))
    btn_2 = ft.ElevatedButton(text= "2", data = "2",on_click = click,width=85, height=40, bgcolor= "#FFFFFF", color="#232323" ,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)))
    btn_3 = ft.ElevatedButton(text= "3", data = "3",on_click = click,width=85, height=40, bgcolor= "#FFFFFF", color="#232323" ,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)))
    btn_total = ft.ElevatedButton(text= "+", data = "+",on_click = click,width=85, height=40, bgcolor= "#80AF81", color="#232323" ,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)))

    btn_clear = ft.ElevatedButton(text= "C", data="C",on_click = click,width=85, height=40, bgcolor= "#80AF81", color="#232323" ,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)))
    btn_0 = ft.ElevatedButton(text= "0", data = "0",on_click = click,width=85, height=40, bgcolor= "#FFFFFF", color="#232323" ,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)))
    btn_dot = ft.ElevatedButton(text= ".", data = ".",on_click = click,width=85, height=40, bgcolor= "#FFFFFF", color="#232323" ,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)))
    btn_equal = ft.ElevatedButton(text= "=", data="=",on_click = click,width=85, height=40, bgcolor= "#80AF81", color="#232323" ,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)))

    






    page.add(Txt,

             ft.Row(controls=[btn_sin, btn_cos, btn_tan, btn_cot], alignment= ft.MainAxisAlignment.SPACE_AROUND
),              
             ft.Row(controls=[btn_square, btn_abs, btn_pi, btn_squareـroot], alignment= ft.MainAxisAlignment.SPACE_AROUND
), 
             ft.Row(controls=[btn_delete_char, btn_parentheses_open, btn_parentheses_close, btn_division], alignment= ft.MainAxisAlignment.SPACE_AROUND
),
             ft.Row(controls=[btn_7, btn_8, btn_9, btn_multiplication], alignment= ft.MainAxisAlignment.SPACE_AROUND
),
             ft.Row(controls=[btn_4, btn_5, btn_6, btn_subtraction], alignment= ft.MainAxisAlignment.SPACE_AROUND
),
             ft.Row(controls=[btn_1, btn_2, btn_3, btn_total], alignment= ft.MainAxisAlignment.SPACE_AROUND
),
             ft.Row(controls=[btn_clear, btn_0, btn_dot, btn_equal], alignment= ft.MainAxisAlignment.SPACE_AROUND
),
    )
    page.update()

ft.app(target=main)