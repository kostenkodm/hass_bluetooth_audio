DOMAIN = "bluetooth_audio"

async def async_setup(hass, config):
    """Set up the Bluetooth Audio component."""
    hass.data[DOMAIN] = {"entities": []}
    return True

async def async_setup_entry(hass, entry):
    """Set up Bluetooth Audio from a config entry."""
    hass.data[DOMAIN][entry.entry_id] = entry.data

    async def handle_reconnect_service(call):
        """Handle the reconnect service call."""
        entity_id = call.data.get("entity_id")
        for entity in hass.data[DOMAIN]["entities"]:
            if entity.entity_id == entity_id:
                await entity.async_reconnect()
                return

    hass.services.async_register(DOMAIN, "reconnect", handle_reconnect_service)

    hass.config_entries.async_setup_platforms(entry, ["media_player"])
    return True

async def async_unload_entry(hass, entry):
    """Unload a config entry."""
    hass.data[DOMAIN].pop(entry.entry_id)
    return await hass.config_entries.async_unload_platforms(entry, ["media_player"])