#!/usr/bin/env bash
pylint code --fail-under=9.85 || echo "FAIL"
