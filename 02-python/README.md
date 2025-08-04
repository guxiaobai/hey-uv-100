# 02 Python

* 安装Python 后，它将自动被 `uv`命令使用。`uv`还会自动将已安装的版本添加到`PATH`中

```bash
python3.13
```



默认情况下，uv仅安装版本化可执行文件。要安装`python`和`python3`可执行文件，请包含实验性`--default`选项

```bash
uv python install 3.13 --default
```



```bash
# 查看可用和已安装的
uv python list

# 安装特的版本
uv python install 3.13
```

## Ref



* <https://docs.astral.sh/uv/guides/install-python/>