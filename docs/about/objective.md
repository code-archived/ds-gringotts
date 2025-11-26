<div align = "center">

# Project Objective

</div>

<div align = "justify">

The [GitHub Gists](https://gist.github.com/) is a simple place of sharing code snippets with all the features of a Git
repository but better in handling simple code snippets. In addition, Gists are a great way to keep your GitHub account
clean by not creating too many repositories with a single file. The repository is organized as follows:

  * **docs/**: This directory contains the Sphinx-generated documentation for all the utility functions included in this
    repository. This documentation is continuously updated to reflect the latest changes and additions.
  * **modules/**: This directory includes all the utility libraries, each added as a Git submodule. The modular structure
    allows for easy integration and reuse of the code across different projects.

### Project Dependencies
To ensure that the utility functions work seamlessly, all necessary dependencies are listed in the `requirements-doc.txt`
file. Please install them using the following command:

```bash
git submodule init # initialize all in ./modules/ directory
git submodule update # optional, update to the latest changes

pip install -r docs/requirements-doc.txt
make html
```

</div>
