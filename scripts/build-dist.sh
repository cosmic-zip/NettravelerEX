#! /bin/bash
cd ..
echo "[x] Setup Build"
nuitka --onefile \
       --static-libpython=yes \
       --include-package=auxiliary \
       --lto=yes \
       --remove-output \
       nettraveler.py \
       && mv nettraveler.bin nettraveler

echo "[x] Setup dist"
mkdir dist temp
mv spellbook/models/ temp/
mv spellbook/ dist/
mv nettraveler dist/
tar -czvf nettraveler_lite.tar.gz dist/
mv temp/models/ dist/spellbook/
tar -czvf nettraveler_full.tar.gz dist/

echo "[x] Cleanup"
mv dist/spellbook/ ./
rm -r temp/
mv nettraveler_lite.tar.gz dist/
mv nettraveler_full.tar.gz dist/