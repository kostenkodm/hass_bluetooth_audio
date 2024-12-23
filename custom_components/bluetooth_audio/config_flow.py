import logging
import voluptuous as vol

from homeassistant import config_entries
from bluetooth import discover_devices
from . import DOMAIN

_LOGGER = logging.getLogger(__name__)

class BluetoothAudioConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Bluetooth Audio."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            return self.async_create_entry(title=user_input["device_name"], data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("device_name"): str,
                vol.Required("device_address"): str,
            }),
        )

    async def async_step_discovery(self, user_input=None):
        """Handle Bluetooth device discovery."""
        if user_input is not None:
            return self.async_create_entry(title=user_input["device_name"], data=user_input)

        devices = await self.hass.async_add_executor_job(discover_devices, 8, True)
        device_choices = {addr: name for addr, name in devices}

        return self.async_show_form(
            step_id="discovery",
            data_schema=vol.Schema({
                vol.Required("device"): vol.In(device_choices),
            }),
        )