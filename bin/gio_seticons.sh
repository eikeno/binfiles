#!/bin/bash
# Set preferences for custom icons in home dir, with Gtk based File browsers.
# To find existing metadata do:
#  gio info -a metadata $HOME/<dir>
# To find possible settings:
#  gio info -w $HOME/<dir>
# depends : gio

function set_image {
	gio set -t "string" "$1" "metadata::custom-icon" "file://$2"
}
function set_stock {
	gio set -t "string" "$1" "metadata::custom-icon-name" "$2"
}

HOMEDIRS="stock	arch	distributor-logo-archlinux
stock	bin	applications-system
stock	go	$HOME/.icons/folder-golang.svg
stock	Config	systemsettings
stock	.config	systemsettings
stock	Desktop	folder-desktop
stock	Documents	folder-documents
stock	Dotfiles	folder-database
stock	.dotfiles	folder-database
stock	Downloads	folder-downloads
image	ES-DE	$HOME/.icons/org.es_de.frontend.svg
stock	Git	folder-git
stock	Gits	folder-git
image	Hypr	$HOME/.icons/folder-hyprland.svg
image	LUTRIS	$HOME/.icons/folder-lutris.svg
image	moin2	$HOME/.icons/moin-logo-large.svg
stock	Music	folder-music
stock	Pictures	folder-pictures
stock	Projects	folder-projects
stock	Public	folder-public
stock	Python	python
stock	Tmp	folder-temp
stock	.tmp	folder-temp
stock	snap	folder-snap
stock	Templates	folder-templates
stock	Videos	folder-videos"

echo "$HOMEDIRS" | while read -r i; do
	echo "------- i: $i"
	TYPE=$(echo "$i" | awk -F '	' '{print $1}')
	DIR=$(echo "$i"  | awk -F '	' '{print $2}')
	NAME=$(echo "$i" | awk -F '	' '{print $3}')

	case "$TYPE" in
		'stock') set_stock "$HOME/$DIR" "$NAME" ;;
		'image') set_image "$HOME/$DIR" "s$NAME" ;;
		*) exit 1 ;;
	esac

done

