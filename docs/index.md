<div align = "center">

# DS Documentation Vault

[![Zenith Clown](https://img.shields.io/badge/🧠-Debmalya_Pramanik-blue)](https://zenithclown.github.io/)
[![REPO:ADMIN](https://img.shields.io/badge/GitHub-ZenithClown-2A8542?logo=github)](https://github.com/ZenithClown)
[![REPO:ADMIN](https://img.shields.io/badge/GitLab-ZenithClown-2A8542?logo=gitlab)](https://gitlab.com/ZenithClown)
[![REPO:ADMIN](https://img.shields.io/badge/dPramanik-7287B4?logo=linkedin)]([https://github.com/ZenithClown](https://www.linkedin.com/in/dpramanik/))
<br>
✨ *The Gringotts of Utility Functions for Data Science Projects* ✨

</div>

<div align = "justify">

Welcome to the repository of self-developed Python utility functions aimed at streamlining data science, machine learning
workflows, and Python development in general. This collection has been refined throughout my professional work, with a focus
on enhancing efficiency and productivity for data scientists, machine learning engineers, and Python developers.

## Getting Started

The codes are available in [GitHub Gists](https://gist.github.com/ZenithClown) and the same can be accessed from the
[./modules](../modules/) directory respectively. GitHub Gist typically do not have inherent capability to display the
comments associated with the commits, howver the same is maintained.

GitHub generates a checksum key for a `gists` thus it is advisable to clone with a desired name using `git`, and adding
the same to path variable allows Python to look for the packages in the system. Typically the name of directory can be
set as the name of the file (or first `.py` file, in case of multiple file) or to any desired

```shell
git clone https://gist.github.com/username/checksum.git name
$ export PYTHONPATH="${PYTHONPATH}:name" # cd into the directory
```

## Motivation & Design

Desgining and maintaining functions and its documentation is a tedious task, and to somewhat automate the same and auto-update
the documents to the latest version - I've selected [sphinx](https://www.sphinx-doc.org/en/master/) and
[ReadTheDocs](https://docs.readthedocs.io/en/stable/) to host and document the same.

## Table of Contents

```{toctree}
prettify.md
```

## Contributing Guidelines

If you find the code useful, please do put reference/stars. For contributing, please follow
[CONTRIBUTING.md](https://github.com/ZenithClown/.github/blob/master/.github/CONTRIBUTING.md) guidelines.

</div>
