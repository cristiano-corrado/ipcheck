# ipcheck
Simple script which queries iplocation for ip geolocation information and return a list of items describing the ip

## Install
```
pip3 install -r requirements.txt
```
## Execute 

### With file

the ips in file must be one by line:

```
python3 ipcheck.py -f filewithip.txt
```

### Single IP

```
python3 ipcheck.py -i 8.8.8.8
```

### Output 

```
$ python3 ipcheck.py 8.8.8.8
['8.8.8.8', 'United States', 'California', 'Mountain View', 'Google LLC', 'Google LLC (google.com)', '37.3860', '-122.0838']
```
