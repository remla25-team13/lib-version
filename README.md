# lib-version

This repository contains a small utility library that provides version information at runtime.

## Features

- Provides a `VersionUtil` class to programmatically retrieve the package version.
- Useful for system information in logs, debug output, or API responses.
- Version is automatically aligned with Git tags using package metadata.

## Installation

Install directly from GitHub using pip:

```bash
pip install git+https://github.com/remla25-team13/lib-version.git
```

or specify a version:

```bash
pip install git+https://github.com/remla25-team13/lib-version.git@v1.0.0
```

Make sure to replace `v1.0.0` with the latest released tag if applicable.

## Usage

```python
from lib_version.version_util import VersionUtil

print("Library Version:", VersionUtil.get_version())
```

## Versioning

This package follows [Semantic Versioning](https://semver.org/), using tags like `v1.0.0`, `v1.1.0`, etc.  
The version can be retrieved at runtime using the provided `VersionUtil` class.

## Development

### Build Locally

```bash
pip install build
python -m build
```

### Run Tests

```bash
pip install pytest
pytest
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

