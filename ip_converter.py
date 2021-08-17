import argparse
import re

def ip_converter(ip:str) -> str:
    octets = ip.split(".")
    result = {
        "original": ip,
        "to_dotted_octet": [],
        "to_octet": "",
        "to_decimal": "",
        "to_dotted_hex": "",
        "to_hex": "",
        "octets": [],
    }
    tmp_b_arr, tmp_o_arr, tmp_h_arr = [], [], []
    for octet in octets:
        tmp_b_arr.append(format(int(octet), '08b'))
        tmp_o_arr.append(oct(int(octet))[2:].zfill(4))
        tmp_h_arr.append(hex(int(octet)))
        result["octets"].append([octet, tmp_o_arr[-1], tmp_h_arr[-1]])

    result["to_dotted_octet"] = '.'.join(tmp_o_arr)
    result["to_dotted_hex"] = '.'.join(tmp_h_arr)
    result["to_octet"] = "0"+oct(int(''.join(tmp_b_arr), 2))[2:]
    result["to_decimal"] = int(''.join(tmp_b_arr), 2)
    result["to_hex"] = "0x"+hex(int(''.join(tmp_b_arr), 2))[2:]

    print("[*] Base IP       : {}".format(result['original']))
    print(" - To_octet       : {}".format(result['to_octet']))
    print(" - To_dotted_octet: {}".format(result['to_dotted_octet']))
    print(" - To_decimal     : {}".format(result['to_decimal']))
    print(" - To_hex         : {}".format(result['to_hex']))
    print(" - To_dotted_hex  : {}".format(result['to_dotted_hex']))
    return result

def output_payloads(fmt:str, ips:dict, mixed:bool=False):
    if mixed:
        print(fmt.format(ips['original']))
        print(fmt.format(ips['to_dotted_octet']))
        print(fmt.format(ips['to_dotted_hex']))
        for octet1 in ips['octets'][0]:
            for octet2 in ips['octets'][1]:
                for octet3 in ips['octets'][2]:
                    for octet4 in ips['octets'][3]:
                        print(fmt.format('.'.join([octet1, octet2, octet3, octet4])))

    else:
        for key, val in ips.items():
            if key == 'octets':
                continue
            print(fmt.format(val))

def check_ip(arg:str):
    pattern = re.compile(r'^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$')
    return True if re.search(pattern, arg) else False

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('ip', help='IP')
    parser.add_argument('--format', help='output format.The converted IP will be inserted in \'{}\'')
    parser.add_argument('--mixed', help='', action='store_true')

    args = parser.parse_args()

    if check_ip(args.ip):
        ips = ip_converter(args.ip)
        if args.format:
            output_payloads(args.format, ips, args.mixed)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()