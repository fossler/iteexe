# ===========================================================================
# eXe 
# Copyright 2004-2005, University of Auckland
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
# ===========================================================================

import sys
import logging
from exe.engine.idevice import Idevice

log = logging.getLogger(__name__)


# ===========================================================================
class Field(object):
    def __init__(self, name, fieldType=None, class_="", content=""):
        self.name      = name
        self.fieldType = fieldType
        self.content   = content
        self.class_    = class_

    def __cmp__(self, other):
        return cmp(self.name, other.name)


# ===========================================================================
class GenericIdevice(Idevice):
    """
    A generic Idevice is one built up from simple fields... as such it
    can have a multitude of different forms all of which are just simple
    XHTML fields.
    """
    def __init__(self):
        Idevice.__init__(self)
        self.fields    = []

    def addField(self, name, fieldType, class_, content=""):
        self.fields.append(Field(name, fieldType, class_, content))

    def __setitem__(self, name, value):
        key   = Field(name)
        index = self.fields.index(key)
        self.fields[index].content = value

    def __getitem__(self, name):
        key   = Field(name)
        index = self.fields.index(key)
        return self.fields[index].content

    def __iter__(self):
        return iter(self.fields)


# ===========================================================================
