import tkinter
import tkinter.messagebox

class gallonConverterGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.miles_label = tkinter.Label(self.top_frame, text='Enter a distance in Miles: ')
        self.gallons_label = tkinter.Label(self.middle_frame, text='Enter number of Gallons in tank: ')

        self.gallon_entry = tkinter.Entry(self.top_frame, width=10)
        self.miles_entry = tkinter.Entry(self.middle_frame, width=10)

        self.gallons_label.pack(side='top')
        self.miles_label.pack(side='top')
        self.gallon_entry.pack(side='top')
        self.miles_entry.pack(side='top')

        self.calc_button = tkinter.Button(self.bottom_frame, text='Convert', command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window. destroy)

        self.describe_label = tkinter.Label(self.middle_frame, text='Converted to miles per gallons: ')

        self.value = tkinter.StringVar()

        self.miles_label = tkinter.Label(self.middle_frame, textvariable=self.value)

        self.describe_label.pack(side='left')
        self.miles_label.pack(side='left')

        self.calc_button.pack(side='left')
        self.quit_button.pack(side='right')

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def convert(self):
        gallon = float(self.gallon_entry.get())
        miles = float(self.miles_entry.get())
        mpg = miles/gallon
        self.value.set(format(mpg, ',.2f'))

gui = gallonConverterGUI()
