# Bluetooth Audio Integration for Home Assistant

The **Bluetooth Audio** component for Home Assistant allows you to connect, manage, and control Bluetooth audio devices. It provides functionalities for discovering Bluetooth devices, connecting them, and even reconnecting if the device gets disconnected.

## Features
- **Device Discovery**: Automatically discover available Bluetooth audio devices.
- **Device Management**: Add and manage Bluetooth audio devices directly from the Home Assistant UI.
- **Reconnect Button**: If the device gets disconnected, a reconnect button is available to manually re-establish the connection.
- **Media Control**: Play, pause, and stop audio playback on Bluetooth devices.

## Requirements
- Home Assistant (latest version recommended)
- `pybluez` library for Bluetooth functionality
  - This will be installed automatically when you add the component.

## Installation

### 1. Install the component
1. Download or clone this repository into the `custom_components` folder of your Home Assistant setup. The directory should look like this:
custom_components/bluetooth_audio/

3. Restart Home Assistant.

### 2. Configure the component
After installation, the component will be available for configuration via the Home Assistant UI.

1. Go to **Settings** → **Integrations**.
2. Click the **Add Integration** button.
3. Search for **Bluetooth Audio** and click on it.
4. Follow the on-screen instructions to add your Bluetooth audio device.

You will either need to:
- **Manually enter** the device's name and address (from your Bluetooth settings) if you know them.
- **Discover devices** by selecting one from the list of available Bluetooth devices.

### 3. Reconnect a Device
If a device disconnects, you can manually reconnect it via the Home Assistant service.

1. Go to **Developer Tools** → **Services**.
2. Select the `bluetooth_audio.reconnect` service.
3. In the service data, enter the `entity_id` of the media player you want to reconnect:
```yaml
service: bluetooth_audio.reconnect
data:
  entity_id: media_player.your_device_entity_id
