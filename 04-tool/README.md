# 04 Tools



`uvx` 是 `uv tool run`的别名。工具被安装到**临时的隔离**环境中

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



默认情况下，uv 在运行、安装或升级工具时将使用默认的 Python 解释器（它找到的第一个）。您可以指定要与 `--python` 一起使用的 Python 解释器 选择

> 第一个是如何找到的

```
uv python pin 3.11
uv python find
```



`@TODO` 这里还需要实验验证一下❌

```
uvx --from ansible-core ansible --version(3.13.5)
uvx --python 3.11 --from ansible-core ansible --version(3.11.13)
uv tool install --python 3.12 ansible-core(3.12)
```

---

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



* <https://docs.astral.sh/uv/guides/tools/>
* <https://docs.astral.sh/uv/concepts/tools/>