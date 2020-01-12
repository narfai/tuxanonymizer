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

### Anonymized xml string to dict


```
from tuxanonymizer import anonymize_xml_string

xml_string = """<?xml version="1.0" encoding='UTF-8'?>
<MaBalise monAttribut="Test123456789">
    Test123456789
</MaBalise>
"""

print(
    anonymize_xml_string(
        xml_string
    )
)
```

Will output :

```
{'MaBalise': {'@monAttribut': 'Cwbb442896383', '#text': 'Prmw771412734'}}
```

### Anonymized dict

```
from tuxanonymizer import anonymize_dict


input_dict = {'MaBalise': {'@monAttribut': 'Test123456789', '#text': 'Test123456789'}}

print(
    anonymize_dict(
        input_dict
    )
)
```

Will output :
```
{'MaBalise': {'@monAttribut': 'Ogfo718887842', '#text': 'Rfar127762898'}}
```