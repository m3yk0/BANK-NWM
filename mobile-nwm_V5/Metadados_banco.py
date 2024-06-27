#[BANCO NWM]

name = "Banco nwm"
version = "04.06.2024 - V4.6.3"
description = "Programa para operações bancárias de um RPG chamado N.W.M."
readme = "READ.me"
requires_python = ">=3.9"
#license = {file = "LICENSE.txt"}
keywords = ["banco", "run", "start", "nwm", "m3yk0"]
authors = {'email': "ofc.nwm@gmail.com", 'name': "M3YK0"}
maintainers = {'name': "Gabriel", 'email': "contato.grabielpettine@gmail.com"}
classifiers = [
  "Development Status :: 4 - Beta",
  "Programming Language :: Python"]

dependencies = [
  "httpx",
  "gidgethub[httpx]>4.0.0",
  "django>2.1; os_name != 'nt'",
  "django>2.0; os_name == 'nt'",
  "datetime",
  "pandas",
  "babel"
]

#[project.optional-dependencies]
test = [
  "pytest < 5.0.0",
  "pytest-cov[all]"
]

#[project.urls]
homepage = "https://example.com"
documentation = "https://readthedocs.org"
repository = "https://github.com"
changelog = "https://github.com/me/spam/blob/master/CHANGELOG.md"
github = "https://github.com/m3yk0/BANK-NWM/tree/main"

#[project.scripts]
spam_cli = "spam:main_cli"

#[project.gui-scripts]
#spam-gui = "spam:main_gui"

#[project.entry-points."spam.magical"]
#tomatoes = "spam:main_tomatoes"
