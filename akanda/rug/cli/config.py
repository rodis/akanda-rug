# Copyright 2014 DreamHost, LLC
#
# Author: DreamHost, LLC
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


"""Commands related to the application configuration
"""
import logging

from akanda.rug import commands
from akanda.rug.cli import message


class ConfigReload(message.MessageSending):
    """reload the configuration file(s)"""

    log = logging.getLogger(__name__)

    def make_message(self, parsed_args):
        self.log.info(
            'sending config reload instruction',
        )
        return {
            'command': commands.CONFIG_RELOAD,
        }
