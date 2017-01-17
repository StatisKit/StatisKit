cat > version.c <<EOF
#include <stdio.h>

int main() {

  printf("%d.%d\n",__GNUC__,__GNUC_MINOR__);
  return 0;
}
EOF

gcc -o gcc_version.out version.c
export __GNUC__=`./gcc_version.out`

cat > version.cpp <<EOF
#include <stdio.h>

int main() {

  srd::cout << __GNUC__ << "." << __GNUC_MINOR__ << std::endl;
  return 0;
}
EOF

g++ -o g++_version.out version.c
if [[ "$__GNUC__" -ne `./g++_version.out` ]]; then
    echo "gcc and g++ versions are not the same."
    exit 1;
fi
cat > version.py <<EOF
from distutils.version import StrictVersion
import os
print(StrictVersion("5.1") <= StrictVersion(os.environ["__GNUC__"]))
EOF

__GNUC__=`python version.py`
if [[ "$__GNUC__" -ne  "True" ]]; then
    echo "gcc and g++ versions should be superior to 5.1."
    exit 1;
fi