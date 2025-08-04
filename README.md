

# Hey Uv 101




## [Installing Python](https://docs.astral.sh/uv/guides/install-python/) 


* 安装Python 后，它将自动被 `uv`命令使用。`uv`还会自动将已安装的版本添加到`PATH`中

```bash
python3.13
```


```bash
# 查看可用和已安装的
uv python list

# 安装特地版本
uv python install 3.13
```

默认情况下，uv仅安装版本化可执行文件。要安装`python`和`python3`可执行文件，请包含实验性`--default`选项

```bash
uv python install 3.13 --default
```



##  [Python versions](https://docs.astral.sh/uv/concepts/python-versions/)

> `managed`、`system`

```bash
# 在大多数uv命令中，可以使用 --python 选项安装python
uv run --python 3.13 python
uv run --python /usr/bin/python3 python
```

> `.python-version`

```bash
# current directory
uv python pin 3.13

# global: ~/.config/uv/.python-version
uv python pin 3.13 --global
```



```bash
# https://docs.astral.sh/uv/concepts/python-versions/#installing-python-executables
uv tool update-shell

# /Users/lemon/.config/fish/config.fish
fish_add_path "/Users/lemon/.local/bin"
```



```bash
uv python find
```







## Tools

> <https://docs.astral.sh/uv/guides/tools/>

`uvx` 是 `uv tool run`的别名。安装到**临时的隔离**环境中

```
uvx ruff
```

有时包名和命令名称不同

```bash
uvx --from httpie http
uvx --from ansible-core ansible
```

如果**经常使用**某个工具，将其安装到持久环境并将其添加到`PATH`而不重复调用`uvx`

```bash
uv tool install ruff
```

默认情况下，将使用默认的Python解释器（它找到的第一个)。可以使用`--python`选项指定版本

`@TODO`: 第一个是如何找到的


```
uvx --from ansible-core ansible --version(3.13.5)
uvx --python 3.11 --from ansible-core ansible --version(3.11.13)

uv tool install --python 3.12 ansible-core(3.12)
```




> <https://docs.astral.sh/uv/concepts/tools/>

* 在大多数情况下，使用`uvx` 执行工具比安装更合适。
* 使用`uv tool install` 安装工具后，`uvx` 将默认使用已安装的版本

```bash
# UV_CACHE_DIR: ~/.cache/uv
uvx cache dir
```

```bash
# UV_TOOL_DIR: ~/.local/share/uv/tools
uv tool dir
```





## Ref

* <https://docs.astral.sh/uv/>
* [用uv管理Python的一切！ - YouTube](https://www.youtube.com/watch?v=aVXs8lb7i9U)