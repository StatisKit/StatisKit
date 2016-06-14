SIZE=`identify -ping -format '%wx%h' branch-4.png`
convert -dispose previous -delay 100 branch-4.png branch-3.png branch-2.png branch-1.png branch-0.png branch.gif
convert -reverse branch.gif branch.gif
