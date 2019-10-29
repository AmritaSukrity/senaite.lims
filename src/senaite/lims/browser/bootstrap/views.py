# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.LIMS.
#
# SENAITE.LIMS is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Copyright 2018-2019 by it's authors.
# Some rights reserved, see README and LICENSE.

from bika.lims import api
from Products.CMFPlone.controlpanel.browser.overview import \
    OverviewControlPanel
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from senaite.lims import logger


def icon_cache_key(method, self, brain_or_object):
    """Generates a cache key for the icon lookup

    Includes the virtual URL to handle multiple HTTP/HTTPS domains
    Example: http://senaite.local/clients?modified=1512033263370
    """
    url = api.get_url(brain_or_object)
    modified = api.get_modification_date(brain_or_object).millis()
    key = "{}?modified={}".format(url, modified)
    logger.debug("Generated Cache Key: {}".format(key))
    return key


class SenaiteOverviewControlPanel(OverviewControlPanel):
    template = ViewPageTemplateFile(
        "templates/plone.app.controlpanel.overview.pt")
