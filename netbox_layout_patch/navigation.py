# menu.py
from netbox.plugins import PluginMenuButton, PluginMenuItem
from netbox.choices import ButtonColorChoices

# Define menu items for the plugin
menu_items = (
    PluginMenuItem(
        link='plugins:netbox_layout_patch:rackarea_list',
        link_text='Rack Areas',
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_layout_patch:rackarea_add',
                title='Add Rack Area',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,
                permissions=['netbox_layout_patch.add_rackarea']
            ),
        ),
    ),
)
