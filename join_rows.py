# encoding=='utf-8'


# 处理从 Coursera下载的字幕：消除异常换行


def process_one_file(filename):
    """
    处理一个文件
    :param filename: 文件名
    :return: None
    """
    with open(filename, 'r', encoding='utf-8') as in_fp:
        with open('tidy_' + filename, 'w', encoding='utf-8') as out_fp:
            string = in_fp.read().replace('\n', ' ').replace(' >> ', '\n\n') + '\n'*10 + 'So_simple loves Amyyyy!'
            out_fp.write(string)
        out_fp.close()
    in_fp.close()


def process_multi_files(num_file):
    """
    同时处理多个文件
    原文件命名必须按数字顺序从1开始命名，如'1.txt','2.txt', ...
    :param num_file: 处理文件个数
    :return: None
    """
    for i in range(1, num_file+1):
        filename = str(i) + '.txt'
        process_one_file(filename)


if __name__ == '__main__':
    num_files = 42
    process_multi_files(42)
