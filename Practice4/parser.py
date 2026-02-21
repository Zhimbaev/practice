import json

with open("/Users/zamirzimbaev/Desktop/practice/Practice4/data.json", "r") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 75)

print(f"{'DN':43} {'Description':15} {'Speed':7} {'MTU':6}")
print("-" * 43, "-" * 15, "-" * 7, "-" * 6)

for item in data["imdata"]:
    attrs = item["l1PhysIf"]["attributes"]

    dn = attrs.get("dn", "")
    descr = attrs.get("descr", "")
    speed = attrs.get("speed", "")
    mtu = attrs.get("mtu", "")

    print(f"{dn:43} {descr:15} {speed:7} {mtu:6}")