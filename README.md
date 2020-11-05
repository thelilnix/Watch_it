# Watch it
Watch your users while they're watching a clock.

[![Test_Lint](https://github.com/ebsa491/Watch_it/workflows/Testing%20and%20Linting/badge.svg)](https://github.com/ebsa491/Watch_it/actions)
[![Python: 3.8](https://img.shields.io/badge/Python-3.8-blue)](https://www.python.org/)
[![License: GPL](https://img.shields.io/badge/License-GPL--3.0-red)](https://www.gnu.org/licenses/gpl-3.0)
[![Release](https://img.shields.io/github/v/release/ebsa491/Watch_it)](https://github.com/ebsa491/Watch_it/releases)
![Last commit](https://img.shields.io/github/last-commit/ebsa491/Watch_it)
[![Follow me](https://img.shields.io/github/followers/ebsa491?label=Follow%20me&style=social)](https://github.com/ebsa491)

![Screenshot](./screenshot.png)

## Table of contents
* [Requirements/Credit](#requirements)
* [Setup](#setup)
* [Run](#run)
* [Contributing](#contributing)
* [Bug Reporting](#bug-reporting)
* [TODO](#todo)
* [Other](#other)

## Requirements

For requirements see [requirements.txt](./requirements.txt)

Templates credit:

* [Home template](https://codepen.io/jaysalvat/pen/ogQbKB/)
* [Admin template](https://themewagon.com/themes/bootstrap-admin-dashboard-template/)
* [Login template](https://colorlib.com/wp/template/login-form-v15/)
* [404 template](https://codepen.io/uiswarup/pen/dyoyLOp)
* [403 template](https://codepen.io/blecaf/pen/NLoEPY)

## Setup

Shell:

```shell
(ROOT_PROJECT_DIR)$ pip3 install -r requirements.txt # You can use virtual env too.
(ROOT_PROJECT_DIR)$ ./configure.sh
```

## Run

For running the app just run

```shell
(ROOT_PROJECT_DIR)$ ./run.sh # /login for Admin panel.
```

or
```shell
(ROOT_PROJECT_DIR)$ export FLASK_APP=src/Watch_it
(ROOT_PROJECT_DIR)$ export FLASK_ENV=production # or development for developing
(ROOT_PROJECT_DIR)$ flask run
```

## Contributing

I will be glad! Open an issue first or work on your assigned issue.

## Bug Reporting
If you have found any important bug or vulnerability,
open an issue and contact me please.

email: ebsa491@gmail.com
## TODO

See [TODO.md](./TODO.md)

## Other

Nothing more! Just pay attention to [`LICENSE`](./LICENSE) and enjoy my free software.
