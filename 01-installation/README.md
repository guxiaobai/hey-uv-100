# 01 Installation


## 结论二: 自己添加环境变量更清爽

```bash
mkdir ~/.local/bin/
fish_add_path ~/.local/bin/

# 在安装之前配置好环境变量，逻辑更清晰
# 结论一中所探讨的文件也不会安装了
```

```

# 默认可执行文件都是安装到: ~/.local/bin
uv tool update-shell
uv python update-shell
```


```bash
curl -LsSf https://astral.sh/uv/0.8.4/install.sh | sh

# enable shell autocompletion for uv commands
echo 'uv generate-shell-completion fish | source' > ~/.config/fish/completions/uv.fish

# enable shell autocompletion for uvx
echo 'uvx --generate-shell-completion fish | source' > ~/.config/fish/completions/uvx.fish
```



## 结论一: 不需要自己添加环境变量了(推荐使用结论二的方案)

```bash
# 来源: uv-installer.sh(v0.84)
# Line: 1305
cat ~/.config/fish/conf.d/uv.env.fish
cat ~/.local/bin/env.fish

# 所以不需要执行这条命令了
fish_add_path ~/.local/bin/
```





## Ref



* <https://docs.astral.sh/uv/getting-started/installation/>
* <https://docs.astral.sh/uv/reference/installer/>