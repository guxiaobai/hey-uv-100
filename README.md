

# Hey Uv 101


## macOS

```bash
# ls -al /opt/homebrew/share/fish/vendor_completions.d|grep uv
brew install uv

# echo $PATH
# ~/.local/bin
uv tool update-shell
```



## Standalone

```bash
curl -LsSf https://astral.sh/uv/0.8.4/install.sh | sh

# enable shell autocompletion for uv commands
echo 'uv generate-shell-completion fish | source' > ~/.config/fish/completions/uv.fish

# enable shell autocompletion for uvx
echo 'uvx --generate-shell-completion fish | source' > ~/.config/fish/completions/uvx.fish
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