wget https://pypi.python.org/packages/source/S/SCons/scons-2.5.0.tar.gz
tar -zxvf scons-2.5.0.tar.gz
rm scons-2.5.0.tar.gz
cp -r scons-2.5.0 scons-2.5.0-py35
cd scons-2.5.0-py35
sed -i'' -e '49,54d' setup.py
sed -i'' -e '58,64d' script/scons
sed -i'' -e '39d' engine/SCons/Util.py
sed -i'' -e 's#exceptions#builtins#g' engine/SCons/Errors.py
2to3 --output-dir=engine/SCons3 -W -n engine/SCons
rm -rf engine/SCons
mv engine/SCons3 engine/SCons
2to3 -w -n script/scons
2to3 -w -n script/sconsign
2to3 -w -n script/scons-time
grep -r -l "pickle\.dumps(obj)" * | xargs sed -i'' -e 's#pickle\.dumps(obj)#pickle\.dumps(obj, 0)\.decode()#g' 
grep -r -l "exec(_file_, call_stack\[-1\]\.globals)" * | xargs sed -i -e "s#exec(_file_, call_stack\[-1\]\.globals)#exec(compile(_file_\.read(), _file_\.name, 'exec'), call_stack\[-1\]\.globals)#g"
grep -r -l "DefaultToolpath=\[\]" * | xargs sed -i'' -e 's#DefaultToolpath=\[\]#DefaultToolpath=__path__#g'
cd engine/SCons/Tool
grep -r -l "from \. import" * | xargs sed -i'' 's/from \. import/from SCons.Tool import/g'
cd ..
sed -i'' '104d' onftest.py
cd ..
mv scons-2.5.0 scons-2.5.0-py27