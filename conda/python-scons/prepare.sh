set -xe

[[ -d "scons-2.5.0" ]] && rm -rf scons-2.5.0 || echo "passed"
[[ -d "scons-2.5.0-py27" ]] && rm -rf scons-2.5.0-py27 || echo "passed"
[[ -d "scons-2.5.0-py35" ]] && rm -rf scons-2.5.0-py35 || echo "passed"


wget https://pypi.python.org/packages/source/S/SCons/scons-2.5.0.tar.gz
tar -zxvf scons-2.5.0.tar.gz
rm scons-2.5.0.tar.gz
cp -r scons-2.5.0 scons-2.5.0-py35
cd scons-2.5.0-py35
sed -i'' -e '49,54d' setup.py
sed -i'' -e '58,64d' script/scons
sed -i'' -e '39d' engine/SCons/Util.py
sed -i'' -e 's|exceptions|builtins|g' engine/SCons/Errors.py
2to3 --output-dir=engine/SCons3 -W -n engine/SCons
rm -rf engine/SCons
mv engine/SCons3 engine/SCons
2to3 -w -n script/scons
2to3 -w -n script/sconsign
2to3 -w -n script/scons-time
grep -r -l "pickle\.dumps(obj)" * | xargs sed -i'' -e 's|pickle\.dumps(obj)|pickle\.dumps(obj, 0)\.decode(errors="ignore")|g' 
grep -r -l "exec(_file_, call_stack\[-1\]\.globals)" * | xargs sed -i -e "s|exec(_file_, call_stack\[-1\]\.globals)|exec(compile(_file_\.read(), _file_\.name, 'exec'), call_stack\[-1\]\.globals)|g"
grep -r -l "DefaultToolpath=\[\]" * | xargs sed -i'' -e 's|DefaultToolpath=\[\]|DefaultToolpath=__path__|g'
cd engine/SCons/Tool/MSCommon
grep -r -l "from \. import" * | xargs sed -i'' 's|from \. import|from SCons.Tool.MSCommon import|g'
grep -r -l "from \." * | xargs sed -i'' 's|from \.|from SCons\.Tool\.MSCommon\.|g'
cd ..
grep -r -l "from \. import" * | xargs sed -i'' 's|from \. import|from SCons.Tool import|g'
grep -r -l "from \." * | xargs sed -i'' 's|from \.|from SCons\.Tool\.|g'
grep -r -l "= pipe\.stdout\.readline()" * | xargs sed -i'' 's|= pipe\.stdout\.readline()|= pipe\.stdout\.readline()\.decode(errors="ignore")|g'
cd ..
sed -i'' '104d' Conftest.py
grep -r -l "m\.update(str(blck))" * | xargs sed -i'' 's|m\.update(str(blck))|m\.update(blck)|g'
grep -r -l "m\.update(str(s))" * | xargs sed -i'' 's|m\.update(str(s))|m\.update(str(s).encode())|g'
grep -r -l "pickle\.dumps(self.entries, 1)" * | xargs sed -i'' 's|pickle\.dumps(self.entries, 1)|pickle\.dumps(self.entries, 0).decode(errors="ignore")|g'
grep -r -l "re\.findall(node\.get_text_contents()" * | xargs sed -i'' 's|re\.findall(node\.get_text_contents()|re\.findall(node\.get_text_contents()\.decode(errors="ignore")|g'
grep -r -l "MethodType(function, obj, obj\.__class__)" * | xargs sed -i'' 's|MethodType(function, obj, obj\.__class__)|MethodType(function, obj)|g'
grep -r -l "MethodType(function, None, obj)" * | xargs sed -i'' 's|MethodType(function, None, obj)|MethodType(function, obj)|g'
grep -r -l "sys32_dir not" * | xargs sed -i'' 's|sys32_dir not|sys32_dir.decode() not|g'
grep -r -l "\+ sys32_dir" * | xargs sed -i'' 's|+ sys32_dir|+ sys32_dir.decode()|g'
cd ../../..
mv scons-2.5.0 scons-2.5.0-py27
