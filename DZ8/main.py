import re


def main(input_string):
    pattern = r"let\s+(\w+)\s+to\s+(\w+)\."
    matches = re.findall(pattern, input_string)
    result = {match[1]: match[0] for match in matches}
    return result

if __name__ == '__main__':
    #input_string = "<block> <: let usbe_65 to rilea. :><: let riedza_388 to tige. :> <: let xequte to cesoin. :> </block>"
    #input_string = "<block><: let inteor to aenza_627. :> <: let diisra_224 to iserza.:> <: let ererxe_182 to xemaed_764.:><: let isbibe to tige_348. :></block>"
    #input_string = "<block> <: let usbe_65 to rilea. :><: let riedza_388 to tige. :> <:\nlet xequte to cesoin. :> </block>"
    input_string = "<block> <:let cebi to sobi.:> <: let maso to oronve_815. :> <: let\nsoso_638 to zaqube.:></block>"

    parsed_result = main(input_string)
    print(parsed_result)
