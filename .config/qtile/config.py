import datetime
import subprocess
from pathlib import Path

from libqtile import bar, hook, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

@hook.subscribe.startup_once
def autostart():
    subprocess.run([Path.home() / '.config' / 'qtile' / 'autostart.sh'])

def screenshot(area=False, save=False):
    def f(qtile):
        path = Path.home() / 'Pictures' / f'Screenshot_{datetime.datetime.now():%Y-%m-%dT%H-%M-%S}.png'
        shot = subprocess.run(['maim', '-u', '-s'] if area else ['maim', '-u'], stdout=subprocess.PIPE)

        if save:
            with open(path, 'wb') as sc:
                sc.write(shot.stdout)
        else:
            subprocess.run(['xclip', '-selection', 'clipboard', '-t', 'image/png'], input=shot.stdout)
    return f

mod = "mod4"
terminal = guess_terminal()

color_focus = "#98a5b3"
color_normal = "#292e33"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html

    # Switch focus of windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to the left"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to the right"),
    Key([mod], "Tab", lazy.layout.next(), desc="Move focus to next window"),
    Key([mod, "shift"], "Tab", lazy.layout.previous(), desc="Move focus to previous window"),

    # Switch position of windows
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),

    # Resize windows
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Manage window columns
    Key([mod, "control", "shift"], "Left", lazy.layout.swap_column_left(), desc="Swap column to the left"),
    Key([mod, "control", "shift"], "Right", lazy.layout.swap_column_right(), desc="Swap column to the right"),
    Key([mod], "x", lazy.layout.toggle_split(), desc="Toggle between split/unsplit stack"),

    # Toggle window modes
    Key([mod], "s", lazy.window.toggle_floating(), desc="Float window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Fullscreen window"),
    Key([mod], "m", lazy.window.toggle_maximize(), desc="Maximize window"),
    Key([mod], "n", lazy.window.toggle_minimize(), desc="Minimize window"),

    # Toggle window layouts
    Key([mod], "w", lazy.next_layout(), desc="Toggle between layouts"),

    # Applications
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "space", lazy.spawn("rofi -show drun -disable-history"), desc="Launch an application using Rofi"),

    # Audio
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --unmute --increase 2"), desc="Raise volume (2%)"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --unmute --decrease 2"), desc="Lower volume (2%)"),
    Key(["shift"], "XF86AudioRaiseVolume", lazy.spawn("pamixer --unmute --increase 1"), desc="Raise volume (1%)"),
    Key(["shift"], "XF86AudioLowerVolume", lazy.spawn("pamixer --unmute --decrease 1"), desc="Lower volume (1%)"),
    Key([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute"), desc="Toggle volume mute"),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc="Toggle audio play/pause"),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Play next audio"),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="Play previous audio"),

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -fps 60 -time 100 -inc 5"), desc="Increase screen brightness"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -fps 60 -time 100 -dec 5"), desc="Decrease screen brightness"),

    # Screenshot
    Key([], "Print", lazy.function(screenshot()), desc="Screenshot"),
    Key(["shift"], "Print", lazy.function(screenshot(area=True)), desc="Screenshot area"),
    Key(["control"], "Print", lazy.function(screenshot(save=True)), desc="Screenshot to file"),
    Key(["control", "shift"], "Print", lazy.function(screenshot(area=True, save=True)), desc="Screenshot area to file"),

    # System
    Key([mod], "l", lazy.spawn("loginctl lock-session"), desc="Lock screen"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

groups = [Group(i) for i in "12345678"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(), desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        #Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True), desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # mod1 + shift + letter of group = move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name), desc="Move focused window to group {}".format(i.name)),
    ])

layouts = [
    layout.Columns(
        border_focus=color_focus,
        border_normal=color_normal,
        grow_amount=2,
        insert_position=1,
    ),
    layout.Max(),
]

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=4,
)
extension_defaults = widget_defaults.copy()

def topbar_widgets():
    widgets = []

    widgets.extend([
        widget.CurrentLayoutIcon(
            padding=0,
            scale=0.6,
        ),
        widget.GroupBox(
            disable_drag=True,
            spacing=2,
        ),
        widget.Sep(
            padding=8,
            size_percent=100,
        ),
        widget.Prompt(
            record_history=False,
        ),
        widget.TaskList(
            spacing=2,
            max_title_width=200,
            txt_floating='🗗 ',
            txt_maximized='🗖 ',
            txt_minimized='🗕 ',
        ),
        widget.Volume(
            get_volume_command=Path.home() / '.config' / 'qtile' / 'scripts' / 'get_volume.sh',
            volume_up_command='pamixer --unmute --increase 2',
            volume_down_command='pamixer --unmute --decrease 2',
            mute_command='pamixer --toggle-mute',
        ),
    ])

    if Path('/sys/class/power_supply/BAT0').exists():
        widgets.extend([
            widget.Battery(
                format='<span size="8000" rise="1550">{char}</span>{percent:.0%}',
                charge_char='🡱 ',
                discharge_char='🡳 ',
                empty_char='',
                full_char='',
                unknown_char='',
            ),
        ])

    widgets.extend([
        widget.Spacer(
            length=4,
        ),
        widget.Clock(
            padding=0,
            format='%I:%M%p %d/%m/%Y',
        ),
        widget.Systray(
            padding=4,
        ),
        widget.Spacer(
            length=4,
        ),
    ])

    return widgets

screens = [
    Screen(
        top=bar.Bar(
            widgets=topbar_widgets(),
            size=30,
        ),
    ),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_focus=color_focus,
    border_normal=color_normal,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),  # gitk
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(wm_class='ssh-askpass'),  # ssh-askpass
        Match(title='branchdialog'),  # gitk
        Match(title='pinentry'),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

