# COMPAS WebViewer

This repo provides a basic Vue + ThreeJS + FastAPI setup for experimenting with COMPAS in the browser.
The repo is configured for local development, with COMPAS running on a local server...

## Installation

Set up the Vue project.

```bash
yarn install
```

Install COMPAS and other required Python packages.

```bash
pip install -r requirements.txt
```

## Starting the Client

To start the frontend development server with hot-reload, run the following command. The server will be accessible at [http://localhost:3000](http://localhost:3000):

```bash
yarn dev
```

## Starting the Server

To start the COMPAS backend server:

```bash
python server.py
```

## Usage

The viewer is available at [http://localhost:3000](http://localhost:3000).
It has a few buttons that run some basic functions on the server and visualise the result in the ThreeJS CAD environment.

The "Getting Started" button runs the code from the corresponding example on the COMPAS main website: [Getting Started](https://tomvanmele.github.io/compas2.dev/#/gettingstarted).