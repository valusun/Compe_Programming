from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal

from file_generator import py_file, rs_file, json_file


@dataclass(frozen=True)
class Contest:
    contest: str
    file_count: int
    filenames: list[str] = field(init=False, default_factory=list)
    problem_names: tuple[str, ...] = ("A", "B", "C", "D", "E", "F", "G", "Ex")

    def __post_init__(self):
        if self.file_count > len(self.problem_names):
            raise TypeError("問題の数が想定を超えています")
        # HACK: `frozen=True`の弊害
        object.__setattr__(self, "filenames", self.problem_names[: self.file_count])

    @property
    def contest_type(self):
        return self.contest[:3]


def ContestFactory(contest_name: str) -> Contest:
    match contest_name[:3]:
        case "ABC":
            return Contest(contest_name, 4)
        case "ARC":
            return Contest(contest_name, 3)
        case "AGC":
            return Contest(contest_name, 1)
        case "AHC":
            return Contest(contest_name, 1)
        case _:
            raise TypeError("指定されたコンテストは存在しません")


@dataclass
class FolderGenerator:
    contest_infos: Contest

    def _generate_contest_type_folder(self, parent_dir: Path) -> Path:
        """コンテストの種類のフォルダを作成する(例: ABC, ARC)"""

        (contest_dir := parent_dir / self.contest_infos.contest_type).mkdir(exist_ok=True)
        return contest_dir

    def _generate_contest_name_folder(self, parent_dir: Path) -> Path:
        """コンテストのフォルダを作成する(例: ABC001, ARC001)"""

        (contest_id_dir := parent_dir / self.contest_infos.contest).mkdir()
        return contest_id_dir

    def generate_folder(self) -> Path:
        """対象のコンテスト名(`ABC001`, `ARC001`など)のフォルダを作成する"""

        root_dir = Path(__file__).parents[2]
        contest_dir = self._generate_contest_type_folder(root_dir)
        problem_dir = self._generate_contest_name_folder(contest_dir)
        return problem_dir


@dataclass
class FileGenerator:
    contest_info: Contest
    parent_dir: Path

    def generate_source_files(self, lang: Literal["python", "rust"]) -> None:
        """ソースコードファイルを作成する"""
        for file_name in self.contest_info.filenames:
            if lang == "python":
                py_file.PythonFile().generate_file(self.parent_dir, file_name)
            elif lang == "rust":
                rs_file.RustFile().generate_file(self.parent_dir, file_name)
        if lang == "rust":
            json_file.Settings(self.parent_dir).setting_rust_analyzer()


def Validate(lang):
    if lang not in ("python", "rust"):
        raise ValueError("pythonかrustを入力してください")


def main():
    contest_name = input("Contest Name?: ").upper()
    lang = input("Language?(python / rust): ").lower()
    Validate(lang)
    contest_info = ContestFactory(contest_name)
    folder = FolderGenerator(contest_info).generate_folder()
    FileGenerator(contest_info, folder).generate_source_files(lang)


if __name__ == "__main__":
    main()
