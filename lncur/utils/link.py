import os
import pathlib

# Get working directory
str_dir = pathlib.Path.cwd()
dir = os.fsencode(str_dir)

syms = {
  "default": ['arrow', 'left_ptr', 'size-bdiag', 'size-fdiag', 'size-hor', 'size-ver', 'top_left_arrow', 'copy', 'dnd-copy', 'openhand', 'grab', 'alias', '1081e37283d90000800003c07f3ef6bf', '3085a0e285430894940527032f8b26df', '6407b0e94181790501fd1e167b474872', '640fb0e74195791501fd1ed57b41487f', 'a2a266d0498c3104214a47bd64ab0fc8', 'b66166c04f8c3109214a4fbd64a50fc8'],
  "pointer": ['hand1', 'hand2', 'pointing_hand', '9d800788f1b08800ae810202380a0822', 'e29285e634086352946a0e7090d73106'],
  "crosshair": ['cross', 'tcross'],
  "fleur": ['all-scroll','size_all', 'grabbing', 'closehand', 'dnd-none', 'move', 'dnd-move', '4498f0e0c1937ffe01fd06f973665830', '9081237383d90e509aa00f00170e968f', 'fcf21c00b30f7e3f83fe0dfd12e71cff'],
  "help": ['whats_this', 'question_arrow', 'left_ptr_help', '5c6cd98b3f3ebcb1f9c7f1c204630408', 'd9ce0ab605698f320427677b458ad60b'],
  "not-allowed": ['circle', 'crossed_circle', 'pirate', '03b6e0fcb3499374a867c041f52298f0'],
  "pencil": [],
  "progress": ['half-busy', 'left_ptr_watch', '00000000000000020006000e7e9ffc3f', '08e8e1c95fe2fc01f976f1e063a24ccd', '3ecb610c1bf2410f44200f48c40d3599'],
  "size_bdiag": ['nesw-resize', 'sw-resize', 'ne-resize', 'top_left_corner','bottom_left_corner'],
  "size_fdiag": ['nw-resize', 'se-resize', 'nwse-resize', 'top_right_corner','bottom_right_corner'],
  "size_hor": ['e-resize', 'h_double_arrow', 'ew-resize', 'w-resize', 'sb_h_double_arrow',  'left_side', 'right_side', 'col-resize' ,'split_h'],
  "size_ver": ['s-resize', 'sb_v_double_arrow', 'n-resize', 'v_double_arrow', "ns-resize", 'bottom_side', 'top_side', 'row-resize', 'split_v', '00008160000006810000408080010102'],
  "text": ['ibeam', 'xterm'],
  "up-arrow": ['center_ptr'],
  "wait": ['watch'],
}

def link_files(file, symlist):
  """Create symlinks"""
  for sym in symlist:
    os.symlink(file, sym)
  print(f"Created symlinks for {file}")

def list_syms(dirname):
  """List of symlinks"""
  sym = []
  for name in os.listdir(dirname):
    if name not in (os.curdir, os.pardir):
      full = os.path.join(dirname, name)
    if os.path.islink(full):
      sym.append(name)
  return sym


def link():
  """Links all the cursors files."""

  print(f"Working directory : {str_dir}")

  # Remove symlinks
  print("Removing symlinks")
  for e in list_syms(str_dir):
    if os.path.exists(e):
      os.remove(e)

  # Loop to create symlinks
  for file in os.listdir(dir):
    filename = os.fsdecode(file)
    for key in syms:
      if filename.startswith(key):
        link_files(filename, syms[filename])
