#!/bin/bash

[ $# -eq 0 ] && echo 'RTFSC' && exit 0

ACTION=$1
shift +1

run () {
	echo -e "##\n$*\n##" && "$@"
}


case $ACTION in 
pass1) 
	echo "# entrering pass 1"
	run mencoder "$@" -ovc x264\
		 -x264encopts subq=5:8x8dct:frameref=2:bframes=3:b_pyramid:weight_b:qp=30:pass=1:turbo=1:threads=auto  \
		 -oac copy -o /dev/null
;;

pass2)
	echo 'implement me'
;;


pass3)
	echo "# entrering pass 3" 
        run mencoder "$@" -ovc x264\
                 -x264encopts subq=5:8x8dct:frameref=2:bframes=3:b_pyramid:weight_b:qp=30:pass=3:threads=auto  \
                 -oac mp3lame -lameopts abr:br=128 -o out.avi
;;


esac

exit $?
