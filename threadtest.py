#Boa:Frame:Frame1
import time
import wx
from wx.lib.delayedresult import startWorker as worker
def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1BUTTON2, wxID_FRAME1BUTTON3, 
 wxID_FRAME1PANEL1, wxID_FRAME1STATICTEXT1, 
] = [wx.NewId() for _init_ctrls in range(6)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(464, 373), size=wx.Size(400, 251),
              style=wx.DEFAULT_FRAME_STYLE, title='Frame1')
        self.SetClientSize(wx.Size(392, 217))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(392, 217),
              style=wx.TAB_TRAVERSAL)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label='staticText1', name='staticText1', parent=self.panel1,
              pos=wx.Point(40, 40), size=wx.Size(312, 104), style=0)

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1, label='button1',
              name='button1', parent=self.panel1, pos=wx.Point(128, 176),
              size=wx.Size(75, 23), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME1BUTTON1)

        self.button2 = wx.Button(id=wxID_FRAME1BUTTON2, label='button2',
              name='button2', parent=self.panel1, pos=wx.Point(48, 184),
              size=wx.Size(75, 23), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_FRAME1BUTTON2)

        self.button3 = wx.Button(id=wxID_FRAME1BUTTON3, label='button3',
              name='button3', parent=self.panel1, pos=wx.Point(208, 192),
              size=wx.Size(75, 23), style=0)
        self.button3.Bind(wx.EVT_BUTTON, self.OnButton3Button,
              id=wxID_FRAME1BUTTON3)

    def __init__(self, parent):
        self._init_ctrls(parent)
#The good stuff the OnButton.... is just what is called when you click a button

#As you can see they print the button clicked then after the worker is created

#What is the t.... stuff
    def OnButton1Button(self, event):
        print 'button1 clicked'
        worker(self.change_lable, t.call_just_to_call)
        print 'after worker'
    def OnButton2Button(self, event):
        print 'button2 clicked'
        worker(self.change_lable, t.change_to_true)
        print 'after worker'
    def OnButton3Button(self, event):
        print 'button3 clicked'
        worker(self.change_lable, t.change_to_false)
        print 'after worker'
    def change_lable(self, some_var):
        print some_var
        print t.var        

class test_class(object):
    def __init__(self):
        self.var = 'Unchanged'
    def change_to_true(self):
        time.sleep(10)
        self.var = True
    def change_to_false(self):
        time.sleep(10)
        self.var = False
    def call_just_to_call(self):
        time.sleep(10)

t = test_class()#An instance of test_class

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()
