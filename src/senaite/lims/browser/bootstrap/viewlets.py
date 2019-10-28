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

from cgi import escape

from plone.app.layout.viewlets.common import GlobalSectionsViewlet
from plone.app.layout.viewlets.common import SiteActionsViewlet
from plone.app.layout.viewlets.content import DocumentActionsViewlet
from Products.CMFPlone.utils import safe_unicode
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getMultiAdapter


class SenaiteSectionsDropdownViewlet(GlobalSectionsViewlet):
    index = ViewPageTemplateFile(
        'templates/senaite.lims.browser.bootstrap.viewlets.sections_dropdown.pt')

    def update(self):
        super(SenaiteSectionsDropdownViewlet, self).update()
        portal_state = getMultiAdapter((self.context, self.request),
                                       name=u'plone_portal_state')
        self.navigation_root_url = portal_state.navigation_root_url()
        self.portal_title = escape(
            safe_unicode(portal_state.navigation_root_title()))


class SenaiteSiteActionsViewlet(SiteActionsViewlet):
    index = ViewPageTemplateFile(
        "templates/plone.app.layout.viewlets.site_actions.pt")


class SenaiteDocumentActionsViewlet(DocumentActionsViewlet):
    index = ViewPageTemplateFile(
        'templates/plone.app.layout.viewlets.documentactions.pt')
