
#!/bin/bash
for nam in *.m4a
	do nice mplayer -ao pcm "$nam" -ao pcm:file="$nam.wav" && nice oggenc -q7 "$nam.wav" -o "$(basename "$nam" .m4a).ogg" 
	rm -f "$nam.wav" 
done
