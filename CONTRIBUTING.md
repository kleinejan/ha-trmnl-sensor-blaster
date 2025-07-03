# Contributing to TRMNL Sensor Blaster

Thank you for your interest in contributing to the TRMNL Sensor Blaster integration for Home Assistant! This document provides guidelines and instructions for contributing.

## How to Contribute

1. Fork the repository
2. Create a new branch for your feature or bugfix
3. Make your changes
4. Test your changes thoroughly
5. Submit a pull request

## Development Setup
This is tricky because of the way Home Assistant handles integrations.

Once you have the integration installed then you can edit the files locally and send to the home assistant server via scp.

```bash
scp custom_components/trmnl_sensor_blaster/* user@homeassistant.local:/var/homeassistant/custom_components/trmnl_sensor_blaster
```
_You may need to change permissions on the files to make them writable._

You then need to restart the home assistant server to load the new files.

You can generate the API token from the Home Assistant web interface and then use that to restart the server.

```bash
curl -X POST \
    -H "Authorization: Bearer ${HASS_API_TOKEN}" \
    -H "Content-Type: application/json" \
    "${HASS_URL}/api/services/homeassistant/restart"
```



## Testing

Before submitting a PR, please ensure:

1. Your code follows the [Home Assistant development guidelines](https://developers.home-assistant.io/docs/development_guidelines)
2. You have tested your changes thoroughly in Home Assistant
3. Your code is well-documented if required


## Pull Request Process

1. Update the README.md with details of any changes to the interface or functionality
2. Update the version number in manifest.json following [semantic versioning](https://semver.org/)
3. Ensure your PR description clearly describes the problem and solution
4. Link any related issues

## Reporting Issues

When reporting issues, please include:

1. A clear description of the problem
2. Steps to reproduce the issue
3. Expected behavior
4. Actual behavior
5. Home Assistant version
6. Integration version
7. Relevant logs

## Feature Requests

Feature requests are welcome! Please provide:

1. A clear description of the feature
2. Use cases for the feature
3. Any potential implementation details you've considered

## Questions?

If you have questions about contributing, please:

1. Check existing issues and discussions
2. Open a new discussion if your question hasn't been addressed

## License

By contributing to this project, you agree that your contributions will be licensed under the MIT License. 