import yaml


def read_yml(path):
    # 读取yml文件
    with open(path, mode='r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        # print(data)

    return data


if __name__ == '__main__':
    print(read_yml('./data.yml'))
    print(read_yml('./data.yml')['datas'])
