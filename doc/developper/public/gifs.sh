convert -dispose previous -delay 100 branch/branch-4.png branch/branch-3.png branch/branch-2.png branch/branch-1.png branch/branch-0.png branch/branch.gif
convert -reverse branch/branch.gif branch/branch.gif
convert -dispose previous -delay 100 commit/commit-1.png commit/commit-0.png commit/commit.gif
convert -reverse commit/commit.gif commit/commit.gif
convert -dispose previous -delay 100 upload/upload-1.png upload/upload-0.png upload/upload.gif
convert -reverse upload/upload.gif upload/upload.gif
