# NetBox Layout Plugin

## Overview

The NetBox Layout Plugin is designed to enhance the NetBox interface by adding layout cards on location pages with clickable links to racks. This plugin aims to improve the visualization and navigation of rack layouts within NetBox.

## Features

- Adds layout cards to location pages.
- Clickable links to racks for easy navigation.
- Seamless integration with NetBox.

## Installation

To install the NetBox Layout Plugin, follow these steps:

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/Nishkarsh01/netbox-layout-plugin.git
    cd netbox-layout-plugin
    ```

2. **Install the Plugin**:
    ```sh
    python setup.py devlop
    ```

3. **Update NetBox Configuration**:
    Add the plugin to your NetBox configuration file (`configuration.py`):
    ```python
    PLUGINS = [
        'netbox_layout_patch',
    ]
    ```

4. **Run Database Migrations**:
    ```sh
    python manage.py migrate netbox_layout_patch
    ```

5. **Restart NetBox**:
    Restart the NetBox service to apply the changes.
