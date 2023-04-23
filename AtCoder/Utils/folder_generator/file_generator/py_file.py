import shutil
import subprocess
from pathlib import Path
from dataclasses import dataclass


@dataclass
class PythonFile:
    template_file_path: Path = (Path(__file__).parent / "./template/template.py").resolve()

    def generate_file(self, parent_dir: Path, file_name: str) -> None:
        """pythonファイルを作成する"""
        py_file = Path(f"{parent_dir}/{file_name}.py")
        shutil.copy(self.template_file_path, py_file)
        # ファイルを開いて2行目の5列目にマウスカーソルを持っていく
        subprocess.run(["code", "-g", f"{py_file}:2:5"], shell=True)
