echo ffmpeg -framerate $2 -pattern_type glob -i 'output/'$1'/*.png' -c:v ffv1 output/$1/walk.avi
ffmpeg -framerate $2 -pattern_type glob -i 'output/'$1'/*.png' -c:v ffv1 output/$1/walk.avi
