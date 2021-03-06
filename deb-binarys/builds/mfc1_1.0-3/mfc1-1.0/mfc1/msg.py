#!/usr/bin/python
# -*- coding: utf-8 -*-

# With the MindfulClock you turn your device into a Bell of Mindfulness.
# Concept, Design: Marcurs Möller
#                  <marcus.moeller@outlook.com>
#                  <http://apps.microsoft.com/windows/de-de/app/
#                   mindfulclock/58063160-9cc6-4dee-9d92-17df4ce4318a>
# Programming: Andreas Ulrich
#              <ulrich3110@gmail.com>,
#              <http://erasand.jimdo.com/kontakt/>
#
# This file is part of the "MindfulClock".
# "MindfulClock" is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# "MindfulClock" is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
# See the GNU General Public License for more details. You should
# have received a copy of the GNU General Public License along with
# "MindfulClock".  If not, see <http://www.gnu.org/licenses/>.


import wx


class Msg(wx.Dialog):
    '''mfc1.Msg(parent, title, size, icon, text)
       Show the text notification for the MindfulClock.
       parent = wx.window
       title = 'dialog title'
       size = (width, height)
       borderdist = integer, distance between widgets
       icon = 'path' to icon for close button
       text = 'notification text'
       font = (size, 'family', 'style', 'weight')

    on_close(event)
    Event for bitmap button.

    set_font(font)
    Set the wx.Font from the tuple font to the caption.

    Dialog styles:
        wx.CAPTION
        wx.DEFAULT_DIALOG_STYLE
        wx.RESIZE_BORDER
        wx.SYSTEM_MENU
        wx.CLOSE_BOX
        wx.MAXIMIZE_BOX
        wx.MINIMIZE_BOX
        wx.THICK_FRAME
        wx.STAY_ON_TOP

    '''

    def __init__(self, parent, title, size, icon, text, font):
        # Subclass.
        wx.Dialog.__init__(self,
                           parent=parent,
                           title=title,
                           size=size,
                           style=wx.DEFAULT_DIALOG_STYLE |
                                 wx.STAY_ON_TOP | wx.RESIZE_BORDER)
        # Text notification.
        self.__caption = wx.StaticText(self, label=text)
        # Set font.
        self.set_font(font)
        # Calculate border distance.
        bdist = font[0]
        # Close button.
        button = wx.BitmapButton(parent=self,
                                 bitmap=wx.Bitmap(icon))
        # Bindings
        button.Bind(event=wx.EVT_BUTTON, handler=self.on_close)
        # Layout.
        vbox = wx.BoxSizer(orient=wx.VERTICAL)
        vbox.Add(item=self.__caption,
                 flag=wx.EXPAND | wx.ALL | wx.ALIGN_CENTER_HORIZONTAL |
                      wx.ALIGN_TOP,
                 proportion=2,
                 border=bdist)
        vbox.Add(item=button,
                 flag=wx.ALL | wx.ALIGN_CENTER_HORIZONTAL |
                      wx.ALIGN_BOTTOM,
                 border=bdist)
        self.SetSizer(vbox)
        self.Centre()

    def on_close(self, event):
        '''Event for bitmap button.'''
        self.Close()

    def set_font(self, font):
        '''Set the wx.Font from the tuple font to the caption.'''
        # font = (size, 'family', 'style', 'weight')
        familydic = {'decorative': wx.FONTFAMILY_DECORATIVE,
                     'default': wx.FONTFAMILY_DEFAULT,
                     'modern': wx.FONTFAMILY_MODERN,
                     'roman': wx.FONTFAMILY_ROMAN,
                     'script': wx.FONTFAMILY_SCRIPT,
                     'swiss': wx.FONTFAMILY_SWISS,
                     'teletype': wx.FONTFAMILY_TELETYPE}
        styledic = {'normal': wx.NORMAL,
                    'slant': wx.SLANT,
                    'italic': wx.ITALIC}
        weightdic = {'normal': wx.FONTWEIGHT_NORMAL,
                     'light': wx.FONTWEIGHT_LIGHT,
                     'bold': wx.FONTWEIGHT_BOLD}
        textfont = self.__caption.GetFont()
        textfont.SetPointSize(font[0])
        textfont.SetFamily(familydic[font[1]])
        textfont.SetStyle(styledic[font[2]])
        textfont.SetWeight(weightdic[font[3]])
        self.__caption.SetFont(textfont)


class wxTestFrame(wx.Frame):
    '''wxTestFrame().'''

    def __init__(self):
        wx.Frame.__init__(self, parent=None)
        wx.FutureCall(millis=100, callable=self.show_dlg())
        self.Centre()
        self.Show()

    def show_dlg(self):
        '''Show dialogue.'''
        t = 'Please enter your message ..'
        dlg = Msg(parent=self,
                  title='MindfulClock',
                  size=(300, 300),
                  icon='icons/32/weather-clear.png',
                  text=t,
                  font=(20, 'default', 'italic', 'bold'))
        dlg.ShowModal()
        dlg.Destroy()

        #              Test fonts
        #                     'decorative'  'normal'  'normal'
        #                     'default'     'slant'   'light'
        #                     'modern'      'italic'  'bold'
        #                     'roman'
        #                     'script'
        #                     'swiss'
        #                     'teletype'


if __name__ == '__main__':
    app = wx.App()
    frame = wxTestFrame()
    app.MainLoop()
