<div align = "center">

# Project Objective

</div>

<div align = "justify">

The [GitHub Gists](https://gist.github.com/) is a simple place of sharing code snippets with all the features of a Git
repository but better in handling simple code snippets. In addition, Gists are a great way to keep your (main) GitHub account
clean by not creating too many repositories with a single file. The repository is organized as follows:

<div align = "center">

| **Directory Name** | **Detail Description(s)** |
| :---: | --- |
| **`docs/`** | Parent directory containing Sphinx-generation documentation. |
| **`modules/`** | All the utility libraries, each added as a submodule. |

</div>

## Getting Started
To start working on the documentation, all necessary dependencies are listed in the `requirements-doc.txt` file. Please
install them using `pip` with the following command:

```bash
git submodule init # initialize all in ./modules/ directory
git submodule update # optional, update to the latest changes

pip install -r docs/requirements-doc.txt
make html
```

### Collaboration on Code Development

A [GitHub Gists](https://gist.github.com/) does not allow a PR/patch update like traditional repository. However, to
collaborate, please raise a PR at [GitHub/ZenithClown](https://github.com/code-archived/ds-gringotts) providing the public URL
of the fork and the same will be merged after verification in the following manner:

```bash
$ git remote add feature https://gist.github.com/collaborator/abcdhashkey.git
$ git fetch feature/master
$ git merge feature/maser
$ git push -u origin master
```

The collab request thus preserves the original author, and the credit is provided both in the PR and in the code. More details
at [here](https://docs.github.com/en/get-started/writing-on-github/editing-and-sharing-content-with-gists/forking-and-cloning-gists).

</div>
