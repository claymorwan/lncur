{
  lib,
  python3Packages,
}:

let
  rootPath = builtins.path { path = ./../..; };
  pyprojectToml = fromTOML (builtins.readFile "${rootPath}/pyproject.toml");
in
python3Packages.buildPythonApplication rec {
  pname = pyprojectToml.project.name;
  version = pyprojectToml.project.version;
  pyproject = true;

  src = rootPath;

  build-system = with python3Packages; [
    hatchling
  ];

  meta = {
    changelog = "https://codeberg.org/claymorwan/lncur/releases/tag/v${version}";
    description = "Python CLI easily symlink files when porting Windows cursors to Linux";
    homepage = "https://codeberg.org/claymorwan/lncur";
    license = lib.licenses.mit;
    maintainers = with lib.maintainers; [
      claymorwan
    ];
  };
}

