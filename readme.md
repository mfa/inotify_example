# inotify example

check if file is closed in a folder for further processing

# install

```
mkvirtualenv -p `which python3` inotify_example
pip install -r requirements.txt
python inotify_example.py
```

# run

in another shell now add a file to current folder:

```
echo "test" > test.txt
```
