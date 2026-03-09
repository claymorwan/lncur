{
  lib,
  python3Packages,

  # build-system
  hatch,
}:

python3Packages.buildPythonApplication rec {
  pname = "lncur";
  version = "1.1.0";
  pyproject = true;

  src = ./../..;

  build-system = [
    hatch
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

