#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2014-2015 Avencall
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

from setuptools import setup
from setuptools import find_packages

setup(
    name='xivo_amid_client',
    version='1.0',

    description='a simple client library for the xivo-amid HTTP interface',

    author='Avencall',
    author_email='dev@avencall.com',

    url='https://github.com/wazo-pbx/xivo-amid-client',

    packages=find_packages(),

    entry_points={
        'amid_client.commands': [
            'action = xivo_amid_client.commands.action:ActionCommand',
            'command = xivo_amid_client.commands.command:CommandCommand',
        ],
    }
)
