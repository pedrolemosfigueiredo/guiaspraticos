import wx
def treta(event): print 'treta'
class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()
        pass
    def InitUI(self):
        menubar = wx.MenuBar(); fileMenu = wx.Menu()
        ftr = fileMenu.Append(103, 'TRETA', 'TRETA')
        fit = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit')
        menubar.Append(fileMenu, '&File');
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.OnQuit, fit)
        self.Bind(wx.EVT_MENU, treta, ftr)
        self.SetSize((300,200)); self.SetTitle('Menu')
        self.Centre(); self.Show(True)
        pass
    def OnQuit(self,e): self.Close()
    pass
def main(): ex = wx.App(); Example(None); ex.MainLoop()
if __name__ == '__main__': main()
