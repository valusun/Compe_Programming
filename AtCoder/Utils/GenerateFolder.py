import logging
import os
import shutil
import string
import subprocess
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path

template_file_path: Path = Path("Utils/template.py")

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
logger.setLevel(logging.INFO)
logger.addHandler(handler)
logging.basicConfig(level=logging.DEBUG)


@dataclass
class Generator(metaclass=ABCMeta):
    contest_name: str
    folder_name: str = field(init=False, default=str)

    def __post_init__(self):
        self.folder_name = self.contest_name[:3]

    def GenerateFolder(self):
        os.makedirs(path := (Path(f"./{self.folder_name}/{self.contest_name}")))
        logger.info(f"{self.contest_name}フォルダを作成しました")
        object.__setattr__(self, "path", path)

    def _GenerateFiles(self, file_cnt: int) -> None:
        """受け取った個数分のファイルを作成する。

        Notes:
            A,B,...,Y,Zとナンバリングしたファイルを作る
            とりあえずA~Zまで対応する(26より大きい数値はエラーを吐く)
        """
        if file_cnt > 26:
            logger.ERROR("26以内で指定してください")
            return
        for num in range(file_cnt):
            file_name = string.ascii_uppercase[num]
            shutil.copy(
                template_file_path, file_path := (Path(f"{self.path}/{file_name}.py"))
            )
            subprocess.run(["code", "-g", f"{file_path}:2:5"], shell=True)

    @abstractmethod
    def GenerateFile(self):
        pass


@dataclass
class ABC(Generator):
    def GenerateFile(self):
        self._GenerateFiles(4)


@dataclass
class ARC(Generator):
    def GenerateFile(self):
        self._GenerateFiles(2)


@dataclass
class AHC(Generator):
    def GenerateFile(self):
        self._GenerateFiles(1)


def main():
    contest_name = input("Contest Name?: ").upper()
    cls: Generator = globals()[contest_name[:3]](contest_name)
    cls.GenerateFolder()
    cls.GenerateFile()


if __name__ == "__main__":
    main()
