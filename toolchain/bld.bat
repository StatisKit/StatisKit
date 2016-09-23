cd %PREFIX%
mkdir -p ./etc/conda/activate.d
cd ./etc/conda/activate.d/
type NUL > .\etc\conda\activate.d\env_vars.bat

echo "set TOOLCHAIN=mingw47" >> env_vars.bat

cd %PREFIX%
mkdir -p ./etc/conda/deactivate.d
cd ./etc/conda/deactivate.d/
type NUL > .\etc\conda\deactivate.d\env_vars.bat
echo "set TOOLCHAIN=" >> env_vars.bat