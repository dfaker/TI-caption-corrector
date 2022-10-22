import os
from PIL import Image
import tkinter as tk
from PIL import ImageTk
import sys

sourcedir = sys.argv[-1]

if not os.path.isdir(sourcedir):
    print(sourcedir, 'is not a directory. Exiting.')
    exit()

file_caption_sets = []

for f in os.listdir(sourcedir):
    if f.upper().endswith('.TXT'):
        continue

    txt_f = os.path.splitext(f)[0]+'.txt'

    path_f = os.path.join(sourcedir, f)
    path_txt = os.path.join(sourcedir, txt_f)

    if os.path.exists(path_f) and os.path.exists(path_txt):
        file_caption_sets.append((path_f, path_txt, open(path_txt, 'r').read()))

file_caption_sets = sorted(file_caption_sets)

root = tk.Tk()
root.geometry("1224x800")

image = ImageTk.PhotoImage(Image.open(file_caption_sets[0][0]).resize((512, 512)))
label = tk.Label(root, image=image)
txt = tk.Text(root, spacing1=10, spacing2=10)
txtind = 0
txt.insert("0.0", '\n'.join([x[2].strip().replace('\n',' ') for x in file_caption_sets]).strip())
txt.configure(undo=True)


def save():
    print('saving')
    captions = [x.strip() for x in txt.get("1.0", tk.END).split('\n')]
    changeCount = 0
    for newline, oldline in zip(captions, file_caption_sets):
        if newline != oldline[2]:
            changeCount += 1
            open(oldline[1], 'w').write(newline)
            print('\nfile:',oldline[1])
            print('old caption:',oldline[2])
            print('new caption:',newline)
    print('changes: ', changeCount)


save = tk.Button(root, text='Save', command=save)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=2)
root.rowconfigure(2, weight=0)

label.grid(row=0, column=0, sticky='nsew')
txt.grid(row=1, column=0, sticky='nsew')
save.grid(row=2, column=0, sticky='nsew')


def changeSelection():
    global image, txtind
    ind = int(txt.index('insert').split('.')[0])-1
    if ind != txtind:
        image = ImageTk.PhotoImage(Image.open(file_caption_sets[ind][0]).resize((512, 512)))
        label.configure(image=image)
        txtind = ind

    captions = [x.strip() for x in txt.get("1.0", tk.END).split('\n')]
    if len(captions)-1 != len(file_caption_sets):
        txt.edit_undo()


def changeSelectionEvt(e):
    root.after(100, changeSelection)


txt.bind('<<Selection>>', changeSelectionEvt)
txt.bind('<Key>', changeSelectionEvt)
txt.bind('<1>', changeSelectionEvt)
txt.bind('<2>', changeSelectionEvt)

root.mainloop()
