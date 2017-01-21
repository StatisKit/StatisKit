for i in $(ls -R -d ./*/*-[0-9]*.svg); do
    j=${i/svg/png}
    inkscape ${i} --export-png=${j} --export-area-drawing
done

sources=`ls -r -R -d ./branch/branch-[0-9]*.png`
target=./branch/branch.gif
convert -dispose previous -delay 100 ${sources} ${target}
convert -reverse ${target} ${target}

sources=`ls -r -R -d ./commit/commit-[0-9]*.png`
target=./commit/commit.gif
convert -dispose previous -delay 100 ${sources} ${target}
convert -reverse ${target} ${target}

sources=`ls -r -R -d ./upload/upload-[0-9]*.png`
target=./upload/upload.gif
convert -dispose previous -delay 100 ${sources} ${target}
convert -reverse ${target} ${target}

sources=`ls -r -R -d ./submit/prepare-[0-9]*.png`
target=./submit/prepare.gif
convert -dispose previous -delay 100 ${sources} ${target}
convert -reverse ${target} ${target}

sources=`ls -r -R -d ./submit/propose-[0-9]*.png`
target=./submit/propose.gif
convert -dispose previous -delay 100 ${sources} ${target}
convert -reverse ${target} ${target}

sources=`ls -r -R -d ./submit/integrate-[0-9]*.png`
target=./submit/integrate.gif
convert -dispose previous -delay 100 ${sources} ${target}
convert -reverse ${target} ${target}
