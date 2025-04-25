#!/bin/bash
#sudo apt-get install faad id3v2 lame faad id3v2
if ! which faad >/dev/null; then echo "faad executable not found." >&2; exit 1;fi
if ! which metaflac >/dev/null; then echo "metaflac executable not found." >&2; exit 1;fi
if ! which lame >/dev/null; then echo "lame executable not found." >&2; exit 1;fi
if ! which id3v2 >/dev/null; then echo "id3v2 executable not found." >&2; exit 1;fi

for m4afile in *.m4a
do
mp3file=$(echo "$m4afile" | sed s/\.m4a/.mp3/g)

ARTIST=$(faad -i "$m4afile" 2>&1 | grep '^artist: ' | sed 's/^artist: //')
TITLE=$(faad -i "$m4afile" 2>&1 | grep '^title: ' | sed 's/^title: //')
ALBUM=$(faad -i "$m4afile" 2>&1 | grep '^album: ' | sed 's/^album: //')
GENRE=$(faad -i "$m4afile" 2>&1 | grep '^genre: ' | sed 's/^genre: //')
TRACKNUMBER=$(faad -i "$m4afile" 2>&1 | grep '^track: ' | sed 's/^track: //')
DATE=$(faad -i "$m4afile" 2>&1 | grep '^date: ' | sed 's/^date: //')
COMMENT=$(faad -i "$m4afile" 2>&1 | grep '^comment: ' | sed 's/^comment: //')
CONGROUP=$(faad -i "$m4afile" 2>&1 | grep '^contentgroup: ' | sed 's/^contentgroup: //')
COMPOSER=$(faad -i "$m4afile" 2>&1 | grep '^writer: ' | sed 's/^writer: //')
PERFORMER=$(faad -i "$m4afile" 2>&1 | grep '^performer: ' | sed 's/^performer: //')
ALBARTIST=$(faad -i "$m4afile" 2>&1 | grep '^album_artist: ' | sed 's/^album_artist: //')

echo "$m4afile -> $mp3file"
faad -q -o - "$m4afile" 2>/dev/null | lame -m j -q 0 --vbr-new -V 0 -s 44.1 - "$mp3file" 2>/dev/null

echo -e "$ARTIST / $ALBUM [$DATE] / $TRACKNUMBER - $TITLE"
id3v2 -t "$TITLE" -T "${TRACKNUMBER:-0}" -a "$ARTIST" -A "$ALBUM" -y "$DATE" -g "${GENRE:-12}" -c "$COMMENT" --TORY "$DATE" --IPLS "$ALBARTIST" --TCOM "$COMPOSER" --TIT1 "$CONGROUP" --TIT2 "$TITLE" --TOPE "$PERFORMER" --TPE1 "$ARTIST" --TPE2 "$ALBARTIST" --TRCK "$TRACKNUMBER" "$mp3file" 2>/dev/null
done
echo "Conversion complete!"
