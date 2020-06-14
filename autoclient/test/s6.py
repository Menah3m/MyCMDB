s="""
Handle 0x0100, DMI type 1, 27 bytes
System Information
	Manufacturer: Alibaba Cloud
	Product Name: Alibaba Cloud ECS
	Version: pc-i440fx-2.1
	Serial Number: bb1c4d10-3f12-4c01-9586-12cb280257c3
	UUID: bb1c4d10-3f12-4c01-9586-12cb280257c3
	Wake-up Type: Power Switch
	SKU Number: Not Specified
	Family: Not Specified

"""

"""
{
    'manufacturer':'Alibaba Cloud',
    'product-name':'Alibaba Cloud ECS',
    'serial-number':'bb1c4d10-3f12-4c01-9586-12cb280257c3',

}
"""
key_map = {
    'Manufacturer':'manufacturer',
    'Product Name':'product-name',
    'Serial Number':'serial-number',
}
res= s.split('\n')
response = {}

for info in res:
    if info:
        v = info.strip().split(':')
        if len(v) == 2:
            if v[0] in key_map:
                response[key_map[v[0]]]=v[1]

print(response)