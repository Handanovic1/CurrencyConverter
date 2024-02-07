import requests
from tkinter import *
url = "https://api.currencyapi.com/v3/latest"
headers = {
    'apikey': 'cur_live_HHXUDQivjnox9SOhxUJhBAmvLCNHtdN74plCHLaA'
}
response = requests.request("GET", url, headers=headers)
converts = response.json()['data']

### Logic ###
def convert():
     fromCurr = fromEntry.get()[0:fromEntry.get().index(',')]
     toCurr = toEntry.get()[0:toEntry.get().index(',')]
     usdConv = float(amountEntry.get())/converts[fromCurr]['value']
     result = usdConv * converts[toCurr]['value']
     resultLabel.config(text=f'Your amount is: {"%.2f" % result}')


### UI ###
# Create window 
window = Tk() 
window.config(padx=50,pady=50)

# Dropdown menu options 
data = None
with open('API-Projects\CurrencyConverter\Currencies.csv','r') as file:
	data = file.readlines()			

def fromUpdate_data():
    search_query = fromSearch_var.get().strip().lower()
    # Clear the listbox
    fromListbox.delete(0, END)
    # Insert the filtered list to the listbox
    for item in data:
        if search_query in item.lower():
            fromListbox.insert(END, item)

def toUpdate_data():
    search_query = toSearch_var.get().strip().lower()
    # Clear the listbox
    toListbox.delete(0, END)
    # Insert the filtered list to the listbox
    for item in data:
        if search_query in item.lower():
            toListbox.insert(END, item)

fromSearch_var = StringVar()
fromSearch_var.trace_add('write', lambda name, index, mode: fromUpdate_data())

toSearch_var = StringVar()
toSearch_var.trace_add('write', lambda name, index, mode: toUpdate_data())
# Entry widget
fromEntry = Entry(window, textvariable=fromSearch_var)
fromEntry.grid(row=1,column=0)

toEntry = Entry(window, textvariable=toSearch_var)
toEntry.grid(row=1,column=1)

amountEntry = Entry()
amountEntry.grid(row=1,column=2)
# Texts
fromLabel = Label(text='From')
fromLabel.grid(row=0,column=0)
toLabel = Label(text='To')
toLabel.grid(row=0,column=1)
amountLabel = Label(text='Amount')
amountLabel.grid(row=0,column=2)
resultLabel = Label(text='Your amount is: ')
resultLabel.grid(row=4,column=2)

# Button
convertButton = Button(text='convert', command=convert)
convertButton.grid(row=2,column=2)


# Listbox widget
fromListbox = Listbox(window)
fromListbox.grid(row=2,column=0,rowspan=8)

toListbox = Listbox(window)
toListbox.grid(row=2,column=1,rowspan=8)

# Adds data to listbox
for i in data:
	fromListbox.insert(END, i)
	toListbox.insert(END, i)
    


def fromOnselect(evt):
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    fromEntry.delete(0,END)
    fromEntry.insert(0, value)

def toOnselect(evt):
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    toEntry.delete(0,END)
    toEntry.insert(0, value)

fromListbox.bind('<<ListboxSelect>>', fromOnselect)
toListbox.bind('<<ListboxSelect>>', toOnselect)


# Execute tkinter 
window.mainloop() 
