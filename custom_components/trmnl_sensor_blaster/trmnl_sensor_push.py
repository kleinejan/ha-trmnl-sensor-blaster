"""Platform for TRMNL Entity Blaster integration."""
import logging
from homeassistant.core import HomeAssistant
from homeassistant.helpers.template import Template

from .const import CONF_SENSOR_GROUPS, DEFAULT_SENSOR_GROUPS

# Get the logger
_LOGGER = logging.getLogger(__name__)

def get_entities_by_groups(hass: HomeAssistant, groups: list[str]) -> dict[str, list[str]]:
    """Get entities with specified group labels using template, organized by group."""
    _LOGGER.debug("TRMNL: Fetching entities for groups: %s", groups)
    grouped_entities = {}
    
    for group in groups:
        _LOGGER.debug("TRMNL: Processing group: %s", group)
        template_str = f"{{{{ label_entities('{group}') }}}}"
        template = Template(template_str, hass)
        try:
            group_entities = template.async_render()
            if group_entities:
                grouped_entities[group] = group_entities
                _LOGGER.debug("TRMNL: Found %d entities in group '%s'", len(group_entities), group)
            else:
                _LOGGER.debug("TRMNL: No entities found in group '%s'", group)
        except Exception as err:
            _LOGGER.error("TRMNL: Error processing group '%s': %s", group, err)
    
    return grouped_entities

def get_trmnl_entities(hass: HomeAssistant) -> list[str]:
    """Get entities with TRMNL label using template (backward compatibility)."""
    template_str = "{{ label_entities('TRMNL') }}"
    template = Template(template_str, hass)
    try:
        result = template.async_render()
        _LOGGER.debug("TRMNL: Found %d entities with TRMNL label", len(result) if result else 0)
        return result if result else []
    except Exception as err:
        _LOGGER.error("TRMNL: Error fetching TRMNL entities: %s", err)
        return []

def setup_platform(hass: HomeAssistant, entry) -> None:
    """Set up the TRMNL Entity Blaster platform."""
    # Get sensor groups from config entry
    sensor_groups = entry.data.get(CONF_SENSOR_GROUPS, DEFAULT_SENSOR_GROUPS)
    
    def process_trmnl_entities():
        """Find and process entities with configured sensor group labels."""
        # Get grouped entities
        grouped_entities = get_entities_by_groups(hass, sensor_groups)
        
        total_entities = sum(len(entities) for entities in grouped_entities.values())
        _LOGGER.info("TRMNL: Found %d entities across %d groups", total_entities, len(grouped_entities))
        
        # Log the groups and their entities
        for group, entities in grouped_entities.items():
            _LOGGER.info("TRMNL: Group '%s' has %d entities", group, len(entities))
            for entity_id in entities:
                _LOGGER.debug("TRMNL: Entity in group '%s': %s", group, entity_id)

    # Run the processing function
    hass.add_job(process_trmnl_entities)