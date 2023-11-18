from pathlib import Path, PurePosixPath
from dataclasses import dataclass


@dataclass
class Settings:
    parent_dir: Path

    def _get_cargo_files(self) -> list[Path]:
        """ディレクトリ内の'Cargo.toml'ファイルのパスを取得する"""

        return list(self.parent_dir.glob("**/Cargo.toml"))

    def _recreate_settings_file(self) -> Path:
        """jsonファイルを作り直す"""

        settings_file = Path("./.vscode/settings.json").resolve()
        settings_file.unlink(missing_ok=True)
        settings_file.parent.mkdir(exist_ok=True)
        settings_file.touch()
        return settings_file

    def setting_rust_analyzer(self) -> None:
        """`.vscode/settings.json`を作成し、rust-analyzerが動くように設定する"""

        settings_file = self._recreate_settings_file()
        cargo_paths = self._get_cargo_files()
        # HACK: jsonで機能するファイルパスにあわせるため`PurePosixPath`に変換を噛ませているが綺麗じゃない
        formatted_path = ",\n".join([f'"{PurePosixPath(p)}"' for p in cargo_paths])
        writing_data = f'{{"rust-analyzer.linkedProjects":[{formatted_path}]}}'
        with open(settings_file, "w") as sf:
            sf.write(writing_data)
