# Copyright 2016 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Stratisd error classes.
"""

from enum import IntEnum


def value_to_name(klass):
    """
    Generate a function to convert an IntEnum value to its name.

    :param type klass: the class defining the IntEnum
    :returns: a function to convert a single number to a name
    :rtype: int -> str
    """

    def the_func(num):
        """
        Convert the enum value to a string which is just its name.
        Replace underscores in the name with spaces.

        If there is no name for the value, return a special string.

        :param int num: the number to convert
        :returns: the name for the number or an error string
        :rtype: str
        """
        try:
            the_str = str(klass(num)).rsplit('.')[-1].replace("_", " ")
        except ValueError:
            the_str = "Unknown value (%s) for %s constant" % (num,
                                                              klass.__name__)
        return the_str

    return the_func


class StratisdErrors(IntEnum):
    """
    Stratisd Errors
    """
    OK = 0
    ERROR = 1

    ALREADY_EXISTS = 2
    BUSY = 3
    IO_ERROR = 4
    INTERNAL_ERROR = 5
    NIX_ERROR = 6
    NOT_FOUND = 7


STRATISD_ERROR_TO_NAME = value_to_name(StratisdErrors)


class RedundancyCodes(IntEnum):
    """
    Redundancy Codes
    """
    NONE = 0


REDUNDANCY_CODE_TO_NAME = value_to_name(RedundancyCodes)
