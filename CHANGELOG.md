# Changelog

All notable changes to the TRMNL Entity Blaster integration will be documented in this file.

## [0.4.0] - 2025-06-24

### Changed
- Changed domain from `trmnl_sensor_push` to `trmnl_entity_blaster` to avoid conflicts
- Renamed directory structure to match new domain
- Breaking change: Requires uninstall/reinstall of integration

## [0.3.3] - 2025-06-24

### Fixed
- Removed deprecated explicit config_entry assignment in options flow
- Ensures compatibility with Home Assistant 2025.12+

## [0.3.2] - 2025-06-24

### Added
- Icon support in entity payloads when available from Home Assistant
- Icons included as optional third field alongside name and value

### Enhanced
- Payload structure now: `{"name": "toilet", "value": "25°C", "icon": "mdi:thermometer"}`
- Maintains efficiency with icons only added when present on entities

## [0.3.0] - 2025-06-24

### Added
- Grouped JSON payload structure organizing sensors by category
- Multi-group sensor selection with Home Assistant labels
- Group-aware payload size management for 2KB limits
- Custom sensor group support (temperatures, garbage, humidity, etc.)
- Automatic payload truncation while preserving group structure

### Changed
- Payload format now groups entities: `{"temperatures": [{"name": "toilet", "value": "25°C"}]}`
- Configuration flow supports multiple label selection with custom values
- Improved logging with group-specific information

### Maintained
- Backward compatibility with "TRMNL" label
- 30-minute update intervals
- Minimal payload format (name + value only)
- 2KB payload limit compliance

## [0.2.0] - 2025-06-24

### Added
- Custom sensor group configuration via Home Assistant labels
- Multi-select dropdown for sensor group selection
- Enhanced configuration validation
- Options flow for reconfiguration

### Changed
- Replaced single "TRMNL" label with configurable sensor groups
- Updated payload structure to include group metadata

## [0.1.0] - 2025-06-24

### Added
- Initial TRMNL Entity Blaster integration
- Basic webhook functionality
- Entity filtering by "TRMNL" label
- 30-minute update intervals
- Basic payload size management