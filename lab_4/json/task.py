import json
with open("C:\\Users\\Elnur\\Desktop\\PP2_Labs\\lab_4\\json\\sample-data.json", "r") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 90)
print("{:<60} {:<10} {:<8} {:<8}".format("DN", "Description", "Speed", "MTU"))
print("{:-<60} {:-<10} {:-<8} {:-<8}".format("", "", "", ""))

for item in data["imdata"][:3]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes.get("dn", "")
    descr = attributes.get("descr", "")
    speed = attributes.get("speed", "")
    mtu = attributes.get("mtu", "")
    
    print("{:<60} {:<10} {:<8} {:<8}".format(dn, descr, speed, mtu))