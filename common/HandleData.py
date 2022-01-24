import yaml


def get_yaml(yaml_file):
    with open(yaml_file, "r", encoding="utf-8") as fp:
        f = fp.read()  # 读出来是字符串
        print(type(f))
    d = yaml.load(f, Loader=yaml.FullLoader)  # 转列表
    print("读取到yaml文件数据")
    print(d)
    print(type(d))
    return d


def yaml_data_with_key(key):
    return get_yaml('test_data.yaml')[key]
