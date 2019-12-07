from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _
from cms.menu_bases import CMSAttachMenu

class TestMenu(CMSAttachMenu):

    name = _("test menu")

    def get_nodes(self, request):
        nodes = []
        n1 = NavigationNode(_('sample anchor 1'), "/#sa1", 1)
        n2 = NavigationNode(_('sample anchor 2'), "/#sa2", 2)
        n3 = NavigationNode(_('sample anchor 3'), "/#sa3", 3)

        nodes.append(n1)
        nodes.append(n2)
        nodes.append(n3)
        return nodes

menu_pool.register_menu(TestMenu)