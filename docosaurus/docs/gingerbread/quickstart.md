---
sidebar_position: 1
---

# Quickstart

We are hosting the package on private pypi-server so we need to add a small configuration to the pip command.

## Installation ☕

**Using pip**

For pypi we need to add a small configuration to the pip command. This will prompt you for a username and password, these are given by the NeoMedSys team.

```bash title="~bash"
pip install --index-url https://pypi.neomodels.app/ gingerbread
```

**Using poetry**

First we need to add the authentication to poetry, this is done by running the following command.

```bash title="~bash"
poetry config http-basic.neomedsys <username> <password>
```

Then we need to add the private pypi-server to the poetry configuration.

```bash title="~bash"
poetry source add --priority=default neomedsys https://pypi.neomodels.app
```

Now we can install the package.

```bash title="~bash"
poetry add gingerbread
```

## Usage ✌

After installing you can initate a new project by using the command line interface.

**pip**
```bash title="~bash"
gingerbread-bake
```

**poetry**
```bash title="~bash"
poetry run gingerbread-bake
```

This will generate a folder named "gingerbread". This folder will contain the central_processing.py file and a models folder containing example model setup. These files are altered according to the researchers need. The config file needs to be in the format generated.