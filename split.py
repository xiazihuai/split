# 读取OGnumber.txt文件
og_file_path = 'OGnumber.txt'
og_data = {}
with open(og_file_path, 'r') as og_file:
    next(og_file)  # 跳过表头
    for line in og_file:
        species, sequence, source = line.strip().split('\t')
        og_data[sequence] = source

# 处理temp2.cds文件
cds_file_path = 'temp2.cds'
current_sequence = ''
output_files = {}
with open(cds_file_path, 'r') as cds_file:
    for line in cds_file:
        if line.startswith('>'):
            # 提取标识行中的Species和Sequence
            line = line.strip().lstrip('>')
            species, sequence = line.split('@')
            current_sequence = sequence

            # 根据Sequence查找对应的Source
            if current_sequence in og_data:
                source = og_data[current_sequence]

                # 创建或打开对应的输出文件
                if source not in output_files:
                    output_file_path = f'{source}.cds'
                    output_files[source] = open(output_file_path, 'w')

        else:
            # 将内容行写入对应的输出文件
            if current_sequence in output_files:
                output_files[current_sequence].write(line)

# 关闭所有输出文件
for file in output_files.values():
    file.close()