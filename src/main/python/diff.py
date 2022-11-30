import difflib
from program import Program


class DiffParser:
    def __init__(self, prog1: Program, prog2: Program):
        self.__prog1__ = prog1
        self.__prog2__ = prog2
        with (open(prog1.get_path()) as file1,
              open(prog2.get_path()) as file2):
            self.__diff__ = list(
                difflib.ndiff(
                    file1.read().splitlines(),
                    file2.read().splitlines()
                )
            )

    def parse_diff(self):
        lineno = 0
        while lineno < len(self.__diff__):
            result = {}
            line = self.__diff__[lineno]
            diff_type = line[:2]
            result['line'] = line[2:]
            match diff_type:
                case '  ':
                    result['type'] = 'S'
                case '- ':
                    incremental_diff_result = self.__parse_incremental_diff(lineno)
                    if not incremental_diff_result:
                        result['type'] = 'L'
                    else:
                        result['type'] = 'D'
                        result['left_diff'] = incremental_diff_result['left'] if 'left' in incremental_diff_result else None
                        result['right_diff'] = incremental_diff_result['right'] if 'right' in incremental_diff_result else None
                        result['newline'] = incremental_diff_result['newline']
                        lineno += incremental_diff_result['skiplines']
                case '+ ':
                    result['type'] = 'R'
            yield result
            lineno += 1

    def __match_diff(self, lineno, pattern):
        if lineno + len(pattern) >= len(self.__diff__):
            return False
        for i in range(len(pattern)):
            if self.__diff__[lineno + i][:2] != pattern[i]:
                return False

        return True

    def __parse_incremental_diff(self, lineno):
        changes = {}
        # ('-', '?', '+', '?') internal_diff
        if self.__match_diff(lineno, ['- ', '? ', '+ ', '? ']):
            changes['left'] = [i for (i, c) in enumerate(self.__diff__[lineno + 1][2:]) if c in ['-', '^']]
            changes['right'] = [i for (i, c) in enumerate(self.__diff__[lineno + 3][2:]) if c in ['+', '^']]
            changes['newline'] = self.__diff__[lineno + 2][2:]
            changes['skiplines'] = 3
            return changes
        # ('-', '+', '?') right_text has more
        elif self.__match_diff(lineno, ['- ', '+ ', '? ']):
            changes['right'] = [i for (i, c) in enumerate(self.__diff__[lineno + 2][2:]) if c in ['+', '^']]
            changes['left'] = []
            changes['newline'] = self.__diff__[lineno + 1][2:]
            changes['skiplines'] = 2
            return changes
        # ('-', '?', '+') left_text has more
        elif self.__match_diff(lineno, ['- ', '? ', '+ ']):
            changes['right'] = []
            changes['left'] = [i for (i, c) in enumerate(self.__diff__[lineno + 1][2:]) if c in ['-', '^']]
            changes['newline'] = self.__diff__[lineno + 2][2:]
            changes['skiplines'] = 2
            return changes
        # no incremental change
        else:
            return None
