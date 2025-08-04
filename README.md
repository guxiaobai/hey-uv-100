

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



## Ref

* <https://docs.astral.sh/uv/>
* [用uv管理Python的一切！ - YouTube](https://www.youtube.com/watch?v=aVXs8lb7i9U)