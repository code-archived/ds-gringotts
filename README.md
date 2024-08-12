<div align = "center">

# DS Documentation Vault

[![Zenith Clown](https://img.shields.io/badge/🧠-Debmalya_Pramanik-blue)](https://zenithclown.github.io/)
[![REPO:ADMIN](https://img.shields.io/badge/GitHub-ZenithClown-2A8542?logo=github)](https://github.com/ZenithClown)
[![REPO:ADMIN](https://img.shields.io/badge/dPramanik-7287B4?logo=linkedin)]([https://github.com/ZenithClown](https://www.linkedin.com/in/dpramanik/))
[![Documentation Status](https://readthedocs.org/projects/ds-gringotts/badge/?version=latest)](https://ds-gringotts.readthedocs.io/en/latest/?badge=latest)
<br>
✨ *The Gringotts of Utility Functions for Data Science Projects* ✨

</div>

<div align = "justify">

Welcome to the repository of self-developed Python utility functions aimed at streamlining data science, machine learning
workflows, and Python development in general. This collection has been refined throughout my professional work, with a focus
on enhancing efficiency and productivity for data scientists, machine learning engineers, and Python developers.

## Repository Structure

The repository is organized as follows:
  * **docs/**: This directory contains the Sphinx-generated documentation for all the utility functions included in this
  repository. This documentation is continuously updated to reflect the latest changes and additions.
  * **modules/**: This directory includes all the utility libraries, each added as a Git submodule. The modular structure
  allows for easy integration and reuse of the code across different projects.

## Getting Started
To ensure that the utility functions work seamlessly, all necessary dependencies are listed in the `requirements.txt` file.
Please install them using the following command:

```bash
git submodule init # initialize all in ./modules/ directory
git submodule update # optional, update to the latest changes

pip install -r docs/requirements.txt
make html
```

</div>
