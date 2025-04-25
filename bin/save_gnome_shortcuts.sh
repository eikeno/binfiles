#!/bin/bash
# gsettings list-keys org.gnome.shell.keybindings
# gsettings get org.gnome.shell.keybindings screensho
#
DUMPD="$HOME/.config/gnome-shortkeys-dump"
CATS=""
CATS="$CATS org.gnome.settings-daemon.plugins.media-keys"
CATS="$CATS org.gnome.desktop.wm.keybindings"
CATS="$CATS org.gnome.shell.keybindings"
CATS="$CATS org.gnome.mutter.keybindings"
CATS="$CATS org.gnome.mutter.wayland.keybindings"

rm -Rf "$DUMPD"/*

for i in $CATS; do 
	echo "CAT: $i"
	mkdir -p "$DUMPD/$i"
	gsettings list-keys $i | while read -r k; do
		v=$(gsettings get $i $k)
		echo "$v" > "$DUMPD/$i/$k"
		echo "saved $DUMPD/$i/$k"
	done
done
