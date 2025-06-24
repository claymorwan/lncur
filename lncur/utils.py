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

def lncur():
    """Links all the cursors files."""

    print(f"Working directory : {str_dir}")
    
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

    # Remove symlinks
    print("Removing symlinks")
    for e in list_syms(str_dir):
        if os.path.exists(e):
            os.remove(e)

    # Loop to create symlinks
    for file in os.listdir(dir):
        filename = os.fsdecode(file)

        # default
        if filename.startswith("default"):
            link_files(filename, syms[filename])

        # pointer
        if filename.startswith("pointer"):
            link_files(filename, syms[filename])

        # crosshair
        if filename.startswith("crosshair"):
            link_files(filename, syms[filename])

        # fleur
        if filename.startswith("fleur"):
            link_files(filename, syms[filename])

        # help
        if filename.startswith("help"):
            link_files(filename, syms[filename])

        # not-allowed
        if filename.startswith("not-allowed"):
            link_files(filename, syms[filename])

        # pencil
        if filename.startswith("pencil"):
            link_files(filename, syms[filename])

        # pencil
        if filename.startswith("pencil"):
            link_files(filename, syms[filename])

        # progress
        if filename.startswith("progress"):
            link_files(filename, syms[filename])

        # size_bdiag
        if filename.startswith("size_bdiag"):
            link_files(filename, syms[filename])

        # size_fdiag
        if filename.startswith("size_fdiag"):
            link_files(filename, syms[filename])

        # size_hor
        if filename.startswith("size_hor"):
            link_files(filename, syms[filename])

        # size_ver
        if filename.startswith("size_ver"):
            link_files(filename, syms[filename])

        # text
        if filename.startswith("text"):
            link_files(filename, syms[filename])

        # up-arrow
        if filename.startswith("up-arrow"):
            link_files(filename, syms[filename])

        # wait
        if filename.startswith("wait"):
            link_files(filename, syms[filename])

