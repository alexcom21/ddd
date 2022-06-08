import re


def main(text: str) -> dict[str, list[str]]:
    text = text.replace("\n", ' ')
    result = dict()
    data_list = re.findall(r"t\s*\(.*?\)", text)
    keys = re.findall(r"\(\w*\)", text)
    for n in range(len(keys)):
        keys[n] = keys[n].replace('(', '')
        keys[n] = keys[n].replace(')', '')
        data_list[n] = re.sub(r"t\s*\(\s*", '', data_list[n])
        data_list[n] = re.sub(r"\s*\)", '', data_list[n])
        print(data_list[n])
        result[keys[n]] = data_list[n].split(" ")
    return result
