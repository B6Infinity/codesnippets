# Add this to the settings.json file:

    {
        ...,
        "terminal.integrated.profiles.linux": {
            "Run Command": {
                "path": "/bin/bash",
                "args": ["-c", "echo ELLO; exec $SHELL"]
            }
        },
        "terminal.integrated.defaultProfile.linux": "Run Command"
    }
