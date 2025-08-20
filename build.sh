nuitka --onefile \
       --static-libpython=yes \
       --include-package=auxiliary \
       --lto=yes \
       --remove-output \
       nettraveler.py