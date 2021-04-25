from tkinter import *
from tkinter.ttk import Combobox
from tkinter.ttk import Radiobutton
#from W-Net-Pytorch import test.py
from fesi.py import fesi
import normal.adaptive_color_deconvolution
def process():
    a = combo.get()
    lbl.configure(text=a)  
def process_norm():
    pass

def process_not_norm():
    pass

window = Tk()  
window.title("Segmentation")
window.geometry('800x500')
lbl = Label(window, text = '', font=("Arial Bold", 14))  
lbl.grid(column=0, row=2)  
combo = Combobox(window)  
combo['values'] = ('вырезать просветы желез','не вырезать просветы желез')  
combo.current(1)  # установите вариант по умолчанию  
combo.grid(column=0, row=0)  
btn = Button(window, text="Do!",command = process)
btn.grid(column=4, row=0)

selected = IntVar()  
rad1 = Radiobutton(window,text='нормализовывать', value=1, variable=selected, command = process_norm)  
rad2 = Radiobutton(window,text='не нормализовывать', value=2, variable=selected, command = process_not_norm)   
rad1.grid(column=2, row=0)  
rad2.grid(column=3, row=0)  

window.mainloop()
