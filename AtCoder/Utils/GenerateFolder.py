import logging
import os
import shutil
import string
import subprocess
from dataclasses import dataclass, field
from pathlib import Path

template_python_file: Path = Path(__file__).parent / "template.py"
template_rust_file: Path = Path(__file__).parent / "main.rs"
template_toml_file: Path = Path(__file__).parent / "template.toml"

# ログ設定
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
format_setting = "%(asctime)s [%(levelname)s] %(message)s"
formatter = logging.Formatter(format_setting)
handler.setFormatter(formatter)
logger.addHandler(handler)


@dataclass
class Generator:
    # TODO: 命名考える
    contest_name: str
    folder_name: str = field(init=False, default_factory=str)
    folder_path: Path = field(init=False, default_factory=Path)

    def __post_init__(self):
        self.folder_name = self.contest_name[:3]
        self._GenerateFolder()

    def _GenerateFolder(self):
        base_path = Path(__file__).parents[1]
        self.folder_path = base_path / self.folder_name / self.contest_name
        os.makedirs(self.folder_path)
        logger.info(f"{self.contest_name}フォルダを作成しました")

    def _GeneratePythonFile(self, file_name: str) -> None:
        file_path = Path(f"{self.folder_path}/{file_name}.py")
        shutil.copy(template_python_file, file_path)
        subprocess.run(["code", "-g", f"{file_path}:2:5"], shell=True)

    def _GenerateRustFile(self, file_name: str) -> None:
        toml_file_path = Path(f"{self.folder_path}/{file_name.lower()}")
        subprocess.run(["cargo", "new", toml_file_path])
        main_file_path = Path(f"{self.folder_path}/{file_name.lower()}/src")
        shutil.copy(template_rust_file, main_file_path)
        self._EditCargoTomlFile(toml_file_path, file_name)

    def _EditCargoTomlFile(self, file_path: Path, package_name: str):
        """Cargoパッケージ内のtomlを編集する"""

        def GetWriteData() -> str:
            """書き込むデータを取得する"""
            with open(edited_file, "r", encoding="utf-8") as file:
                template = string.Template(file.read())
                place_holders = {"package_name": package_name.lower()}
                return template.substitute(place_holders)

        edited_file = file_path / "Cargo.toml"
        shutil.copy(template_toml_file, edited_file)
        template = GetWriteData()
        with open(edited_file, "w", encoding="utf-8") as file:
            file.write(template)

    def _GenerateFiles(self, file_cnt: int) -> None:
        """受け取った個数分のファイルを作成する。

        Notes:
            A,B,...,Y,Zとナンバリングしたファイルを作る
            とりあえずA~Zまで対応する(26より大きい数値はエラーを吐く)
        """

        if file_cnt > 26:
            raise ValueError("ファイル数は26以内で指定してください")
        for num in range(file_cnt):
            file_name = string.ascii_uppercase[num]
            self._GeneratePythonFile(file_name)
            self._GenerateRustFile(file_name)

    def GenerateFiles(self, file_cnt: int):
        self._GenerateFiles(file_cnt)


# TODO: いい感じにする
class ABC(Generator):
    def Generate(self):
        self.GenerateFiles(4)


class ARC(Generator):
    def Generate(self):
        self.GenerateFiles(2)


class AHC(Generator):
    def Generate(self):
        self.GenerateFiles(1)


def main():
    contest_name = input("Contest Name?: ").upper()
    cls: Generator = globals()[contest_name[:3]](contest_name)
    cls.Generate()


if __name__ == "__main__":
    main()
