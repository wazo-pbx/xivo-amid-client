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

import json

from hamcrest import assert_that
from hamcrest import equal_to

from xivo_lib_rest_client.tests.command import RESTCommandTestCase

from ..action import ActionCommand


class TestAction(RESTCommandTestCase):

    Command = ActionCommand

    def test_action_no_params(self):
        self.session.post.return_value = self.new_response(200, json={'return': 'value'})

        result = self.command('QueueSummary')

        self.session.post.assert_called_once_with(
            '{base}/QueueSummary'.format(base=self.base_url),
            params={},
            json=None)
        assert_that(result, equal_to({'return': 'value'}))

    def test_action_with_params(self):
        self.session.post.return_value = self.new_response(200, json={'return': 'value'})

        result = self.command('DBGet', {'Family': 'family', 'Key': 'key'})

        self.session.post.assert_called_once_with(
            '{base}/DBGet'.format(base=self.base_url),
            params={},
            json={'Family': 'family', 'Key': 'key'})
        assert_that(result, equal_to({'return': 'value'}))
