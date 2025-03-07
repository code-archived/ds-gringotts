<div align = "center">

# DS Documentation Vault

[![Zenith Clown](https://img.shields.io/badge/🧠-Debmalya_Pramanik-blue)](https://zenithclown.github.io/)
[![REPO:ADMIN](https://img.shields.io/badge/GitHub-ZenithClown-2A8542?logo=github)](https://github.com/ZenithClown)
[![REPO:ADMIN](https://img.shields.io/badge/GitLab-ZenithClown-2A8542?logo=gitlab)](https://gitlab.com/ZenithClown)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-dPramanik-blue?logo=linkedin)](https://www.linkedin.com/in/dpramanik/)

[![Documentation Status](https://readthedocs.org/projects/ds-gringotts/badge/?version=latest)](https://ds-gringotts.readthedocs.io/en/latest/?badge=latest)
[![Dependabot Updates](https://github.com/code-archived/ds-gringotts/actions/workflows/dependabot/dependabot-updates/badge.svg)](https://github.com/code-archived/ds-gringotts/actions/workflows/dependabot/dependabot-updates)
<br>
✨ *The Gringotts of Utility Functions for Data Science Projects* ✨

</div>

<div align = "justify">

Welcome to the repository of self-developed Python utility functions aimed at streamlining data science, machine learning
workflows, and Python development in general. This collection has been refined throughout my professional work, with a focus
on enhancing efficiency and productivity for data scientists, machine learning engineers, and Python developers.

## Getting Started

Documentation is not for the *"faint-hearted"* and writing efficient code is not an expertise of most of the coders. Well,
to avoid a simple problem like forgetting what these piece of s*** does, I tend to write some basic notes.

> The Code is the Documentation!

The documentation provides a one-stop solution to manage code documentation and host the same at
[Read the Docs](http://readthedocs.org/) for end users.

### Repository Structure

The [GitHub Gists](https://gist.github.com/) is a simple place of sharing code snippets with all the features of a Git
repository but better in handling simple code snippets. In addition, Gists are a great way to keep your GitHub account
clean by not creating too many repositories with a single file. The repository is organized as follows:

  * **docs/**: This directory contains the Sphinx-generated documentation for all the utility functions included in this
  repository. This documentation is continuously updated to reflect the latest changes and additions.
  * **modules/**: This directory includes all the utility libraries, each added as a Git submodule. The modular structure
  allows for easy integration and reuse of the code across different projects.

### Project Dependencies
To ensure that the utility functions work seamlessly, all necessary dependencies are listed in the `requirements.txt` file.
Please install them using the following command:

```bash
git submodule init # initialize all in ./modules/ directory
git submodule update # optional, update to the latest changes

pip install -r docs/requirements.txt
make html
```

## Contributing Guidelines

If you find the code useful, please do put reference/stars. For contributing, please follow
[CONTRIBUTING.md](https://github.com/ZenithClown/.github/blob/master/.github/CONTRIBUTING.md) guidelines.

</div>
