#!/usr/bin/env python

import json
import yaml


def load_config(filename):
    """Load configuration from a yaml file"""
    with open(filename) as f:
        return yaml.load(f)


def save_config(config, filename):
    """Save configuration to a yaml file"""
    with open(filename, "w+") as f:
        yaml.safe_dump(config, f, default_flow_style=False)


def pretty_print_json(data):
    print(json.dumps(data, indent=4, sort_keys=True))
