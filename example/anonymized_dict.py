from tuxanonymizer import anonymize_dict


input_dict = {'MaBalise': {'@monAttribut': 'Test123456789', '#text': 'Test123456789'}}

print(
    anonymize_dict(
        input_dict
    )
)

