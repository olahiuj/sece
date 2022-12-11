"""
This module provides a Parser for difflib results.
"""
import difflib
from program import Program


class DiffParser:
    """parser for difflib results"""
    def __init__(self, prog1: Program, prog2: Program):
        """initialize diff results for (prog1, prog2)"""
        self.__prog1__ = prog1
        self.__prog2__ = prog2
        with (open(prog1.get_path(), encoding='utf-8') as file1,
              open(prog2.get_path(), encoding='utf-8') as file2):
            self.__diff__ = list(
                difflib.ndiff(
                    file1.read().splitlines(),
                    file2.read().splitlines()
                )
            )

    def parse_diff(self):
        """parse diff results"""
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
                        result['left_diff'] = incremental_diff_result.get('left', None)
                        result['right_diff'] = incremental_diff_result.get('right', None)
                        result['newline'] = incremental_diff_result['newline']
                        lineno += incremental_diff_result['skiplines']
                case '+ ':
                    result['type'] = 'R'
            yield result
            lineno += 1

    def __match_diff(self, lineno, pattern):
        """
        check if difflib result matches pattern

        patter:
        1. ['- ', '? ', '+ ', '? ']: line-internal diff
        2. ['- ', '+ ', '? ']:       right-only diff
        3. ['- ', '? ', '+ ']:       left-only diff
        """
        if lineno + len(pattern) > len(self.__diff__):
            return False
        for i in range(len(pattern)):
            if self.__diff__[lineno + i][:2] != pattern[i]:
                return False

        return True

    def __enumerate_filter(self, lineno, chars):
        """filter out indices that causes diff(appeared in chars)"""
        result = []
        for (i, character) in enumerate(self.__diff__[lineno][2:]):
            if character in chars:
                result.append(i)
        return result

    def __parse_incremental_diff(self, lineno):
        """
        distinguish between left-only/right-only/line-internal-diff
        and returns a map {
            'left': diff-left,
            'right': diff-right,
            'newline': contents,
            'skiplines': number of lines to skip in the difflib result
        }
        """
        changes = {}
        # ('-', '?', '+', '?') internal_diff
        if self.__match_diff(lineno, ['- ', '? ', '+ ', '? ']):
            changes['left'] = self.__enumerate_filter(lineno + 1, ['-', '^'])
            changes['right'] = self.__enumerate_filter(lineno + 3, ['+', '^'])
            changes['newline'] = self.__diff__[lineno + 2][2:]
            changes['skiplines'] = 3
        # ('-', '+', '?') right_text has more
        elif self.__match_diff(lineno, ['- ', '+ ', '? ']):
            changes['right'] = self.__enumerate_filter(lineno + 2, ['+', '^'])
            changes['left'] = []
            changes['newline'] = self.__diff__[lineno + 1][2:]
            changes['skiplines'] = 2
        # ('-', '?', '+') left_text has more
        elif self.__match_diff(lineno, ['- ', '? ', '+ ']):
            changes['right'] = []
            changes['left'] = self.__enumerate_filter(lineno + 1, ['-', '^'])
            changes['newline'] = self.__diff__[lineno + 2][2:]
            changes['skiplines'] = 2
        return changes
