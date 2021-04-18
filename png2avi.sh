ffmpeg -framerate $2 -pattern_type glob -i 'output/'$1'/*.png' -i 'output/'$1'/walk.wav' -c:v ffv1 output/$1/walk.avi
