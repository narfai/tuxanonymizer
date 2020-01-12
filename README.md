# Tux Anonymizer

Customer data obfuscation : generate anonymized file with sames structures and value format
Currenty only supportes xml files.

## Install

```
pip install tuxanonymizer
```

## CLI

```
tuxanonymizer /path/to/my/file.xml
```

Will output an obfuscated xml file in stdout.

## Library


### Anonymized file to string

```
from anonymize_xml_file import tuxanonymizer

print(anonymize_xml_file('/path/to/my/file.xml'))
```