from json import load, dumps
from os import scandir
from os.path import isfile

settings = {}
with open(".vscode/settings.json") as f:
    settings = load(f)
    settings["rust-analyzer.linkedProjects"][0]["crates"] = []
    for sub_dir in scandir("."):
        if sub_dir.is_dir():
            if isfile(f"{sub_dir.path}/main.rs"):
                settings["rust-analyzer.linkedProjects"][0]["crates"].append(
                    {
                        "root_module": f"{sub_dir.path}/main.rs",
                        "edition": "2021",
                        "deps": [],
                    }
                )

with open(".vscode/settings.json", "w") as f:
    f.write(dumps(settings))
