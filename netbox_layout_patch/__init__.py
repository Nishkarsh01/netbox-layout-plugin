from netbox.plugins import PluginConfig
# import plugin    exntesion file

class NetBoxLayoutPatchConfig(PluginConfig):
    name = "netbox_layout_patch"
    verbose_name = "NetBox Layout Patch"
    description = "A plugin to add layout cards on location pages with clickable links to racks."
    version = "1.0.0"
    author = "Nishkarsh Dubb"
    author_email = "ndubb@evertz.com"
    base_url = "netbox-layout-patch"
    template_extensions = "template_content.template_extensions"

config = NetBoxLayoutPatchConfig

