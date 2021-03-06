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


import unittest
from data import Data
from lock import Lock


class Test01_MfcData(unittest.TestCase):
    '''Unittest for mfc1.Data().'''

    def setUp(self):
        '''Prepare test.'''

    def test_system(self):
        '''Testing  mfc1.Data.system[key].'''
        data = Data()
        r = data.system['config_file']
        self.failUnlessEqual(first=r, second='mfc')

    def test_user(self):
        '''Testing  mfc1.Data.user[key].'''
        data = Data()
        # Read user datas.
        r = data.user['interval']
        self.failUnlessEqual(first=r, second=30)
        r = data.user['text']
        self.failUnlessEqual(first=r, second='Text ..')
        # Write user datas.
        data.user['interval'] = 15.6
        r = data.user['interval']
        self.failUnlessEqual(first=r, second=15.6)
        data.user['text'] = 'Yipiehjeyeyah ..'
        r = data.user['text']
        self.failUnlessEqual(first=r, second='Yipiehjeyeyah ..')

    def test_textdic(self):
        '''Testing  str(mfc1.Data.user).'''
        data = Data()
        r = str(data.user)
        print('str(mfc1.Data.user): %s' % (r))
        self.failIfEqual(first=r, second=None)

    def test_set_user_default(self):
        '''Testing  mfc1.Data.set_user_default().'''
        data = Data()
        r = data.set_user_default()
        self.failUnlessEqual(first=r, second=None)

    def test_set_user_textdic(self):
        '''Testing  mfc1.Data.set_user_textdic(text).'''
        data = Data()
        textdic = str(data.user)
        r = data.set_user_textdic(textdic)
        self.failUnlessEqual(first=r, second=None)
        # test with bad settings
        data.user['interval'] = 'a'
        data.user['frame_size'] = 'list'
        data.user['msg_size'] = ('a', False)
        data.user['text'] = True
        data.user['sound'] = 123
        textdic = str(data.user)
        data.set_user_textdic(textdic)
        r = data.user['interval']
        self.failUnlessEqual(first=r, second=30)
        r = data.user['frame_size']
        self.failUnlessEqual(first=r, second=(400, 400))
        r = data.user['msg_size']
        self.failUnlessEqual(first=r, second=(300, 300))
        r = data.user['text']
        self.failUnlessEqual(first=r, second='True')
        r = data.user['sound']
        self.failUnlessEqual(first=r,
                             second='sounds/pv-bell.ogg')


class Test02_MfcLock(unittest.TestCase):
    '''Unittest for mfc1.Lock().'''

    def setUp(self):
        '''Prepare test.'''
        self.lock = Lock('./', 'andy')

    def test_get_pid(self):
        '''Testing mfc1.Lock.get_pid().'''
        r = self.lock.get_pid('mindfulclock1')
        self.failUnlessEqual(first=r, second=0)

    def test_one_instance(self):
        '''Testing mfc1.Lock.one_instance().'''
        r = self.lock.one_instance('mindfulclock1')
        self.failUnlessEqual(first=r, second=True)

    def test_write_check_delete_lock(self):
        '''Testing write_lock(), check_lock(), delete_lock().'''
        r = self.lock.write_lock()
        self.failUnlessEqual(first=r, second=True)
        # chek lock file.
        r = self.lock.is_lock()
        self.failUnlessEqual(first=r, second=True)
        # delete lock file.
        r = self.lock.delete_lock()
        self.failUnlessEqual(first=r, second=True)


if __name__ == '__main__':
    unittest.main()
