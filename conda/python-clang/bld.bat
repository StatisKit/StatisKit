mkdir %SP_DIR%\clang
xcopy bindings\python\clang %SP_DIR%\clang /sy
echo "from path import path" >> %SP_DIR%\clang\cindex.py
echo "library_path = path(__path__)" >> %SP_DIR%\clang\cindex.py
echo "while not (library_path/'Library').exists()\:" >> %SP_DIR%\clang\cindex.py
echo "    library_path = library_path.parent" >> %SP_DIR%\clang\cindex.py
echo "library_path = library_path/'Library'" >> %SP_DIR%\clang\cindex.py
echo "conf.set_library_path((library_path/'lib').abspath())" >> %SP_DIR%\clang\cindex.py