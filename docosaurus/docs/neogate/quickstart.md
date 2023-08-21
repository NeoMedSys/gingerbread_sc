---
sidebar_position: 1
---

# Quickstart ✌

We are hosting the package on private pypi-server so we need to add a small configuration to the pip command.

# Installation ☕

**Using pip**

For pypi we need to add a small configuration to the pip command. This will prompt you for a username and password, these are given by the NeoMedSys team.

```jsx title="~bash"
pip install --index-url https://pypi.neomedsys.app/ gingerbread
```

**Using poetry**

First we need to add the authentication to poetry, this is done by running the following command.

```jsx title="~bash"
poetry config http-basic.neomedsys <username> <password>
```

Then we need to add the private pypi-server to the poetry configuration.

```jsx title="~bash"
poetry source add --priority=default neomedsys https://pypi.neomodels.app
```

Now we can install the package.

```jsx title="~bash"
poetry add gingerbread
```

### Usage

After installing you can initate a new project by using the command line interface.

**pip**
```jsx title="~bash"
gingerbread-bake
```

**poetry**
```jsx title="~bash"
poetry run gingerbread-bake
```

This will generate a folder named "gingerbread". This folder will contain the central_processing.py file and a models folder containing example model setup. These files are altered according to the researchers need. The config file needs to be in the format generated.