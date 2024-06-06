# 文件管理脚本

这是一个Python脚本，用于管理文件和目录。它可以从`config.yaml`文件中读取路径列表，然后对每个路径执行以下操作：

1. 将所有文件移动到根目录。
2. 删除所有空目录。

## 使用方法

首先，确保你的系统中已经安装了Python和必要的库。这个脚本需要`os`, `shutil`, `sys`和`yaml`库。

然后，你需要创建一个`config.yaml`文件，其中包含你想要管理的路径列表。如果`config.yaml`文件不存在，脚本会自动从`example.config.yaml`复制一份，并提示你修改路径。

最后，运行脚本：

```bash
python main.py
```

## 功能说明

- `move_files_to_root_dir(root_dir)`: 这个函数会遍历指定目录下的所有文件，如果文件不在根目录，就将其移动到根目录。如果根目录下已经存在同名文件，它会自动重命名新移动的文件，避免覆盖。

- `remove_empty_folders(root_dir)`: 这个函数会遍历指定目录下的所有子目录，如果发现某个子目录是空的，就将其删除。

- `main()`: 这是主函数，它首先检查`config.yaml`文件是否存在，如果不存在，就从`example.config.yaml`复制一份。然后，它会读取`config.yaml`中的路径列表，并对每个路径执行上述两个函数。

