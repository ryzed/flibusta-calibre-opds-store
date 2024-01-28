# -*- coding: utf-8 -*-

from __future__ import (unicode_literals, division, absolute_import, print_function)

__license__ = 'GPL 3'
__copyright__ = '2012, Sergey Kuznetsov <clk824@gmail.com>'
__docformat__ = 'restructuredtext en'

from calibre.customize import StoreBase

class FlibustaStore(StoreBase):
    name = 'Флибуста'
    version = (0, 0, 2)
    author = 'Sergey Kuznetsov, Eduard Ryzhov, Alexander Bykov'
    description = _('Книжное братство')
    actual_plugin = 'calibre_plugins.store_flibusta.flibusta:FlibustaStore'
