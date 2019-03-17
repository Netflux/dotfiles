# Set default editor
export EDITOR="nvim"
export VISUAL="nvim"

# Set SSH Agent variable
export SSH_AUTH_SOCK="$XDG_RUNTIME_DIR/ssh-agent.socket"

# Set XDG Config Folder path
export XDG_CONFIG_HOME="$HOME/.config"

# Set NPM global modules path
export NPM_CONFIG_PREFIX="$HOME/.npm"
export PATH="$PATH:$HOME/.npm/bin"

# Set Java path
export JAVA_HOME="/usr/lib/jvm/default"

# Set Android SDK path
export ANDROID_SDK_ROOT="$HOME/Android/Sdk"
export PATH="$PATH:$ANDROID_SDK_ROOT/tools/bin:$ANDROID_SDK_ROOT/platform-tools:$ANDROID_SDK_ROOT/emulator"

# Fix for Java application windows in tiling WM
export _JAVA_AWT_WM_NONREPARENTING=1
