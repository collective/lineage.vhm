from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

import lineage.vhm


LINEAGE_VHM = PloneWithPackageLayer(
    zcml_package=lineage.vhm,
    zcml_filename='testing.zcml',
    gs_profile_id='lineage.vhm:testing',
    name="LINEAGE_VHM")

LINEAGE_VHM_INTEGRATION = IntegrationTesting(
    bases=(LINEAGE_VHM, ),
    name="LINEAGE_VHM_INTEGRATION")

LINEAGE_VHM_FUNCTIONAL = FunctionalTesting(
    bases=(LINEAGE_VHM, ),
    name="LINEAGE_VHM_FUNCTIONAL")
