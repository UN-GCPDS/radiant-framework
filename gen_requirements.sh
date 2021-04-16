pipreqs --ignore radiant/brython-3.9.1 --savepath requirements.tmp --force radiant
rm requirements.txt
sed '/browser==/d' requirements.tmp >> requirements.txt
rm requirements.tmp
sed -i 's/==/>=/' requirements.txt
cat requirements.txt
