import subprocess
import shutil
import string
from dataclasses import dataclass
from pathlib import Path


@dataclass
class RustFile:
    template_main_file: Path = (Path(__file__).parent / "./template/main.rs").resolve()
    template_toml_file: Path = (Path(__file__).parent / "./template/template.toml").resolve()

    def _run_cargo(self, parent_dir: Path) -> None:
        """新しいCargoプロジェクトを開始する"""
        subprocess.run(["cargo", "new", parent_dir])

    def _edit_cargo_toml(self, cargo_path: Path, package_name: str) -> None:
        """Cargo.tomlをテンプレートのものに置き換える"""

        def _write_toml_data() -> str:
            """Cargo.tomlに書き込むデータを取得する"""
            with open(cargo_path, "r", encoding="utf-8") as file:
                template = string.Template(file.read())
                return template.substitute({"package_name": package_name.lower()})

        shutil.copy(self.template_toml_file, cargo_path)
        with open(cargo_path, "w", encoding="utf-8") as file:
            file.write(_write_toml_data())

    def generate_file(self, parent_dir: Path, package_name: str) -> None:
        """対象のフォルダ下にRustファイルを作成する"""
        rust_dir = Path(f"{parent_dir}/{package_name.lower()}")  # パッケージ名は小文字
        self._run_cargo(rust_dir)
        shutil.copy(self.template_main_file, Path(f"{rust_dir}/src"))
        self._edit_cargo_toml(rust_dir / "Cargo.toml", package_name)
