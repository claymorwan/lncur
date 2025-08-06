import os, pathlib, argparse

version = "1.0.2"

# Get working directory
str_dir = pathlib.Path().resolve()
dir = os.fsencode(str_dir)

syms = {
    "default": ['arrow', 'left_ptr', 'size-bdiag', 'size-fdiag', 'size-hor', 'size-ver', 'top_left_arrow', 'copy', 'dnd-copy', 'openhand', 'grab', 'alias'],
    "pointer": ['hand1', 'hand2', 'pointing_hand', ],
    "crosshair": ['cross', 'tcross'],
    "fleur": ['all-scroll','size_all', 'grabbing', 'closehand', 'dnd-none', 'move', 'dnd-move'],
    "help": ['whats_this', 'question_arrow', 'left_ptr_help'],
    "not-allowed": ['circle', 'crossed_circle', 'pirate'],
    "pencil": [],
    "progress": ['half-busy', 'left_ptr_watch'],
    "size_bdiag": ['nesw-resize', 'sw-resize', 'ne-resize', 'top_left_corner','bottom_left_corner'],
    "size_fdiag": ['nw-resize', 'se-resize', 'nwse-resize', 'top_right_corner','bottom_right_corner'],
    "size_hor": ['e-resize', 'h_double_arrow', 'ew-resize', 'w-resize', 'sb_h_double_arrow',  'left_side', 'right_side', 'col-resize' ,'split_h'],
    "size_ver": ['s-resize', 'sb_v_double_arrow', 'n-resize', 'v_double_arrow', "ns-resize", 'bottom_side', 'top_side', 'row-resize', 'split_v'],
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
