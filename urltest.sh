#!/bin/bash
chrome-browser http://www.youtube.com/watch?v=7bLaLJ51rRk http://www.youtube.com/watch?v=OxYSaT_NfjQ &
n=$((RANDOM%90+30))
echo $n
sleep $n
killall chrome-browser
echo "all done!"
