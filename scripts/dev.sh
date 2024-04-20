#!/bin/bash
. .venv/bin/activate
set -a && . ./.env && set +a
gradio src/main.py
