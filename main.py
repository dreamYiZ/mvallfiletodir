import os
import shutil
import sys
import yaml

def move_files_to_root_dir(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if dirpath != root_dir:
            for file_name in filenames:
                new_name = file_name
                while os.path.exists(os.path.join(root_dir, new_name)):
                    base, ext = os.path.splitext(new_name)
                    new_name = base + '_1' + ext
                shutil.move(os.path.join(dirpath, file_name), os.path.join(root_dir, new_name))

def remove_empty_folders(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        if dirpath != root_dir and not os.listdir(dirpath):
            os.rmdir(dirpath)

def main():
    if not os.path.exists('config.yaml'):
        shutil.copyfile('example.config.yaml', 'config.yaml')
        print("文件已创建，请修改config.yml中path路径")
    else:
        with open('config.yaml', 'r') as f:
            config = yaml.safe_load(f)

            paths = config['paths']  # now 'paths' is a list of your paths

            if not paths:
                print("No paths found in .env file.")
                sys.exit(1)

            for root_dir in paths:
                if not os.path.exists(root_dir):
                    print(f"路径 {root_dir} 不存在，请检查配置文件")
                    sys.exit(1)
                else:
                    print(f"路径 {root_dir} 存在")
                    move_files_to_root_dir(root_dir.strip())
                    remove_empty_folders(root_dir.strip())        
    

if __name__ == "__main__":
    main()
