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