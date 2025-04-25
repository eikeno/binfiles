#!/bin/bash
# gsettings list-keys org.gnome.shell.keybindings
# gsettings get org.gnome.shell.keybindings
#
DUMPD="$HOME/.config/gnome-shortkeys-dump"
CATS=""
CATS="$CATS org.gnome.settings-daemon.plugins.media-keys"
CATS="$CATS org.gnome.desktop.wm.keybindings"
CATS="$CATS org.gnome.shell.keybindings"
CATS="$CATS org.gnome.mutter.keybindings"
CATS="$CATS org.gnome.mutter.wayland.keybindings"

ls -1 $DUMPD | while read -r CAT; do
	ls -1 $DUMPD/$CAT | while read -r k; do
		echo "Disabling $k"
		gsettings set $CAT $k "['']" || exit 1
	done
done

exit 0

