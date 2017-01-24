cp -rf bindings/python/clang $SP_DIR

echo "from path import path" >> $SP_DIR/clang/cindex.py
echo "library_path = path(__file__)" >> $SP_DIR/clang/cindex.py
echo "while not (library_path/'lib').exists():" >> $SP_DIR/clang/cindex.py
echo "    library_path = library_path.parent" >> $SP_DIR/clang/cindex.py
echo "conf.set_library_path((library_path/'lib').asbpath())" >> $SP_DIR/clang/cindex.py