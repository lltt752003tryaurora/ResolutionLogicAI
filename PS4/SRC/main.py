import os
from resolution import pl_resolution

def read_input_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    alpha = lines[0].strip()
    n = int(lines[1].strip())
    kb = [line.strip() for line in lines[2:2+n]]
    return kb, alpha

def write_output_file(file_path, resolution_process, conclusion):
    with open(file_path, 'w') as file:
        # Kiểm tra nếu resolution_process không rỗng hoặc conclusion không phải là 'NO'
        if resolution_process or conclusion != 'NO':
            for step in resolution_process:
                if step == "{}":
                    file.write("1\n")  # Số lượng mệnh đề là 1 vì chỉ có mệnh đề rỗng
                    file.write(step + '\n')
                else:
                    # Sắp xếp các mệnh đề trước khi ghi ra file
                    sorted_step = sorted([' OR '.join(sorted(clause)) for clause in step])
                    # Kiểm tra nếu có mệnh đề trong bước này
                    if len(sorted_step) > 0:
                        file.write(str(len(sorted_step)) + '\n')  # Số lượng mệnh đề trong bước này
                        file.writelines(clause_str + '\n' for clause_str in sorted_step)
        
            if conclusion == 'NO':
                file.write("0\n")
        
            file.write(conclusion + '\n')

def main(input_folder='INPUT', output_folder='OUTPUT'):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Xử lý mỗi file input
    for file_name in os.listdir(input_folder):
        input_path = os.path.join(input_folder, file_name)
        kb, alpha = read_input_file(input_path)
        resolution_process, conclusion = pl_resolution(kb, alpha)
        
        # Kiểm tra nếu resolution_process rỗng và conclusion là 'NO', thì không ghi file output
        if resolution_process or conclusion != 'NO':
            output_path = os.path.join(output_folder, file_name.replace('input', 'output'))
            write_output_file(output_path, resolution_process, conclusion)

if __name__ == '__main__':
    main()
