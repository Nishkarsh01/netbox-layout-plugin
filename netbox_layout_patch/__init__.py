# plugin_config.py
from netbox.plugins import PluginConfig

class NetBoxLayoutPatchConfig(PluginConfig):
    """
    Configuration for the NetBox Layout Patch plugin.
    """
    name = "netbox_layout_patch"
    verbose_name = "NetBox Layout Patch"
    description = "A plugin to add layout cards on location pages with clickable links to racks."
    version = "0.1"
    author = "Nishkarsh Dubb (Nish)"
    author_email = "ndubb@evertz.com"
    base_url = "netbox-layout-patch"
    template_extensions = "template_content.template_extensions"

# Instantiate the plugin configuration
config = NetBoxLayoutPatchConfig
