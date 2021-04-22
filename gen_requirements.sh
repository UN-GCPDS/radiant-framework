rm requirements.txt
pipreqs --ignore radiant/brython-3.9.1 --savepath requirements.txt --force radiant
sed -i '/browser==/d' requirements.txt
sed -i 's/==.*//' requirements.txt
python -c "[print(f'\'{line[:-1]}\',') for line in open('requirements.txt').readlines()]"
