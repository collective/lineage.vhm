from zope.interface import Interface
from zope import schema
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('collective.lineage')


class ILineageVHMSettings(Interface):
    """ Lineage URL mapping Settings
    """

    vhm_map = schema.Dict(title=_(u"VHM Path Map"),
                          description=_(u"help_vhm_map",
                            default=u"You can define a mapping of paths in \
                                    the site hierachy and the hostname \
                                    used to access that part of the tree."),
                          required=False,
                          default={},)
