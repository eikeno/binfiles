#!/bin/bash
# eikenault@gmail.com

SELF="${BASH_SOURCE[0]}"
SELF_BN="$(basename "$SELF")"

function usage {
cat > /dev/stdout << EOT
Usage: $SELF_BN <FILENAME|DIRNAME>

Renames given file or directory with each word capitalized.
Example:

\$ $SELF_BN \"two WORDS.txt\"
- Renaming 'two WORDS.txt' to 'Two Words.txt'"
EOT
	exit 1
}

function cap () {
	extension="${*##*.}"
	base="${*//$extension}"

	for w in $base;	do
		w="${w,,}" # first lowercase the whole word
		r+="${w^} "  # upper first character of the word
	done
	# leave extension as-is:
	echo -n "$r" |  sed -e 's/[[:space:]]*$//'
	echo "$extension"
}

[ "$#" -ne 1 ] && usage
new="$(cap "$@")"
echo "- Renaming '$*' to '$new'" 1>&2
mv "$@" "$new" || exit 1
exit 0
