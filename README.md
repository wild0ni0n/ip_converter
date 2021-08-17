# IP converter
This tool converts IP addresses into octal/decimal/hexadecimal format.  
It can also output URLs using the converted IP addresses.  
The URL can also use a different decimal number for each octet. The tool can output all combinations by using the `--mixed` option.  

# Usage
```bash
$ python .\ip_converter.py 192.168.1.1
[*] Base IP       : 192.168.1.1
 - To_octet       : 030052000401
 - To_dotted_octet: 0300.0250.0001.0001
 - To_decimal     : 3232235777
 - To_hex         : 0xc0a80101
 - To_dotted_hex  : 0xc0.0xa8.0x1.0x1
```


```bash
$ python .\ip_converter.py 192.168.1.1 --format "http://{}:8080/foo/bar"
[*] Base IP       : 192.168.1.1
 - To_octet       : 030052000401
 - To_dotted_octet: 0300.0250.0001.0001
 - To_decimal     : 3232235777
 - To_hex         : 0xc0a80101
 - To_dotted_hex  : 0xc0.0xa8.0x1.0x1
http://192.168.1.1:8080/foo/bar
http://0300.0250.0001.0001:8080/foo/bar
http://030052000401:8080/foo/bar
http://3232235777:8080/foo/bar
http://0xc0.0xa8.0x1.0x1:8080/foo/bar
http://0xc0a80101:8080/foo/bar
```

