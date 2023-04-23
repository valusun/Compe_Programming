from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from pathlib import Path

from file_generator import py_file, rs_file, json_file


@dataclass
class Contest(ABC):
    contest_name: str
    contest_type: str = field(init=False)
    problems: tuple[str, ...] = ("a", "b", "c", "d", "e", "f", "g", "ex")

    def __post_init__(self):
        self.contest_type = self.contest_name[:3]

    def _generate_contest_type_folder(self, parent_dir: Path) -> Path:
        """コンテストの種類のフォルダを作成する(例: ABC, AEC)"""

        (contest_dir := parent_dir / self.contest_type).mkdir(exist_ok=True)
        return contest_dir

    def _generate_contest_name_folder(self, parent_dir: Path) -> Path:
        """コンテストのフォルダを作成する(例: ABC001, ARC001)"""

        (contest_id_dir := parent_dir / self.contest_name).mkdir()
        return contest_id_dir

    def _generate_source_files(self, parent_dir: Path, problems: tuple[str, ...]) -> None:
        """ソースコードファイルを作成する"""
        for file_name in problems:
            py_file.PythonFile().generate_file(parent_dir, file_name)
            rs_file.RustFile().generate_file(parent_dir, file_name)

    def _generate_problem_folder(self, tgt_problems: tuple[str, ...]) -> None:

        root_dir = Path(__file__).parents[2]
        contest_dir = self._generate_contest_type_folder(root_dir)
        problem_dir = self._generate_contest_name_folder(contest_dir)
        self._generate_source_files(problem_dir, tgt_problems)
        json_file.Settings(problem_dir).setting_rust_analyzer()

    @abstractmethod
    def generate_folder(self) -> None:
        """対象のコンテストで使用するフォルダを作成する"""
        ...


class ABCContest(Contest):
    def generate_folder(self) -> None:
        self._generate_problem_folder(self.problems[:5])


class ARCContest(Contest):
    def generate_folder(self) -> None:
        self._generate_problem_folder(self.problems[:3])


class AGCContest(Contest):
    def generate_folder(self) -> None:
        self._generate_problem_folder(self.problems[:1])


class AHCContest(Contest):
    def generate_folder(self) -> None:
        self._generate_problem_folder(self.problems[:1])


def main():
    contest_name = input("Contest Name?: ").upper()
    match contest_name[:3]:
        case "ABC":
            print(contest_name)
            contest = ABCContest(contest_name)
        case "ARC":
            contest = ARCContest(contest_name)
        case "AGC":
            contest = AGCContest(contest_name)
        case "AHC":
            contest = AHCContest(contest_name)
        case _:
            TypeError("指定されたコンテストは存在しません")
    contest.generate_folder()


if __name__ == "__main__":
    main()
