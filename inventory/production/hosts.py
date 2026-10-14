#!/usr/bin/env python3

import json
inventory = {
    'webservers': {
        'hosts': ['web1.example.com', 'web2.example.com'],
        'vars': {
            'http_port': 80
        }
    },
    'databases': {
        'hosts': ['db1.example.com'],
        'vars': {
            'postgresql_port': 5432
        }
    }
}
print(json.dumps(inventory))