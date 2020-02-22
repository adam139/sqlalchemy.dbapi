#-*- coding: UTF-8 -*-
import datetime
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting,FunctionalTesting

from plone.app.testing import (
IntegrationTesting,
FunctionalTesting,
login, logout, setRoles,
PLONE_FIXTURE,
TEST_USER_NAME,
SITE_OWNER_NAME,
)

from plone.testing import z2
from plone.namedfile.file import NamedImage
from plone import namedfile
from zope.configuration import xmlconfig



class SitePolicy(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)
    
    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import sqlalchemy.dbapi 
        xmlconfig.file('configure.zcml', sqlalchemy.dbapi, context=configurationContext)     
       
    
    def tearDownZope(self, app):
        pass
        # Uninstall products installed above
        
        
    def setUpPloneSite(self, portal):
        pass
      


class IntegrationSitePolicy(SitePolicy):      
        
    def setUpPloneSite(self, portal):

        #make global request work
        from zope.globalrequest import setRequest
        setRequest(portal.REQUEST)
        # login doesn't work so we need to call z2.login directly
        z2.login(portal.__parent__.acl_users, SITE_OWNER_NAME)
#        setRoles(portal, TEST_USER_ID, ('Manager',))
#        login(portal, TEST_USER_NAME)
              
        self.portal = portal 

POLICY_FIXTURE = SitePolicy()
POLICY_INTEGRATION_FIXTURE = IntegrationSitePolicy()
POLICY_INTEGRATION_TESTING = IntegrationTesting(bases=(POLICY_INTEGRATION_FIXTURE,), name="Site:Integration")
FunctionalTesting = FunctionalTesting(bases=(POLICY_FIXTURE,), name="Site:FunctionalTesting")