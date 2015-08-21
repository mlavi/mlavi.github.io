from watchdog.tricks import ShellCommandTrick
# https://gist.github.com/norm/271bf72f77ae9df0fd9e
# watchmedo tricks-from tricks.yaml
class LandslideTrick(ShellCommandTrick):
    def __init__(self, target=None, patterns=None):
        make_command='make -B %s' % target
        super(LandslideTrick, self).__init__(
            shell_command=make_command,
            patterns=patterns,
            wait_for_process=True,
        )
