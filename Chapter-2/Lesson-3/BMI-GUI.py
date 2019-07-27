import wx

def BMI(w, h):
    tbmi = w / (h**2)
    if tbmi < 18.5:
        txtBMI = "Under Weight"
    elif 18.5 <= tbmi <=24.9:
        txtBMI = "Normal"
    elif 25 <= tbmi <= 29.9:
        txtBMI = "Over Weight"
    elif 30 <= tbmi <= 34.9:
        txtBMI = "Obese"
    elif tbmi>35:
        txtBMI = "Extremly Obese"
    return txtBMI

def bmiOnClick(event):
    tW = eval(txtWeight.GetValue())
    tH = eval(txtHeight.GetValue())
    lblResult.SetLabel("Your BIM means: "+BMI(tW, tH))
    lblResult.SetForegroundColour((255,0,0))
    return

app = wx.App()
win = wx.Frame(None, title="BMI Dialog", size=(410,235))

lblWeight = wx.StaticText(win,label="Weight", pos=(5,5))
lblHeight = wx.StaticText(win,label="Height", pos=(5,35))
lblResult = wx.StaticText(win,label="", pos=(5,75))

txtWeight = wx.TextCtrl(win, pos=(50,5), size=(210,25))
txtHeight = wx.TextCtrl(win, pos=(50,35), size=(210,25))

btnBMICalc = wx.Button(win, label = "BMI",pos=(300,5))
btnBMICalc.Bind(wx.EVT_BUTTON, bmiOnClick)

win.Show()


app.MainLoop()






