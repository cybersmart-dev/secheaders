# SecHeaders
#### SecHeaders is a tool design to find security headers missing in http response

## installation 

```shell
git clone https://github.com/cybersmart-dev/secheaders.git
```
```shell
cd secheaders
python secheaders.py
```

## Usage
```sh
python secheaders.py -h
```
```yaml
usage: secheaders.py [-h] [-u URL] [-l LIST]

SecHeaders

optional arguments:
  -h, --help            show this help message and
                        exit
  -u URL, --url URL     Target url
  -l LIST, --list LIST  Target list input
```
### scan single url 
```sh
python secheaders.py -u https://example.com
```
### scan multiple urls
```sh
python secheaders.py -l path/to/urls.txt
```

